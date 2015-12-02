#!/usr/bin/env python

# Copyright (c) 2015 Intel Corporation.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of works must retain the original copyright notice, this
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Intel Corporation nor the names of its contributors
#   may be used to endorse or promote products derived from this work without
#   specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors:
#         Li, Hao <haox.li@intel.com>

import os
import shutil
import glob
import time
import sys
import subprocess
from optparse import OptionParser, make_option


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PARAMETERS = None

#msiexec /i C:\\packages\\opt\\tct-backgrounds-css3-tests\\tct-backgrounds-css3-tests.msi /qn /quiet
LOCAL_INSTALL_CMD = "msiexec /i %s /qn /quiet"
#msiexec /x C:\\packages\\opt\\tct-backgrounds-css3-tests\\tct-backgrounds-css3-tests.msi /qn /quiet
LOCAL_UNINSTALL_CMD = "msiexec /x %s /qf"
#curl http://10.239.250.79:8000/powershell_install -d '{"suite": "tct-backgrounds-css3-tests", "file": "opt/tct-backgrounds-css3-tests/tct-backgrounds-css3-tests.msi"}' -X POST
REMOTE_INSTALL_CMD = "curl http://%s:8000/powershell_install -d '{\"suite\": \"%s\", \"host\": \"%s\", \"file\": \"%s\"}' -X POST"
#curl http://10.239.250.79:8000/powershell_uninstall -d '{"suite": "tct-backgrounds-css3-tests"}' -X POST
REMOTE_UNINSTALL_CMD = "curl http://%s:8000/powershell_uninstall -d '{\"suite\": \"%s\"}' -X POST"

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


def uninstPKGs():
    action_status = False
    for root, dirs, files in os.walk(SCRIPT_DIR):
        for file in files:
            if file.endswith(".msi"):
                app_name = file.split(".")[0]
                if PARAMETERS.device is not None:
                    # Uninstall from remote windows device
                    cmd = REMOTE_UNINSTALL_CMD % (PARAMETERS.device, app_name)
                    (return_code, output) = doCMD(cmd)
                    for line in output:
                        if "OK" in line:
                            action_status = True
                            break
                else:
                    pkg_name = "org.xwalk." + app_name.replace("-", "")
                    if checkInstalled(pkg_name):
                        # Uninstall from local windows device
                        cmd = LOCAL_UNINSTALL_CMD % os.path.join(root, file)
                        (return_code, output) = doCMD(cmd)
                        if not checkInstalled(pkg_name):
                            # Installed files may be uninstalled fail, clear them manually
                            pkg_cache = os.path.join("C:\\Program Files", app_name)
                            if os.path.exists(pkg_cache):
                                shutil.rmtree(pkg_cache)
                            else:
                                #For 32bits
                                pkg_cache = os.path.join("C:\\Program Files (x86)", app_name)
                                if os.path.exists(pkg_cache):
                                    shutil.rmtree(pkg_cache)
                            action_status = True
                            print action_status
                    else:
                        sys.stdout.write("%s has been uninstalled\n" % pkg_name)

    return action_status


def instPKGs():
    action_status = False
    for root, dirs, files in os.walk(SCRIPT_DIR):
        for file in files:
            if file.endswith(".msi"):
                if (PARAMETERS.device is not None) and (PARAMETERS.hostip is not None) :
                    app_name = file.split(".")[0]
                    app_relative_path = "opt" + os.sep + os.path.join(root, file).split(os.sep + "opt" + os.sep)[-1]
                    # Install to remote windows device
                    cmd = REMOTE_INSTALL_CMD % (PARAMETERS.device, app_name, PARAMETERS.hostip, app_relative_path)
                    (return_code, output) = doCMD(cmd)
                    for line in output:
                        if "OK" in line:
                            action_status = True
                            break
                else:
                    pkg_name = "org.xwalk." + file.split(".")[0].replace("-", "")
                    if not checkInstalled(pkg_name):
                        # Install to local windows device
                        cmd = LOCAL_INSTALL_CMD % os.path.join(root, file)
                        (return_code, output) = doCMD(cmd)
                        if checkInstalled(pkg_name):
                            action_status = True
                    else:
                        sys.stdout.write("%s has been installed\n" % pkg_name)

    return action_status


def checkInstalled(pkg_name):
    action_status = False
    cmd = "reg query \"HKEY_CURRENT_USER\Software\org.xwalk\%s\" /v \"installed\"" % pkg_name
    (return_code, output) = doCMD(cmd)
    for line in output:
        if "installed" in line:
            action_status = True
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
            "-d", dest="device", action="store", help="Device IP Address")
        opts_parser.add_option(
            "-m", dest="hostip", action="store", help="Host IP Address")
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
        if not instPKGs():
            sys.exit(1)

if __name__ == "__main__":
    main()
    sys.exit(0)
