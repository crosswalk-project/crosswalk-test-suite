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
#         Liu, Yun <yunx.liu@intel.com>

import unittest
import os
import comm
from xml.etree import ElementTree
import json


class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_versionCode_normal(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build"
        buildstatus = os.popen(buildcmd).readlines()
        index = 0
        for x in range(len(buildstatus),0,-1):
            index = x -1
            if buildstatus[index].find("Using android:versionCode") != -1:
                break
        versionCode = buildstatus[index].strip(" *\nUsing android:versionCode")[1:-1]
        root = ElementTree.parse(comm.ConstPath + "/../tools/org.xwalk.test/prj/android/AndroidManifest.xml").getroot()
        attributes = root.attrib
        for x in attributes.keys():
            if x.find("versionCode") != -1:
                versionCode_xml = attributes[x]
                break
        comm.clear("org.xwalk.test")
        self.assertEquals(versionCode, versionCode_xml)

    def test_update_app_version_onedot(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        jsonfile = open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json", "r")
        jsons = jsonfile.read()
        jsonfile.close()
        jsonDict = json.loads(jsons)
        jsonDict["xwalk_app_version"] = "0.1"
        json.dump(jsonDict, open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json", "w"))
        with open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json") as json_file:
            data = json.load(json_file)
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build"
        buildstatus = os.popen(buildcmd).readlines()
        index = 0
        for x in range(len(buildstatus),0,-1):
            index = x -1
            if buildstatus[index].find("Using android:versionCode") != -1:
                break
        versionCode = buildstatus[index].strip(" *\nUsing android:versionCode")[1:-1]
        root = ElementTree.parse(comm.ConstPath + "/../tools/org.xwalk.test/prj/android/AndroidManifest.xml").getroot()
        attributes = root.attrib
        for x in attributes.keys():
            if x.find("versionCode") != -1:
                versionCode_xml = attributes[x]
                break
        comm.clear("org.xwalk.test")
        self.assertEquals(data['xwalk_app_version'].strip(os.linesep), "0.1")
        self.assertEquals(versionCode, versionCode_xml)

    def test_update_app_version_twodot(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        jsonfile = open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json", "r")
        jsons = jsonfile.read()
        jsonfile.close()
        jsonDict = json.loads(jsons)
        jsonDict["xwalk_app_version"] = "0.0.1"
        json.dump(jsonDict, open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json", "w"))
        with open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json") as json_file:
            data = json.load(json_file)
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build"
        buildstatus = os.popen(buildcmd).readlines()
        index = 0
        for x in range(len(buildstatus),0,-1):
            index = x -1
            if buildstatus[index].find("Using android:versionCode") != -1:
                break
        versionCode = buildstatus[index].strip(" *\nUsing android:versionCode")[1:-1]
        root = ElementTree.parse(comm.ConstPath + "/../tools/org.xwalk.test/prj/android/AndroidManifest.xml").getroot()
        attributes = root.attrib
        for x in attributes.keys():
            if x.find("versionCode") != -1:
                versionCode_xml = attributes[x]
                break
        comm.clear("org.xwalk.test")
        self.assertEquals(data['xwalk_app_version'].strip(os.linesep), "0.0.1")
        self.assertEquals(versionCode, versionCode_xml)

    def test_update_app_version_threedot(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        jsonfile = open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json", "r")
        jsons = jsonfile.read()
        jsonfile.close()
        jsonDict = json.loads(jsons)
        jsonDict["xwalk_app_version"] = "0.0.0.1"
        json.dump(jsonDict, open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json", "w"))
        with open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json") as json_file:
            data = json.load(json_file)
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build"
        return_code = os.system(buildcmd)
        comm.clear("org.xwalk.test")
        self.assertEquals(data['xwalk_app_version'].strip(os.linesep), "0.0.0.1")
        self.assertNotEquals(return_code, 0)

    def test_update_app_version_out_of_range(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        jsonfile = open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json", "r")
        jsons = jsonfile.read()
        jsonfile.close()
        jsonDict = json.loads(jsons)
        jsonDict["xwalk_app_version"] = "1000"
        json.dump(jsonDict, open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json", "w"))
        with open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json") as json_file:
            data = json.load(json_file)
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build"
        return_code = os.system(buildcmd)
        comm.clear("org.xwalk.test")
        self.assertEquals(data['xwalk_app_version'].strip(os.linesep), "1000")
        self.assertNotEquals(return_code, 0)

if __name__ == '__main__':
    unittest.main()
