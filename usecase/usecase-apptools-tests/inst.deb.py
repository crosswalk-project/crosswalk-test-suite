#!/usr/bin/env python

import os
import sys
import subprocess
from optparse import OptionParser

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
        if output_line == '' and cmd_return_code is not None:
            break
        sys.stdout.write("%s\n" % output_line)
        sys.stdout.flush()
        output.append(output_line)

    return (cmd_return_code, output)


def uninstPKGs():
    action_status = True
    for root, dirs, files in os.walk(SCRIPT_DIR):
        for file in files:
            if file.endswith(".deb"):
                debName = os.path.basename(os.path.splitext(file)[0])
                pkg_id = debName.split("_")[0]
                if doCMD("which %s" % pkg_id)[0] == 0:
                    (return_code, output) = doCMD(
                        "sudo dpkg -P %s" % pkg_id)
                    if return_code != 0:
                        action_status = False
                        break
    return action_status


def instPKGs():
    action_status = True
    for root, dirs, files in os.walk(SCRIPT_DIR):
        for file in files:
            if file.endswith(".deb") and file.find("upgrade") == -1:
                cmd = "sudo dpkg -i %s/%s" % (root, file)
                (return_code, output) = doCMD(cmd)
                if return_code != 0:
                    action_status = False
                    break
    return action_status


def initEnv():
    action_status = True
    xwalk_dir = "/usr/bin"
    cmd = "which xwalk"
    (return_code, xwalk_path) = doCMD(cmd)
    if return_code == 0:
        xwalk_dir = os.path.dirname(xwalk_path[0])
    cmdList = ["sudo rm -rf %s/xwalk", "sudo cp -rf xwalk.sh %s/", "sudo ln /usr/bin/xwalk.sh %s/xwalk"]
    for cmdstr in cmdList:
        cmd = cmdstr % xwalk_dir
        (return_code, xwalk_path) = doCMD(cmd)
        if return_code != 0:
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
        global PARAMETERS
        (PARAMETERS, args) = opts_parser.parse_args()
    except Exception as e:
        print "Got wrong option: %s, exit ..." % e
        sys.exit(1)

    if PARAMETERS.binstpkg and PARAMETERS.buninstpkg:
        print "-i and -u are conflict"
        sys.exit(1)

    if PARAMETERS.buninstpkg:
        if not uninstPKGs():
            sys.exit(1)
    else:
        if not initEnv():
            sys.exit(1)
        if not instPKGs():
            sys.exit(1)

if __name__ == "__main__":
    main()
    sys.exit(0)
