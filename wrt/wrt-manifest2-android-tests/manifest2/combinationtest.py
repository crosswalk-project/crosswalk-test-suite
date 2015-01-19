#!/usr/bin/env python
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
import os, sys, commands
import comm

class TestManifestFunctions(unittest.TestCase):
    def test_field_combination(self):
        comm.setUp()
        manifestPath = comm.ConstPath + "/../testapp/splashscreen_launchscreen_field_tests/manifest.json"
        cmd = "python %smake_apk.py --package=org.xwalk.example --arch=%s --mode=%s --manifest=%s" % \
              (comm.Pck_Tools, comm.ARCH, comm.MODE, manifestPath)
        packstatus = commands.getstatusoutput(cmd)
        self.assertEquals(0, packstatus[0])
        print "Generate APK ----------------> OK!"
        inststatus = commands.getstatusoutput("adb -s " + comm.device + " install -r Example*apk")
        self.assertEquals(0, inststatus[0])
        print "Install APK ----------------> OK"
        pmstatus = commands.getstatusoutput("adb -s " + comm.device + " shell pm list packages |grep org.xwalk.example")
        self.assertEquals(0, pmstatus[0])
        print "Find Package in device ---------------->O.K"
        launchstatus = commands.getstatusoutput("adb -s " + comm.device + " shell am start -n org.xwalk.example/.ExampleActivity")
        self.assertEquals(0, launchstatus[0])
        print "Launch APK ---------------->OK"
        stopstatus = commands.getstatusoutput("adb -s " + comm.device + " shell am force-stop org.xwalk.example")
        if stopstatus[0] == 0:
            print "Stop APK ---------------->O.K"
            unistatus = commands.getstatusoutput("adb -s " + comm.device + " uninstall org.xwalk.example")
            self.assertEquals(0, unistatus[0])
            print "Uninstall APK ---------------->O.K"
        else:
            print "Stop APK ---------------->Error"
            os.system("adb -s " + comm.device + " uninstall org.xwalk.example")
        os.system("rm -rf *.apk")

if __name__ == '__main__':
    unittest.main()
