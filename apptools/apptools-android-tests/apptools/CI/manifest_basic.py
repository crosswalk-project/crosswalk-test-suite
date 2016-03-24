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
from xml.etree import ElementTree
import json
import sys
sys.path.append("../")
import comm

class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_apkName_contains_appVersion(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        with open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json") as json_file:
            data = json.load(json_file)
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build"
        appVersion = comm.build(self, buildcmd)
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(data['xwalk_app_version'].strip(os.linesep), "0.1")
        self.assertEquals(data['xwalk_app_version'].strip(os.linesep), appVersion)

    def test_name_normal(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build"
        comm.build(self, buildcmd)
        root = ElementTree.parse(comm.ConstPath + "/../tools/org.xwalk.test/prj/android/AndroidManifest.xml").getroot()
        application_attributes = root.find('application').attrib
        for x in application_attributes.keys():
            if x.find("label") != -1:
                application_xml = application_attributes[x]
                break
        activity_attributes = root.find('application').find('activity').attrib
        for y in activity_attributes.keys():
            if y.find("label") != -1:
                activity_xml = activity_attributes[y]
                break
        comm.clear("org.xwalk.test")
        self.assertEquals(application_xml, "org.xwalk.test")
        self.assertEquals(activity_xml, "org.xwalk.test")

    def test_packageID_normal(self):
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        with open(comm.ConstPath + "/../tools/org.xwalk.test/app/manifest.json") as json_file:
            data = json.load(json_file)
        comm.clear("org.xwalk.test")
        self.assertEquals(data['xwalk_package_id'].strip(os.linesep), "org.xwalk.test")

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
        versionCode = buildstatus[index].strip(" *\nUsing android:versionCode").split(' ')[-1][1:-1]
        root = ElementTree.parse(comm.ConstPath + "/../tools/org.xwalk.test/prj/android/AndroidManifest.xml").getroot()
        attributes = root.attrib
        for x in attributes.keys():
            if x.find("versionCode") != -1:
                versionCode_xml = attributes[x]
                break
        comm.run(self)
        comm.clear("org.xwalk.test")
        self.assertEquals(versionCode, versionCode_xml)

if __name__ == '__main__':
    unittest.main()
