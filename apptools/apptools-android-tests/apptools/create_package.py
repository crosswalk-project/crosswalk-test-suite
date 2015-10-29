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


class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_create_package_basic(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android " + comm.ConstPath + "/../testapp/create_package_basic/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".apk") and "x86" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".apk") and "arm" in apks[i]:
                apkLength = apkLength + 1
        self.assertEquals(apkLength, 2)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_package_missing_icon_startUrl(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android " + comm.ConstPath + "/../testapp/create_package_missing_icon_startUrl/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".apk") and "x86" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".apk") and "arm" in apks[i]:
                apkLength = apkLength + 1
        self.assertEquals(apkLength, 2)
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
            "crosswalk-pkg --platforms=android --crosswalk=stable " + comm.ConstPath + "/../testapp/create_package_missing_icon_startUrl/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".apk") and "x86" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".apk") and "arm" in apks[i]:
                apkLength = apkLength + 1
        self.assertEquals(apkLength, 2)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_package_beta(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --crosswalk=beta " + comm.ConstPath + "/../testapp/create_package_missing_icon_startUrl/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".apk") and "x86" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".apk") and "arm" in apks[i]:
                apkLength = apkLength + 1
        self.assertEquals(apkLength, 2)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_package_canary(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --crosswalk=canary " + comm.ConstPath + "/../testapp/create_package_missing_icon_startUrl/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".apk") and "x86" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".apk") and "arm" in apks[i]:
                apkLength = apkLength + 1
        self.assertEquals(apkLength, 2)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_package_version(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --crosswalk=" + comm.crosswalkVersion + " " + comm.ConstPath + "/../testapp/create_package_missing_icon_startUrl/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".apk") and "x86" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".apk") and "arm" in apks[i]:
                apkLength = apkLength + 1
        self.assertEquals(apkLength, 2)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_package_pathToRelease(self):
        comm.setUp()
        for i in range(len(os.listdir(comm.XwalkPath))):
                if os.listdir(comm.XwalkPath)[i].endswith(".zip"):
                    androidCrosswalk = os.listdir(comm.XwalkPath)[i]
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --crosswalk=" + comm.XwalkPath + androidCrosswalk + " " + comm.ConstPath + "/../testapp/create_package_missing_icon_startUrl/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".apk") and "x86" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".apk") and "arm" in apks[i]:
                apkLength = apkLength + 1
        self.assertEquals(apkLength, 2)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_build_package_release(self):
        comm.setUp()
        for i in range(len(os.listdir(comm.XwalkPath))):
                if os.listdir(comm.XwalkPath)[i].endswith(".zip"):
                    androidCrosswalk = os.listdir(comm.XwalkPath)[i]
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --release=true " + comm.ConstPath + "/../testapp/create_package_missing_icon_startUrl/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".apk") and "x86" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".apk") and "arm" in apks[i]:
                apkLength = apkLength + 1
        self.assertEquals(apkLength, 2)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_package_crosswalkdir(self):
        comm.setUp()
        for i in range(len(os.listdir(comm.XwalkPath))):
                if os.listdir(comm.XwalkPath)[i].endswith(".zip"):
                    androidCrosswalk = os.listdir(comm.XwalkPath)[i]
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        crosswalkzip = zipfile.ZipFile(comm.XwalkPath + androidCrosswalk,'r')
        for file in crosswalkzip.namelist():
            crosswalkzip.extract(file, r'.')
        crosswalkzip.close()
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --crosswalk=" + comm.XwalkPath + androidCrosswalk[:androidCrosswalk.index(".zip")] + "/ " + comm.ConstPath + "/../testapp/create_package_basic/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".apk") and "x86" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".apk") and "arm" in apks[i]:
                apkLength = apkLength + 1
        self.assertEquals(apkLength, 2)
        comm.run(self)
        comm.clear("org.xwalk.test")
        shutil.rmtree(androidCrosswalk[:androidCrosswalk.index(".zip")])
        self.assertEquals(return_code, 0)
        self.assertEquals(apkLength, 1)

    def test_create_package_without_channel(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android  " + comm.ConstPath + "/../testapp/create_package_basic/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".apk") and "x86" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".apk") and "arm" in apks[i]:
                apkLength = apkLength + 1
        self.assertEquals(apkLength, 2)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

    def test_create_package_manifest(self):
        comm.setUp()
        for i in range(len(os.listdir(comm.XwalkPath))):
                if os.listdir(comm.XwalkPath)[i].endswith(".zip"):
                    androidCrosswalk = os.listdir(comm.XwalkPath)[i]
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --crosswalk=" + comm.XwalkPath + androidCrosswalk + " --manifest=org.xwalk.test " + comm.ConstPath + "/../testapp/start_url/"
        return_code = os.system(cmd)
        apks = os.listdir(os.getcwd())
        apkLength = 0
        for i in range(len(apks)):
            if apks[i].endswith(".apk") and "x86" in apks[i]:
                apkLength = apkLength + 1
            if apks[i].endswith(".apk") and "arm" in apks[i]:
                apkLength = apkLength + 1
        self.assertEquals(apkLength, 2)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)

if __name__ == '__main__':
    unittest.main()
