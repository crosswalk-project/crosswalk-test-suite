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

if __name__ == '__main__':  
    unittest.main()
