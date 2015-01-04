#!/usr/bin/env python

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
