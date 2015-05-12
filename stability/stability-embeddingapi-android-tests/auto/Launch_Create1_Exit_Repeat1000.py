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
#         Yongyong, Zhu<yongyongx.zhu@intel.com>

import unittest
import os, sys, commands, shutil
import time
import subprocess
reload(sys)
sys.setdefaultencoding( 'utf-8' )

SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)

def setUp():
    global device
    #device = 'E6OKCY410821'
    device = os.environ.get('DEVICE_ID')
    if not device:
        print 'Get env error\n'
        sys.exit(1)

class TestStabilityIterativeFunctions(unittest.TestCase):
    def test_launch_exit_repeatedly(self):
        setUp()
        runtime = 1000
        pre_time = time.time()
        testName = "test_launch_exit_repeatedly_1000"
        sysmon_path = ConstPath + '/sysmon.sh'
        sysmon_cmd = sysmon_path + ' ' + testName + ' ' + str(runtime) + ' org.xwalkview.maximum.app'
        subprocess.Popen(args=sysmon_cmd, shell=True)
        i = 0
        for i in range(0, 1000):
            i = i + 1
            print i, 'Times'
            pmstatus = commands.getstatusoutput('adb -s ' + device + ' shell pm list packages |grep org.xwalkview.maximum.app')
            if pmstatus[0] == 0:
                launchstatus = commands.getstatusoutput('adb -s ' + device + ' shell am start -n org.xwalkview.maximum.app' + '/.XWalkViewsActivity')
                self.assertNotIn('Error', launchstatus[1])
                time.sleep(20)
                commands.getstatusoutput('adb -s ' + device + ' shell am force-stop org.xwalkview.maximum.app')
                stopresult = commands.getstatusoutput('adb -s ' + device + ' shell ps |grep org.xwalkview.maximum.app')
                self.assertNotIn('org.xwalkview.maximum.app', stopresult[1])
            else:
                print 'Please install apk frist'
                sys.exit(1) 
   

if __name__ == '__main__':
    unittest.main()
