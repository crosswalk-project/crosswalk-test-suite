#!/usr/bin/env python

import os
import shutil
import glob
import time
import sys
import subprocess
import string
from optparse import OptionParser, make_option


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PKG_NAME = os.path.basename(SCRIPT_DIR)
PARAMETERS = None
#XW_ENV = "export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/5000/dbus/user_bus_socket"
SRC_DIR = ""
PKG_SRC_DIR = ""


def doCMD(cmd):
    # Do not need handle timeout in this short script, let tool do it
    print "-->> \"%s\"" % cmd
    output = []
    cmd_return_code = 1
    cmd_proc = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

    while True:
        output_line = cmd_proc.stdout.readline().strip("\r\n")
        cmd_return_code = cmd_proc.poll()
        if output_line == '' and cmd_return_code is not None:
            break
        sys.stdout.write("%s\n" % output_line)
        sys.stdout.flush()
        output.append(output_line)

    return (cmd_return_code, output)


def updateCMD(cmd=None):
    if "pkgcmd" in cmd:
        cmd = "su - %s -c '%s;%s'" % (PARAMETERS.user, XW_ENV, cmd)
    return cmd


def getUSERID():
    if PARAMETERS.mode == "SDB":
        cmd = "sdb -s %s shell id -u %s" % (
            PARAMETERS.device, PARAMETERS.user)
    else:
        cmd = "ssh %s \"id -u %s\"" % (
            PARAMETERS.device, PARAMETERS.user)
    return doCMD(cmd)


def getPKGID(pkg_name=None):
    if PARAMETERS.mode == "SDB":
        cmd = "sdb -s %s shell %s" % (
            PARAMETERS.device, updateCMD('pkgcmd -l'))
    else:
        cmd = "ssh %s \"%s\"" % (
            PARAMETERS.device, updateCMD('pkgcmd -l'))

    (return_code, output) = doCMD(cmd)
    if return_code != 0:
        return None

    test_pkg_id = None
    for line in output:
        if line.find("[" + pkg_name + "]") != -1:
            pkgidIndex = line.split().index("pkgid")
            test_pkg_id = line.split()[pkgidIndex + 1].strip("[]")
            break
    return test_pkg_id


def doRemoteCMD(cmd=None):
    if PARAMETERS.mode == "SDB":
        cmd = "sdb -s %s shell %s" % (PARAMETERS.device, updateCMD(cmd))
    else:
        cmd = "ssh %s \"%s\"" % (PARAMETERS.device, updateCMD(cmd))

    return doCMD(cmd)


def doRemoteCopy(src=None, dest=None):
    if PARAMETERS.mode == "SDB":
        cmd_prefix = "sdb -s %s push" % PARAMETERS.device
        cmd = "%s %s %s" % (cmd_prefix, src, dest)
    else:
        cmd = "scp -r %s %s:/%s" % (src, PARAMETERS.device, dest)

    (return_code, output) = doCMD(cmd)
    doRemoteCMD("sync")

    if return_code != 0:
        return True
    else:
        return False


def uninstPKGs():
    action_status = True
    for root, dirs, files in os.walk(SCRIPT_DIR):
        for file in files:
            if file.endswith(".wgt"):
                pkg_id = getPKGID(os.path.basename(os.path.splitext(file)[0]))
                if not pkg_id:
                    action_status = False
                    continue
                (return_code, output) = doRemoteCMD(
                    "pkgcmd -u -t wgt -q -n %s" % pkg_id)
                for line in output:
                    if "Failure" in line:
                        action_status = False
                        break

    (return_code, output) = doRemoteCMD(
        "rm -rf %s" % PKG_SRC_DIR)
    if return_code != 0:
        action_status = False

    (return_code, output) = doRemoteCMD("rm -rf %s/%s" % (SRC_DIR, PKG_NAME))
    if return_code != 0:
        action_status = False

    return action_status


def instPKGs():
    action_status = True
    (return_code, output) = doRemoteCMD(
        "mkdir -p %s" % PKG_SRC_DIR)
    if return_code != 0:
        action_status = False
    for root, dirs, files in os.walk(SCRIPT_DIR):
        for file in files:
            if file.endswith(".wgt"):
                if not doRemoteCopy(
                        os.path.join(root, file), "%s/%s" % (SRC_DIR, file)):
                    action_status = False
                (return_code, output) = doRemoteCMD(
                    "pkgcmd -i -t wgt -q -p %s/%s" % (SRC_DIR, file))
                doRemoteCMD("rm -rf %s/%s" % (SRC_DIR, file))
                for line in output:
                    if "Failure" in line:
                        action_status = False
                        break

    if not doRemoteCopy("%s/media" % SCRIPT_DIR, "%s/%s" %
                        (SRC_DIR, PKG_NAME)):
        action_status = False

    return action_status


def main():
    try:
        usage = "usage: inst.py -i"
        opts_parser = OptionParser(usage=usage)
        opts_parser.add_option(
            "-m", dest="mode", action="store", help="Specify mode")
        opts_parser.add_option(
            "-s", dest="device", action="store", help="Specify device")
        opts_parser.add_option(
            "-i", dest="binstpkg", action="store_true", help="Install package")
        opts_parser.add_option(
            "-u", dest="buninstpkg", action="store_true", help="Uninstall package")
        opts_parser.add_option(
            "-a", dest="user", action="store", help="User name")
        global PARAMETERS
        (PARAMETERS, args) = opts_parser.parse_args()
    except Exception as e:
        print "Got wrong option: %s, exit ..." % e
        sys.exit(1)

    if not PARAMETERS.user:
        PARAMETERS.user = "app"

    global SRC_DIR, PKG_SRC_DIR
    SRC_DIR = "/home/%s/content" % PARAMETERS.user
    PKG_SRC_DIR = "%s/tct/opt/%s" % (SRC_DIR, PKG_NAME)

    if not PARAMETERS.mode:
        PARAMETERS.mode = "SDB"

    if PARAMETERS.mode == "SDB":
        if not PARAMETERS.device:
            (return_code, output) = doCMD("sdb devices")
            for line in output:
                if str.find(line, "\tdevice") != -1:
                    PARAMETERS.device = line.split("\t")[0]
                    break
    else:
        PARAMETERS.mode = "SSH"

    if not PARAMETERS.device:
        print "No device provided"
        sys.exit(1)

    user_info = getUSERID()
    re_code = user_info[0]
    if re_code == 0:
        global XW_ENV
        userid = user_info[1][0]
        XW_ENV = "export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/%s/dbus/user_bus_socket" % str(
            userid)
    else:
        print "[Error] cmd commands error : %s" % str(user_info[1])
        sys.exit(1)
    if PARAMETERS.binstpkg and PARAMETERS.buninstpkg:
        print "-i and -u are conflict"
        sys.exit(1)

    if PARAMETERS.buninstpkg:
        if not uninstPKGs():
            sys.exit(1)
    else:
        if not instPKGs():
            sys.exit(1)

if __name__ == "__main__":
    main()
    sys.exit(0)
