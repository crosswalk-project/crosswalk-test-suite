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


class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_create_package_relative_path(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip + " ../../testapp/create_package_basic/"
        return_code = os.system(cmd)
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

    def test_create_package_non_exist_relative_path(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip + " ../../testapp/non_exist_path/"
        return_code = os.system(cmd)
        comm.clear("org.xwalk.test")
        self.assertNotEquals(return_code, 0)

    def test_create_package_non_exist_path(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip + " " + comm.ConstPath + "/../testapp/non_exist_path/"
        return_code = os.system(cmd)
        comm.clear("org.xwalk.test")
        self.assertNotEquals(return_code, 0)

    def test_create_package_missing_path(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip
        return_code = os.system(cmd)
        comm.clear("org.xwalk.test")
        self.assertNotEquals(return_code, 0)

    def test_create_package_missing_manifest(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip + " " + comm.ConstPath + "/../testapp/start_url/"
        return_code = os.system(cmd)
        comm.clear("org.xwalk.test")
        self.assertNotEquals(return_code, 0)

    def test_create_package_missing_manifest_relative_path(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip + " ../../testapp/start_url/"
        return_code = os.system(cmd)
        comm.clear("org.xwalk.test")
        self.assertNotEquals(return_code, 0)

    def test_create_package_filepath(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip + " " + comm.ConstPath + "/../testapp/create_package_basic/manifest.json"
        return_code = os.system(cmd)
        comm.clear("org.xwalk.test")
        self.assertNotEquals(return_code, 0)

    def test_create_package_relative_filepath(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip + " ../../testapp/create_package_basic/manifest.json"
        return_code = os.system(cmd)
        comm.clear("org.xwalk.test")
        self.assertNotEquals(return_code, 0)

    def test_create_package_missing_icon_startUrl(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip + " " + comm.ConstPath + "/../testapp/create_package_missing_icon_startUrl/"
        return_code = os.system(cmd)
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

    def test_create_package_stable(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + ' --crosswalk=stable --targets="' + comm.BIT + '" ' + comm.ConstPath + "/../testapp/create_package_basic/"
        (return_code, output) = comm.getstatusoutput(cmd)
        version = comm.check_crosswalk_version(self, "stable")
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
        self.assertIn(version, output[0])

    def test_create_package_beta(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + ' --crosswalk=beta --targets="' + comm.BIT + '" ' + comm.ConstPath + "/../testapp/create_package_basic/"
        (return_code, output) = comm.getstatusoutput(cmd)
        version = comm.check_crosswalk_version(self, "beta")
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
        self.assertIn(version, output[0])

    def test_create_package_canary(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + ' --crosswalk=canary --targets="' + comm.BIT + '" ' + comm.ConstPath + "/../testapp/create_package_basic/"
        (return_code, output) = comm.getstatusoutput(cmd)
        version = comm.check_crosswalk_version(self, "canary")
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
        self.assertIn(version, output[0])

    def test_build_package_release(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " --release=true --crosswalk=" + comm.crosswalkzip + " " + comm.ConstPath + "/../testapp/create_package_basic/"
        return_code = os.system(cmd)
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

    def test_create_package_reading_manifest(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        if os.path.exists(comm.ConstPath + "/../testapp/start_url/manifest.json"):
            os.remove(comm.ConstPath + "/../testapp/start_url/manifest.json")
        os.chdir('org.xwalk.test')
        if comm.SHELL_FLAG == "False":
            cmd = comm.HOST_PREFIX + comm.PackTools + \
                "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip + ' --manifest "{ """xwalk_package_id""": """org.xwalk.test""", """start_url""": """start.html""" }" ' + comm.ConstPath + "/../testapp/start_url/"
        else:
            cmd = comm.HOST_PREFIX + comm.PackTools + \
                "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip + " --manifest '{ \"xwalk_package_id\": \"org.xwalk.test\", \"start_url\": \"start.html\" }' " + comm.ConstPath + "/../testapp/start_url/"
        return_code = os.system(cmd)
        with open(comm.ConstPath + "/../testapp/start_url/manifest.json") as json_file:
            data = json.load(json_file)
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
        os.remove(comm.ConstPath + "/../testapp/start_url/manifest.json")
        self.assertEquals(return_code, 0)
        self.assertEquals(data['xwalk_package_id'].strip(os.linesep), "org.xwalk.test")

    def test_extensions_without_jsFile(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        shutil.copytree(comm.ConstPath + "/../testapp/extension_permission/", comm.XwalkPath + "/org.xwalk.test/extension_permission/")
        os.remove(comm.XwalkPath + "/org.xwalk.test/extension_permission/contactextension/contactextension.js")
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip + " " + comm.XwalkPath + "/org.xwalk.test/extension_permission/"
        return_code = os.system(cmd)
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

    def test_external_extensions_way(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " --keep --crosswalk=canary " + comm.ConstPath + "/../testapp/extension_permission/"
        (return_code, output) = comm.getstatusoutput(cmd)
        projectDir = output[0].split(" * " + os.linesep)[-1].split(' ')[-1].strip(os.linesep)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertNotIn("extensions-config.json", os.listdir(projectDir + "/prj/android/assets/"))
        self.assertIn("contactextension", os.listdir(projectDir + "/prj/android/assets/xwalk-extensions/"))
        self.assertIn("contactextension.js", os.listdir(projectDir + "/prj/android/assets/xwalk-extensions/contactextension/"))
        self.assertIn("contactextension.json", os.listdir(projectDir + "/prj/android/assets/xwalk-extensions/contactextension/"))

    def test_create_package_skip_dummy_using_s_option(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " -s --crosswalk=" + comm.crosswalkzip + " " + comm.ConstPath + "/../testapp/create_package_basic/"
        (return_code, output) = comm.getstatusoutput(cmd)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertIn("Skipping host setup check", output[0])

    def test_create_package_skip_dummy_using_skip_check_option(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " --skip-check --crosswalk=" + comm.crosswalkzip + " " + comm.ConstPath + "/../testapp/create_package_basic/"
        (return_code, output) = comm.getstatusoutput(cmd)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertIn("Skipping host setup check", output[0])

    def test_create_package_skip_dummy_default_in_subprocess(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip + " " + comm.ConstPath + "/../testapp/create_package_basic/"
        (return_code, output) = comm.getstatusoutput(cmd)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertIn("Skipping host setup check", output[0])

    def test_create_package_skip_dummy_no(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " -s no --crosswalk=" + comm.crosswalkzip + " " + comm.ConstPath + "/../testapp/create_package_basic/"
        (return_code, output) = comm.getstatusoutput(cmd)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertIn("Checking host setup", output[0])

    def test_create_package_default_non_interactive(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " --crosswalk=" + comm.crosswalkzip + " " + comm.ConstPath + "/../testapp/create_package_basic/ > 1.log 2>&1"
        (return_code, output) = comm.getstatusoutput(cmd)
        cmd = "cat 1.log"
        (return_code, output) = comm.getstatusoutput(cmd)
        comm.clear("org.xwalk.test")
        comm.clear("1.log")
        self.assertEquals(return_code, 0)
        self.assertIn("Skipping host setup check", output[0])
if __name__ == '__main__':
    unittest.main()
