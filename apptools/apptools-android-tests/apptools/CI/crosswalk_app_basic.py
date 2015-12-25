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
import shutil
import json
from xml.etree import ElementTree
import sys
sys.path.append("../")
import comm


class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_tools_version(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        cmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app version"
        (return_code, output) = comm.getstatusoutput(cmd)
        with open(comm.PackTools + "../package.json") as json_file:
            data = json.load(json_file)
        self.assertEquals(
            data['version'].strip(os.linesep),
            output[0].strip(os.linesep))

    def test_build_debug(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build"
        comm.build(self, buildcmd)
        comm.run(self)
        comm.clear("org.xwalk.test")

    def test_check_host_without_platforms(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        cmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app check"
        (return_code, output) = comm.getstatusoutput(cmd)
        self.assertEquals(return_code, 0)

    def test_check_host_android(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        cmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app check android"
        (return_code, output) = comm.getstatusoutput(cmd)
        self.assertEquals(return_code, 0)
        self.assertNotIn("ERROR:", output[0])

    def test_target_create(self):
        comm.setUp()
        if comm.SHELL_FLAG == "False":
            cmd = "where android"
        else:
            cmd = "which android"
        (return_code, androidpath) = comm.getstatusoutput(cmd)
        targetversionpath = os.path.dirname(os.path.dirname(androidpath[0]))
        os.rename(targetversionpath + "/platforms/", targetversionpath + "/backup/")
        comm.clear("org.xwalk.test")
        os.chdir(comm.XwalkPath)
        createcmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-app create org.xwalk.test" + comm.MODE + " --android-crosswalk=" + \
            comm.crosswalkzip
        (return_create_code, output) = comm.getstatusoutput(createcmd)
        os.rename(targetversionpath + "/backup/", targetversionpath + "/platforms/")
        comm.clear("org.xwalk.test")
        self.assertNotEquals(return_create_code, 0)

    def test_target_build(self):
        comm.setUp()
        comm.clear("org.xwalk.test")
        os.chdir(comm.XwalkPath)
        comm.create(self)
        if comm.SHELL_FLAG == "False":
            cmd = "where android"
        else:
            cmd = "which android"
        (return_code, androidpath) = comm.getstatusoutput(cmd)
        targetversionpath = os.path.dirname(os.path.dirname(androidpath[0]))
        os.rename(targetversionpath + "/platforms/", targetversionpath + "/backup/")
        os.chdir(comm.XwalkPath + "org.xwalk.test")
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build"
        (return_build_code, buildstatus) = comm.getstatusoutput(buildcmd)
        os.rename(targetversionpath + "/backup/", targetversionpath + "/platforms/")
        comm.clear("org.xwalk.test")
        self.assertNotEquals(return_build_code, 0)
        self.assertIn("project target", buildstatus[0])

    def test_create_with_platform_android(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        cmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app create org.xwalk.test" + comm.MODE + " --platform=android --android-crosswalk=" + comm.crosswalkzip
        packstatus = os.system(cmd)
        self.assertEquals(packstatus, 0)
        os.chdir('org.xwalk.test')
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build"
        comm.build(self, buildcmd)
        comm.run(self)
        comm.clear("org.xwalk.test")

    def test_init_manifest_androidPlatforms(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-app manifest " + \
            comm.XwalkPath + "org.xwalk.test --platform=android"
        os.system(cmd)
        with open(comm.ConstPath + "/../tools/org.xwalk.test/manifest.json") as json_file:
            data = json.load(json_file)
        comm.clear("org.xwalk.test")
        self.assertEquals(data['xwalk_target_platforms'][0].strip(os.linesep), "android")

    def test_init_manifest_packageid(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-app manifest " + \
            comm.XwalkPath + "org.xwalk.test --platform=android --package-id=org.xwalk.test"
        os.system(cmd)
        with open(comm.ConstPath + "/../tools/org.xwalk.test/manifest.json") as json_file:
            data = json.load(json_file)
        updatecmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-app manifest " + \
            comm.XwalkPath + "org.xwalk.test --platform=android --package-id=org.test.foo"
        os.system(updatecmd)
        with open(comm.ConstPath + "/../tools/org.xwalk.test/manifest.json") as json_file_update:
            updatedata = json.load(json_file_update)
        comm.clear("org.xwalk.test")
        self.assertEquals(data['xwalk_package_id'].strip(os.linesep), "org.xwalk.test")
        self.assertEquals(updatedata['xwalk_package_id'].strip(os.linesep), "org.test.foo")

    def test_list_target_platforms(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        cmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app platforms"
        status = os.popen(cmd).readlines()
        self.assertEquals("android", status[0].strip(" * " + os.linesep))

if __name__ == '__main__':
    unittest.main()
