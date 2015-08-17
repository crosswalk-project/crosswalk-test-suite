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

class TestStabilityInLowBatteryFunctions(unittest.TestCase):

    def test_app_repeatedly_in_lowbattery(self):
        setUp()
        testapp = TestApp(device, ConstPath + "/../testapp/lowresourcetest.apk",
                                "org.xwalk.lowresourcetest", "LowresourcetestActivity")
        if testapp.isInstalled():
            testapp.uninstall()

        for i in range(20):
            if testapp.install() and testapp.launch():
                switchresult = False
                for i in range(2):
                    time.sleep(1)
                    # swtich app
                    switchresult = testapp.switch()

                if switchresult:
                    time.sleep(1)
                    if testapp.stop() and testapp.uninstall():
                        time.sleep(1)
                    else:
                        testapp.uninstall()
                        self.assertTrue(False)
                else:
                    testapp.uninstall()
                    self.assertTrue(False)
            else:
                testapp.uninstall()
                self.assertTrue(False)

            testapp.uninstall()
            self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
