#!/usr/bin/env python
#
# Copyright (c) 2016 Intel Corporation.
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
#         Liu, Yun <yunx.liu@intel.com>

import unittest
import os
import comm


class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_setting_value(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip + " ../../testapp/manifest_xwalk_target_platforms/windows_platform/"
        (return_code, output) = comm.getstatusoutput(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    if comm.BIT == "64":
                        self.assertIn("64", apks[i])
                    apkLength = apkLength + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    if comm.BIT == "64":
                        self.assertIn("64", apks[i])
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 2)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertIn("Loading 'android' platform backend", output[0])
        self.assertNotIn("Loading 'windows' platform backend", output[0])

    def test_without_platforms(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --android=" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip + " ../../testapp/create_package_basic/"
        (return_code, output) = comm.getstatusoutput(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    if comm.BIT == "64":
                        self.assertIn("64", apks[i])
                    apkLength = apkLength + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    if comm.BIT == "64":
                        self.assertIn("64", apks[i])
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 2)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertIn("Loading 'android' platform backend", output[0])

    def test_with_target_platforms(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --android=" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip + " ../../testapp/manifest_xwalk_target_platforms/android_platform/"
        (return_code, output) = comm.getstatusoutput(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    if comm.BIT == "64":
                        self.assertIn("64", apks[i])
                    apkLength = apkLength + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    if comm.BIT == "64":
                        self.assertIn("64", apks[i])
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 2)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertIn("Loading 'android' platform backend", output[0])

if __name__ == '__main__':
    unittest.main()
