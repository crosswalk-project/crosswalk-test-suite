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
    def test_launch_exit_repeatedly(self):
        setUp()
        runtime = 14400
        pre_time = time.time()
        testName = "test_launch_exit_repeatedly"
        sysmon_path = ConstPath + '/sysmon.sh'
        sysmon_cmd = sysmon_path + ' ' + testName + ' ' + str(runtime) + ' org.xwalk.*'
        subprocess.Popen(args=sysmon_cmd, shell=True)
        i = 0
        while True:
            i = i + 1
            apps_list = { 'tct_fileapi_w3c_tests':'TctFileapiW3cTests',
                          'tct_fullscreen_nonw3c_tests':'TctFullscreenNonw3cTests',
                          'tct_mediacapture_w3c_tests':'TctMediacaptureW3cTests',
                          'tct_websocket_w3c_tests':'TctWebsocketW3cTests',
                          'gallery':'Gallery',
                          'hangonman':'Hangonman',
                          'hexgl':'Hexgl',
                          'sysapps':'Sysapps',
                          'memorygame':'Memorygame'
            }
            elapsed_time = time.time() - pre_time
            if elapsed_time >= runtime:
                print i, elapsed_time, 'Process finished'
                break
            else:
                for name, pkg in apps_list.items():
                    #print '%s\t%s' % (name, pkg)
                    print i,  elapsed_time, 'Continue'
                    pmstatus = commands.getstatusoutput('adb -s ' + device + ' shell pm list packages |grep org.xwalk.' + name)
                    if pmstatus[0] == 0:
                        launchstatus = commands.getstatusoutput('adb -s ' + device + ' shell am start -n org.xwalk.' + name + '/.' + pkg + 'Activity')
                        self.assertNotIn('Error', launchstatus[1])
                        commands.getstatusoutput('adb -s ' + device + ' shell am force-stop org.xwalk.' + name)
                        stopresult = commands.getstatusoutput('adb -s ' + device + ' shell ps |grep org.xwalk.' + name)
                        self.assertNotIn('org.xwalk.' + name, stopresult[1])
                    else:
                        print 'Please install apk ' + name + ' frist'
                        sys.exit(1)

if __name__ == '__main__':
    unittest.main()
