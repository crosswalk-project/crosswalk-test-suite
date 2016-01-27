#!/usr/bin/env python
#
# Copyright (c) 2016 Intel Corporation.
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
from xml.etree import ElementTree
import json


class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_permission_default(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + ' --manifest="org.xwalk.test" --keep --crosswalk=' + comm.crosswalkzip + " ./"
        (return_code, output) = comm.getstatusoutput(cmd)
        projectDir = output[0].split(" * " + os.linesep)[-1].split(' ')[-1].strip(os.linesep)
        root = ElementTree.parse(projectDir + "/prj/android/AndroidManifest.xml").getroot()
        permission_attributes = root.findall('uses-permission')
        name = []
        for x in permission_attributes:
            name.append(x.attrib.items()[0][1])
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertEquals(len(permission_attributes), 3)
        self.assertIn("android.permission.ACCESS_NETWORK_STATE", name)
        self.assertIn("android.permission.ACCESS_WIFI_STATE", name)
        self.assertIn("android.permission.INTERNET", name)

    def test_permission_name(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=android --android=" + comm.ANDROID_MODE + " --keep --crosswalk=" + comm.crosswalkzip + " " + comm.ConstPath + "/../testapp/camera_permissions_enable/"
        (return_code, output) = comm.getstatusoutput(cmd)
        projectDir = output[0].split(" * " + os.linesep)[-1].split(' ')[-1].strip(os.linesep)
        root = ElementTree.parse(projectDir + "/prj/android/AndroidManifest.xml").getroot()
        permission_attributes = root.findall('uses-permission')
        name = []
        for x in permission_attributes:
            name.append(x.attrib.items()[0][1])
        comm.clear("org.xwalk.test")
        self.assertEquals(return_code, 0)
        self.assertEquals(len(permission_attributes), 4)
        self.assertIn("android.permission.CAMERA", name)

if __name__ == '__main__':
    unittest.main()
