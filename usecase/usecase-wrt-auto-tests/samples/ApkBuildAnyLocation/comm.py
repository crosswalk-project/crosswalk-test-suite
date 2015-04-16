#!/usr/bin/env python
#coding=utf-8
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
#         Hongjuan, Wang<hongjuanx.wang@intel.com>

import unittest
import os
import sys
import commands
import shutil

reload(sys)
sys.setdefaultencoding( "utf-8" )

SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)
Pck_Tools = ConstPath + "/../../tools/crosswalk/"

def setUp():
    global ARCH, MODE, device, AppName

    #device = "E6OKCY318006"
    device = os.environ.get('DEVICE_ID')
    if not device:
        print (" get env error\n")
        sys.exit(1)

    fp = open(ConstPath + "/../../arch.txt", 'r')
    if fp.read().strip("\n\t") != "x86":
        ARCH = "arm"
    else:
        ARCH = "x86"
    fp.close()

    mode = open(ConstPath + "/../../mode.txt", 'r')
    if mode.read().strip("\n\t") != "shared":
        MODE = "embedded"
        AppName = "Example_" + ARCH + ".apk"
    else:
        MODE = "shared"
        AppName = "Example.apk"
    mode.close()


# test for build, install, launch and uninstall
def gen_pkg(cmd, self):
    setUp()
    if os.path.exists(Pck_Tools + "/" + AppName):
        os.remove(Pck_Tools + "/" + AppName)
    if os.path.exists(ConstPath + "/../" + AppName):
        os.remove(ConstPath + "/../" + AppName)
    packstatus = commands.getstatusoutput(cmd)
    self.assertEquals(0, packstatus[0])
    print "Generate APK ----------------> OK!"
    result = commands.getstatusoutput("ls")
    self.assertIn(AppName, result[1])
    inststatus = commands.getstatusoutput("adb -s " + device + " install -r " + AppName)
    self.assertEquals(0, inststatus[0])
    print "Install APK ----------------> OK"
    pmstatus = commands.getstatusoutput("adb -s " + device + " shell pm list packages |grep org.xwalk.example")
    self.assertEquals(0, pmstatus[0])
    print "Find Package in device ---------------->O.K"
    launchstatus = commands.getstatusoutput("adb -s " + device + " shell am start -n org.xwalk.example/.ExampleActivity")
    self.assertEquals(0, launchstatus[0])
    print "Launch APK ---------------->OK"
    stopstatus = commands.getstatusoutput("adb -s " + device + " shell am force-stop org.xwalk.example")
    if stopstatus[0] == 0:
        print "Stop APK ---------------->O.K"
        unistatus = commands.getstatusoutput("adb -s " + device + " uninstall org.xwalk.example")
        self.assertEquals(0, unistatus[0])
        print "Uninstall APK ---------------->O.K"
    else:
        print "Stop APK ---------------->Error"
        os.system("adb -s " + device + " uninstall org.xwalk.example")
    if os.path.exists(os.getcwd() + "/" + AppName):
        os.remove(os.getcwd() + "/" + AppName)
    if os.path.exists(ConstPath + "/../" + AppName):
        os.remove(ConstPath + "/../" + AppName)

