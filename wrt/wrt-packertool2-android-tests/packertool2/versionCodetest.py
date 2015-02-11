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

class TestPackertoolsFunctions(unittest.TestCase):      
    def test_manifest_versionCode(self):
        comm.setUp()
        comm.clear_versionCode()
        targetDir = comm.ConstPath + "/../testapp/example/"
        manfiestPath = targetDir + "manifest.json"
        os.chdir(targetDir)
        versionCode = " --app-versionCode=11"
        versionCodeBase = ""
        cmd = "python %smake_apk.py --package=org.xwalk.example --arch=%s --mode=%s --manifest=%s --project-dir=test" % \
        (comm.Pck_Tools, comm.ARCH, comm.MODE, manfiestPath)
        comm.versionCode(cmd, versionCode, versionCodeBase, self)
        comm.clear_versionCode()

    def test_manifest_no_versionCode(self):
        comm.setUp()
        comm.clear_versionCode()
        targetDir = comm.ConstPath + "/../testapp/example/"
        manfiestPath = targetDir + "manifest.json"
        os.chdir(targetDir)
        versionCode = ""
        versionCodeBase = ""
        cmd = "python %smake_apk.py --package=org.xwalk.example --arch=%s --mode=%s --manifest=%s --project-dir=test" % \
        (comm.Pck_Tools, comm.ARCH, comm.MODE, manfiestPath)
        comm.versionCode(cmd, versionCode, versionCodeBase, self)
        comm.clear_versionCode()

    def test_manifest_versionCodeBase(self):
        comm.setUp()
        comm.clear_versionCode()
        targetDir = comm.ConstPath + "/../testapp/example/"
        manfiestPath = targetDir + "manifest.json"
        os.chdir(targetDir)
        versionCode = ""
        versionCodeBase = ""
        versionCodeBase = " --app-versionCodeBase=1234567"
        cmd = "python %smake_apk.py --package=org.xwalk.example --arch=%s --mode=%s --manifest=%s --project-dir=test --app-version=1.0.0" % \
        (comm.Pck_Tools, comm.ARCH, comm.MODE, manfiestPath)
        comm.versionCode(cmd, versionCode, versionCodeBase, self)
        comm.clear_versionCode()

    def test_manifest_version_versionCode(self):
        comm.setUp()
        comm.clear_versionCode()
        targetDir = comm.ConstPath + "/../testapp/example/"
        manfiestPath = targetDir + "manifest.json"
        os.chdir(targetDir)
        versionCode = ""
        versionCodeBase = ""
        cmd = "python %smake_apk.py --package=org.xwalk.example --arch=%s --mode=%s --manifest=%s --project-dir=test --app-version=1.0.0.0" % \
        (comm.Pck_Tools, comm.ARCH, comm.MODE, manfiestPath)
        packstatus = commands.getstatusoutput(cmd)
        errorinfo = "please specify --app-versionCode or --app-versionCodeBase"
        self.assertNotEquals(0, packstatus[0])
        self.assertIn(errorinfo, packstatus[1])
        comm.clear_versionCode()

if __name__ == '__main__':  
    unittest.main()  
