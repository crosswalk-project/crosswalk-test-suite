#!/usr/bin/env python
# coding=utf-8
#
# Copyright (c) 2016 Intel Corporation.
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

import os
import sys
import commands
import shutil
import glob
import fnmatch
import re
import json
from os.path import join, getsize
reload(sys)
sys.setdefaultencoding("utf-8")
script_path = os.path.realpath(__file__)
const_path = os.path.dirname(script_path)
tool_path = const_path + "/../tools/"
plugin_tool = const_path + "/../tools/cordova-plugin-crosswalk-webview/"
testapp_path = "/tmp/cordova-sampleapp/"


def setUp():
    global ARCH, MODE, device, CROSSWALK_VERSION, CROSSWALK_BRANCH, PACK_TYPE

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
    elif arch_tmp.strip("\n\t") == "arm64":
        ARCH = "arm64"
    elif arch_tmp.strip("\n\t") == "x86_64":
        ARCH = "x86_64"
    else:
        print (
            " get arch error, the content of arch.txt should be 'arm' or 'x86' or arm64 or x86_64\n")
        sys.exit(1)
    f_arch.close()

    f_mode = open(const_path + "/../mode.txt", 'r')
    mode_tmp = f_mode.read()
    if mode_tmp.strip("\n\t") == "shared":
        MODE = "shared"
    elif mode_tmp.strip("\n\t") == "embedded":
        MODE = "embedded"
    elif mode_tmp.strip("\n\t") == "lite":
        MODE = "lite"
    else:
        print (
            " get mode error, the content of mode.txt should be 'shared' or 'embedded' or 'lite'\n")
        sys.exit(1)
    f_mode.close()


    f_pack_type = open(const_path + "/../pack-type", 'r')
    pack_type_tmp = f_pack_type.read()
    if pack_type_tmp.strip("\n\t") == "local":
        PACK_TYPE = "local"
    elif pack_type_tmp.strip("\n\t") == "npm":
        PACK_TYPE = "npm"
    else:
        print (
            " get pack type error, the content of pack-type should be 'local' or 'npm'\n")
        sys.exit(1)
    f_pack_type.close()

    with open(const_path + "/../VERSION", "rt") as pkg_version_file:
        pkg_version_raw = pkg_version_file.read()
        pkg_version_file.close()
        pkg_version_json = json.loads(pkg_version_raw)
        CROSSWALK_VERSION = pkg_version_json["main-version"]
        CROSSWALK_BRANCH = pkg_version_json["crosswalk-branch"]

def checkFileSize(file_path, min_size, max_size, self):
    print "Check file size from %s --------------> START" % file_path
    size = getsize(file_path)/1024/1024
    print "this file is %s MB" % size
    self.assertTrue(size > min_size)
    self.assertTrue(size < max_size)
    print "Check file size from %s --------------> OK" % file_path


def installWebviewPlugin(pkg_mode, self, multiple_apks = None):
    print "Install Crosswalk WebView Plugin --------------> START"
    pkg_mode_tmp = "core"
    if pkg_mode == "shared":
        pkg_mode_tmp = "shared"

    xwalk_version = "%s" % CROSSWALK_VERSION
    if CROSSWALK_BRANCH == "beta":
        xwalk_version = "org.xwalk:xwalk_%s_library_beta:%s" % (pkg_mode_tmp, CROSSWALK_VERSION)

    plugin_crosswalk_source = plugin_tool
    if PACK_TYPE == "npm":
        plugin_crosswalk_source = "cordova-plugin-crosswalk-webview"

    plugin_install_cmd = "cordova plugin add %s --variable XWALK_MODE=\"%s\"" \
                " --variable XWALK_VERSION=\"%s\"" % (plugin_crosswalk_source, pkg_mode, xwalk_version)

    if multiple_apks is not None:
        plugin_install_cmd = plugin_install_cmd + " --variable XWALKMULTIPLEAPK=\"%s\"" % multiple_apks

    print plugin_install_cmd

    pluginstatus = commands.getstatusoutput(plugin_install_cmd)
    self.assertEquals(0, pluginstatus[0])

def create(appname, pkgname, mode, sourcecodepath, replace_index_list, self, extra_plugin = None, multiple_apks = None):
    os.chdir(tool_path)
    if os.path.exists(os.path.join(tool_path, appname)):
        print "Existing %s project, try to clean up..." % appname
        do_remove(glob.glob(os.path.join(tool_path, appname)))
    print "Create project %s ----------------> START" % appname
    cmd = "cordova create %s %s %s" % (appname, pkgname, appname)
    createstatus = commands.getstatusoutput(cmd)
    self.assertEquals(0, createstatus[0])
    print "\nGenerate project %s ----------------> OK\n" % appname
    result = commands.getstatusoutput("ls")
    self.assertIn(appname, result[1])
    project_root = os.path.join(tool_path, appname)
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
    installWebviewPlugin(mode, self, multiple_apks)

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

def buildGoogleApp(appname, sourcecodepath, self):
    os.chdir(tool_path)
    if os.path.exists(os.path.join(tool_path, appname)):
        print "Existing %s project, try to clean up..." % appname
        do_remove(glob.glob(os.path.join(tool_path, appname)))
    print "Build project %s ----------------> START" % appname
    if sourcecodepath is None:
        print "sourcecodepath can't be none"
        return False

    if checkContains(appname, "CIRC"):
        cordova_app = os.path.join(tool_path, "circ")
        create_cmd = "cca create " + appname + " --link-to circ/package"
    elif checkContains(appname, "EH"):
        cordova_app = os.path.join(tool_path, "workshop-cca-eh")
        create_cmd = "cca create " + appname + " --link-to workshop-cca-eh/workshop/step4"

    if os.path.exists(cordova_app):
        do_remove(glob.glob(cordova_app))
    if not do_copy(sourcecodepath, cordova_app):
        return False

    print create_cmd
    buildstatus = commands.getstatusoutput(create_cmd)
    self.assertEquals(0, buildstatus[0])
    os.chdir(os.path.join(tool_path, appname))

    print "Add android platforms to this project --------------> START"
    add_android_cmd = "cca platform add android"
    addstatus = commands.getstatusoutput(add_android_cmd)
    self.assertEquals(0, addstatus[0])

    print "uninstall webview default plugin from this project --------------> START"
    plugin_uninstall_webview = "cordova plugin remove cordova-plugin-crosswalk-webview"
    uninstallStatus = commands.getstatusoutput(plugin_uninstall_webview)
    self.assertEquals(0, uninstallStatus[0])

    installWebviewPlugin(MODE, self)

    build_cmd = "cca build android"
    if ARCH == "x86_64" or ARCH == "arm64":
        build_cmd = "cca build android --xwalk64bit"

    buildstatus = commands.getstatusoutput(build_cmd)
    self.assertEquals(0, buildstatus[0])
    checkApkExist(appname, self)

def build(appname, isDebug, self, isCopy=False, isMultipleApk=True):
    os.chdir(os.path.join(tool_path, appname))
    print "Build project %s ----------------> START" % appname

    pack_arch_tmp = ARCH
    if ARCH == "x86_64":
        pack_arch_tmp = "x86 --xwalk64bit"
    elif ARCH == "arm64":
        pack_arch_tmp = "arm --xwalk64bit"

    cmd_mode = ""
    apk_name_mode = "debug"
    if isDebug == 1:
        print "build debug app"
        cmd_mode = "--debug"
    elif isDebug == -1:
        print "build release app"
        cmd_mode = "--release"
        apk_name_mode = "release-unsigned"

    cmd = "cordova build android %s -- --gradleArg=-PcdvBuildArch=%s --minSdkVersion=16" % (cmd_mode, pack_arch_tmp)

    print cmd
    buildstatus = commands.getstatusoutput(cmd)
    self.assertEquals(0, buildstatus[0])
    print "\nBuild project %s ----------------> OK\n" % appname
    checkApkExist(appname, self, isCopy, isMultipleApk, apk_name_mode)
    

def checkApkExist(appname, self, isCopy=False, isMultipleApk=True, apk_name_mode="debug"):
    print "Check  %s Apk Exist ----------------> START" % appname
    outputs_dir = os.path.join(
                      tool_path,
                      appname,
                      "platforms",
                      "android",
                      "build",
                      "outputs",
                      "apk")
    apk_name = "android-%s.apk" % apk_name_mode
    if isMultipleApk == True and MODE == "embedded":
        apk_name_arch = "armv7"
        if ARCH != "arm":
            apk_name_arch = ARCH
        apk_name = "android-%s-%s.apk" % (apk_name_arch, apk_name_mode)

        if not os.path.exists(os.path.join(outputs_dir, apk_name)):
            apk_name = "%s-%s-%s.apk" % (appname, apk_name_arch, apk_name_mode)
    else:
        if not os.path.exists(os.path.join(outputs_dir, apk_name)):
            apk_name = "%s-%s.apk" % (appname, apk_name_mode)
    self.assertTrue(os.path.exists(os.path.join(outputs_dir, apk_name)))
    if isCopy == True:
        self.assertTrue(do_copy(os.path.join(outputs_dir, apk_name), os.path.join(testapp_path, "%s.apk" % appname)))
    
    print "Check  %s Apk Exist ----------------> OK" % appname

def run(appname, self):
    os.chdir(os.path.join(tool_path, appname))
    print "Run project %s ----------------> START" % appname
    cmd = "cordova run android"
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
    print cmd_inst
    inststatus = commands.getstatusoutput(cmd_inst)
    self.assertEquals(0, inststatus[0])
    print "Install APK ----------------> OK"
    self.assertTrue(check_app_installed(pkgname, self))

def checkContains(origin_str=None, key_str=None):
    if origin_str.upper().find(key_str.upper()) >= 0:
        return True
    return False


def check_app_installed(pkgname, self):
    print "Check if app is installed ----------------> START"
    cmd_find = "adb -s " + device + \
        " shell pm list packages |grep %s" % pkgname
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
