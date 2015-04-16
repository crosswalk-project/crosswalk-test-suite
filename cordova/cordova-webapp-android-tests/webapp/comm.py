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
#         Cici,Li<cici.x.li@intel.com>
#         Lin, Wanming <wanming.lin@intel.com>

import os, sys, commands, shutil, glob
reload(sys)
sys.setdefaultencoding( "utf-8" )

script_path = os.path.realpath(__file__)
const_path = os.path.dirname(script_path)
sample_src_pref = "/tmp/crosswalk-demos/"
pack_tool = const_path + "/../tools/cordova/"
plugin_tool = const_path + "/../tools/cordova-crosswalk-engine/"
testapp_path = "/tmp/cordova-sampleapp/"

def setUp():
    global ARCH, MODE, VERSION, device

    device = os.environ.get('DEVICE_ID')

    if not device:
        print (" get env error\n")
        sys.exit(1)

    f_arch = open(const_path + "/../arch.txt", 'r')
    if f_arch.read().strip("\n\t") == "arm":
        ARCH = "arm"
    elif f_arch.read().strip("\n\t") == "x86":
        ARCH = "x86"
    else:
        print (" get arch error, the content of arch.txt should be 'arm' or 'x86'\n")
        sys.exit(1)
    f_arch.close()

    f_mode = open(const_path + "/../mode.txt", 'r')
    if f_mode.read().strip("\n\t") == "shared":
        MODE = "shared"
    elif f_mode.read().strip("\n\t") == "embedded":
        MODE = "embedded"
    else:
        print (" get mode error, the content of mode.txt should be 'shared' or 'embedded'\n")
        sys.exit(1)
    f_mode.close()

    f_version = open(const_path + "/../cordova-version", 'r')
    if f_version.read().strip("\n\t") != "3.6":
        VERSION = "4.0"
    else:
        VERSION = "3.6"
    f_version.close()

def create(cmd, appname, self):
    os.chdir(pack_tool)
    if os.path.exists(os.path.join(pack_tool, appname)):
        print "Existing %s project, try to clean up..." % appname
        do_remove(glob.glob(os.path.join(pack_tool, appname)))
    print "Create project %s ----------------> START" % appname
    print cmd
    createstatus = commands.getstatusoutput(cmd)
    self.assertEquals(0, createstatus[0])
    print "\nGenerate project %s ----------------> OK\n" % appname
    result = commands.getstatusoutput("ls")
    self.assertIn(appname, result[1])
    if VERSION == "4.0":
        print "Install Crosswalk WebView Plugin --------------> START"
        os.chdir(os.path.join(pack_tool, appname))
        plugin_install_cmd = "plugman install --platform android --project ./ --plugin %s" % plugin_tool
        pluginstatus = commands.getstatusoutput(plugin_install_cmd)
        self.assertEquals(0, pluginstatus[0])

def build(cmd, appname, self):
    os.chdir(os.path.join(pack_tool, appname))
    print "Build project %s ----------------> START" % appname
    print cmd
    buildstatus = commands.getstatusoutput(cmd)
    self.assertEquals(0, buildstatus[0])
    print "\nBuild project %s ----------------> OK\n" % appname
    if VERSION == "4.0":
        os.chdir(os.path.join(pack_tool, appname, "build", "outputs", "apk"))
    else:
        os.chdir(os.path.join(pack_tool, appname, "bin"))
    result = commands.getstatusoutput("ls")
    self.assertIn(".apk", result[1])
    self.assertIn(appname, result[1])

def run(cmd, appname, self):
    os.chdir(os.path.join(pack_tool, appname))
    print "Run project %s ----------------> START" % appname
    print cmd
    runstatus = commands.getstatusoutput(cmd)
    self.assertEquals(0, runstatus[0])
    self.assertIn("LAUNCH SUCCESS", runstatus[1])
    print "\nRun project %s ----------------> OK\n" % appname

def app_install(appname, pkgname, self):
    print "Install APK ----------------> START"
    os.chdir(testapp_path)
    apk_file = commands.getstatusoutput("ls | grep %s" % appname)[1]
    if apk_file == "":
        print "Error: No app: %s found in directory: %s" % (appname, testapp_path)
    cmd_inst = "adb -s " + device + " install -r " + apk_file
    inststatus = commands.getstatusoutput(cmd_inst)
    self.assertEquals(0, inststatus[0])
    print "Install APK ----------------> OK"
    self.assertTrue(check_app_installed(pkgname, self))

def check_app_installed(pkgname, self):
    print "Check if app is installed ----------------> START"
    cmd_find = "adb -s " + device + " shell pm list packages |grep %s" % pkgname
    pmstatus = commands.getstatusoutput(cmd_find)
    if pmstatus[0] == 0:
        print "App is installed."
        return True
    else:
        print "App is uninstalled."
        return False

def app_launch(cmd, self):
    print "Launch APK ----------------> START" 
    launchstatus = commands.getstatusoutput(cmd)
    self.assertNotIn("error", launchstatus[1].lower())
    print "Launch APK ----------------> OK"

def app_stop(cmd, self):
    print "Stop APK ----------------> START" 
    stopstatus = commands.getstatusoutput(cmd)
    self.assertEquals(0, stopstatus[0])
    print "Stop APK ----------------> OK"

def app_uninstall(pkgname, self):
    print "Uninstall APK ----------------> START"
    cmd_uninst = "adb -s " + device + " uninstall %s" % (pkgname)
    unistatus = commands.getstatusoutput(cmd_uninst)
    self.assertEquals(0, unistatus[0])
    print "Uninstall APK ----------------> OK"

def replace_key(file_path, content, key):
    print "Replace value ----------------> START"
    f = open(file_path, "r")
    f_content = f.read()
    f.close()
    pos = f_content.find(key)
    if pos != -1:
        f_content = f_content.replace(key, content)
        f = open(file_path, "w")
        f.write(f_content)
        f.close()
    else:
        print "Fail to replace: %s with: %s in file: %s" % (content, key, file_path)
        return False
    print "Replace value ----------------> OK"
    return True

def do_remove(target_file_list=None):
    for i_file in target_file_list:
        print "Removing %s" % i_file
        try:
            if os.path.isdir(i_file):
                shutil.rmtree(i_file)
            else:
                os.remove(i_file)
        except Exception as e:
            print "Fail to remove file %s: %s" % (i_file, e)
            return False
    return True



