#!/usr/bin/env python

import unittest
import os, sys, commands
import comm

class TestPackertoolsFunctions(unittest.TestCase):
    def test_manifest1(self):
        comm.setUp()
        os.chdir("resource")
        cmd = "python %smake_apk.py --package=org.hello.world --arch=%s --mode=%s --manifest=%s" % \
        (comm.Pck_Tools, comm.ARCH, comm.MODE, comm.MANIFEST_PATH[0])
        packstatus = commands.getstatusoutput(cmd)
        if packstatus[0] == 0:
            print "Generate APK ----------------> OK!"
            result = commands.getstatusoutput("ls")
            self.assertIn(comm.AppName, result[1])
        else:
            print "Generate APK ----------------> Error!"
            result = commands.getstatusoutput("ls")
            self.assertNotIn(comm.AppName, result[1])
        os.remove(comm.AppName)
        os.chdir("..")

    def test_manifest2(self):
        comm.setUp()
        os.chdir("resource")
        cmd = "python %smake_apk.py --package=org.hello.world --arch=%s --mode=%s --manifest=%s" % \
        (comm.Pck_Tools, comm.ARCH, comm.MODE, comm.MANIFEST_PATH[1])
        packstatus = commands.getstatusoutput(cmd)
        print cmd
        print packstatus
        if packstatus[0] == 0:
            print "Generate APK ----------------> OK!"
            result = commands.getstatusoutput("ls")
            self.assertIn(comm.AppName, result[1])
        else:
            print "Generate APK ----------------> Error!"
            result = commands.getstatusoutput("ls")
            self.assertNotIn(comm.AppName, result[1])
        os.remove(comm.AppName)
        os.chdir("..")

    def test_manifest3(self):
        comm.setUp()
        os.chdir("resource")
        cmd = "python %smake_apk.py --package=org.hello.world --arch=%s --mode=%s --manifest=%s" % \
        (comm.Pck_Tools, comm.ARCH, comm.MODE, comm.MANIFEST_PATH[2])
        packstatus = commands.getstatusoutput(cmd)
        if packstatus[0] == 0:
            print "Generate APK ----------------> OK!"
            result = commands.getstatusoutput("ls")
            self.assertIn(comm.AppName, result[1])
        else:
            print "Generate APK ----------------> Error!"
            result = commands.getstatusoutput("ls")
            self.assertNotIn(comm.AppName, result[1])
        os.remove(comm.AppName)

if __name__ == '__main__':  
    unittest.main()
