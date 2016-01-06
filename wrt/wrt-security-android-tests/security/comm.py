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
#         Hongjuan, Wang<hongjuanx.wang@intel.com>

import unittest
import os
import sys
import commands
import shutil
reload(sys)
sys.setdefaultencoding("utf-8")

SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)
app_tools_dir = os.environ.get('CROSSWALK_APP_TOOLS_CACHE_DIR')

def setUp():
    global ARCH, MODE, device, xwalk_version, apptools, crosswalkzip

    #device = "E6OKCY411012"
    device = os.environ.get('DEVICE_ID')
    if not device:
        print (" get env error\n")
        sys.exit(1)

    if not app_tools_dir:
        print ("Not find CROSSWALK_APP_TOOLS_CACHE_DIR\n")
        sys.exit(1)

    fp = open(ConstPath + "/../arch.txt", 'r')
    ARCH = fp.read().strip("\n\t")
    fp.close()

    mode = open(ConstPath + "/../mode.txt", 'r')
    MODE = mode.read().strip("\n\t")
    mode.close()

    # app tools commend
    apptools = "crosswalk-pkg"
    if os.system(apptools) != 0:
        apptools = app_tools_dir + "/crosswalk-app-tools/src/crosswalk-pkg"

    # crosswalk lib
    xwalk_version = os.environ.get('XWALK_VERSION')
    if not xwalk_version:
        zips = glob.glob(os.path.join(app_tools_dir, "crosswalk-*.zip"))
        if len(zips) == 0:
            print ("Not find crosswalk zip in CROSSWALK_APP_TOOLS_CACHE_DIR\n")
            sys.exit(1)
        # latest version
        zips.sort(reverse = True)
        crosswalkzip = zips[0]
    else:
        if "64" in ARCH:
            crosswalkzip = os.path.join(app_tools_dir, "crosswalk-%s-64bit.zip" % xwalk_version)
        else:
            crosswalkzip = os.path.join(app_tools_dir, "crosswalk-%s.zip" % xwalk_version)
        if not os.path.exists(crosswalkzip):
            crosswalkzip = xwalk_version


# test for build, install, launch and uninstall


def gen_pkg(cmd, appname, self):
    setUp()
    commands.getstatusoutput("rm -rf org.xwalk.%s*" % appname)
    packstatus = commands.getstatusoutput(cmd)
    self.assertEquals(0, packstatus[0])
    print "Generate APK ----------------> OK!"
    result = commands.getstatusoutput("ls |grep org.xwalk.%s" % appname)
    self.assertTrue(len(result) > 0)
    inststatus = commands.getstatusoutput(
        "adb -s %s install -r %s" % (device, result[1]))
    self.assertEquals(0, inststatus[0])
    print "Install APK ----------------> OK"
    pmstatus = commands.getstatusoutput(
        "adb -s %s shell pm list packages |grep org.xwalk.%s" % (device, appname))
    self.assertEquals(0, pmstatus[0])
    print "Find Package in device ---------------->O.K"
    launchstatus = commands.getstatusoutput(
        "adb -s %s shell am start -n org.xwalk.%s/.%sActivity" \
      % (device, appname, appname.capitalize()))
    self.assertEquals(0, launchstatus[0])
    print "Launch APK ---------------->OK"
    stopstatus = commands.getstatusoutput(
        "adb -s %s shell am force-stop org.xwalk.%s" % (device, appname))
    if stopstatus[0] == 0:
        print "Stop APK ---------------->O.K"
        unistatus = commands.getstatusoutput(
            "adb -s %s uninstall org.xwalk.%s" % (device, appname))
        self.assertEquals(0, unistatus[0])
        print "Uninstall APK ---------------->O.K"
    else:
        print "Stop APK ---------------->Error"
        os.system("adb -s %s uninstall org.xwalk.%s"% (device, appname))
