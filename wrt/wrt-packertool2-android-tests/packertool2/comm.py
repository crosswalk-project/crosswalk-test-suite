#!/usr/bin/env python

import unittest
import os, sys, commands, shutil

SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)
APP_PATH = ConstPath + "/../testapp/example/"
Pck_Tools = ConstPath + "/../tools/crosswalk/"
MANIFEST_PATH = ["manifest.json", "./manifest.json", ConstPath + "/../testapp/example/manifest.json"]
INDEX_PATH = ["index.html", "./index.html", ConstPath + "/../testapp/example/index.html"]
per1 = '<uses-permission android:name="android.permission.READ_CONTACTS"/><uses-permission android:name="android.permission.WRITE_CONTACTS"/>'
per2 = '<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION"/><uses-permission android:name="android.permission.READ_SMS"/><uses-permission android:name="android.permission.READ_PHONE_STATE"/><uses-permission android:name="android.permission.RECEIVE_SMS"/><uses-permission android:name="android.permission.SEND_SMS"/><uses-permission android:name="android.permission.WRITE_SMS"/>'


def setUp():
    global ARCH, MODE, AppName, device

    device = os.environ.get('DEVICE_ID')
    if not device:
        print (" get env error\n")
        sys.exit(1)

    fp = open(ConstPath + "/../arch.txt", 'r')
    if fp.read().strip("\n\t") != "x86":
        ARCH = "arm"
    else:
        ARCH = "x86"
    fp.close()

    mode = open(ConstPath + "/../mode.txt", 'r')
    if mode.read().strip("\n\t") != "shared":
        MODE = "embedded"
        AppName = "Example_" + ARCH +".apk"
    else:
        MODE = "shared"
        AppName = "Example.apk"
    mode.close()

def clear_permission(targetDir):
    if os.path.exists(ConstPath + "/../" + targetDir + "/permission"):
       try:
          os.remove(ConstPath + "/../" + targetDir + "/Permission_0.1.apk")
          shutil.rmtree(ConstPath + "/../" + targetDir + "/permission")
       except Exception,e:
          os.system("rm -rf " + ConstPath + "/../" + targetDir + "/permission")
          os.system(ConstPath + "/../" + targetDir + "/*.apk")

def perm(targetDir, manifestPath, self):
    setUp()
    clear_permission(targetDir)
    print os.getcwd()
    os.chdir(ConstPath + "/../" + targetDir)
    cmd = "python %smake_apk.py --package=org.xwalk.permission --project-dir=permission --arch=%s --mode=%s --manifest=%s" % \
    (Pck_Tools, ARCH, MODE, manifestPath)
    packstatus = commands.getstatusoutput(cmd)
    self.assertEquals(0, packstatus[0])
    os.chdir("permission/Permission")
    manifestPath = os.getcwd() + "/manifest.json"
    fp = open(os.getcwd() + "/AndroidManifest.xml")
    lines = fp.readlines()
    for i in range(len(lines)): 
        l = lines[i].strip("\n\r").strip()
        if i < len(lines):
            if per1 in l:
                if "duplicate" in targetDir:
                    self.assertIn(per1, l)
                else:
                    self.assertIn(per1, l)
                    self.assertIn(per2, l)
                print "Found"
            else:
                print "Continue find"
        else:
            if "duplicate" not in targetDir:
                self.assertFalse(true, "Not found " + per1)
            else:
                self.assertFalse(true, "Not found " + per1 + " and " + per2)
    os.chdir(ConstPath + "/..")
    clear_permission(targetDir)

def gen_pkg(cmd, self):
    setUp()
    if os.path.exists(Pck_Tools + "/" + AppName):
        os.remove(Pck_Tools + "/" + AppName)
    if os.path.exists(ConstPath + "/../" + AppName):
        os.remove(ConstPath + "/../" + AppName)
    packstatus = commands.getstatusoutput(cmd)
    self.assertEquals(0, packstatus[0])
    print "Generate APK ----------------> OK!"
    result = commands.getstatusoutput("ls")
    self.assertIn(AppName, result[1])
    inststatus = commands.getstatusoutput("adb -s " + device + " install -r " + AppName)
    self.assertEquals(0, inststatus[0])
    print "Install APK ----------------> OK"
    pmstatus = commands.getstatusoutput("adb -s " + device + " shell pm list packages |grep org.xwalk.example")
    self.assertEquals(0, pmstatus[0])
    print "Find Package in device ---------------->O.K"
    launchstatus = commands.getstatusoutput("adb -s " + device + " shell am start -n org.xwalk.example/.TestActivity")
    self.assertEquals(0, launchstatus[0])
    print "Launch APK ---------------->OK"
    stopstatus = commands.getstatusoutput("adb -s " + device + " shell am force-stop org.xwalk.example")
    if stopstatus[0] == 0:
        print "Stop APK ---------------->O.K"
        unistatus = commands.getstatusoutput("adb -s " + device + " uninstall org.xwalk.example")
        self.assertEquals(0, unistatus[0])
        print "Uninstall APK ---------------->O.K"
    else:
        print "Stop APK ---------------->Error"
        os.system("adb -s " + device + " uninstall org.xwalk.example")
    if os.path.exists(os.getcwd() + "/" + AppName):
        os.remove(os.getcwd() +  "/" + AppName)
        
def anyLocation():
    chmodstatus = commands.getstatusoutput("chmod +x " + Pck_Tools + "make_apk.py")
    os.system("export PATH=$PATH:" + Pck_Tools)
