#!/usr/bin/env python

import unittest
import os, sys, commands, shutil
import comm

class TestPackertoolsFunctions(unittest.TestCase):
  def test_anyLocation_hostApp(self):
      comm.setUp()
      comm.anyLocation()
      cmd = "make_apk.py --package=org.xwalk.example --name=example --arch=%s --mode=%s --app-url=https://crosswalk-project.org/" % \
            (comm.ARCH, comm.MODE)
      comm.gen_pkg(cmd, self)

  def test_anyLocationtest_manifest(self):
      comm.setUp()
      manifestPath = comm.ConstPath + "/../testapp/example/manifest.json"
      cmd = "make_apk.py --package=org.xwalk.example --arch=%s --mode=%s --manifest=%s" % \
            (comm.ARCH, comm.MODE, manifestPath)
      comm.gen_pkg(cmd, self)

  def test_anyLocationtest_package(self):
      comm.setUp()
      appRoot = comm.ConstPath + "/../testapp/example/"
      cmd = "make_apk.py --package=org.xwalk.example --name=example --arch=%s --mode=%s --app-root=%s --app-local-path=index.html" % \
            (comm.ARCH, comm.MODE, appRoot)
      comm.gen_pkg(cmd, self)


if __name__ == '__main__':  
    unittest.main()
