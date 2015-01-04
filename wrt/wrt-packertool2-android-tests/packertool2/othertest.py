#!/usr/bin/env python

import unittest
import os, sys, commands
import comm

class TestPackertoolsFunctions(unittest.TestCase):
    def test_packertool_help(self):
        comm.setUp()
        cmd = "python %smake_apk.py -h" % \
              (comm.Pck_Tools)
        packstatus = commands.getstatusoutput(cmd)
        #print packstatus
        self.assertEquals(0, packstatus[0])
        cmd2 = "python %smake_apk.py --help" % \
               (comm.Pck_Tools)
        packstatus2 = commands.getstatusoutput(cmd2)
        self.assertEquals(0, packstatus2[0])

    def test_packertool_arm(self):
        comm.setUp()
        appRoot = comm.ConstPath + "/../testapp/example/"
        if comm.ARCH == "arm":
            cmd = "python %smake_apk.py --package=org.xwalk.example --name=example --arch=%s --mode=%s --app-root=%s --app-local-path=index.html" % \
                  (comm.Pck_Tools, comm.ARCH, comm.MODE, appRoot)
            comm.gen_pkg(cmd, self)
        else:
            self.assertFalse(True, "The case requires to run on arm platfrom")

    def test_packertool_undefinedOption(self):
        comm.setUp()
        manifestPath = comm.ConstPath + "/../testapp/example/manifest.json"
        cmd = "python %smake_apk.py --package=org.xwalk.example --name=example --arch=%s --mode=%s --manifest=%s --undefinedOption=undefined" % \
              (comm.Pck_Tools, comm.ARCH, comm.MODE, manifestPath)
        #print cmd
        packstatus = commands.getstatusoutput(cmd)
        #print packstatus
        errorInfo = "no such option: --undefinedOption"
        self.assertIn(errorInfo, packstatus[1])


if __name__ == '__main__':
    unittest.main()  
