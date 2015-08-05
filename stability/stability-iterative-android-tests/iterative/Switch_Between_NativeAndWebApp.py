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
# THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION 'AS IS'
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

import unittest
import os
import sys
import commands
import shutil
import time
import subprocess
from TestApp import *
reload(sys)
sys.setdefaultencoding('utf-8')

SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)

def setUp():
    global device
    #device = 'E6OKCY411012'
    device = os.environ.get('DEVICE_ID')
    if not device:
        print 'Get env error\n'
        sys.exit(1)

class TestSwitchBetweenNativeAndWebApp(unittest.TestCase):
    global testapp

    def test_swith_between_nativeandwebapp(self):
        setUp()
        testapp = TestApp(device, ConstPath + "/../iterative.apk",
                                "org.xwalk.iterative", "IterativeActivity")
        try:
            if not testapp.isInstalled():
                testapp.install()

            testapp.launch()
            # Pause and Resume 50 times
            for i in range(50):
                time.sleep(2)
                # swtich to native home app
                self.switchToHomeapp()
                self.assertFalse(testapp.isActivity())
                time.sleep(2)
                # swtich back
                self.assertTrue(testapp.switch())
            testapp.stop()
        except Exception as e:
            print "Error: %s" % e
            testapp.stop()
            self.assertTrue(False)

    def switchToHomeapp(self):
        action_status = False
        # Android Home App
        homeappname = "android.intent.category.HOME"
        cmd = "%s -s %s shell dumpsys activity|grep %s|awk -F \"cmp=\" '{print $2}'|awk '{print $1}'" % (ADB_CMD, device, homeappname)
        (return_code, output) = doCMD(cmd)
        if len(output) > 0:
            cmd = "%s -s %s shell am start -n %s" % (ADB_CMD, device, output[0])
            (return_code, output) = doCMD(cmd)
            action_status = True
        else:
            print "-->> Fail to find %s." % homeappname

        return action_status
        
if __name__ == '__main__':
    unittest.main()
