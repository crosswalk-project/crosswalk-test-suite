#!/usr/bin/env python

import unittest
import os, sys, commands, shutil, stat
import comm

class TestPackertoolsFunctions(unittest.TestCase):
    def test_projectdir_readOnly(self):
        comm.setUp()
        os.chdir(comm.Pck_Tools)
        manifestPath = comm.ConstPath + "/../testapp/example/manifest.json"
        if not os.path.exists(comm.Pck_Tools + "readOnly"):
            os.mkdir("readOnly")
        os.chmod("readOnly", stat.S_IREAD)
        cmd = "python make_apk.py --package=org.xwalk.example --arch=%s --mode=%s --manifest=%s --project-dir=readOnly" % \
              (comm.ARCH, comm.MODE, manifestPath)
        packstatus = commands.getstatusoutput(cmd)
        errormsg = "OSError: [Errno 13] Permission denied"
        self.assertNotEqual(packstatus[0] ,0)
        self.assertIn(errormsg, packstatus[1])
        self.assertIn(comm.AppName, os.listdir(comm.Pck_Tools))
        try:
            shutil.rmtree(comm.Pck_Tools + "readOnly")
            os.remove(comm.Pck_Tools + comm.AppName)
        except Exception,e:
            os.system("rm -rf "  + comm.Pck_Tools + "readOnly &>/dev/null")
            os.system("rm -rf "  + comm.Pck_Tools + "*apk &>/dev/null")

    def test_projectdir_existFile(self):
        comm.setUp()
        os.chdir(comm.Pck_Tools)
        manifestPath = comm.ConstPath + "/../testapp/example/manifest.json"
        if "existFile.txt" not in os.listdir(comm.Pck_Tools):
            os.mknod("existFile.txt")
        cmd = "python make_apk.py --package=org.xwalk.example --arch=%s --mode=%s --manifest=%s --project-dir=existFile.txt" % \
              (comm.ARCH, comm.MODE, manifestPath)
        packstatus = commands.getstatusoutput(cmd)
        errormsg = "Unable to create a project directory during the build"
        self.assertEqual(packstatus[0] ,0)
        self.assertIn(errormsg, packstatus[1])
        self.assertIn(comm.AppName, os.listdir(comm.Pck_Tools))
        os.remove(comm.Pck_Tools + "/existFile.txt")
        os.remove(comm.Pck_Tools + comm.AppName)

    def test_projectdir_existDir(self):
        comm.setUp()
        os.chdir(comm.Pck_Tools)
        manifestPath = comm.ConstPath + "/../testapp/example/manifest.json"
        if not os.path.exists(comm.Pck_Tools + "testapp"):
            os.makedirs("testapp/testapp")
        cmd = "python make_apk.py --package=org.xwalk.example --arch=%s --mode=%s --manifest=%s --project-dir=testapp/testapp" % \
              (comm.ARCH, comm.MODE, manifestPath)
        packstatus = commands.getstatusoutput(cmd)
        self.assertEqual(packstatus[0] ,0)
        buildDir = comm.Pck_Tools + "testapp/testapp/Example"
        buildList = os.listdir(buildDir)
        self.assertTrue(os.path.isdir(buildDir + "/res"))
        self.assertIn("res", buildList)
        self.assertTrue(os.path.isfile(buildDir + "/build.xml"))
        self.assertIn("build.xml", buildList)
        try:
            shutil.rmtree(comm.Pck_Tools + "testapp")
            os.remove(comm.Pck_Tools + comm.AppName)
        except Exception,e:
            os.system("rm -rf "  + comm.Pck_Tools + "testapp &>/dev/null")
            os.system("rm -rf "  + comm.Pck_Tools + "*apk &>/dev/null")


    def test_projectdir_antbuild(self):
        comm.setUp()
        if os.path.exists(comm.Pck_Tools + "example"):
            try:
                shutil.rmtree(comm.Pck_Tools + "example")
                os.remove(comm.Pck_Tools + comm.AppName)
            except Exception,e:
                os.system("rm -rf "  + comm.Pck_Tools + "example &>/dev/null")
                os.system("rm -rf "  + comm.Pck_Tools + "*apk &>/dev/null")
        os.chdir(comm.Pck_Tools)
        manifestPath = comm.ConstPath + "/../testapp/example/manifest.json"
        cmd = "python make_apk.py --package=org.xwalk.example --arch=%s --mode=%s --manifest=%s --project-dir=example" % \
              (comm.ARCH, comm.MODE, manifestPath)
        packstatus = commands.getstatusoutput(cmd)
        self.assertEqual(packstatus[0] ,0)
        os.remove(comm.Pck_Tools + comm.AppName)
        buildDir = comm.Pck_Tools + "example/Example"
        buildList = os.listdir(buildDir)
        self.assertIn("res", buildList)
        self.assertIn("bin", buildList)
        self.assertIn("AndroidManifest.xml", buildList)
        buildstatus = commands.getstatusoutput("ant release -f " + buildDir + "/build.xml")
        self.assertEqual(buildstatus[0] ,0)
        apkName = "Example-release.apk"
        self.assertIn(apkName, os.listdir(buildDir + "/bin"))
        shutil.copyfile(buildDir + "/bin/" + apkName, comm.Pck_Tools + comm.AppName)
        inststatus = commands.getstatusoutput("adb -s " + comm.device + " install -r " + comm.AppName)
        self.assertEquals(0, inststatus[0])
        print "Install APK ----------------> OK"
        pmstatus = commands.getstatusoutput("adb -s " + comm.device + " shell pm list packages |grep org.xwalk.example")
        self.assertEquals(0, pmstatus[0])
        print "Find Package in comm.device ---------------->O.K"
        launchstatus = commands.getstatusoutput("adb -s " + comm.device + " shell am start -n org.xwalk.example/.TestActivity")
        self.assertEquals(0, launchstatus[0])
        print "Launch APK ---------------->OK"
        stopstatus = commands.getstatusoutput("adb -s " + comm.device + " shell am force-stop org.xwalk.example")
        if stopstatus[0] == 0:
            print "Stop APK ---------------->O.K"
            unistatus = commands.getstatusoutput("adb -s " + comm.device + " uninstall org.xwalk.example")
            self.assertEquals(0, unistatus[0])
            print "Uninstall APK ---------------->O.K"
        else:
            print "Stop APK ---------------->Error"
            os.system("adb -s " + comm.device + " uninstall org.xwalk.example")
        if os.path.exists(comm.Pck_Tools + "example"):
            try:
                shutil.rmtree(comm.Pck_Tools + "example")
                os.remove(comm.Pck_Tools + comm.AppName)
            except Exception,e:
                os.system("rm -rf "  + comm.Pck_Tools + "example &>/dev/null")
                os.system("rm -rf "  + comm.Pck_Tools + "*apk &>/dev/null")

if __name__ == '__main__':
    unittest.main()
