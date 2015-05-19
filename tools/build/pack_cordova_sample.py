#!/usr/bin/env python
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
#         Fan, Yugang <yugang.fan@intel.com>
#         Lin, Wanming <wanming.lin@intel.com>

import os
import shutil
import glob
import time
import sys
import stat
import random
import json
import logging
import signal
import commands
import fnmatch
import subprocess
import re
import pexpect
from optparse import OptionParser

reload(sys)
sys.setdefaultencoding('utf8')

TOOL_VERSION = "v0.1"
VERSION_FILE = "VERSION"
DEFAULT_CMD_TIMEOUT = 600
PKG_NAMES = ["gallery", "helloworld", "remotedebugging", "mobilespec"]
CORDOVA_VERSIONS = ["3.6", "4.0"]
PKG_MODES = ["shared", "embedded"]
PKG_ARCHS = ["x86", "arm"]
BUILD_PARAMETERS = None
BUILD_ROOT = None
LOG = None
LOG_LEVEL = logging.DEBUG
BUILD_TIME = time.strftime('%Y%m%d',time.localtime(time.time()))

class ColorFormatter(logging.Formatter):

    def __init__(self, msg):
        logging.Formatter.__init__(self, msg)

    def format(self, record):
        red, green, yellow, blue = range(4)
        colors = {'INFO': green, 'DEBUG': blue,
                  'WARNING': yellow, 'ERROR': red}
        msg = record.msg
        if msg[0] == "+":
            msg = "\33[01m" + msg[1:] + "\033[0m"
        elif msg[0] == "=":
            msg = "\33[07m" + msg + "\033[0m"
        levelname = record.levelname
        if levelname in colors:
            msg_color = "\033[0;%dm" % (
                31 + colors[levelname]) + msg + "\033[0m"
            record.msg = msg_color

        return logging.Formatter.format(self, record)

def replaceUserString(path, fnexp, old_s, new_s):
    for sub_file in iterfindfiles(path,fnexp):
        try:
            with open(sub_file,'r') as sub_read_obj:
                read_string = sub_read_obj.read()
        except IOError as err:
            LOG.error("Read %s Error : "%sub_file + str(err))
            continue
        if read_string.find(old_s) >= 0:
            try:
                with open(sub_file,'w') as sub_write_obj:
                    sub_write_obj.write(re.sub(old_s,new_s,read_string))
            except IOError as err:
                LOG.error("Modify %s Error : "%sub_file + str(err))
                continue

def iterfindfiles(path, fnexp):
    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files, fnexp):
            yield os.path.join(root, filename)

def isWindows():
    return sys.platform == "cygwin" or sys.platform.startswith("win")


def killProcesses(ppid=None):
    if isWindows():
        subprocess.check_call("TASKKILL /F /PID %s /T" % ppid)
    else:
        ppid = str(ppid)
        pidgrp = []

        def GetChildPids(ppid):
            command = "ps -ef | awk '{if ($3 ==%s) print $2;}'" % str(ppid)
            pids = os.popen(command).read()
            pids = pids.split()
            return pids

        pidgrp.extend(GetChildPids(ppid))
        for pid in pidgrp:
            pidgrp.extend(GetChildPids(pid))

        pidgrp.insert(0, ppid)
        while len(pidgrp) > 0:
            pid = pidgrp.pop()
            try:
                os.kill(int(pid), signal.SIGKILL)
                return True
            except OSError:
                try:
                    os.popen("kill -9 %d" % int(pid))
                    return True
                except Exception:
                    return False


def checkContains(origin_str=None, key_str=None):
    if origin_str.upper().find(key_str.upper()) >= 0:
        return True
    return False


def getRandomStr():
    str_pool = list("abcdefghijklmnopqrstuvwxyz1234567890")
    random_str = ""
    for i in range(15):
        index = random.randint(0, len(str_pool) - 1)
        random_str = random_str + str_pool[index]

    return random_str

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


def doCopy(src_item=None, dest_item=None):
    LOG.info("Copying %s to %s" % (src_item, dest_item))
    try:
        if os.path.isdir(src_item):
            overwriteCopy(src_item, dest_item, symlinks=True)
        else:
            if not os.path.exists(os.path.dirname(dest_item)):
                LOG.info("Create non-existent dir: %s" %
                         os.path.dirname(dest_item))
                os.makedirs(os.path.dirname(dest_item))
            shutil.copy2(src_item, dest_item)
    except Exception as e:
        LOG.error("Fail to copy file %s: %s" % (src_item, e))
        return False

    return True


def doRemove(target_file_list=None):
    for i_file in target_file_list:
        LOG.info("Removing %s" % i_file)
        try:
            if os.path.isdir(i_file):
                shutil.rmtree(i_file)
            else:
                os.remove(i_file)
        except Exception as e:
            LOG.error("Fail to remove file %s: %s" % (i_file, e))
            return False
    return True


def exitHandler(return_code=1):
    LOG.info("+Cleaning build root folder ...")
    if not BUILD_PARAMETERS.bnotclean and os.path.exists(BUILD_ROOT):
        if not doRemove([BUILD_ROOT]):
            LOG.error("Fail to clean build root, exit ...")
            sys.exit(1)

    if return_code == 0:
        LOG.info("================ DONE ================")
    else:
        LOG.error(
            "================ Found Something Wrong !!! ================")
    sys.exit(return_code)


def prepareBuildRoot():
    LOG.info("+Preparing build root folder ...")
    global BUILD_ROOT

    while True:
        BUILD_ROOT = os.path.join("/tmp", getRandomStr())
        if os.path.exists(BUILD_ROOT):
            continue
        else:
            break

    if not doRemove(
            glob.glob(os.path.join("%s*.apk" % PKG_NAME))):
        return False

    return True


def doCMD(cmd, time_out=DEFAULT_CMD_TIMEOUT, no_check_return=False):
    LOG.info("Doing CMD: [ %s ]" % cmd)
    pre_time = time.time()
    cmd_proc = subprocess.Popen(args=cmd, shell=True)
    while True:
        cmd_exit_code = cmd_proc.poll()
        elapsed_time = time.time() - pre_time
        if cmd_exit_code is None:
            if elapsed_time >= time_out:
                killProcesses(ppid=cmd_proc.pid)
                LOG.error("Timeout to exe CMD")
                return False
        else:
            if not no_check_return and cmd_exit_code != 0:
                LOG.error("Fail to exe CMD")
                return False
            break
        time.sleep(2)
    return True

def replaceKey(file_path, content, key):
    f = open(file_path, "r")
    f_content = f.read()
    f.close()
    pos = f_content.find(key)
    if pos != -1:
        f_content = f_content.replace(key, content)
#       content = content[:(pos-1)] + line_content + "\n" + key + "\n" + content[pos:]
        f = open(file_path, "w")
        f.write(f_content)
        f.close()
    else:
        LOG.error("Fail to replace: %s with: %s in file: %s" % (content, key, file_path))
        return False
    return True

def packMobileSpec(app_name=None):
    pack_tool = os.path.join(BUILD_ROOT, "cordova")
    if not os.path.exists(pack_tool):
        if not doCopy(
                os.path.join(BUILD_PARAMETERS.pkgpacktools, "cordova"),
                pack_tool):
            return False

    orig_dir = os.getcwd()
    os.chdir(pack_tool)
    if BUILD_PARAMETERS.pkgmode == "shared":
        pack_cmd = "bin/create mobilespec org.apache.mobilespec mobilespec --xwalk-shared-library"
    else:
        pack_cmd = "bin/create mobilespec org.apache.mobilespec mobilespec"

    if not doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False
    mobilespec_src = os.path.join(BUILD_ROOT, "mobilespec_src")
    if not os.path.exists(mobilespec_src):
        if not doCopy(
                os.path.join(BUILD_PARAMETERS.pkgpacktools, "mobilespec"),
                mobilespec_src):
            return False

    if not doCopy(
            os.path.join(pack_tool, "mobilespec", "CordovaLib"), 
            os.path.join(mobilespec_src, "platforms", "android", "CordovaLib")):
        return False

    if not doCopy(
            os.path.join(pack_tool, "VERSION"), 
            os.path.join(mobilespec_src, "platforms", "android")):
        return False

    os.chdir(os.path.join(mobilespec_src, "platforms", "android"))

    ANDROID_HOME = "echo $(dirname $(dirname $(which android)))"
    updateproject_cmd = "android update project --subprojects --path . --target \"android-21\""
    antdebug_cmd = "ant debug"
    build_cmd = "cordova build android"
    os.environ['ANDROID_HOME'] = commands.getoutput(ANDROID_HOME)
    if not doCMD(updateproject_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False
    os.chdir(os.path.join(mobilespec_src, "platforms", "android", "CordovaLib"))
    if not doCMD(antdebug_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False
    os.chdir(mobilespec_src)
    if not doCMD(build_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    app_dir = os.path.join(mobilespec_src, "platforms", "android", "out")
    if not doCopy(os.path.join(app_dir, "%s-debug.apk" % app_name),
            os.path.join(orig_dir, "%s.apk" % app_name)):
        if not doCopy(os.path.join(app_dir, "%s-debug-unaligned.apk" % app_name),
            os.path.join(orig_dir, "%s.apk" % app_name)):
            os.chdir(orig_dir)
            return False
    os.chdir(orig_dir)
    return True


def packSampleApp(app_name=None):
    pack_tool = os.path.join(BUILD_ROOT, "cordova")
    if not os.path.exists(pack_tool):
        if not doCopy(
                os.path.join(BUILD_PARAMETERS.pkgpacktools, "cordova"),
                pack_tool):
            return False

    orig_dir = os.getcwd()
    os.chdir(pack_tool)
    if BUILD_PARAMETERS.pkgmode == "shared":
        pack_cmd = "bin/create " + app_name + " com.example." + app_name + " " + app_name + " --xwalk-shared-library"
    else:
        pack_cmd = "bin/create " + app_name + " com.example." + app_name + " " + app_name + " --shared"
    if not doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    if checkContains(app_name, "GALLERY"):
        getsource_cmd = "git clone https://github.com/blueimp/Gallery"
        if not doCMD(getsource_cmd, DEFAULT_CMD_TIMEOUT):
            os.chdir(orig_dir)
            return False
        if not doRemove(glob.glob(os.path.join(pack_tool, app_name, "assets", "www"))):
            os.chdir(orig_dir)
            return False
        if not doCopy(os.path.join(pack_tool, "Gallery"), 
                os.path.join(pack_tool, app_name, "assets", "www")):
            os.chdir(orig_dir)
            return False

    if checkContains(app_name, "HELLOWORLD"):
        if not replaceKey(os.path.join(pack_tool, app_name, "assets", "www", "index.html"), 
                "<a href='http://www.intel.com'>Intel</a>\n</body>",
                "</body>"):
            os.chdir(orig_dir)
            return False

    os.chdir(os.path.join(pack_tool, app_name))

    if BUILD_PARAMETERS.cordovaversion == "4.0":
        if BUILD_PARAMETERS.pkgarch == "x86":
            cordova_tmp_path = os.path.join(BUILD_ROOT, "cordova", app_name, "build", "outputs", "apk", "%s-x86-debug.apk" % app_name)
        else:
            cordova_tmp_path = os.path.join(BUILD_ROOT, "cordova", app_name, "build", "outputs", "apk", "%s-armv7-debug.apk" % app_name)

        plugin_tool = os.path.join(BUILD_ROOT, "cordova_plugins", "cordova-crosswalk-engine")
        if not os.path.exists(plugin_tool):
            if not doCopy(
                    os.path.join(BUILD_PARAMETERS.pkgpacktools, "cordova_plugins", "cordova-crosswalk-engine"),
                    plugin_tool):
                return False
            plugin_install_cmd = "plugman install --platform android --project " \
                                 "./ --plugin %s" % plugin_tool
            if not doCMD(plugin_install_cmd, DEFAULT_CMD_TIMEOUT):
                os.chdir(orig_dir)
                return False
    else:
        cordova_tmp_path = os.path.join(BUILD_ROOT, "cordova", app_name, "bin", "%s-debug.apk" % app_name)
    pack_cmd = "./cordova/build"

    if checkContains(app_name, "REMOTEDEBUGGING"):
        pack_cmd = "./cordova/build --debug"

    ANDROID_HOME = "echo $(dirname $(dirname $(which android)))"
    os.environ['ANDROID_HOME'] = commands.getoutput(ANDROID_HOME)

    if not doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
        pack_cmd = "ant debug"
        if not doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
            os.chdir(orig_dir)
            return False

    if not doCopy(cordova_tmp_path,
            os.path.join(orig_dir, app_name + ".apk")):
        os.chdir(orig_dir)
        return False
    os.chdir(orig_dir)
    return True

def packMobileSpec_cli(app_name=None):
    project_root = os.path.join(BUILD_ROOT, app_name)
    output = commands.getoutput("cordova -v")
    if output != "5.0.0":
        LOG.error("Cordova 4.0 build requires Cordova-CLI 5.0.0, install with command: '$ sudo npm install cordova@5.0.0 -g'")
        return False

    plugin_tool = os.path.join(BUILD_ROOT, "cordova-plugin-crosswalk-webview")
    if not doCopy(os.path.join(BUILD_PARAMETERS.pkgpacktools, "cordova_plugins", "cordova-plugin-crosswalk-webview"), plugin_tool):
        return False

    cordova_mobilespec = os.path.join(BUILD_ROOT, "cordova-mobile-spec")
    if not doCopy(os.path.join(BUILD_PARAMETERS.pkgpacktools, "mobilespec", "cordova-mobile-spec"), cordova_mobilespec):
        return False

    cordova_coho = os.path.join(BUILD_ROOT, "cordova-coho")
    if not doCopy(os.path.join(BUILD_PARAMETERS.pkgpacktools, "mobilespec", "cordova-coho"), cordova_coho):
        return False

    orig_dir = os.getcwd()
    os.chdir(cordova_coho)
    output = commands.getoutput("git pull").strip("\r\n")

    os.chdir(cordova_mobilespec)
    output = commands.getoutput("git pull").strip("\r\n")
    if output == "Already up-to-date.":
        if not doCopy(os.path.join(BUILD_PARAMETERS.pkgpacktools, "mobilespec", "mobilespec"), project_root):
            return False
    else:
        node_modules = os.path.join(cordova_mobilespec, "createmobilespec", "node_modules")
        os.chdir(os.path.join(cordova_mobilespec, "createmobilespec"))
        install_cmd = "sudo npm install"
        LOG.info("Doing CMD: [ %s ]" % install_cmd)
        run = pexpect.spawn(install_cmd)

        index = run.expect(['password', 'node_modules', pexpect.EOF, pexpect.TIMEOUT])
        if index == 0:
            run.sendline(BUILD_PARAMETERS.userpassword)
            index = run.expect(['node_modules', 'password', pexpect.EOF, pexpect.TIMEOUT])
            if index == 0:
                print 'The user password is Correctly'
            else:
                print 'The user password is wrong'
                run.close(force=True)
                return False
        elif index != 1:
            print 'The user password is wrong'
            run.close(force=True)
            return False

        os.chdir(BUILD_ROOT)
        createmobilespec_cmd = "cordova-mobile-spec/createmobilespec/createmobilespec.js --android --global"
        if not doCMD(createmobilespec_cmd, DEFAULT_CMD_TIMEOUT * 3):
            os.chdir(orig_dir)
            return False
        os.chdir(project_root)
        mv_cmd = "mv platforms/android/src/org/apache/mobilespec/MainActivity.java platforms/android/src/org/apache/mobilespec/mobilespec.java"
        if not doCMD(mv_cmd, DEFAULT_CMD_TIMEOUT):
            os.chdir(orig_dir)
            return False
        sed_cmd = "sed -i 's/MainActivity/mobilespec/g' `grep MainActivity -rl *`"
        if not doCMD(sed_cmd, DEFAULT_CMD_TIMEOUT):
            os.chdir(orig_dir)
            return False
    os.chdir(project_root)
    add_webview_cmd = "cordova plugin add ../cordova-plugin-crosswalk-webview/"
    if not doCMD(add_webview_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    ANDROID_HOME = "echo $(dirname $(dirname $(which android)))"
    os.environ['ANDROID_HOME'] = commands.getoutput(ANDROID_HOME)
    pack_cmd = "cordova build android"
    if not doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False
    outputs_dir = os.path.join(project_root, "platforms", "android", "build", "outputs", "apk")
    if BUILD_PARAMETERS.pkgarch == "x86":
        cordova_tmp_path = os.path.join(outputs_dir, "%s-x86-debug.apk"%app_name)
        cordova_tmp_path_spare = os.path.join(outputs_dir, "android-x86-debug.apk")
    else:
        cordova_tmp_path = os.path.join(outputs_dir, "%s-armv7-debug.apk"%app_name)
        cordova_tmp_path_spare = os.path.join(outputs_dir, "android-armv7-debug.apk")
    if os.path.exists(cordova_tmp_path):
        if not doCopy(cordova_tmp_path, os.path.join(orig_dir, "%s.apk" % app_name)):
            os.chdir(orig_dir)
            return False
    elif os.path.exists(cordova_tmp_path_spare):
        if not doCopy(cordova_tmp_path_spare, os.path.join(orig_dir, "%s.apk" % app_name)):
            os.chdir(orig_dir)
            return False
    else:
        os.chdir(orig_dir)
        return False
    os.chdir(orig_dir)
    return True


def packSampleApp_cli(app_name=None):
    project_root = os.path.join(BUILD_ROOT, app_name)

    output = commands.getoutput("cordova -v")
    if output != "5.0.0":
        LOG.error("Cordova 4.0 build requires Cordova-CLI 5.0.0, install with command: '$ sudo npm install cordova@5.0.0 -g'")
        return False

    plugin_tool = os.path.join(BUILD_ROOT, "cordova_plugins")
    if not os.path.exists(plugin_tool):
        if not doCopy(
                os.path.join(BUILD_PARAMETERS.pkgpacktools, "cordova_plugins"),
                plugin_tool):
            return False

    orig_dir = os.getcwd()
    os.chdir(BUILD_ROOT)
    pack_cmd = "cordova create %s com.example.%s %s" % (
        app_name, app_name, app_name)

    if not doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    ### Set activity name as app_name
    replaceUserString(project_root, 'config.xml', '<widget', '<widget android-activityName="%s"' % app_name)
    ### Workaround for XWALK-3679
    replaceUserString(project_root, 'config.xml', '</widget>', '    <allow-navigation href="*" />\n</widget>')

    if checkContains(app_name, "GALLERY"):
        getsource_cmd = "git clone https://github.com/blueimp/Gallery"
        if not doCMD(getsource_cmd, DEFAULT_CMD_TIMEOUT):
            os.chdir(orig_dir)
            return False
        if not doRemove(glob.glob(os.path.join(project_root, "www"))):
            os.chdir(orig_dir)
            return False
        if not doCopy(os.path.join(BUILD_ROOT, "Gallery"), 
                os.path.join(project_root, "www")):
            os.chdir(orig_dir)
            return False

    if checkContains(app_name, "HELLOWORLD"):
        if not replaceKey(os.path.join(project_root, "www", "index.html"), 
                "<a href='http://www.intel.com'>Intel</a>\n</body>",
                "</body>"):
            os.chdir(orig_dir)
            return False

    os.chdir(project_root)
    pack_cmd = "cordova platform add android"
    if not doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    plugin_dirs = os.listdir(plugin_tool)
    for i_dir in plugin_dirs:
        i_plugin_dir = os.path.join(plugin_tool, i_dir)
        plugin_install_cmd = "cordova plugin add %s" % i_plugin_dir
        if not doCMD(plugin_install_cmd, DEFAULT_CMD_TIMEOUT):
            os.chdir(orig_dir)
            return False

    ANDROID_HOME = "echo $(dirname $(dirname $(which android)))"
    os.environ['ANDROID_HOME'] = commands.getoutput(ANDROID_HOME)
    pack_cmd = "cordova build android"

    if checkContains(app_name, "REMOTEDEBUGGING"):
        pack_cmd = "cordova build android --debug"

    if not doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    outputs_dir = os.path.join(project_root, "platforms", "android", "build", "outputs", "apk")

    if BUILD_PARAMETERS.pkgarch == "x86":
        cordova_tmp_path = os.path.join(outputs_dir, "%s-x86-debug.apk"%app_name)
        cordova_tmp_path_spare = os.path.join(outputs_dir, "android-x86-debug.apk")
    else:
        cordova_tmp_path = os.path.join(outputs_dir, "%s-armv7-debug.apk"%app_name)
        cordova_tmp_path_spare = os.path.join(outputs_dir, "android-armv7-debug.apk")

    if not os.path.exists(cordova_tmp_path):
        if not doCopy(cordova_tmp_path_spare, os.path.join(orig_dir, "%s.apk" % app_name)):
            os.chdir(orig_dir)
            return False
    else:
        if not doCopy(cordova_tmp_path, os.path.join(orig_dir, "%s.apk" % app_name)):
            os.chdir(orig_dir)
            return False
    os.chdir(orig_dir)
    return True

def packAPP(app_name=None):
    LOG.info("Packing %s" % (app_name))

    if checkContains(app_name, "MOBILESPEC"):
        if BUILD_PARAMETERS.cordovaversion == "4.0":
            if not BUILD_PARAMETERS.userpassword:
                LOG.error("User password is required")
                return False
            if not packMobileSpec_cli(app_name):
                return False
        else:
            if not packMobileSpec(app_name):
                return False
    else:
        if BUILD_PARAMETERS.cordovaversion == '4.0':
            if not packSampleApp_cli(app_name):
                return False
        else:
            if not packSampleApp(app_name):
                return False

    LOG.info("Success to pack APP: %s" % app_name)
    return True


def main():
    global LOG
    LOG = logging.getLogger("pack-tool")
    LOG.setLevel(LOG_LEVEL)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(LOG_LEVEL)
    stream_formatter = ColorFormatter("[%(asctime)s] %(message)s")
    stream_handler.setFormatter(stream_formatter)
    LOG.addHandler(stream_handler)

    try:
        usage = "Usage: ./pack.py -t apk -m shared -a x86"
        opts_parser = OptionParser(usage=usage)
        opts_parser.add_option(
            "-n",
            "--name",
            dest="pkgname",
            help="specify the pkg name, e.g. gallery, helloworld, remotedebugging, mobilespec ...")
        opts_parser.add_option(
            "--cordova-version",
            dest="cordovaversion",
            help="specify the cordova, e.g. 3.6, 4.0 ...")
        opts_parser.add_option(
            "--tools",
            dest="pkgpacktools",
            help="specify the parent folder of pack tools")
        opts_parser.add_option(
            "--notclean",
            dest="bnotclean",
            action="store_true",
            help="disable the build root clean after the packing")
        opts_parser.add_option(
            "-v",
            "--version",
            dest="bversion",
            action="store_true",
            help="show this tool's version")
        opts_parser.add_option(
            "-m",
            "--mode",
            dest="pkgmode",
            help="specify the apk mode, not for cordova version 4.0, e.g. shared, embedded")
        opts_parser.add_option(
            "-a",
            "--arch",
            dest="pkgarch",
            help="specify the apk arch, not for cordova version 3.6, e.g. x86, arm")
        opts_parser.add_option(
            "-p",
            "--password",
            dest="userpassword",
            help="specify the user password of PC")

        if len(sys.argv) == 1:
            sys.argv.append("-h")

        global BUILD_PARAMETERS
        (BUILD_PARAMETERS, args) = opts_parser.parse_args()
    except Exception as e:
        LOG.error("Got wrong options: %s, exit ..." % e)
        sys.exit(1)

    if BUILD_PARAMETERS.bversion:
        print "Version: %s" % TOOL_VERSION
        sys.exit(0)

    if not BUILD_PARAMETERS.pkgname:
        LOG.error("No pkg name provided, exit ...")
        sys.exit(1)
    elif not BUILD_PARAMETERS.pkgname in PKG_NAMES:
        LOG.error("Wrong pkg name, only support: %s, exit ..." %
                  PKG_NAMES)
        sys.exit(1)

    if not BUILD_PARAMETERS.cordovaversion:
        LOG.error("No cordova version provided, exit ...")
        sys.exit(1)
    elif not BUILD_PARAMETERS.cordovaversion in CORDOVA_VERSIONS:
        LOG.error("Wrong cordova version, only support: %s, exit ..." %
                  CORDOVA_VERSIONS)
        sys.exit(1)

    if BUILD_PARAMETERS.pkgarch and not BUILD_PARAMETERS.pkgarch in PKG_ARCHS:
        LOG.error("Wrong pkg-arch, only support: %s, exit ..." %
                  PKG_ARCHS)
        sys.exit(1)

    if BUILD_PARAMETERS.pkgmode and not BUILD_PARAMETERS.pkgmode in PKG_MODES:
        LOG.error("Wrong pkg-mode, only support: %s, exit ..." %
                  PKG_MODES)
        sys.exit(1)

    if BUILD_PARAMETERS.cordovaversion == '3.6' and BUILD_PARAMETERS.pkgarch:
        LOG.error("Command -a is not for cordova version 3.6")
        sys.exit(1)

    if BUILD_PARAMETERS.cordovaversion == '4.0' and BUILD_PARAMETERS.pkgmode:
        LOG.error("Command -m is only for cordova version 3.6")
        sys.exit(1)

    if not BUILD_PARAMETERS.pkgpacktools:
        BUILD_PARAMETERS.pkgpacktools = os.path.join(os.getcwd(), "..", "..", "tools")
    BUILD_PARAMETERS.pkgpacktools = os.path.expanduser(
        BUILD_PARAMETERS.pkgpacktools)

    config_json = None

    global PKG_NAME, CORDOVA_VERSION
    PKG_NAME = BUILD_PARAMETERS.pkgname
    CORDOVA_VERSION = BUILD_PARAMETERS.cordovaversion

    LOG.info("================= %s (cordova-%s) ================" %
             (PKG_NAME, CORDOVA_VERSION))

    if not prepareBuildRoot():
        exitHandler(1)

    LOG.info("+Building package APP ...")
    if not packAPP(PKG_NAME):
        exitHandler(1)

if __name__ == "__main__":
    main()
    exitHandler(0)
