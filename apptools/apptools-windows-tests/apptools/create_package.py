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
import shutil
import urllib2
import zipfile
import json


class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_create_package_relative_path(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=windows --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk + " ../../testapp/create_package_basic/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".msi"):
                apkLength = apkLength + 1
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertEquals(apkLength, 1)

    def test_create_package_non_exist_path(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=windows --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk + " " + comm.ConstPath + "/../testapp/non_exist_path/"
        return_code = os.system(cmd)
        comm.clear("org.xwalk.test")
        self.assertNotEquals(return_code, 0)

    def test_create_package_non_exist_relative_path(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=windows --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk + " ../../testapp/non_exist_path/"
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
            "crosswalk-pkg --platforms=windows --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk
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
            "crosswalk-pkg --platforms=windows --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk + " " + comm.ConstPath + "/../testapp/start_url/"
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
            "crosswalk-pkg --platforms=windows --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk + " ../../testapp/start_url/"
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
            "crosswalk-pkg --platforms=windows --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk + " " + comm.ConstPath + "/../testapp/create_package_basic/manifest.json"
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
            "crosswalk-pkg --platforms=windows --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk + " ../../testapp/create_package_basic/manifest.json"
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
            "crosswalk-pkg --platforms=windows --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk + " " + comm.ConstPath + "/../testapp/create_package_missing_icon_startUrl/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".msi"):
                apkLength = apkLength + 1
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertEquals(apkLength, 1)

    def test_create_package_without_channel(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=windows " + comm.ConstPath + "/../testapp/create_package_basic/"
        (return_code, output) = comm.getstatusoutput(cmd)
        version = comm.check_crosswalk_version(self, "stable")
        crosswalk = 'crosswalk-{}.zip'.format(version)
        crosswalk64 = 'crosswalk64-{}.zip'.format(version)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".msi"):
                apkLength = apkLength + 1
        if not comm.cachedir:
            namelist = os.listdir(os.getcwd())
        else:
            newcachedir = os.environ.get('CROSSWALK_APP_TOOLS_CACHE_DIR')
            os.chdir(newcachedir)
            namelist = os.listdir(os.getcwd())
        crosswalkexist = 1
        if crosswalk not in namelist and crosswalk64 not in namelist:
            crosswalkexist = 0
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertIn("stable", output[0])
        self.assertIn(version, output[0])
        self.assertEquals(crosswalkexist, 1)
        self.assertEquals(apkLength, 1)

    def test_create_package_reading_manifest(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        if os.path.exists(comm.ConstPath + "/../testapp/start_url/manifest.json"):
            os.remove(comm.ConstPath + "/../testapp/start_url/manifest.json")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=windows --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk + ' --manifest "{ """xwalk_package_id""": """org.xwalk.test""", """start_url""": """start.html""" }" ' + comm.ConstPath + "/../testapp/start_url/"
        return_code = os.system(cmd)
        with open(comm.ConstPath + "/../testapp/start_url/manifest.json") as json_file:
            data = json.load(json_file)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".msi"):
                apkLength = apkLength + 1
        comm.clear("org.xwalk.test")
        os.remove(comm.ConstPath + "/../testapp/start_url/manifest.json")
        self.assertEquals(return_code, 0)
        self.assertEquals(data['xwalk_package_id'].strip(os.linesep), "org.xwalk.test")
        self.assertEquals(apkLength, 1)

    def test_create_package_k(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=windows --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk + " -k " + comm.ConstPath + "/../testapp/create_package_basic/"
        (return_code, output) = comm.getstatusoutput(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".msi"):
                apkLength = apkLength + 1
        projectDir = output[0].split(" * " + os.linesep)[-1].split(' ')[-1].strip(os.linesep)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertEquals(apkLength, 1)
        self.assertIn("app", os.listdir(projectDir))
        self.assertIn("prj", os.listdir(projectDir))

    def test_create_package_p(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg -p windows --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk + " " + comm.ConstPath + "/../testapp/create_package_basic/"
        (return_code, output) = comm.getstatusoutput(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".msi"):
                apkLength = apkLength + 1
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertIn("candle", output[0])
        self.assertIn("light", output[0])
        self.assertNotIn("Loading 'android' platform backend", output[0])
        self.assertNotIn("armeabi-v7a,x86", output[0])
        self.assertEquals(apkLength, 1)

    def test_create_package_c(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=windows -c canary " + comm.ConstPath + "/../testapp/create_package_basic/"
        (return_code, output) = comm.getstatusoutput(cmd)
        version = comm.check_crosswalk_version(self, "canary")
        crosswalk = 'crosswalk-{}.zip'.format(version)
        crosswalk64 = 'crosswalk64-{}.zip'.format(version)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".msi"):
                apkLength = apkLength + 1
        if not comm.cachedir:
            namelist = os.listdir(os.getcwd())
        else:
            newcachedir = os.environ.get('CROSSWALK_APP_TOOLS_CACHE_DIR')
            os.chdir(newcachedir)
            namelist = os.listdir(os.getcwd())
        crosswalkexist = 1
        if crosswalk not in namelist and crosswalk64 not in namelist:
            crosswalkexist = 0
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertIn("canary", output[0])
        self.assertIn(version, output[0])
        self.assertEquals(crosswalkexist, 1)
        self.assertEquals(apkLength, 1)

    def test_create_package_m(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        if os.path.exists(comm.ConstPath + "/../testapp/start_url/manifest.json"):
            os.remove(comm.ConstPath + "/../testapp/start_url/manifest.json")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=windows --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk + " -m org.xwalk.test " + comm.ConstPath + "/../testapp/start_url/"
        return_code = os.system(cmd)
        with open(comm.ConstPath + "/../testapp/start_url/manifest.json") as json_file:
            data = json.load(json_file)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".msi"):
                apkLength = apkLength + 1
        comm.clear("org.xwalk.test")
        os.remove(comm.ConstPath + "/../testapp/start_url/manifest.json")
        self.assertEquals(return_code, 0)
        self.assertEquals(data['xwalk_package_id'].strip(os.linesep), "org.xwalk.test")
        self.assertEquals(apkLength, 1)

    def test_multiple_backends_crosswalkrelease(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            'crosswalk-pkg --platforms="windows android" --crosswalk=' + comm.XwalkPath + comm.windowsCrosswalk + " " + comm.ConstPath + "/../testapp/create_package_basic/"
        os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        msiLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".apk") and "x86" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".apk") and "arm" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".msi"):
                msiLength = msiLength + 1
        comm.clear("org.xwalk.test")
        self.assertEquals(apkLength, 0)
        self.assertEquals(msiLength, 1)

    def test_multiple_backends_stable(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            'crosswalk-pkg --platforms="windows android" --crosswalk=stable ' + comm.ConstPath + "/../testapp/create_package_basic/"
        os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        msiLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".apk") and "x86" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".apk") and "arm" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".msi"):
                msiLength = msiLength + 1
        comm.clear("org.xwalk.test")
        self.assertEquals(apkLength, 2)
        self.assertEquals(msiLength, 1)

    def test_multiple_backends_canary(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            'crosswalk-pkg --platforms="windows android" --crosswalk=canary ' + comm.ConstPath + "/../testapp/create_package_basic/"
        os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        msiLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".apk") and "x86" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".apk") and "arm" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".msi"):
                msiLength = msiLength + 1
        comm.clear("org.xwalk.test")
        self.assertEquals(apkLength, 2)
        self.assertEquals(msiLength, 1)

    def test_multiple_backends_beta(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            'crosswalk-pkg --platforms="windows android" --crosswalk=beta ' + comm.ConstPath + "/../testapp/create_package_basic/"
        os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        msiLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".apk") and "x86" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".apk") and "arm" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".msi"):
                msiLength = msiLength + 1
        comm.clear("org.xwalk.test")
        self.assertEquals(apkLength, 2)
        self.assertEquals(msiLength, 1)

    def test_multiple_backends_crosswalkversion(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            'crosswalk-pkg --platforms="windows android" --crosswalk=19.49.514.1 ' + comm.ConstPath + "/../testapp/create_package_basic/"
        os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        msiLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".apk") and "x86" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".apk") and "arm" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".msi"):
                msiLength = msiLength + 1
        comm.clear("org.xwalk.test")
        self.assertEquals(apkLength, 2)
        self.assertEquals(msiLength, 1)

    def test_create_package_release(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=windows --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk + " --release=true " + comm.ConstPath + "/../testapp/create_package_basic/"
        (return_code, output) = comm.getstatusoutput(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".msi"):
                apkLength = apkLength + 1
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertEquals(apkLength, 1)

    def test_create_package_release_without_argument(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=windows --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk + " -r " + comm.ConstPath + "/../testapp/create_package_basic/"
        (return_code, output) = comm.getstatusoutput(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".msi"):
                apkLength = apkLength + 1
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertEquals(apkLength, 1)

    def test_create_package_release_without_argument_check_locale(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        comm.unzip_dir(comm.XwalkPath + comm.windowsCrosswalk, comm.XwalkPath)
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=windows --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk.replace('.zip', '') + " -r " + comm.ConstPath + "/../testapp/create_package_basic/"
        (return_code, output) = comm.getstatusoutput(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".msi"):
                apkLength = apkLength + 1
        self.assertEquals(return_code, 0)
        self.assertEquals(apkLength, 1)
	cmd = "msiexec /a %s TARGETDIR=%s" % (apks[0], os.path.join(os.path.abspath(comm.XwalkPath), "test-app"))
        (return_code, output) = comm.getstatusoutput(cmd)
        self.assertEquals(return_code, 0)
	self.assertTrue(os.path.isdir(os.path.join(os.path.abspath(comm.XwalkPath), "test-app", "org.xwalk.test", "locales")))
        comm.clear("org.xwalk.test")
        comm.clear("test-app")

    def test_create_package_skip_dummy_using_s_option(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=windows -s --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk.replace('.zip', '') + " -r " + comm.ConstPath + "/../testapp/create_package_basic/"
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
            "crosswalk-pkg --platforms=windows --skip-check --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk.replace('.zip', '') + " -r " + comm.ConstPath + "/../testapp/create_package_basic/"
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
            "crosswalk-pkg --platforms=windows --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk.replace('.zip', '') + " -r " + comm.ConstPath + "/../testapp/create_package_basic/"
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
            "crosswalk-pkg --platforms=windows -s no --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk.replace('.zip', '') + " -r " + comm.ConstPath + "/../testapp/create_package_basic/"
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
            "crosswalk-pkg --platforms=windows --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk.replace('.zip', '') + " -r " + comm.ConstPath + "/../testapp/create_package_basic/ > 1.log 2>&1"
        (return_code, output) = comm.getstatusoutput(cmd)
        self.assertEquals(return_code, 0)
        cmd = "type 1.log"
        (return_code, output) = comm.getstatusoutput(cmd)
        comm.clear("org.xwalk.test")
        comm.clear("1.log")
        self.assertEquals(return_code, 0)
        self.assertIn("Skipping host setup check", output[0])

if __name__ == '__main__':
    unittest.main()
