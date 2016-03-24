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
from xml.etree import ElementTree
import json
import shutil


class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_build_debug_webp(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        jsonfile = open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json", "r")
        jsons = jsonfile.read()
        jsonfile.close()
        jsonDict = json.loads(jsons)
        jsonDict["xwalk_android_webp"] = "80 80 100"
        json.dump(jsonDict, open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json", "w"))
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build"
        comm.build(self, buildcmd)
        comm.run(self)
        comm.clear("org.xwalk.test")

    def test_build_release_webp(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        jsonfile = open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json", "r")
        jsons = jsonfile.read()
        jsonfile.close()
        jsonDict = json.loads(jsons)
        jsonDict["xwalk_android_webp"] = "80 80 100"
        json.dump(jsonDict, open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json", "w"))
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build release"
        comm.build(self, buildcmd)
        comm.run(self)
        comm.clear("org.xwalk.test")

    def test_build_debug_path_webp(self):
        comm.setUp()
        comm.create(self)
        jsonfile = open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json", "r")
        jsons = jsonfile.read()
        jsonfile.close()
        jsonDict = json.loads(jsons)
        jsonDict["xwalk_android_webp"] = "80 80 100"
        json.dump(jsonDict, open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json", "w"))
        if os.path.exists("pkg"):
            shutil.rmtree("pkg")
        os.mkdir("pkg")
        os.chdir('pkg')
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build " + comm.XwalkPath + "org.xwalk.test"
        comm.build(self, buildcmd)
        comm.run(self)
        os.chdir('../')
        shutil.rmtree("pkg")
        comm.clear("org.xwalk.test")

    def test_build_release_path_webp(self):
        comm.setUp()
        comm.create(self)
        jsonfile = open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json", "r")
        jsons = jsonfile.read()
        jsonfile.close()
        jsonDict = json.loads(jsons)
        jsonDict["xwalk_android_webp"] = "80 80 100"
        json.dump(jsonDict, open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json", "w"))
        if os.path.exists("pkg"):
            shutil.rmtree("pkg")
        os.mkdir("pkg")
        os.chdir('pkg')
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build release " + comm.XwalkPath + "org.xwalk.test"
        comm.build(self, buildcmd)
        comm.run(self)
        os.chdir('../')
        shutil.rmtree("pkg")
        comm.clear("org.xwalk.test")

if __name__ == '__main__':
    unittest.main()
