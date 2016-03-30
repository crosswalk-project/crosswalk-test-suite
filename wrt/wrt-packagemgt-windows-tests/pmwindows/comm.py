#!/usr/bin/env python
# coding=utf-8
#
# Copyright (c) 2016 Intel Corporation.
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
#         Zhu, Yongyong <yongyongx.zhu@intel.com>

import os
import sys
import commands
import shutil
import glob
import fnmatch
import re
import json
import subprocess
import time
reload(sys)
sys.setdefaultencoding("utf-8")
script_path = os.path.realpath(__file__)
const_path = os.path.dirname(script_path)
tool_path = const_path + "/../tools/"
testapp_path = "C:\\stub\\packages"

#msiexec /i C:\\packages\\opt\\tct-backgrounds-css3-tests\\tct-backgrounds-css3-tests.msi /qn /quiet
LOCAL_INSTALL_CMD = "msiexec /i %s /qn /quiet"
#msiexec /x C:\\packages\\opt\\tct-backgrounds-css3-tests\\tct-backgrounds-css3-tests.msi /qn /quiet
LOCAL_UNINSTALL_CMD = "msiexec /x %s /qf"

LAUNCH_CMD = "\"c:\\Program Files\\%s\\xwalk.exe\" \"c:\\Program Files\\%s\\%s\\manifest.json\""
QUERY_CMD = "tasklist | findstr xwalk.exe"
KILL_CMD = "taskkill /im xwalk.exe /f"

def checkInstalled(pkg_name):
    action_status = False
    cmd = "reg query \"HKEY_CURRENT_USER\Software\org.xwalk\%s\" /v \"installed\"" % pkg_name
    (return_code, output) = doCMD(cmd)
    for line in output:
        if "installed" in line:
            action_status = True
            break

    return action_status

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

def app_install(appname, pkgname, self):
    print "Install MSI ----------------> START"
    app_path = os.path.join(testapp_path, "%s.msi" % appname)
    if not os.path.exists(app_path):
        print "Error: No app: %s found in directory: %s" % (appname, testapp_path)

    cmd_inst = LOCAL_INSTALL_CMD % app_path
    print "cmd_inst: %s" % cmd_inst
    (return_code, output) = doCMD(cmd_inst)
    self.assertEquals(0, return_code)
    self.assertTrue(checkInstalled(pkgname))
    print "Install MSI ----------------> OK"

def app_uninstall(appname, pkgname, self):
    print "Uninstall MSI ----------------> START"

    app_path = os.path.join(testapp_path, "%s.msi" % appname)
    if not os.path.exists(app_path):
        print "Error: No app: %s found in directory: %s" % (appname, testapp_path)

    cmd_uninst = LOCAL_UNINSTALL_CMD % app_path
    print "cmd_uninst: %s" % cmd_uninst
    (return_code, output) = doCMD(cmd_uninst)
    self.assertEquals(0, return_code)
    self.assertFalse(checkInstalled(pkgname))
    print "Uninstall MSI ----------------> OK"


def check_app_launched():
    action_status = False
    (return_code, output) = doCMD(QUERY_CMD)
    for line in output:
        if "xwalk.exe" in line:
            action_status = True
        return action_status


def app_launch(appname, pkgname, self):
    print "Launch APP ----------------> START"
    cmd_launch = LAUNCH_CMD % (appname, appname, appname)
    print "cmd_launch: %s" % cmd_launch
    subprocess.Popen(
        cmd_launch, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

    time.sleep(1)
    self.assertTrue(check_app_launched())
    print "Launch APP ----------------> OK"

def app_stop(self):
    print "Stop APK ----------------> START"
    action_status = False
    (return_code, output) = doCMD(KILL_CMD)
    self.assertFalse(check_app_launched())
    print "Stop APK ----------------> OK"


def replace_key(file_path, content, key):
    print "Replace value ----------------> START"
    f = open(file_path, "r")
    f_content = f.read()
    f.close()
    pos = f_content.find(key)
    if pos != -1:
        f_content = f_content.replace(key, content)
        f = open(file_path, "w")
        f.write(f_content)
        f.close()
    else:
        print "Fail to replace: %s with: %s in file: %s" % (content, key, file_path)
        return False
    print "Replace value ----------------> OK"
    return True

