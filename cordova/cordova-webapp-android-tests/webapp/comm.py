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

import os, sys, commands, shutil, glob, fnmatch, re
reload(sys)
sys.setdefaultencoding( "utf-8" )
script_path = os.path.realpath(__file__)
const_path = os.path.dirname(script_path)
tool_path = const_path + "/../tools/"
plugin_tool = const_path + "/../tools/cordova-plugin-crosswalk-webview/"
testapp_path = "/tmp/cordova-sampleapp/"

def setUp():
    global ARCH, MODE, VERSION, device

    device = os.environ.get('DEVICE_ID')

    if not device:
        print (" get env error\n")
        sys.exit(1)

    f_arch = open(const_path + "/../arch.txt", 'r')
    arch_tmp = f_arch.read()
    if arch_tmp.strip("\n\t") == "arm":
        ARCH = "arm"
    elif arch_tmp.strip("\n\t") == "x86":
        ARCH = "x86"
    else:
        print (" get arch error, the content of arch.txt should be 'arm' or 'x86'\n")
        sys.exit(1)
    f_arch.close()

    f_mode = open(const_path + "/../mode.txt", 'r')
    mode_tmp = f_mode.read()
    if mode_tmp.strip("\n\t") == "shared":
        MODE = "shared"
    elif mode_tmp.strip("\n\t") == "embedded":
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

def create(appname, pkgname, mode, sourcecodepath, replace_index_list, self):
    os.chdir(tool_path)
    if os.path.exists(os.path.join(tool_path, appname)):
        print "Existing %s project, try to clean up..." % appname
        do_remove(glob.glob(os.path.join(tool_path, appname)))
    print "Create project %s ----------------> START" % appname
    if VERSION == "4.0":
        cmd = "cordova create %s %s %s" % (appname, pkgname, appname)
    else:
        if mode == "shared":
            cmd = "cordova/bin/create %s %s %s --xwalk-shared-library" % (appname, pkgname, appname)
        else:
            cmd = "cordova/bin/create %s %s %s" % (appname, pkgname, appname)
    createstatus = commands.getstatusoutput(cmd)
    self.assertEquals(0, createstatus[0])
    print "\nGenerate project %s ----------------> OK\n" % appname
    result = commands.getstatusoutput("ls")
    self.assertIn(appname, result[1])
    project_root = os.path.join(tool_path, appname)
    if VERSION == "4.0":
        os.chdir(project_root)
        if not replace_key(os.path.join(project_root, 'config.xml'), 
                '<widget android-activityName="%s"' % appname, '<widget'):
           print "replace key '<widget' failed."
           return False
        if not replace_key(os.path.join(project_root, 'config.xml'), 
                '    <allow-navigation href="*" />\n</widget>', '</widget>'):
           print "replace key '</widget>' failed."
           return False

        print "Add android platforms to this project --------------> START"
        cordova_platform_cmd = "cordova platform add android"
        platformstatus = commands.getstatusoutput(cordova_platform_cmd)
        self.assertEquals(0, platformstatus[0])

        print "Install Crosswalk WebView Plugin --------------> START"
        plugin_install_cmd = "cordova plugin add %s" % plugin_tool
        pluginstatus = commands.getstatusoutput(plugin_install_cmd)
        self.assertEquals(0, pluginstatus[0])
        if replace_index_list is not None and len(replace_index_list) >= 2:
            index_file_path = os.path.join(project_root, "www", "index.html")
            key = replace_index_list[0]
            content = replace_index_list[1]
            if not replace_key(index_file_path, content, key):
                print "replace key: " + key + " failed."
                return False
        if sourcecodepath is not None:
            do_remove(glob.glob(os.path.join(project_root, "www")))
            do_copy(sourcecodepath, os.path.join(tool_path, appname, "www"))
    else:
        if replace_index_list is not None and len(replace_index_list) >= 2:
            index_file_path = os.path.join(project_root, "assets", "www", "index.html")
            key = replace_index_list[0]
            content = replace_index_list[1]
            if not replace_key(index_file_path, content, key):
                print "replace key: " + key + " failed."
                return False
        if sourcecodepath is not None:
            do_remove(glob.glob(os.path.join(project_root, "assets", "www")))
            do_copy(sourcecodepath, os.path.join(tool_path, appname, "assets", "www"))


def build(appname, isDebug, self):
    os.chdir(os.path.join(tool_path, appname))
    print "Build project %s ----------------> START" % appname
    if VERSION == "4.0":
        cmd = "cordova build android"
        if isDebug == True:
            print "build debug app"
            cmd = "cordova build android --debug"
    else:
        cmd = "./cordova/build"
        if isDebug == True:
            print "build debug app"
            cmd = "./cordova/build --debug"
    print cmd
    buildstatus = commands.getstatusoutput(cmd)
    self.assertEquals(0, buildstatus[0])
    print "\nBuild project %s ----------------> OK\n" % appname
    if VERSION == "4.0":
        os.chdir(os.path.join(tool_path, appname, "platforms", "android", "build", "outputs", "apk"))
    else:
        os.chdir(os.path.join(tool_path, appname, "bin"))
    result = commands.getstatusoutput("ls")
    self.assertIn(".apk", result[1])
    print result[1]
    if "android" in result[1]:
        self.assertIn("android", result[1])
    else:
        self.assertIn(appname, result[1])

def run(appname, self):
    os.chdir(os.path.join(tool_path, appname))
    print "Run project %s ----------------> START" % appname
    if VERSION == "4.0":
       cmd = "cordova run android"
    else:
       cmd = "./cordova/run"
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

def iterfindfiles(path, fnexp):
    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files, fnexp):
            yield os.path.join(root, filename)

def checkContains(origin_str=None, key_str=None):
    if origin_str.upper().find(key_str.upper()) >= 0:
        return True
    return False

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

def app_launch(appname, pkgname, self):
    print "Launch APK ----------------> START" 
    cmd = "adb -s " + device + " shell am start -n %s/.%s" % (pkgname, appname)
    launchstatus = commands.getstatusoutput(cmd)
    self.assertNotIn("error", launchstatus[1].lower())
    print "Launch APK ----------------> OK"

# Find whether the app have launched
def check_app_launched(pkgname, self):
    cmd_acti = "adb -s " + device + " shell ps | grep %s" % pkgname
    launched = commands.getstatusoutput(cmd_acti)
    if launched[0] != 0:
        print "App haven't launched."
        return False
    else:
        print "App is have launched."
        return True

def app_stop(pkgname, self):
    print "Stop APK ----------------> START"
    cmd = "adb -s " + device + " shell am force-stop %s" % pkgname
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

def do_copy(src_item=None, dest_item=None):
    print "Copying %s to %s" % (src_item, dest_item)
    try:
        if os.path.isdir(src_item):
            overwriteCopy(src_item, dest_item, symlinks=True)
        else:
            if not os.path.exists(os.path.dirname(dest_item)):
                print "Create non-existent dir: %s" % os.path.dirname(dest_item)
                os.makedirs(os.path.dirname(dest_item))
            shutil.copy2(src_item, dest_item)
    except Exception as e:
        print "Fail to copy file %s: %s" % (src_item, e)
        return False

    return True

def overwriteCopy(src, dest, symlinks=False, ignore=None):
    if not os.path.exists(dest):
        os.makedirs(dest)
        shutil.copystat(src, dest)
    sub_list = os.listdir(src)
    if ignore:
        excl = ignore(src, sub_list)
        sub_list = [x for x in sub_list if x not in excl]
    for i_sub in sub_list:
        s_path = os.path.join(src, i_sub)
        d_path = os.path.join(dest, i_sub)
        if symlinks and os.path.islink(s_path):
            if os.path.lexists(d_path):
                os.remove(d_path)
            os.symlink(os.readlink(s_path), d_path)
            try:
                s_path_s = os.lstat(s_path)
                s_path_mode = stat.S_IMODE(s_path_s.st_mode)
                os.lchmod(d_path, s_path_mode)
            except Exception:
                pass
        elif os.path.isdir(s_path):
            overwriteCopy(s_path, d_path, symlinks, ignore)
        else:
            shutil.copy2(s_path, d_path)

