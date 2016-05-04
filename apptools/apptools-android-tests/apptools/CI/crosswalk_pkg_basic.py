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

import re
import subprocess
import unittest
import os
import zipfile
import shutil
from xml.etree import ElementTree
import json
import sys
sys.path.append("../")
import comm


class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def invokeCrosswalkPkg(self, params=None):
        params = params or []
        cmdline = []
        if comm.HOST_PREFIX:
            cmdline.append(comm.HOST_PREFIX)
        cmdline.extend([os.path.join(comm.PackTools, 'crosswalk-pkg')])
        cmdline.extend(params)
        process = subprocess.Popen(cmdline, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        output, _ = process.communicate()
        self.assertEquals(process.returncode, 0)
        return output

    def test_path_absolute(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        output = self.invokeCrosswalkPkg([
            '--platforms=android',
            '--android=' + comm.ANDROID_MODE,
            '--crosswalk=' + comm.crosswalkzip,
            '--targets=' + comm.BIT,
            comm.ConstPath + '/../testapp/create_package_basic/',
        ])
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
        self.assertIn("target android", output)
        self.assertNotIn("candle", output)
        self.assertNotIn("light", output)

    def test_default_channel(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        output = self.invokeCrosswalkPkg([
            '--platforms=android',
            '--android=' + comm.ANDROID_MODE,
            '--targets=' + comm.BIT,
            comm.ConstPath + '/../testapp/create_package_basic/',
        ])
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
        self.assertIn(version, output)

    def test_crosswalk_release(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        self.invokeCrosswalkPkg([
            '--platforms=android',
            '--android=' + comm.ANDROID_MODE,
            '--crosswalk=' + comm.crosswalkzip,
            '--targets=' + comm.BIT,
            comm.ConstPath + '/../testapp/create_package_basic/',
        ])
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

    def test_crosswalk_build(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        crosswalkdir = zipfile.ZipFile(comm.crosswalkzip,'r')
        for file in crosswalkdir.namelist():
            crosswalkdir.extract(file, r'.')
        crosswalkdir.close()
        os.chdir('org.xwalk.test')
        self.invokeCrosswalkPkg([
            '--platforms=android',
            '--android=' + comm.ANDROID_MODE,
            '--crosswalk=' + comm.crosswalkzip[:-4] + '/',
            '--targets=' + comm.BIT,
            comm.ConstPath + '/../testapp/create_package_basic/',
        ])
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
        shutil.rmtree(comm.crosswalkzip[:-4])

    def test_release_without_argument(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        self.invokeCrosswalkPkg([
            '--platforms=android',
            '--android=' + comm.ANDROID_MODE,
            '--release',
            '--crosswalk=' + comm.crosswalkzip,
            '--targets=' + comm.BIT,
            comm.ConstPath + '/../testapp/create_package_basic/',
        ])
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

    def test_crosswalk_version(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        self.invokeCrosswalkPkg([
            '--platforms=android',
            '--android=' + comm.ANDROID_MODE,
            '--crosswalk=' + comm.crosswalkVersion,
            '--targets=' + comm.BIT,
            comm.ConstPath + '/../testapp/create_package_basic/',
        ])
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

    def test_manifest_packageId(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        if os.path.exists(comm.ConstPath + "/../testapp/start_url/manifest.json"):
            os.remove(comm.ConstPath + "/../testapp/start_url/manifest.json")
        os.chdir('org.xwalk.test')
        self.invokeCrosswalkPkg(['--platforms=android',
                                 '--android=' + comm.ANDROID_MODE,
                                 '--crosswalk=' + comm.crosswalkzip,
                                 '--manifest=org.xwalk.test',
                                 '--targets=' + comm.BIT,
                                 comm.ConstPath + '/../testapp/start_url/'])
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
        self.assertEquals(data['xwalk_package_id'].strip(os.linesep), "org.xwalk.test")

    def test_keep_project(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        output = self.invokeCrosswalkPkg([
            '--platforms=android',
            '--android=' + comm.ANDROID_MODE,
            '--keep',
            '--crosswalk=' + comm.crosswalkzip,
            '--targets=' + comm.BIT,
            comm.ConstPath + '/../testapp/create_package_basic/',
        ])
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
        project_dir = None
        for line in output.split('\n'):
            match = re.search(r'Keeping build tree in (.+)$', line)
            if match is not None:
                project_dir = match.group(1)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertTrue(os.path.isdir(project_dir))
        self.assertTrue(os.path.isdir(os.path.join(project_dir, "app")))
        self.assertTrue(os.path.isdir(os.path.join(project_dir, "prj")))

    def test_target_arch(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        if comm.BIT == "64":
            self.invokeCrosswalkPkg([
                '--platforms=android',
                '--android=' + comm.ANDROID_MODE,
                '--crosswalk=' + comm.crosswalkzip,
                '--targets=arm64-v8a x86_64',
                comm.ConstPath + '/../testapp/create_package_basic/',
            ])
        else:
            self.invokeCrosswalkPkg([
                '--platforms=android',
                '--android=' + comm.ANDROID_MODE,
                '--crosswalk=' + comm.crosswalkzip,
                '--targets=armeabi-v7a x86',
                comm.ConstPath + '/../testapp/create_package_basic/',
            ])
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

    def test_target_a_x(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        self.invokeCrosswalkPkg([
            '--platforms=android',
            '--android=' + comm.ANDROID_MODE,
            '--crosswalk=canary',
            '--targets=a x',
            comm.ConstPath + '/../testapp/create_package_basic/',
        ])
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
            self.assertEquals(x86Length, 1)
            self.assertEquals(armLength, 1)
        else:
            for i in range(len(apks)):
                if apks[i].endswith(".apk") and "shared" in apks[i]:
                    apkLength = apkLength + 1
                    appVersion = apks[i].split('-')[1]
            self.assertEquals(apkLength, 1)
        comm.clear("org.xwalk.test")

    def test_tools_version(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        self.assertEquals(self.invokeCrosswalkPkg(['--version']),
                          self.invokeCrosswalkPkg(['--v']))
        version_output = self.invokeCrosswalkPkg(['--version'])
        with open(comm.PackTools + "../package.json") as json_file:
            data = json.load(json_file)
        self.assertEquals(data['version'], version_output.strip())

if __name__ == '__main__':
    unittest.main()
