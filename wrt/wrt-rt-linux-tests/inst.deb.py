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
PARAMETERS = None

def doCMD(cmd):
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

def getUSERID():
    cmd = "whoami"
    return doCMD(cmd)


def getPKGID(pkg_name=None):
    pkg_id =  None
    pkg_name = pkg_name.split('.')
    num = len(pkg_name)
    pkg_id = pkg_name[num - 1]
    return pkg_id

def uninstPKGs():
    action_status = True
    for root, dirs, files in os.walk(SCRIPT_DIR):
        for file in files:
            if file.endswith(".deb"):
                pkg_id = getPKGID(os.path.basename(os.path.splitext(file)[0]))
                if not pkg_id:
                    action_status = False
                    continue
                (return_code, output) = doCMD(
                    "sudo dpkg -P %s" % pkg_id)
                for line in output:
                    if "error" in line:
                        action_status = False
                        break
    return action_status


def instPKGs():
    action_status = True
    for root, dirs, files in os.walk(SCRIPT_DIR):
        for file in files:
            if file.endswith(".deb"):
                cmd = "sudo dpkg -i %s/%s" % (root, file)
                (return_code, output) = doCMD(cmd)
                for line in output:
                    if "error" in line:
                        action_status = False
                        break
    return action_status


def main():
    try:
        usage = "usage: inst.py -i"
        opts_parser = OptionParser(usage=usage)
        opts_parser.add_option(
            "-i", dest="binstpkg", action="store_true", help="Install package")
        opts_parser.add_option(
            "-u", dest="buninstpkg", action="store_true", help="Uninstall package")
        opts_parser.add_option(
            "-a", dest="user", action="store", help="User name")
        global PARAMETERS
        (PARAMETERS, args) = opts_parser.parse_args()
    except Exception, e:
        print "Got wrong option: %s, exit ..." % e
        sys.exit(1)

    if not PARAMETERS.user:
        (return_code, output) = getUSERID()
        if return_code == 0:
            PARAMETERS.user = output

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
