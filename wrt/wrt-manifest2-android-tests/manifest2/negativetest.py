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
#         Hongjuan, Wang<hongjuanx.wang@intel.com>

import unittest
import os, sys, commands
import comm

class TestManifestFunctions(unittest.TestCase):
    def test_negative_nullfields(self):
        comm.setUp()
        manifestPath = comm.ConstPath + "/../testapp/manifest_negative_nullfields_app/manifest.json"
        cmd = "python %smake_apk.py --package=org.xwalk.example --arch=%s --mode=%s --manifest=%s" % \
              (comm.Pck_Tools, comm.ARCH, comm.MODE, manifestPath)
        packInfo = commands.getstatusoutput(cmd)
        self.assertNotEquals(0, packInfo[0])
        errorInfo = "Error: there is no app launch path defined in manifest.json"
        self.assertIn(errorInfo, packInfo[1])

    def test_negative_nullvalue(self):
        comm.setUp()
        manifestPath = comm.ConstPath + "/../testapp/manifest_negative_nullvalue_app/manifest.json"
        cmd = "python %smake_apk.py --package=org.xwalk.example --arch=%s --mode=%s --manifest=%s" % \
              (comm.Pck_Tools, comm.ARCH, comm.MODE, manifestPath)
        packInfo = commands.getstatusoutput(cmd)
        self.assertNotEquals(0, packInfo[0])
        errorInfo = "Error: there is no app launch path defined in manifest.json"
        self.assertIn(errorInfo, packInfo[1])

    def test_negative_description(self):
        comm.setUp()
        targetDir = comm.ConstPath + "/../testapp/manifest_negative_nullvalue_description"
        manifestPath = targetDir + "/manifest.json"
        os.chdir(targetDir)
        cmd = "python %smake_apk.py --package=org.xwalk.example --arch=%s --mode=%s --manifest=%s --project-dir=desc" % \
              (comm.Pck_Tools, comm.ARCH, comm.MODE, manifestPath)
        packInfo = commands.getstatusoutput(cmd)
        self.assertEquals(0, packInfo[0])
        fp = open(targetDir + "/desc/Example/AndroidManifest.xml")
        lines = fp.readlines()
        for i in range(len(lines)):
            line = lines[i].strip("\n\r").strip()
            findLine = "<manifest"
            if i <= len(lines):
                if findLine in line:
                    print "Find manifest"
                    l = lines[i].strip("\n\r").strip()
                    self.assertNotIn("android:description", l)
                    break
                else:
                    print "Continue find"
            else:
                self.assertIn(findLine, line)
        desc = open(targetDir + "/desc/Example/res/values/strings.xml")
        descs = fp.readlines()
        for j in range(len(descs)):
            d = descs[j].strip("\n\r").strip()
            findLine = "description"
            if j < len(descs):
                if findLine in d:
                    print "Find"
                    self.assertFalse(True, "There should not have description attribute")
                    break
                else:
                    print "Continue find"
            else:
                self.assertNotIn(findLine, line)
        try:
            os.remove(targetDir + "/Example.apk")
            shutil.rmtree(targetDir + "/desc")
        except Exception,e:
            os.system("rm -rf " + targetDir + "/*.apk")
            os.system("rm -rf " + targetDir + "/desc")

    def test_negative_name(self):
        comm.setUp()
        manifestPath = comm.ConstPath + "/../testapp/manifest_negative_nullvalue_name/manifest.json"
        cmd = "python %smake_apk.py --package=org.xwalk.example --arch=%s --mode=%s --manifest=%s" % \
              (comm.Pck_Tools, comm.ARCH, comm.MODE, manifestPath)
        packInfo = commands.getstatusoutput(cmd)
        self.assertNotEquals(0, packInfo[0])
        errorInfo = "error: An APK name is required."
        self.assertIn(errorInfo, packInfo[1])

if __name__ == '__main__':
    unittest.main()
