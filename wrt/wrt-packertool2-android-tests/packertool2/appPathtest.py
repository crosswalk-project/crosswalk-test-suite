#!/usr/bin/env python

import unittest
import os, sys, commands, shutil
import comm

class TestPackertoolsFunctions(unittest.TestCase):      

  def test_appPath(self):
      comm.setUp()
      os.chdir(comm.Pck_Tools)
      appRoot = comm.ConstPath + "/../testapp/example/"
      cmd = "python make_apk.py --package=org.xwalk.example --name=example --arch=%s --mode=%s --app-root=%s --app-local-path=index.html" % \
            (comm.ARCH, comm.MODE, appRoot)
      comm.gen_pkg(cmd, self)
      os.chdir("../../")


if __name__ == '__main__':  
    unittest.main()
