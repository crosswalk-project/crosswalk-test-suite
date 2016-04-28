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
#         Yun, Liu<yunx.liu@intel.com>

import unittest
import os
import comm
import shutil


class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_create_arm32(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-app create org.xwalk.test" + comm.MODE + " --android-crosswalk=canary --android-targets=armeabi-v7a"
        (return_create_code, output) = comm.getstatusoutput(cmd)
        crosswalkVersion = comm.check_crosswalk_version(self, "canary")
        self.assertEquals(return_create_code, 0)
        self.assertIn('crosswalk-{}.zip'.format(crosswalkVersion), output[0])
        self.assertNotIn('crosswalk-{}-64bit.zip'.format(crosswalkVersion), output[0])
        os.chdir(comm.XwalkPath + 'org.xwalk.test')
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build"
        return_code = os.system(buildcmd)
        apks = os.listdir(os.getcwd())
        x86Length = 0
        x86_64Length = 0
        armLength = 0
        arm_64Length = 0
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    if "64" in apks[i]:
                        x86_64Length = x86_64Length + 1
                    else:
                        x86Length = x86Length + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    if "64" in apks[i]:
                        arm_64Length = arm_64Length + 1
                    else:
                        armLength = armLength + 1
            self.assertEquals(x86_64Length, 0)
            self.assertEquals(arm_64Length, 0)
            self.assertEquals(x86Length, 1)
            self.assertEquals(armLength, 1)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_x8632(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-app create org.xwalk.test" + comm.MODE + " --android-crosswalk=canary --android-targets=x86"
        (return_create_code, output) = comm.getstatusoutput(cmd)
        crosswalkVersion = comm.check_crosswalk_version(self, "canary")
        self.assertEquals(return_create_code, 0)
        self.assertIn('crosswalk-{}.zip'.format(crosswalkVersion), output[0])
        self.assertNotIn('crosswalk-{}-64bit.zip'.format(crosswalkVersion), output[0])
        os.chdir(comm.XwalkPath + 'org.xwalk.test')
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build"
        return_code = os.system(buildcmd)
        apks = os.listdir(os.getcwd())
        x86Length = 0
        x86_64Length = 0
        armLength = 0
        arm_64Length = 0
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    if "64" in apks[i]:
                        x86_64Length = x86_64Length + 1
                    else:
                        x86Length = x86Length + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    if "64" in apks[i]:
                        arm_64Length = arm_64Length + 1
                    else:
                        armLength = armLength + 1
            self.assertEquals(x86_64Length, 0)
            self.assertEquals(arm_64Length, 0)
            self.assertEquals(x86Length, 1)
            self.assertEquals(armLength, 1)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_arm64(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-app create org.xwalk.test" + comm.MODE + " --android-crosswalk=canary --android-targets=arm64-v8a"
        (return_create_code, output) = comm.getstatusoutput(cmd)
        crosswalkVersion = comm.check_crosswalk_version(self, "canary")
        self.assertEquals(return_create_code, 0)
        self.assertNotIn('crosswalk-{}.zip'.format(crosswalkVersion), output[0])
        self.assertIn('crosswalk-{}-64bit.zip'.format(crosswalkVersion), output[0])
        os.chdir(comm.XwalkPath + 'org.xwalk.test')
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build"
        return_code = os.system(buildcmd)
        apks = os.listdir(os.getcwd())
        x86Length = 0
        x86_64Length = 0
        armLength = 0
        arm_64Length = 0
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    if "64" in apks[i]:
                        x86_64Length = x86_64Length + 1
                    else:
                        x86Length = x86Length + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    if "64" in apks[i]:
                        arm_64Length = arm_64Length + 1
                    else:
                        armLength = armLength + 1
            self.assertEquals(x86_64Length, 1)
            self.assertEquals(arm_64Length, 1)
            self.assertEquals(x86Length, 0)
            self.assertEquals(armLength, 0)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_x8664(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-app create org.xwalk.test" + comm.MODE + " --android-crosswalk=canary --android-targets=x86_64"
        (return_create_code, output) = comm.getstatusoutput(cmd)
        crosswalkVersion = comm.check_crosswalk_version(self, "canary")
        self.assertEquals(return_create_code, 0)
        self.assertNotIn('crosswalk-{}.zip'.format(crosswalkVersion), output[0])
        self.assertIn('crosswalk-{}-64bit.zip'.format(crosswalkVersion), output[0])
        os.chdir(comm.XwalkPath + 'org.xwalk.test')
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build"
        return_code = os.system(buildcmd)
        apks = os.listdir(os.getcwd())
        x86Length = 0
        x86_64Length = 0
        armLength = 0
        arm_64Length = 0
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    if "64" in apks[i]:
                        x86_64Length = x86_64Length + 1
                    else:
                        x86Length = x86Length + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    if "64" in apks[i]:
                        arm_64Length = arm_64Length + 1
                    else:
                        armLength = armLength + 1
            self.assertEquals(x86_64Length, 1)
            self.assertEquals(arm_64Length, 1)
            self.assertEquals(x86Length, 0)
            self.assertEquals(armLength, 0)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_arm64_x8664(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-app create org.xwalk.test" + comm.MODE + ' --android-crosswalk=canary --android-targets="arm64-v8a x86_64"'
        (return_create_code, output) = comm.getstatusoutput(cmd)
        crosswalkVersion = comm.check_crosswalk_version(self, "canary")
        self.assertEquals(return_create_code, 0)
        self.assertNotIn('crosswalk-{}.zip'.format(crosswalkVersion), output[0])
        self.assertIn('crosswalk-{}-64bit.zip'.format(crosswalkVersion), output[0])
        os.chdir(comm.XwalkPath + 'org.xwalk.test')
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build"
        return_code = os.system(buildcmd)
        apks = os.listdir(os.getcwd())
        x86Length = 0
        x86_64Length = 0
        armLength = 0
        arm_64Length = 0
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    if "64" in apks[i]:
                        x86_64Length = x86_64Length + 1
                    else:
                        x86Length = x86Length + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    if "64" in apks[i]:
                        arm_64Length = arm_64Length + 1
                    else:
                        armLength = armLength + 1
            self.assertEquals(x86_64Length, 1)
            self.assertEquals(arm_64Length, 1)
            self.assertEquals(x86Length, 0)
            self.assertEquals(armLength, 0)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_arm32_x8664(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-app create org.xwalk.test" + comm.MODE + ' --android-crosswalk=canary --android-targets="armeabi-v7a x86_64"'
        return_code = os.system(cmd)
        comm.clear("org.xwalk.test")
        self.assertNotEquals(return_code, 0)

    def test_build_arm32(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-app create org.xwalk.test" + comm.MODE + " --android-crosswalk=canary --android-targets=armeabi-v7a"
        os.system(cmd)
        os.chdir(comm.XwalkPath + 'org.xwalk.test')
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build --android-targets=armeabi-v7a ./"
        return_code = os.system(buildcmd)
        apks = os.listdir(os.getcwd())
        x86Length = 0
        x86_64Length = 0
        armLength = 0
        arm_64Length = 0
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    if "64" in apks[i]:
                        x86_64Length = x86_64Length + 1
                    else:
                        x86Length = x86Length + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    if "64" in apks[i]:
                        arm_64Length = arm_64Length + 1
                    else:
                        armLength = armLength + 1
            self.assertEquals(x86_64Length, 0)
            self.assertEquals(arm_64Length, 0)
            self.assertEquals(x86Length, 0)
            self.assertEquals(armLength, 1)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_build_x8632(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-app create org.xwalk.test" + comm.MODE + " --android-crosswalk=canary --android-targets=armeabi-v7a"
        os.system(cmd)
        os.chdir(comm.XwalkPath + 'org.xwalk.test')
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build --android-targets=x86 ./"
        return_code = os.system(buildcmd)
        apks = os.listdir(os.getcwd())
        x86Length = 0
        x86_64Length = 0
        armLength = 0
        arm_64Length = 0
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    if "64" in apks[i]:
                        x86_64Length = x86_64Length + 1
                    else:
                        x86Length = x86Length + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    if "64" in apks[i]:
                        arm_64Length = arm_64Length + 1
                    else:
                        armLength = armLength + 1
            self.assertEquals(x86_64Length, 0)
            self.assertEquals(arm_64Length, 0)
            self.assertEquals(x86Length, 1)
            self.assertEquals(armLength, 0)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_build_arm32_x8632(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-app create org.xwalk.test" + comm.MODE + " --android-crosswalk=canary --android-targets=armeabi-v7a"
        os.system(cmd)
        os.chdir(comm.XwalkPath + 'org.xwalk.test')
        buildcmd = comm.HOST_PREFIX + comm.PackTools + 'crosswalk-app build --android-targets="armeabi-v7a x86" ./'
        return_code = os.system(buildcmd)
        apks = os.listdir(os.getcwd())
        x86Length = 0
        x86_64Length = 0
        armLength = 0
        arm_64Length = 0
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    if "64" in apks[i]:
                        x86_64Length = x86_64Length + 1
                    else:
                        x86Length = x86Length + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    if "64" in apks[i]:
                        arm_64Length = arm_64Length + 1
                    else:
                        armLength = armLength + 1
            self.assertEquals(x86_64Length, 0)
            self.assertEquals(arm_64Length, 0)
            self.assertEquals(x86Length, 1)
            self.assertEquals(armLength, 1)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_build_arm32_x8664(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-app create org.xwalk.test" + comm.MODE + " --android-crosswalk=canary --android-targets=armeabi-v7a"
        os.system(cmd)
        os.chdir(comm.XwalkPath + 'org.xwalk.test')
        buildcmd = comm.HOST_PREFIX + comm.PackTools + 'crosswalk-app build --android-targets="armeabi-v7a x86_64" ./'
        return_code = os.system(buildcmd)
        apks = os.listdir(os.getcwd())
        x86Length = 0
        x86_64Length = 0
        armLength = 0
        arm_64Length = 0
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    if "64" in apks[i]:
                        x86_64Length = x86_64Length + 1
                    else:
                        x86Length = x86Length + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    if "64" in apks[i]:
                        arm_64Length = arm_64Length + 1
                    else:
                        armLength = armLength + 1
            self.assertEquals(x86_64Length, 0)
            self.assertEquals(arm_64Length, 0)
            self.assertEquals(x86Length, 0)
            self.assertEquals(armLength, 1)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_build_arm64(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-app create org.xwalk.test" + comm.MODE + " --android-crosswalk=canary --android-targets=x86_64"
        os.system(cmd)
        os.chdir(comm.XwalkPath + 'org.xwalk.test')
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build --android-targets=arm64-v8a ./"
        return_code = os.system(buildcmd)
        apks = os.listdir(os.getcwd())
        x86Length = 0
        x86_64Length = 0
        armLength = 0
        arm_64Length = 0
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    if "64" in apks[i]:
                        x86_64Length = x86_64Length + 1
                    else:
                        x86Length = x86Length + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    if "64" in apks[i]:
                        arm_64Length = arm_64Length + 1
                    else:
                        armLength = armLength + 1
            self.assertEquals(x86_64Length, 0)
            self.assertEquals(arm_64Length, 1)
            self.assertEquals(x86Length, 0)
            self.assertEquals(armLength, 0)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_build_x8664(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-app create org.xwalk.test" + comm.MODE + " --android-crosswalk=canary --android-targets=x86_64"
        os.system(cmd)
        os.chdir(comm.XwalkPath + 'org.xwalk.test')
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build --android-targets=x86_64 ./"
        return_code = os.system(buildcmd)
        apks = os.listdir(os.getcwd())
        x86Length = 0
        x86_64Length = 0
        armLength = 0
        arm_64Length = 0
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    if "64" in apks[i]:
                        x86_64Length = x86_64Length + 1
                    else:
                        x86Length = x86Length + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    if "64" in apks[i]:
                        arm_64Length = arm_64Length + 1
                    else:
                        armLength = armLength + 1
            self.assertEquals(x86_64Length, 1)
            self.assertEquals(arm_64Length, 0)
            self.assertEquals(x86Length, 0)
            self.assertEquals(armLength, 0)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_build_arm64_x8664(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-app create org.xwalk.test" + comm.MODE + " --android-crosswalk=canary --android-targets=x86_64"
        os.system(cmd)
        os.chdir(comm.XwalkPath + 'org.xwalk.test')
        buildcmd = comm.HOST_PREFIX + comm.PackTools + 'crosswalk-app build --android-targets="arm64-v8a x86_64" ./'
        return_code = os.system(buildcmd)
        apks = os.listdir(os.getcwd())
        x86Length = 0
        x86_64Length = 0
        armLength = 0
        arm_64Length = 0
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    if "64" in apks[i]:
                        x86_64Length = x86_64Length + 1
                    else:
                        x86Length = x86Length + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    if "64" in apks[i]:
                        arm_64Length = arm_64Length + 1
                    else:
                        armLength = armLength + 1
            self.assertEquals(x86_64Length, 1)
            self.assertEquals(arm_64Length, 1)
            self.assertEquals(x86Length, 0)
            self.assertEquals(armLength, 0)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_build_noABIs(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-app create org.xwalk.test" + comm.MODE + " --android-crosswalk=canary --android-targets=x86"
        os.system(cmd)
        os.chdir(comm.XwalkPath + 'org.xwalk.test')
        buildcmd = comm.HOST_PREFIX + comm.PackTools + 'crosswalk-app build --android-targets="arm64-v8a x86_64" ./'
        return_code = os.system(buildcmd)
        apks = os.listdir(os.getcwd())
        x86Length = 0
        x86_64Length = 0
        armLength = 0
        arm_64Length = 0
        apkLength = 0
        if comm.MODE != " --android-shared":
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "x86" in apks[i]:
                    if "64" in apks[i]:
                        x86_64Length = x86_64Length + 1
                    else:
                        x86Length = x86Length + 1
                if apks[i].endswith(".apk") and "arm" in apks[i]:
                    if "64" in apks[i]:
                        arm_64Length = arm_64Length + 1
                    else:
                        armLength = armLength + 1
            self.assertEquals(x86_64Length, 0)
            self.assertEquals(arm_64Length, 0)
            self.assertEquals(x86Length, 0)
            self.assertEquals(armLength, 0)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

if __name__ == '__main__':
    unittest.main()
