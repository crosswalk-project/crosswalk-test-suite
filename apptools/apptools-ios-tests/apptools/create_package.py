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
import commands
import comm
from xml.etree import ElementTree
import json


class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_multiple_backends(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.PackTools + 'crosswalk-pkg --platforms="ios android" ' + comm.ConstPath + "/../testapp/create_package_basic/"
        packstatus = commands.getstatusoutput(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        ipaLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".apk") and "x86" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".apk") and "arm" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".ipa"):
                ipaLength = ipaLength + 1
        comm.clear("org.xwalk.test")
        self.assertEquals(packstatus[0], 0)
        self.assertEquals(apkLength, 2)
        self.assertEquals(ipaLength, 1)

    def test_path_absolute(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.PackTools + "crosswalk-pkg --platforms=ios " + comm.ConstPath + "/../testapp/create_package_basic/"
        packstatus = commands.getstatusoutput(cmd)
        apks = os.listdir(os.getcwd())
        ipaLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".ipa"):
                ipaLength = ipaLength + 1
        comm.clear("org.xwalk.test")
        self.assertEquals(packstatus[0], 0)
        self.assertEquals(ipaLength, 1)

    def test_path_relative(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.PackTools + "crosswalk-pkg --platforms=ios ../../testapp/create_package_basic/"
        packstatus = commands.getstatusoutput(cmd)
        apks = os.listdir(os.getcwd())
        ipaLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".ipa"):
                ipaLength = ipaLength + 1
        comm.clear("org.xwalk.test")
        self.assertEquals(packstatus[0], 0)
        self.assertEquals(ipaLength, 1)

    def test_non_exist_path_absolute(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.PackTools + "crosswalk-pkg --platforms=ios " + comm.ConstPath + "/../testapp/non_exist_path/"
        packstatus = commands.getstatusoutput(cmd)
        comm.clear("org.xwalk.test")
        self.assertNotEquals(packstatus[0], 0)

    def test_non_exist_path_relative(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.PackTools + "crosswalk-pkg --platforms=ios ../../testapp/non_exist_path/"
        packstatus = commands.getstatusoutput(cmd)
        comm.clear("org.xwalk.test")
        self.assertNotEquals(packstatus[0], 0)

    def test_missing_path(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.PackTools + "crosswalk-pkg --platforms=ios"
        packstatus = commands.getstatusoutput(cmd)
        comm.clear("org.xwalk.test")
        self.assertNotEquals(packstatus[0], 0)

    def test_missing_manifest_path_absolute(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.PackTools + "crosswalk-pkg --platforms=ios " + comm.ConstPath + "/../testapp/start_url/"
        packstatus = commands.getstatusoutput(cmd)
        comm.clear("org.xwalk.test")
        self.assertNotEquals(packstatus[0], 0)

    def test_missing_manifest_path_relative(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.PackTools + "crosswalk-pkg --platforms=ios ../../testapp/start_url/"
        packstatus = commands.getstatusoutput(cmd)
        comm.clear("org.xwalk.test")
        self.assertNotEquals(packstatus[0], 0)

    def test_filepath_absolute(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.PackTools + "crosswalk-pkg --platforms=ios " + comm.ConstPath + "/../testapp/create_package_basic/manifest.json"
        packstatus = commands.getstatusoutput(cmd)
        comm.clear("org.xwalk.test")
        self.assertNotEquals(packstatus[0], 0)

    def test_filepath_relative(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.PackTools + "crosswalk-pkg --platforms=ios ../../testapp/create_package_basic/manifest.json"
        packstatus = commands.getstatusoutput(cmd)
        comm.clear("org.xwalk.test")
        self.assertNotEquals(packstatus[0], 0)

    def test_missing_icon_startUrl(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.PackTools + "crosswalk-pkg -p ios " + comm.ConstPath + "/../testapp/create_package_missing_icon_startUrl/"
        packstatus = commands.getstatusoutput(cmd)
        apks = os.listdir(os.getcwd())
        ipaLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".ipa"):
                ipaLength = ipaLength + 1
        comm.clear("org.xwalk.test")
        self.assertEquals(packstatus[0], 0)
        self.assertEquals(ipaLength, 1)

    def test_build_release(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.PackTools + "crosswalk-pkg --platforms=ios --release=true " + comm.ConstPath + "/../testapp/create_package_basic/"
        packstatus = commands.getstatusoutput(cmd)
        apks = os.listdir(os.getcwd())
        ipaLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".ipa"):
                ipaLength = ipaLength + 1
        comm.clear("org.xwalk.test")
        self.assertEquals(packstatus[0], 0)
        self.assertEquals(ipaLength, 1)

    def test_build_release_without_argument(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.PackTools + "crosswalk-pkg --platforms=ios -r " + comm.ConstPath + "/../testapp/create_package_basic/"
        packstatus = commands.getstatusoutput(cmd)
        apks = os.listdir(os.getcwd())
        ipaLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".ipa"):
                ipaLength = ipaLength + 1
        comm.clear("org.xwalk.test")
        self.assertEquals(packstatus[0], 0)
        self.assertEquals(ipaLength, 1)

    def test_manifest_packageId(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        if os.path.exists(comm.ConstPath + "/../testapp/start_url/manifest.json"):
            os.remove(comm.ConstPath + "/../testapp/start_url/manifest.json")
        os.chdir('org.xwalk.test')
        cmd = comm.PackTools + "crosswalk-pkg --platforms=ios --manifest=org.xwalk.test " + comm.ConstPath + "/../testapp/start_url/"
        packstatus = commands.getstatusoutput(cmd)
        apks = os.listdir(os.getcwd())
        ipaLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".ipa"):
                ipaLength = ipaLength + 1
        comm.clear("org.xwalk.test")
        os.remove(comm.ConstPath + "/../testapp/start_url/manifest.json")
        self.assertEquals(packstatus[0], 0)
        self.assertEquals(ipaLength, 1)

    def test_reading_manifest(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        if os.path.exists(comm.ConstPath + "/../testapp/start_url/manifest.json"):
            os.remove(comm.ConstPath + "/../testapp/start_url/manifest.json")
        os.chdir('org.xwalk.test')
        cmd = comm.PackTools + 'crosswalk-pkg --platforms=ios -m "{ """xwalk_package_id""": """org.xwalk.test""", """start_url""": """start.html""" }" ' + comm.ConstPath + "/../testapp/start_url/"
        packstatus = commands.getstatusoutput(cmd)
        apks = os.listdir(os.getcwd())
        ipaLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".ipa"):
                ipaLength = ipaLength + 1
        comm.clear("org.xwalk.test")
        os.remove(comm.ConstPath + "/../testapp/start_url/manifest.json")
        self.assertEquals(packstatus[0], 0)
        self.assertEquals(ipaLength, 1)

    def test_keep_project(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.PackTools + "crosswalk-pkg --platforms=ios --keep " + comm.ConstPath + "/../testapp/create_package_basic/"
        packstatus = commands.getstatusoutput(cmd)
        apks = os.listdir(os.getcwd())
        ipaLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".ipa"):
                ipaLength = ipaLength + 1
        projectDir = packstatus[1].split(" * " + os.linesep)[-1].split(' ')[-1].strip(os.linesep)
        comm.clear("org.xwalk.test")
        self.assertEquals(packstatus[0], 0)
        self.assertEquals(ipaLength, 1)
        self.assertIn("app", os.listdir(projectDir))
        self.assertIn("prj", os.listdir(projectDir))

    def test_keep_project_k(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.PackTools + "crosswalk-pkg --platforms=ios -k " + comm.ConstPath + "/../testapp/create_package_basic/"
        packstatus = commands.getstatusoutput(cmd)
        apks = os.listdir(os.getcwd())
        ipaLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".ipa"):
                ipaLength = ipaLength + 1
        projectDir = packstatus[1].split(" * " + os.linesep)[-1].split(' ')[-1].strip(os.linesep)
        comm.clear("org.xwalk.test")
        self.assertEquals(packstatus[0], 0)
        self.assertEquals(ipaLength, 1)
        self.assertIn("app", os.listdir(projectDir))
        self.assertIn("prj", os.listdir(projectDir))

    def test_tools_version(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        cmd = comm.PackTools + "crosswalk-pkg --version"
        packstatus = commands.getstatusoutput(cmd)
        cmd_1 = comm.PackTools + "crosswalk-pkg -v"
        packstatus_1 = commands.getstatusoutput(cmd_1)
        with open(comm.PackTools + "../package.json") as json_file:
            data = json.load(json_file)
        self.assertEquals(data['version'].strip(os.linesep), packstatus[1].strip(os.linesep))
        self.assertEquals(data['version'].strip(os.linesep), packstatus_1[1].strip(os.linesep))

if __name__ == '__main__':
    unittest.main()
