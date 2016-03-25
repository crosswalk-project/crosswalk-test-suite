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
#         Yun, Liu<yunx.liu@intel.com>

import unittest
import os
import comm
import zipfile
import shutil
from xml.etree import ElementTree
import json

x86Length = 0
x86_64Length = 0
armLength = 0
arm_64Length = 0
apkLength = 0

class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_create_package_target_bit_crosswalkzip(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip + ' --targets="32 64" ' + comm.ConstPath + "/../testapp/create_package_basic/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
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
            if comm.BIT == "64":
                self.assertEquals(x86_64Length, 1)
                self.assertEquals(arm_64Length, 1)
                self.assertEquals(x86Length, 0)
                self.assertEquals(armLength, 0)
            else:
                self.assertEquals(x86_64Length, 0)
                self.assertEquals(arm_64Length, 0)
                self.assertEquals(x86Length, 1)
                self.assertEquals(armLength, 1)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_package_target_bit_crosswalkdir(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        crosswalkdir = zipfile.ZipFile(comm.crosswalkzip,'r')
        for file in crosswalkdir.namelist():
            crosswalkdir.extract(file, r'.')
        crosswalkdir.close()
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip[:comm.crosswalkzip.index(".zip")] + ' --targets="32 64" ' + comm.ConstPath + "/../testapp/create_package_basic/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
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
            if comm.BIT == "64":
                self.assertEquals(x86_64Length, 1)
                self.assertEquals(arm_64Length, 1)
                self.assertEquals(x86Length, 0)
                self.assertEquals(armLength, 0)
            else:
                self.assertEquals(x86_64Length, 0)
                self.assertEquals(arm_64Length, 0)
                self.assertEquals(x86Length, 1)
                self.assertEquals(armLength, 1)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.run(self)
        comm.clear("org.xwalk.test")
        shutil.rmtree(comm.crosswalkzip[:comm.crosswalkzip.index(".zip")])
        self.assertEquals(return_code, 0)

    def test_create_package_target_bit(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + ' --targets="' + comm.BIT + '"  -c canary ' + comm.ConstPath + "/../testapp/create_package_basic/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
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
            if comm.BIT == "64":
                self.assertEquals(x86_64Length, 1)
                self.assertEquals(arm_64Length, 1)
                self.assertEquals(x86Length, 0)
                self.assertEquals(armLength, 0)
            else:
                self.assertEquals(x86_64Length, 0)
                self.assertEquals(arm_64Length, 0)
                self.assertEquals(x86Length, 1)
                self.assertEquals(armLength, 1)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_package_target_ar_x8(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + ' --targets="ar x8" -c canary ' + comm.ConstPath + "/../testapp/create_package_basic/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
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
            self.assertEquals(x86Length, 1)
            self.assertEquals(armLength, 1)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_package_target_arm_x86(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + ' --targets="arm x86" -c canary ' + comm.ConstPath + "/../testapp/create_package_basic/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
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
            self.assertEquals(x86Length, 1)
            self.assertEquals(armLength, 1)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_package_target_arm(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + ' --targets="arm" -c canary ' + comm.ConstPath + "/../testapp/create_package_basic/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
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
            self.assertEquals(armLength, 1)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_package_target_invalid(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + ' --targets="invalid" -c canary ' + comm.ConstPath + "/../testapp/create_package_basic/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
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
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_package_target_armeabi_x8(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + ' -t "armeabi-v7a x8" -c canary ' + comm.ConstPath + "/../testapp/create_package_basic/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
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
            self.assertEquals(x86Length, 1)
            self.assertEquals(armLength, 1)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_package_target_arm_invalid(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + ' -t "arm invalid" -c canary ' + comm.ConstPath + "/../testapp/create_package_basic/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
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
            self.assertEquals(armLength, 1)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_package_target_x86_invalid(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + ' -t "x86 invalid" -c canary ' + comm.ConstPath + "/../testapp/create_package_basic/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
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
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_package_target_arm_32(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + ' --targets="arm 32" -c canary ' + comm.ConstPath + "/../testapp/create_package_basic/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
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
            self.assertEquals(x86Length, 1)
            self.assertEquals(armLength, 1)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_package_target_x86_64(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + ' --targets="x86 64" -c canary ' + comm.ConstPath + "/../testapp/create_package_basic/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
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
            self.assertEquals(x86Length, 1)
            self.assertEquals(armLength, 0)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

if __name__ == '__main__':
    unittest.main()
