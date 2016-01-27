#!/usr/bin/env python
# coding=utf-8
#
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
#         Li, Hao<haox.li@intel.com>

import sys
import commands
import subprocess
import time
reload(sys)
sys.setdefaultencoding('utf-8')

ADB_CMD = "adb"

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

class TestApp():
    device = ""
    location = ""
    pkgname = ""
    activname = ""

    def __init__(self, device, location, pkgname, activname):
        self.device = device
        self.location = location
        self.pkgname = pkgname
        self.activname = activname

    def install(self):
        action_status = False
        if self.location.endswith(".apk"):
            if not self.isInstalled():
                cmd = "%s -s %s install -r %s" % (ADB_CMD, self.device, self.location)
                (return_code, output) = doCMD(cmd)
                if self.isInstalled():
                    action_status = True
                else:
                    print "-->> %s fail to install." % self.location
            else:
                print "-->> %s has been installed." % self.pkgname
        else:
            print "-->> Invalid apk location: %s " % self.location
        return action_status

    def uninstall(self):
        action_status = False
        if self.isInstalled():
            cmd = "%s -s %s uninstall %s" % (ADB_CMD, self.device, self.pkgname)
            (return_code, output) = doCMD(cmd)
            if not self.isInstalled():
                action_status = True
            else:
                print "-->> %s fail to uninstall." % self.pkgname
        else:
            print "-->> %s has not been installed." % self.pkgname
        return action_status

    def launch(self):
        action_status = False
        if not self.isRunning():
            cmd = "%s -s %s shell am start -n %s/.%s" % (ADB_CMD, self.device, self.pkgname, self.activname)
            (return_code, output) = doCMD(cmd)
            ## waiting for app launch
            time.sleep(5)
            if self.isRunning():
                action_status = True
            else:
                print "-->> %s fail to launch." % self.pkgname
        else:
            print "-->> %s has been launched." % self.pkgname
        return action_status

    def switch(self):
        action_status = False
        # If in Activity, switch to background, otherwise switch to front
        if self.isActivity():
            # Switch to Home
            # keycode
            # 3 --> "KEYCODE_HOME"
            time.sleep(5)
            cmd = "%s -s %s shell input keyevent 3" % (ADB_CMD, self.device)
            (return_code, output) = doCMD(cmd)
            ## waiting for app hidden
            time.sleep(5)
            if not self.isActivity():
                action_status = True
            else:
                print "-->> %s fail to switch to background." % self.pkgname
        else:
            cmd = "%s -s %s shell am start -n %s/.%s" % (ADB_CMD, self.device, self.pkgname, self.activname)
            (return_code, output) = doCMD(cmd)
            ## waiting for app launch
            if self.isActivity():
                action_status = True
            else:
                print "-->> %s fail to switch to front." % self.pkgname

        return action_status

    def stop(self):
        action_status = False
        if self.isRunning():
            cmd = "%s -s %s shell am force-stop %s" % (ADB_CMD, self.device, self.pkgname)
            (return_code, output) = doCMD(cmd)
            if not self.isRunning():
                action_status = True
            else:
                print "-->> %s fail to stop." % self.pkgname
        else:
            print "-->> %s has been stoped." % self.pkgname
        return action_status

    def isInstalled(self):
        action_status = False
        if not self.pkgname == "":
            cmd = "%s -s %s shell pm list packages |grep %s|awk -F ':' '{print $2}'" % (ADB_CMD, self.device, self.pkgname)
            (return_code, output) = doCMD(cmd)
            if self.pkgname in output:
                action_status = True
        return action_status

    def isRunning(self):
        action_status = False
        if not self.pkgname == "":
            cmd = "%s -s %s shell ps |grep %s|awk -F ' ' '{print $NF}'" % (ADB_CMD, self.device, self.pkgname)
            (return_code, output) = doCMD(cmd)
            if self.pkgname in output:
                action_status = True
        return action_status

    def isActivity(self):
        action_status = False
        if not self.pkgname == "":
            cmd = "%s -s %s shell dumpsys activity |grep \"%s\"" % (ADB_CMD, self.device, "Recent #0")
            (return_code, output) = doCMD(cmd)
            for line in output:
                if self.pkgname in line:
                    action_status = True
                    break
        return action_status

