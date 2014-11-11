#!/usr/bin/env python

import unittest
import os, sys, commands
import comm

class TestPackertoolsFunctions(unittest.TestCase):      
    def test_projectonly1(self):
        comm.setUp()
        os.chdir("../resource")
        print os.getcwd()
        cmd = "python %smake_apk.py --package=org.hello.world --arch=%s --mode=%s --manifest=./manifest.json --project-only" % \
        (comm.Pck_Tools, comm.ARCH, comm.MODE)
        packstatus = commands.getstatusoutput(cmd)
        errormsg = "--project-only must be used with --project-dir"
        self.assertNotEqual(packstatus[0] ,0)
        self.assertIn(errormsg, packstatus[1])
        
    def test_projectonly2(self):
        comm.setUp()
        cmd = "python %smake_apk.py --package=org.hello.world --arch=%s --mode=%s --manifest=./manifest.json --project-only --project-dir=world" % \
        (comm.Pck_Tools, comm.ARCH, comm.MODE)
        packstatus = commands.getstatusoutput(cmd)
        print cmd
        print packstatus
        self.assertEqual(packstatus[0] ,0)
        resultstatus = commands.getstatusoutput("ls")
        self.assertNotIn("World.apk", resultstatus[1])
        self.assertIn("world", resultstatus[1])

if __name__ == '__main__':  
    unittest.main()  
