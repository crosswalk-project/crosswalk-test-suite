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
#         Hongjuan, Wang<hongjuanx.wang@intel.com>

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
    #device = 'E6OKCY411012'
    device = os.environ.get('DEVICE_ID')
    if not device:
        print 'Get env error\n'
        sys.exit(1)

class TestStabilityIterativeFunctions(unittest.TestCase):   
    def test_install_uninstall_repeatedly(self):
        setUp()
        global testName, runtime
        testName = 'test_install_uninstall_repeatedly'
        runtime = 7200
        pre_time = time.time()
        sysmon_path = ConstPath + '/sysmon.sh'
        sysmon_cmd = sysmon_path + ' ' + testName + ' ' + str(runtime) + ' org.xwalk.iterative'
        subprocess.Popen(args=sysmon_cmd, shell=True)
        i = 0
        while True:
            i = i + 1
            cmd = 'adb -s ' + device + ' install -r ' + ConstPath + '/../iterative*.apk'
            inststatus = commands.getstatusoutput(cmd)
            elapsed_time = time.time() - pre_time
            if inststatus[0] == 0:
                if elapsed_time >= runtime:
                    #kill process
                    print i, elapsed_time, 'Process finished'
                    uninststatus = commands.getstatusoutput('adb -s ' + device + ' uninstall org.xwalk.iterative')
                    self.assertEquals(uninststatus[0], 0)
                    break
                else:
                    uninststatus = commands.getstatusoutput('adb -s ' + device + ' uninstall org.xwalk.iterative')
                    self.assertEquals(uninststatus[0], 0)
                    print i,  elapsed_time, 'Continue'
                    time.sleep(3)
            else:
                self.assertFalse(True, 'Install apk failed')
                #print 'Install apk failed'
                break

if __name__ == '__main__':
    unittest.main()
