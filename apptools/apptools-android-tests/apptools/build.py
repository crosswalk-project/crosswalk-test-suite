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
import comm
import commands

class TestCrosswalkApptoolsFunctions(unittest.TestCase):
    def test_build_normal(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        buildcmd =  comm.PackTools + "crosswalk-app build"
        comm.build(self, buildcmd)
        comm.run(self)
        comm.clear("org.xwalk.test")

    def test_build_release(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        buildcmd =  comm.PackTools + "crosswalk-app build release"
        comm.build(self, buildcmd)
        comm.run(self)
        comm.clear("org.xwalk.test")

    def test_build_missing_so_file(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        if comm.ARCH == "x86":
            os.remove(os.getcwd() + '/prj/android/xwalk_core_library/libs/armeabi-v7a/libxwalkcore.so')
            buildcmd =  comm.PackTools + "crosswalk-app build"
            buildstatus = commands.getstatusoutput(buildcmd)
            self.assertEquals(buildstatus[0], 0)
            os.chdir('pkg')
            pkgs = os.listdir(os.getcwd())
            self.assertNotIn("test-debug.armeabi-v7a.apk", pkgs)
        else:
            os.remove(os.getcwd() + '/prj/android/xwalk_core_library/libs/x86/libxwalkcore.so')
            buildcmd =  comm.PackTools + "crosswalk-app build"
            buildstatus = commands.getstatusoutput(buildcmd)
            self.assertEquals(buildstatus[0], 0)
            os.chdir('pkg')
            pkgs = os.listdir(os.getcwd())
            self.assertNotIn("test-debug.x86.apk", pkgs)
        comm.run(self)
        comm.clear("org.xwalk.test")

    def test_build_missing_both_so_file(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        os.remove(os.getcwd() + '/prj/android/xwalk_core_library/libs/armeabi-v7a/libxwalkcore.so')
        os.remove(os.getcwd() + '/prj/android/xwalk_core_library/libs/x86/libxwalkcore.so')
        buildcmd =  comm.PackTools + "crosswalk-app build"
        buildstatus = commands.getstatusoutput(buildcmd)
        comm.clear("org.xwalk.test")
        self.assertEquals(buildstatus[0], 1)

if __name__ == '__main__':
    unittest.main()
