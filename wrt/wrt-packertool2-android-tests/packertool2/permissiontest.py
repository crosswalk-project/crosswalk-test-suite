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
  def test_permission_duplicate(self):
      targetDir = "testapp/permission_field_duplicate_tests"
      manifestPath = comm.ConstPath + "/../" + targetDir + "/manifest.json"
      comm.perm(targetDir,manifestPath, self)

  def test_permission_lowercase(self):
      targetDir = "testapp/permission_field_lowercase_tests"
      manifestPath = comm.ConstPath + "/../" + targetDir + "/manifest.json"
      comm.perm(targetDir,manifestPath, self)

  def test_permission_more2(self):
      targetDir = "testapp/permission_field_more2_tests"
      manifestPath = comm.ConstPath + "/../" + targetDir + "/manifest.json"
      comm.perm(targetDir,manifestPath, self)

  def test_permission_uppercase(self):
      targetDir = "testapp/permission_field_uppercase_tests"
      manifestPath = comm.ConstPath + "/../" + targetDir + "/manifest.json"
      comm.perm(targetDir,manifestPath, self)

  def test_permission_duplicate2(self):
      comm.setUp()
      cmd = "python %smake_apk.py --package=org.xwalk.permission --name=example --project-dir=permission --arch=%s --mode=%s --app-url=http://www.intel.com --permission=Contacts --permission=contacts --permission=CONTACTS" % (comm.Pck_Tools, comm.ARCH, comm.MODE)
      num = 2
      comm.perm2(num, cmd, self)

  def test_permission_value3(self):
      comm.setUp()
      cmd = "python %smake_apk.py --package=org.xwalk.permission --name=example --project-dir=permission --arch=%s --mode=%s --app-url=http://www.intel.com --permission=Geolocation --permission=Messaging --permission=Contacts" % (comm.Pck_Tools, comm.ARCH, comm.MODE)
      num = 3
      comm.perm2(num, cmd, self)

  def test_permission_value4(self):
      comm.setUp()
      cmd = "python %smake_apk.py --package=org.xwalk.permission --name=example --project-dir=permission --arch=%s --mode=%s --app-url=http://www.intel.com --permission=Contacts --permission=Geolocation --permission=Messaging --permission=Contacts:Geolocation:Messaging" % (comm.Pck_Tools, comm.ARCH, comm.MODE)
      num = 4
      comm.perm2(num, cmd, self)

if __name__ == '__main__':  
    unittest.main()
