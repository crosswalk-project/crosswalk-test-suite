#!/usr/bin/env python
#coding=utf-8
#
# Copyright (c) 2015 Intel Corporation.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of works must retain the original copyright notice, this
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Intel Corporation nor the names of its contributors
#   may be used to endorse or promote products derived from this work without
#   specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors:
#         Hongjuan, Wang<hongjuanx.wang@intel.com>

import unittest
import os, sys, commands, shutil
reload(sys)
sys.setdefaultencoding( "utf-8" )

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

    #device = "E6OKCY411012"
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

# test for permission
def clear_permission(targetDir):
    if os.path.exists(ConstPath + "/../" + targetDir + "/permission"):
       try:
          os.remove(ConstPath + "/../" + targetDir + "/Permission_0.1.apk")
          shutil.rmtree(ConstPath + "/../" + targetDir + "/permission")
       except Exception,e:
          os.system("rm -rf " + ConstPath + "/../" + targetDir + "/*.apk")
          os.system("rm -rf " + ConstPath + "/../" + targetDir + "/permission")

def perm(targetDir, manifestPath, self):
    setUp()
    clear_permission(targetDir)
    os.chdir(ConstPath + "/../" + targetDir)
    cmd = "python %smake_apk.py --package=org.xwalk.permission --project-dir=permission --arch=%s --mode=%s --manifest=%s" % \
    (Pck_Tools, ARCH, MODE, manifestPath)
    packstatus = commands.getstatusoutput(cmd)
    self.assertEquals(0, packstatus[0])
    os.chdir("permission/Permission")
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
                print "Find"
            else:
                print i
        else:
            if "duplicate" not in targetDir:
                self.assertFalse(true, "No Find " + per1)
            else:
                self.assertFalse(true, "No Find " + per1 + " and " + per2)
    os.chdir(ConstPath + "/..")
    clear_permission(targetDir)

def perm2(num, cmd, self):
    setUp()
    clear_permission2()
    os.chdir(Pck_Tools)
    packstatus = commands.getstatusoutput(cmd)
    self.assertEquals(0, packstatus[0])
    os.chdir(Pck_Tools + "permission/Permission")
    fp = open(os.getcwd() + "/AndroidManifest.xml")
    lines = fp.readlines()
    for i in range(len(lines)): 
        l = lines[i].strip("\n\r").strip()
        if i < len(lines):
            if per1 in l:
                if num < 4:
                    self.assertIn(per1, l)
                else:
                    self.assertIn(per1, l)
                    self.assertIn(per2, l)
                print "Find"
            else:
                print i
        else:
            if num < 4:
                self.assertFalse(true, "No Find " + per1)
            else:
                self.assertFalse(true, "No Find " + per1 + " and " + per2)
    os.chdir(ConstPath + "/..")
    clear_permission2()

def clear_permission2():
    if os.path.exists(Pck_Tools + "permission"):
       try:
          os.remove(Pck_Tools + "Permission_0.1.apk")
          shutil.rmtree(Pck_Tools + "permission")
       except Exception,e:
          os.system("rm -rf " + Pck_Tools + "*.apk")
          os.system("rm -rf " + Pck_Tools + "permission")


# test for build, install, launch and uninstall
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
    launchstatus = commands.getstatusoutput("adb -s " + device + " shell am start -n org.xwalk.example/.ExampleActivity")
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
    if os.path.exists(Pck_Tools + "/" + AppName):
        os.remove(Pck_Tools + "/" + AppName)
    if os.path.exists(ConstPath + "/../" + AppName):
        os.remove(ConstPath + "/../" + AppName)

# test for compressor
def clear_compressor():
    if os.path.exists(ConstPath + "/../testapp/packer_tool_minify_tests/compressor"):
       try:
          os.remove(ConstPath + "/../testapp/packer_tool_minify_tests/Compressor_0.1.apk")
          shutil.rmtree(ConstPath + "/../testapp/packer_tool_minify_tests/compressor")
       except Exception,e:
          os.system("rm -rf " + ConstPath + "/../testapp/packer_tool_minify_tests/compressor")
          os.system(ConstPath + "/../testapp/packer_tool_minify_tests/*.apk")

def compressor(compre, self):
    setUp()
    global compDir, oriDir
    manifestPath = ConstPath + "/../testapp/packer_tool_minify_tests/manifest.json"
    os.chdir(ConstPath + "/../testapp/packer_tool_minify_tests")
    cmd = "python %smake_apk.py --package=org.xwalk.compressor --arch=%s --mode=%s --manifest=%s --project-dir=compressor" % \
            (Pck_Tools, ARCH, MODE, manifestPath)
    packstatus = commands.getstatusoutput(cmd + compre)
    self.assertEquals(0, packstatus[0])
    print "Generate APK ----------------> OK!"
    compDir = ConstPath + "/../testapp/packer_tool_minify_tests/compressor/Compressor/assets/www/resource/"
    oriDir = ConstPath + "/../testapp/packer_tool_minify_tests/resource/"
    self.assertIn("script.js", os.listdir(compDir))
    self.assertIn("style.css", os.listdir(compDir))

#test for description
def clear_description():
    if os.path.exists(ConstPath + "/../testapp/example/example"):
       try:
          os.remove(ConstPath + "/../testapp/example/Example.apk")
          shutil.rmtree(ConstPath + "/../testapp/example/example")
       except Exception,e:
          os.system("rm -rf " + ConstPath + "/../testapp/example/example")
          os.system(ConstPath + "/../testapp/packer_tool_minify_tests/*.apk")

def description(descPara, desc, self):
    setUp()
    clear_description()
    appRoot = ConstPath + "/../testapp/example/"
    os.chdir(appRoot)
    cmd = "python %smake_apk.py --package=org.xwalk.example --name=example --arch=%s --mode=%s --app-root=%s --app-local-path=index.html --project-dir=example" % \
          (Pck_Tools, ARCH, MODE, appRoot)
    print cmd + descPara
    packstatus = commands.getstatusoutput(cmd + descPara)
    self.assertEquals(0, packstatus[0])
    print "Generate APK ----------------> OK!"
    os.chdir("example/Example")
    am = open(os.getcwd() + "/AndroidManifest.xml")
    amlines = am.readlines()
    for i in range(len(amlines)):
         adv = amlines[4][12:54].strip()
         ad = amlines[4][12:32].strip() 
         sd = amlines[4][34:53].strip()
         self.assertIn(ad, adv)
         self.assertIn(sd, adv)

    fp = open(os.getcwd() + "/res/values/strings.xml")
    lines = fp.readlines()
    for i in range(len(lines)):
        l = lines[i].strip("\n\r").strip()
        if i < len(lines):
            if desc in l:
                self.assertIn(desc, l)
                print "Find"
            elif (i == len(lines)-1) and desc not in l:
                self.assertFalse(True, "No find " + desc)
            else:
                print i
        else:
            self.assertFalse(True, "No find " + desc)
    clear_description()

# test manifest versionCode option
def versionCode(cmd, flag, base, self):
    setUp()
    packstatus = commands.getstatusoutput(cmd + flag + base)
    self.assertEquals(packstatus[0] ,0)
    fp = open(ConstPath + "/../testapp/example/test/Example/AndroidManifest.xml")
    lines = fp.readlines()
    for i in range(len(lines)): 
        line = lines[i].strip("\n\r").strip()
        findLine = "<manifest"
        if i <= len(lines):
            if findLine in line:
                print "Find"
                l = lines[i].strip("\n\r").strip()
                result = l.index("versionCode")
                end = l.index("versionName")
                if flag != "":
                    start = result
                    self.assertIn('11', l[start:end])
                elif base != "":
                    start = result
                    self.assertIn('1234567', l[start:end])
                else:
                    start = result
                    self.assertIn('10000', l[start:end])
                break
            else:
                print "Continue find"
        else:
            self.assertIn(findLine, line)
    clear_versionCode()

def clear_versionCode():
    targetDir = ConstPath + "/../testapp/example"
    if os.path.exists(targetDir + "/test"):
        try:
            os.remove(targetDir + "/Example_x86.apk")
            shutil.rmtree(targetDir + "/test")
        except Exception,e:
            os.system("rm -rf " + targetDir + "/*.apk")
            os.system("rm -rf " + targetDir + "/test")
