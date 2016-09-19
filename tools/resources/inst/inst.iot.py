#!/usr/bin/env python

import os
import shutil
import glob
import time
import sys
import subprocess
from optparse import OptionParser, make_option


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PARAMETERS = None


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


def instPKGs():
    action_status = True

    pwd = os.getcwd()
    testsuite = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

    if os.path.exists(os.path.join(pwd, testsuite)):
        cmd = "scp -r %s %s:/opt" % (testsuite, PARAMETERS.device)
        (return_code, output) = doCMD(cmd)
        for line in output:
            if "Failure" in line:
                action_status = False
                break
    
    if os.path.exists(os.path.join(pwd, "sub-app")):
        cmd = "scp -r sub-app %s:/opt/%s" % (PARAMETERS.device, testsuite)
        (return_code, output) = doCMD(cmd)
        for line in output:
            if "Failure" in line:
                action_status = False
                break            
    return action_status


def uninstPKGs():
    action_status = True

    pwd = os.getcwd()
    testsuite = os.path.basename(os.path.dirname(os.path.abspath(__file__)))

    cmd = 'ssh %s "rm -rf /opt/%s"' % (PARAMETERS.device, testsuite)
    (return_code, output) = doCMD(cmd)
    for line in output:
        if "Failure" in line:
            action_status = False
            break

    return action_status


def main():
    try:
        usage = "usage: inst.py -i"
        opts_parser = OptionParser(usage=usage)
        opts_parser.add_option(
            "-s", dest="device", action="store", help="Specify IoT device user and IP: root@<IP addr>")
        opts_parser.add_option(
            "-i", dest="binstpkg", action="store_true", help="Install package")
        opts_parser.add_option(
            "-u", dest="buninstpkg", action="store_true", help="Uninstall package")        

        global PARAMETERS
        (PARAMETERS, args) = opts_parser.parse_args()
    except Exception as e:
        print "Got wrong option: %s, exit ..." % e
        sys.exit(1)

    if not PARAMETERS.device:
        print "IoT host device not specified."
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