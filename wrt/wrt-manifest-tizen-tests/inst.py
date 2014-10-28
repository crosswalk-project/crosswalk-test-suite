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
XW_ENV = "export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/5000/dbus/user_bus_socket"
#SRC_DIR = "/home/app/content"
SRC_DIR = "/opt/usr/media"
PKG_SRC_DIR = "%s/tct/opt/%s" % (SRC_DIR, PKG_NAME)


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
        if output_line == '' and cmd_return_code != None:
            break
        sys.stdout.write("%s\n" % output_line)
        sys.stdout.flush()
        output.append(output_line)

    return (cmd_return_code, output)


def updateCMD(cmd=None):
    if "xwalkctl" in cmd:
        cmd = "su - app -c '%s;%s'" % (XW_ENV, cmd)
    return cmd


def overwriteCopy(src, dest, symlinks=False, ignore=None):
    if not os.path.exists(dest):
        os.makedirs(dest)
        shutil.copystat(src, dest)
    sub_list = os.listdir(src)
    if ignore:
        excl = ignore(src, sub_list)
        sub_list = [x for x in sub_list if x not in excl]
    for i_sub in sub_list:
        s_path = os.path.join(src, i_sub)
        d_path = os.path.join(dest, i_sub)
        if symlinks and os.path.islink(s_path):
            if os.path.lexists(d_path):
                os.remove(d_path)
            os.symlink(os.readlink(s_path), d_path)
            try:
                s_path_s = os.lstat(s_path)
                s_path_mode = stat.S_IMODE(s_path_s.st_mode)
                os.lchmod(d_path, s_path_mode)
            except Exception, e:
                pass
        elif os.path.isdir(s_path):
            overwriteCopy(s_path, d_path, symlinks, ignore)
        else:
            shutil.copy2(s_path, d_path)


def doCopy(src_item=None, dest_item=None):
    try:
        if os.path.isdir(src_item):
            overwriteCopy(src_item, dest_item, symlinks=True)
        else:
            if not os.path.exists(os.path.dirname(dest_item)):
                LOG.info("Create non-existent dir: %s" %
                         os.path.dirname(dest_item))
                os.makedirs(os.path.dirname(dest_item))
            shutil.copy2(src_item, dest_item)
    except Exception, e:
        return False

    return True


def getPKGID(pkg_name=None):
    if PARAMETERS.mode == "SDB":
        cmd = "sdb -s %s shell %s" % (
            PARAMETERS.device, updateCMD('xwalkctl'))
    else:
        cmd = "ssh %s \"%s\"" % (
            PARAMETERS.device, updateCMD('xwalkctl'))

    (return_code, output) = doCMD(cmd)
    if return_code != 0:
        return None

    test_app_id = None
    for line in output:
        pkg_infos = line.split()
        if len(pkg_infos) == 1:
            continue
        name = pkg_infos[1]
        if pkg_name == name:
            test_app_id = pkg_infos[0]
            print test_app_id
            break
    return test_app_id


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
        if root.endswith("mediasrc"):
            continue

        for file in files:
            if file.endswith(".wgt"):
                pkg_id = getPKGID(os.path.basename(os.path.splitext(file)[0]))
                if not pkg_id:
                    action_status = False
                    continue
                (return_code, output) = doRemoteCMD(
                    "xwalkctl -u %s" % pkg_id)
                for line in output:
                    if "Failure" in line:
                        action_status = False
                        break

    (return_code, output) = doRemoteCMD(
        "rm -rf %s" % PKG_SRC_DIR)
    if return_code != 0:
        action_status = False

    return action_status


def instPKGs():
   """ action_status = True
    (return_code, output) = doCMD(
        "mkdir -p %s" % PKG_SRC_DIR)
    if return_code != 0:
        action_status = False

    # Do some special copy/delete... steps
    '''
    (return_code, output) = doRemoteCMD(
        "mkdir -p %s/tests" % PKG_SRC_DIR)
    if return_code != 0:
        action_status = False

    if not doRemoteCopy("specname/tests", "%s/tests" % PKG_SRC_DIR):
        action_status = False
    '''
    for item in glob.glob("%s/*" % SCRIPT_DIR):
        if item.endswith("inst.py"):
            continue
        else:
            item_name = os.path.basename(item)
            if not doCopy(item, "%s/%s" % (PKG_SRC_DIR, item_name)):
                action_status = False
    print "Package push to host /opt/usr/media/tct/ successfully!"
    return action_status
"""

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
        global PARAMETERS
        (PARAMETERS, args) = opts_parser.parse_args()
    except Exception, e:
        print "Got wrong option: %s, exit ..." % e
        sys.exit(1)

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
