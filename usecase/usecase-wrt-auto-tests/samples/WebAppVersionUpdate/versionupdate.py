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
import os
import sys
import commands

SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)
Pck_Tools = ConstPath + "/../../tools/crosswalk/"

def setUp():
    global ARCH, MODE

    fp = open(ConstPath + "/../../arch.txt", 'r')
    if fp.read().strip("\n\t") != "x86":
        ARCH = "arm"
    else:
        ARCH = "x86"
    fp.close()

    mode = open(ConstPath + "/../../mode.txt", 'r')
    if mode.read().strip("\n\t") != "shared":
        MODE = "embedded"
    else:
        MODE = "shared"
    mode.close()

def clear_test(Version):
    if os.path.exists(ConstPath + "/test"):
       try:
          os.remove(ConstPath + "/Test_" + Version + "_"  + ARCH +".apk")
          shutil.rmtree(ConstPath + "/test")
       except Exception,e:
          os.system("rm -rf " + ConstPath + "/*.apk")
          os.system("rm -rf " + ConstPath + "/test")

def checkValue(cmd, self):
    os.chdir(ConstPath)
    packstatus = commands.getstatusoutput(cmd)
    self.assertEquals(0, packstatus[0])
    fp = open(ConstPath + "/test/Test/AndroidManifest.xml")
    lines = fp.readlines()
    for i in range(len(lines)): 
        l = lines[i].strip("\n\r").strip()
        if i < len(lines):
            if "versionName" in l:
                self.assertIn("versionName", l)
                target_value = l[l.index("versionName")+13:l.index("versionName")+18]
                print "Find"
                clear_test(target_value)
                return target_value
                break
            else:
                print i
        else:
            self.assertFalse(true, "No Find " + "version")
    clear_test(target_value)

class TestPackertoolsFunctions(unittest.TestCase):

    def test_version_update(self):
        setUp()
        cmd1 = "python %smake_apk.py --name=Test --package=org.xwalk.test --app-url=http://www.baidu.com --app-version=1.0.0 --arch=%s --mode=%s --project-dir=test" % \
               (Pck_Tools, ARCH, MODE)
        app_version = "1.0.0"
        #clear_test(app_version)
        value1 = checkValue(cmd1, self)
        cmd2 = "python %smake_apk.py --name=Test --package=org.xwalk.test --app-url=http://www.baidu.com --app-version=1.0.1 --arch=%s --mode=%s --project-dir=test" % \
               (Pck_Tools, ARCH, MODE)
        app_version = "1.0.1"
        clear_test(app_version)
        value2 = checkValue(cmd2, self)
        self.assertTrue(value2 > value1)


if __name__ == '__main__':
    unittest.main()  
