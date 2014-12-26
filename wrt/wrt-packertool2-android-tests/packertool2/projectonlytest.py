#!/usr/bin/env python

import unittest
import os, sys, commands
import comm

class TestPackertoolsFunctions(unittest.TestCase):      
    def test_projectonly1(self):
        comm.setUp()
        os.chdir("testapp/example")
        cmd = "python %smake_apk.py --package=org.xwalk.example --arch=%s --mode=%s --manifest=./manifest.json --project-only" % \
        (comm.Pck_Tools, comm.ARCH, comm.MODE)
        packstatus = commands.getstatusoutput(cmd)
        errormsg = "--project-only must be used with --project-dir"
        self.assertNotEqual(packstatus[0] ,0)
        self.assertIn(errormsg, packstatus[1])
        
    def test_projectonly2(self):
        comm.setUp()
        cmd = "python %smake_apk.py --package=org.xwalk.example --arch=%s --mode=%s --manifest=./manifest.json --project-only --project-dir=example" % \
        (comm.Pck_Tools, comm.ARCH, comm.MODE)
        packstatus = commands.getstatusoutput(cmd)
        self.assertEqual(packstatus[0] ,0)
        resultstatus = commands.getstatusoutput("ls")
        self.assertNotIn("Example.apk", resultstatus[1])
        self.assertIn("example", resultstatus[1])
        if os.path.exists(comm.ConstPath + "/../testapp/example/example"):
            try:
                shutil.rmtree(comm.ConstPath + "/../testapp/example/example")
            except Exception,e:
                os.system("rm -rf " + comm.ConstPath + "/../testapp/example/example")

if __name__ == '__main__':  
    unittest.main()  
