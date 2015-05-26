#!/usr/bin/env python
#
# Copyright (c) 2014 Intel Corporation.
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

import os
import shutil
import glob
import time
import sys
import stat
import random
import json
import logging
import zipfile
import signal
import fnmatch
import subprocess
import commands
import re
from optparse import OptionParser

reload(sys)
sys.setdefaultencoding('utf8')

TOOL_VERSION = "v0.1"
VERSION_FILE = "VERSION"
DEFAULT_CMD_TIMEOUT = 600
PKG_TYPES = [
    "apk",
    "xpk",
    "wgt",
    "apk-aio",
    "cordova-aio",
    "cordova",
    "embeddingapi"]
PKG_MODES = ["shared", "embedded"]
PKG_ARCHS = ["x86", "arm"]
PKG_BLACK_LIST = []
PKG_NAME = None
BUILD_PARAMETERS = None
BUILD_ROOT = None
BUILD_ROOT_SRC = None
BUILD_ROOT_SRC_PKG = None
BUILD_ROOT_SRC_PKG_APP = None
BUILD_ROOT_SRC_SUB_APP = None
BUILD_ROOT_PKG = None
BUILD_ROOT_PKG_APP = None
LOG = None
LOG_LEVEL = logging.DEBUG
BUILD_TIME = time.strftime('%Y%m%d', time.localtime(time.time()))


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


def iterfindfiles(path, fnexp):
    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files, fnexp):
            yield os.path.join(root, filename)


def replaceUserString(path, fnexp, old_s, new_s):
    for sub_file in iterfindfiles(path, fnexp):
        try:
            with open(sub_file, 'r') as sub_read_obj:
                read_string = sub_read_obj.read()
        except IOError as err:
            LOG.error("Read %s Error : " % sub_file + str(err))
            continue
        if read_string.find(old_s) >= 0:
            try:
                with open(sub_file, 'w') as sub_write_obj:
                    sub_write_obj.write(re.sub(old_s, new_s, read_string))
            except IOError as err:
                LOG.error("Modify %s Error : " % sub_file + str(err))
                continue


def pidExists(pid):
    if pid < 0:
        return False
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True


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


def safelyGetValue(origin_json=None, key=None):
    if origin_json and key and key in origin_json:
        return origin_json[key]
    return None


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


def zipDir(dir_path, zip_file):
    try:
        if os.path.exists(zip_file):
            if not doRemove([zip_file]):
                return False
        if not os.path.exists(os.path.dirname(zip_file)):
            os.makedirs(os.path.dirname(zip_file))
        z_file = zipfile.ZipFile(zip_file, "w")
        orig_dir = os.getcwd()
        os.chdir(dir_path)
        for root, dirs, files in os.walk("."):
            for i_file in files:
                LOG.info("zip %s" % os.path.join(root, i_file))
                z_file.write(os.path.join(root, i_file))
        z_file.close()
        os.chdir(orig_dir)
    except Exception as e:
        LOG.error("Fail to pack %s to %s: %s" % (dir_path, zip_file, e))
        return False
    LOG.info("Done to zip %s to %s" % (dir_path, zip_file))
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


def updateCopylistPrefix(src_default, dest_default, src_sub, dest_sub):
    src_new = ""
    dest_new = ""
    PACK_TOOL_TAG = "PACK-TOOL-ROOT"

    if src_sub[0:len(PACK_TOOL_TAG)] == PACK_TOOL_TAG:
        src_new = src_sub.replace(PACK_TOOL_TAG, BUILD_PARAMETERS.pkgpacktools)
    else:
        src_new = os.path.join(src_default, src_sub)

    if dest_sub[0:len(PACK_TOOL_TAG)] == PACK_TOOL_TAG:
        dest_new = dest_sub.replace(PACK_TOOL_TAG, BUILD_ROOT)
    else:
        dest_new = os.path.join(dest_default, dest_sub)

    return (src_new, dest_new)


def buildSRC(src=None, dest=None, build_json=None):
    if not os.path.exists(src):
        LOG.info("+Src dir does not exist, skip build src process ...")
        return True

    if not doCopy(src, dest):
        return False
    if "blacklist" in build_json:
        if build_json["blacklist"].count("") > 0:
            build_json["blacklist"].remove("")
        black_file_list = []
        for i_black in build_json["blacklist"]:
            black_file_list = black_file_list + \
                glob.glob(os.path.join(dest, i_black))

        black_file_list = list(set(black_file_list))
        if not doRemove(black_file_list):
            return False
    if "copylist" in build_json:
        for i_s_key in build_json["copylist"].keys():
            if i_s_key and build_json["copylist"][i_s_key]:
                (src_updated, dest_updated) = updateCopylistPrefix(
                    src, dest, i_s_key, build_json["copylist"][i_s_key])
                if not doCopy(src_updated, dest_updated):
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
    global BUILD_ROOT_SRC
    global BUILD_ROOT_SRC_PKG
    global BUILD_ROOT_SRC_PKG_APP
    global BUILD_ROOT_SRC_SUB_APP
    global BUILD_ROOT_PKG
    global BUILD_ROOT_PKG_APP

    while True:
        BUILD_ROOT = os.path.join("/tmp", getRandomStr())
        if os.path.exists(BUILD_ROOT):
            continue
        else:
            break

    BUILD_ROOT_SRC = os.path.join(BUILD_ROOT, PKG_NAME)
    BUILD_ROOT_SRC_PKG = os.path.join(BUILD_ROOT, "pkg")
    BUILD_ROOT_SRC_PKG_APP = os.path.join(BUILD_ROOT, "pkg-app")
    BUILD_ROOT_SRC_SUB_APP = os.path.join(BUILD_ROOT, "sub-app")
    BUILD_ROOT_PKG = os.path.join(BUILD_ROOT, "pkg", "opt", PKG_NAME)
    BUILD_ROOT_PKG_APP = os.path.join(BUILD_ROOT, "pkg-app", "opt", PKG_NAME)

    if not doCopy(BUILD_PARAMETERS.srcdir, BUILD_ROOT_SRC):
        return False
    else:
        replaceUserString(
            BUILD_ROOT_SRC,
            '*',
            'TESTER-HOME-DIR',
            "/home/%s" %
            BUILD_PARAMETERS.user)

    if not doRemove(
            glob.glob(os.path.join(BUILD_ROOT_SRC, "%s*.zip" % PKG_NAME))):
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


def doCMDWithOutput(cmd, time_out=DEFAULT_CMD_TIMEOUT):
    LOG.info("Doing CMD: [ %s ]" % cmd)
    pre_time = time.time()
    output = []
    cmd_return_code = 1
    cmd_proc = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

    while True:
        output_line = cmd_proc.stdout.readline().strip("\r\n")
        cmd_return_code = cmd_proc.poll()
        elapsed_time = time.time() - pre_time
        if cmd_return_code is None:
            if elapsed_time >= time_out:
                killProcesses(ppid=cmd_proc.pid)
                LOG.error("Timeout to exe CMD")
                return False
        elif output_line == '' and cmd_return_code is not None:
            break

        sys.stdout.write("%s\n" % output_line)
        sys.stdout.flush()
        output.append(output_line)
    if cmd_return_code != 0:
        LOG.error("Fail to exe CMD")

    return (cmd_return_code, output)


def packXPK(build_json=None, app_src=None, app_dest=None, app_name=None):
    pack_tool = os.path.join(BUILD_ROOT, "make_xpk.py")
    if not os.path.exists(pack_tool):
        if not doCopy(
                os.path.join(BUILD_PARAMETERS.pkgpacktools, "make_xpk.py"),
                pack_tool):
            return False
    orig_dir = os.getcwd()
    os.chdir(BUILD_ROOT)
    if os.path.exists("key.file"):
        if not doRemove(["key.file"]):
            os.chdir(orig_dir)
            return False

    key_file = safelyGetValue(build_json, "key-file")
    if key_file == "key.file":
        LOG.error(
            "\"key.file\" is reserved name for default key file, "
            "pls change the key file name ...")
        os.chdir(orig_dir)
        return False
    if key_file:
        pack_cmd = "python make_xpk.py %s %s -o %s" % (
            app_src, key_file, os.path.join(app_dest, "%s.xpk" % app_name))
    else:
        pack_cmd = "python make_xpk.py %s key.file -o %s" % (
            app_src, os.path.join(app_dest, "%s.xpk" % app_name))
    if not doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    os.chdir(orig_dir)
    return True


def packWGT(build_json=None, app_src=None, app_dest=None, app_name=None):
    if not zipDir(app_src, os.path.join(app_dest, "%s.wgt" % app_name)):
        return False

    if BUILD_PARAMETERS.signature == True:
        if safelyGetValue(build_json, "sign-flag") == "true":
            if not os.path.exists(os.path.join(BUILD_ROOT, "signing")):
                if not doCopy(
                        os.path.join(BUILD_PARAMETERS.pkgpacktools, "signing"),
                        os.path.join(BUILD_ROOT, "signing")):
                    return False
            signing_cmd = "%s --dist platform %s" % (
                os.path.join(BUILD_ROOT, "signing", "sign-widget.sh"),
                os.path.join(app_dest, "%s.wgt" % app_name))
            if not doCMD(signing_cmd, DEFAULT_CMD_TIMEOUT):
                return False

    return True


def packAPK(build_json=None, app_src=None, app_dest=None, app_name=None):
    app_name = app_name.replace("-", "_")

    if not os.path.exists(os.path.join(BUILD_ROOT, "crosswalk")):
        if not doCopy(
                os.path.join(BUILD_PARAMETERS.pkgpacktools, "crosswalk"),
                os.path.join(BUILD_ROOT, "crosswalk")):
            return False

    files = glob.glob(os.path.join(BUILD_ROOT, "crosswalk", "*.apk"))
    if files:
        if not doRemove(files):
            return False

    ext_opt = ""
    cmd_opt = ""
    url_opt = ""
    mode_opt = ""
    arch_opt = ""
    icon_opt = ""
    version_opt = ""
    pkg_opt = ""
    version_code_opt = ""
    fullscreen_opt = ""

    common_opts = safelyGetValue(build_json, "apk-common-opts")
    if common_opts is None:
        common_opts = ""

    tmp_opt = safelyGetValue(build_json, "apk-ext-opt")
    if tmp_opt:
        ext_opt = "--extensions='%s'" % os.path.join(BUILD_ROOT_SRC, tmp_opt)

    tmp_opt = safelyGetValue(build_json, "apk-version-opt")
    if tmp_opt:
        version_opt = "--app-version='%s'" % ''.join([tmp_opt, BUILD_TIME])
        version_code_opt = "--app-versionCode='%s'" % ''.join(
            ['6', BUILD_TIME])

    tmp_opt = safelyGetValue(build_json, "apk-fullscreen-opt")
    if tmp_opt:
        ext_opt = "--%s" % tmp_opt

    tmp_opt = safelyGetValue(build_json, "apk-pkg-opt")
    if tmp_opt:
        pkg_opt = "--package='org.xwalk.%s'" % tmp_opt

    tmp_opt = safelyGetValue(build_json, "apk-cmd-opt")
    if tmp_opt:
        cmd_opt = "--xwalk-command-line='%s'" % tmp_opt

    tmp_opt = safelyGetValue(build_json, "apk-url-opt")
    if tmp_opt:
        url_opt = "--app-url='%s'" % tmp_opt

    tmp_opt = safelyGetValue(build_json, "apk-mode-opt")
    if tmp_opt:
        if tmp_opt in PKG_MODES:
            mode_opt = "--mode=%s" % tmp_opt
        else:
            LOG.error("Got wrong app mode: %s" % tmp_opt)
            return False
    else:
        mode_opt = "--mode=%s" % BUILD_PARAMETERS.pkgmode

    tmp_opt = safelyGetValue(build_json, "apk-arch-opt")
    if tmp_opt:
        if tmp_opt in PKG_ARCHS:
            arch_opt = "--arch=%s" % tmp_opt
        else:
            LOG.error("Got wrong app arch: %s" % tmp_opt)
            return False
    else:
        arch_opt = "--arch=%s" % BUILD_PARAMETERS.pkgarch

    tmp_opt = safelyGetValue(build_json, "apk-icon-opt")
    if tmp_opt:
        icon_opt = "--icon=%s" % tmp_opt
    elif tmp_opt == "":
        icon_opt = ""
    else:
        icon_opt = "--icon=%s/icon.png" % app_src

    if safelyGetValue(build_json, "apk-type") == "MANIFEST":
        pack_cmd = "python make_apk.py --package=org.xwalk.%s " \
            "--manifest=%s/manifest.json  %s %s %s %s %s %s %s %s %s" % (
                app_name, app_src, mode_opt, arch_opt,
                ext_opt, cmd_opt, common_opts, version_opt, pkg_opt, version_code_opt, fullscreen_opt)
    elif safelyGetValue(build_json, "apk-type") == "HOSTEDAPP":
        if not url_opt:
            LOG.error(
                "Fail to find the key \"apk-url-opt\" for hosted APP packing")
            return False
        pack_cmd = "python make_apk.py --package=org.xwalk.%s --name=%s %s " \
                   "%s %s %s %s %s %s %s %s %s" % (
                       app_name, app_name, mode_opt, arch_opt, ext_opt,
                       cmd_opt, url_opt, common_opts, version_opt, pkg_opt, version_code_opt, fullscreen_opt)
    else:
        pack_cmd = "python make_apk.py --package=org.xwalk.%s --name=%s " \
                   "--app-root=%s --app-local-path=index.html %s %s " \
                   "%s %s %s %s %s %s %s %s" % (
                       app_name, app_name, app_src, icon_opt, mode_opt,
                       arch_opt, ext_opt, cmd_opt, common_opts, version_opt, pkg_opt, version_code_opt, fullscreen_opt)

    orig_dir = os.getcwd()
    os.chdir(os.path.join(BUILD_ROOT, "crosswalk"))
    if not doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    files = glob.glob(os.path.join(BUILD_ROOT, "crosswalk", "*.apk"))
    if files:
        if not doCopy(files[0], os.path.join(app_dest, "%s.apk" % app_name)):
            os.chdir(orig_dir)
            return False
    else:
        LOG.error("Fail to find the apk file")
        os.chdir(orig_dir)
        return False

    os.chdir(orig_dir)
    return True


def packCordova_cli(
        build_json=None, app_src=None, app_dest=None, app_name=None):
    app_name = app_name.replace("-", "_")
    project_root = os.path.join(BUILD_ROOT, app_name)

    output = commands.getoutput("cordova -v")
    if output != "5.0.0":
        LOG.error(
            "Cordova 4.0 build requires Cordova-CLI 5.0.0, install with command: '$ sudo npm install cordova@5.0.0 -g'")
        return False

    plugin_tool = os.path.join(BUILD_ROOT, "cordova_plugins")
    if not doCopy(
            os.path.join(BUILD_PARAMETERS.pkgpacktools, "cordova_plugins"),
            plugin_tool):
        return False

    orig_dir = os.getcwd()
    os.chdir(BUILD_ROOT)
    pack_cmd = "cordova create %s org.xwalk.%s %s" % (
        app_name, app_name, app_name)
    if not doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    # Set activity name as app_name
    replaceUserString(
        project_root,
        'config.xml',
        '<widget',
        '<widget android-activityName="%s"' %
        app_name)
    # Workaround for XWALK-3679
    replaceUserString(
        project_root,
        'config.xml',
        '</widget>',
        '    <allow-navigation href="*" />\n</widget>')

    if not doRemove([os.path.join(project_root, "www")]):
        return False
    if not doCopy(app_src, os.path.join(project_root, "www")):
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

    if not doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    outputs_dir = os.path.join(
        project_root,
        "platforms",
        "android",
        "build",
        "outputs",
        "apk")

    if BUILD_PARAMETERS.pkgarch == "x86":
        cordova_tmp_path = os.path.join(
            outputs_dir,
            "%s-x86-debug.apk" %
            app_name)
        cordova_tmp_path_spare = os.path.join(
            outputs_dir,
            "android-x86-debug.apk")
    else:
        cordova_tmp_path = os.path.join(
            outputs_dir,
            "%s-armv7-debug.apk" %
            app_name)
        cordova_tmp_path_spare = os.path.join(
            outputs_dir,
            "android-armv7-debug.apk")

    if not os.path.exists(cordova_tmp_path):
        if not doCopy(
                cordova_tmp_path_spare, os.path.join(app_dest, "%s.apk" % app_name)):
            os.chdir(orig_dir)
            return False
    else:
        if not doCopy(
                cordova_tmp_path, os.path.join(app_dest, "%s.apk" % app_name)):
            os.chdir(orig_dir)
            return False
    os.chdir(orig_dir)
    return True


def packCordova(build_json=None, app_src=None, app_dest=None, app_name=None):
    pack_tool = os.path.join(BUILD_ROOT, "cordova")
    app_name = app_name.replace("-", "_")
    if not os.path.exists(pack_tool):
        if not doCopy(
                os.path.join(BUILD_PARAMETERS.pkgpacktools, "cordova"),
                pack_tool):
            return False

    plugin_tool = os.path.join(BUILD_ROOT, "cordova_plugins")
    if not doCopy(
            os.path.join(BUILD_PARAMETERS.pkgpacktools, "cordova_plugins"),
            plugin_tool):
        return False

    orig_dir = os.getcwd()
    os.chdir(pack_tool)

    if BUILD_PARAMETERS.pkgmode == "shared":
        pack_cmd = "bin/create %s org.xwalk.%s %s --xwalk-shared-library" % (
            app_name, app_name, app_name)
    else:
        pack_cmd = "bin/create %s org.xwalk.%s %s --shared" % (
            app_name, app_name, app_name)
    if not doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    os.chdir(os.path.join(pack_tool, app_name))
    plugin_dirs = os.listdir(plugin_tool)
    for i_dir in plugin_dirs:
        i_plugin_dir = os.path.join(plugin_tool, i_dir)
        plugin_install_cmd = "plugman install --platform android --project " \
                             "./ --plugin %s" % i_plugin_dir
        if not doCMD(plugin_install_cmd, DEFAULT_CMD_TIMEOUT):
            os.chdir(orig_dir)
            return False
    os.chdir(pack_tool)

    if not doCopy(app_src, os.path.join(pack_tool, app_name, "assets", "www")):
        os.chdir(orig_dir)
        return False
    os.chdir(os.path.join(BUILD_ROOT, "cordova", app_name))
    ANDROID_HOME = "echo $(dirname $(dirname $(which android)))"
    os.environ['ANDROID_HOME'] = commands.getoutput(ANDROID_HOME)
    pack_cmd = "./cordova/build"

    if BUILD_PARAMETERS.subversion == '4.0':
        if BUILD_PARAMETERS.pkgarch == "x86":
            cordova_tmp_path = os.path.join(
                BUILD_ROOT,
                "cordova",
                app_name,
                "build",
                "outputs",
                "apk",
                "%s-x86-debug.apk" %
                app_name)
        else:
            cordova_tmp_path = os.path.join(
                BUILD_ROOT,
                "cordova",
                app_name,
                "build",
                "outputs",
                "apk",
                "%s-armv7-debug.apk" %
                app_name)
    else:
        cordova_tmp_path = os.path.join(
            BUILD_ROOT,
            "cordova",
            app_name,
            "bin",
            "%s-debug.apk" %
            app_name)
    if not doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
        pack_cmd = "ant debug"
        if not doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
            os.chdir(orig_dir)
            return False

    if not doCopy(cordova_tmp_path,
                  os.path.join(app_dest, "%s.apk" % app_name)):
        os.chdir(orig_dir)
        return False
    os.chdir(orig_dir)
    return True


def packEmbeddingAPI_ant(
        build_json=None, app_src=None, app_dest=None, app_name=None, app_version=None):
    app_name = app_name.replace("-", "_")

    library_dir_name = safelyGetValue(build_json, "embeddingapi-library-name")
    if not library_dir_name:
        LOG.error("Fail to get embeddingapi-library-name ...")
        return False

    new_library_dir_name = "core_library"
    pack_tool = os.path.join(app_src, "..", new_library_dir_name)

    if os.path.exists(pack_tool):
        if not doRemove([pack_tool]):
            return False

    if not doCopy(
            os.path.join(BUILD_PARAMETERS.pkgpacktools, library_dir_name),
            pack_tool):
        return False

    if os.path.exists(os.path.join(pack_tool, "bin", "res", "crunch")):
        if not doRemove([os.path.join(pack_tool, "bin", "res", "crunch")]):
            return False

    orig_dir = os.getcwd()
    android_project_path = os.path.join(app_src, "android-project")
    try:
        os.makedirs(android_project_path)
    except Exception as e:
        LOG.error("Fail to create tmp project dir: %s" % e)
        return False

    (return_code, output) = doCMDWithOutput("android list target")
    api_level = ""
    for line in output:
        if "API level:" in line:
            api_level = line.split(":")[1].strip()
    if not api_level:
        LOG.error("Fail to get Android API Level")
        os.chdir(orig_dir)
        return False

    android_project_cmd = "android create project --name %s --target " \
                          "android-%s --path %s --package com.%s " \
                          "--activity MainActivity" % (
                              app_name, api_level, android_project_path, app_name)
    if not doCMD(android_project_cmd):
        os.chdir(orig_dir)
        return False

    try:
        update_file = open(
            os.path.join(android_project_path, "project.properties"), "a+")
        update_file.writelines(
            "{0}\n".format(
                "android.library.reference.1=../%s" %
                new_library_dir_name))
        update_file.close()
    except Exception as e:
        LOG.error(
            "Fail to update %s: %s" %
            (os.path.join(
                android_project_path,
                "project.properties"),
                e))
        os.chdir(orig_dir)
        return False

    if not doCopy(os.path.join(android_project_path, "build.xml"),
                  os.path.join(app_src, "build.xml")):
        os.chdir(orig_dir)
        return False

    if not doCopy(
            os.path.join(android_project_path, "project.properties"),
            os.path.join(app_src, "project.properties")):
        os.chdir(orig_dir)
        return False

    if not doCopy(
            os.path.join(android_project_path, "local.properties"),
            os.path.join(app_src, "local.properties")):
        os.chdir(orig_dir)
        return False

    if not doCopy(
            os.path.join(android_project_path, "local.properties"),
            os.path.join(pack_tool, "local.properties")):
        os.chdir(orig_dir)
        return False

    os.chdir(app_src)
    if not doCMD("ant debug"):
        os.chdir(orig_dir)
        return False

    if not doCopy(
            os.path.join(app_src, "bin", "%s-debug.apk" % app_name),
            os.path.join(app_dest, "%s.apk" % app_name)):
        os.chdir(orig_dir)
        return False
    os.chdir(orig_dir)
    return True


def packEmbeddingAPI_gradle(
        build_json=None, app_src=None, app_dest=None, app_name=None, app_version=None):
    app_name = app_name.replace("-", "_")
    orig_dir = os.getcwd()
    LOG.info("app_src: %s" % app_src)
    LOG.info("app_dest: %s" % app_dest)
    os.chdir(app_src)
    if not doCMD("gradle build"):
        os.chdir("..")
        return False
    if BUILD_PARAMETERS.pkgarch and BUILD_PARAMETERS.pkgarch == "arm":
        if not doCopy(
                os.path.join(
                    app_src,
                    "build",
                    "outputs",
                    "apk",
                    "%s-armv7-debug.apk" %
                    app_name),
                os.path.join(app_dest, "%s.apk" % app_name)):
            return False
    else:
        if not doCopy(
                os.path.join(
                    app_src,
                    "build",
                    "outputs",
                    "apk",
                    "%s-x86-debug.apk" %
                    app_name),
                os.path.join(app_dest, "%s.apk" % app_name)):
            return False
    os.chdir(orig_dir)
    return True


def packEmbeddingAPI_maven(
        build_json=None, app_src=None, app_dest=None, app_name=None, app_version=None):
    app_name = app_name.replace("-", "_")
    orig_dir = os.getcwd()
    LOG.info("app_src: %s" % app_src)
    LOG.info("app_dest: %s" % app_dest)
    os.chdir(app_src)
    replaceUserString(
        app_src,
        'AndroidManifest.xml',
        'android:versionCode=\"1\"',
        'android:versionCode=\"${app.version.code}\"')
    replaceUserString(
        app_src,
        'AndroidManifest.xml',
        'android:versionName=\"1.0\"',
        'android:versionName=\"${app.version.name}\"')
    if not doCopy(
            os.path.join(app_src, "AndroidManifest.xml"), os.path.join(app_src, "src", "main", "AndroidManifest.xml")):
        return False
    if not doCopy(
            os.path.join(app_src, "res"), os.path.join(app_src, "src", "main", "res")):
        return False
    if not doCopy(
            os.path.join(app_src, "assets"), os.path.join(app_src, "src", "main", "assets")):
        return False
    if not doCopy(
            os.path.join(app_src, "src", "org"), os.path.join(app_src, "src", "main", "java", "org")):
        return False
    if BUILD_PARAMETERS.pkgarch and BUILD_PARAMETERS.pkgarch == "arm":
        if not doCMD("mvn clean install -Px86"):
            return False
        if not doCopy(
                os.path.join(
                    app_src,
                    "target",
                    "%s-armv7-debug.apk" %
                    app_name),
                os.path.join(app_dest, "%s.apk" % app_name)):
            return False
    else:
        if not doCMD("mvn clean install -Parm"):
            return False
        if not doCopy(
                os.path.join(app_src, "target", "%s-x86-debug.apk" % app_name),
                os.path.join(app_dest, "%s.apk" % app_name)):
            return False
    os.chdir(orig_dir)
    return True


def packAPP(build_json=None, app_src=None, app_dest=None, app_name=None):
    LOG.info("Packing %s(%s)" % (app_name, app_src))
    if not os.path.exists(app_dest):
        try:
            os.makedirs(app_dest)
        except Exception as e:
            LOG.error("Fail to init package install dest dir: %s" % e)
            return False

    app_tpye = safelyGetValue(build_json, 'app-type')

    if checkContains(BUILD_PARAMETERS.pkgtype, "XPK"):
        if not packXPK(build_json, app_src, app_dest, app_name):
            return False
    elif checkContains(BUILD_PARAMETERS.pkgtype, "WGT"):
        if not packWGT(build_json, app_src, app_dest, app_name):
            return False
    elif checkContains(BUILD_PARAMETERS.pkgtype, "APK") and app_tpye != "EMBEDDINGAPI":
        if not packAPK(build_json, app_src, app_dest, app_name):
            return False
    elif checkContains(BUILD_PARAMETERS.pkgtype, "CORDOVA"):
        if BUILD_PARAMETERS.subversion == '4.0':
            if not packCordova_cli(build_json, app_src, app_dest, app_name):
                return False
        else:
            if not packCordova(build_json, app_src, app_dest, app_name):
                return False
    elif checkContains(BUILD_PARAMETERS.pkgtype, "EMBEDDINGAPI") or app_tpye == "EMBEDDINGAPI":
        app_version = None
        if "_" in app_name:
            index_flag = app_name.index("_")
            app_version = app_name[index_flag + 1:]
        if app_version:
            replaceUserString(
                app_src,
                'AndroidManifest.xml',
                'org.xwalk.embedding.test',
                "org.xwalk.embedding.test." +
                app_version)
            replaceUserString(
                app_src,
                'AndroidManifest.xml',
                'EmbeddingApiTestUnit',
                "EmbeddingApiTestUnit" +
                app_version)
            main_dest = os.path.join(app_src, "src/org/xwalk/embedding")
            replaceUserString(
                main_dest,
                'MainActivity.java',
                'org.xwalk.embedding.test',
                "org.xwalk.embedding.test." +
                app_version)
        if BUILD_PARAMETERS.packtype and checkContains(
                BUILD_PARAMETERS.packtype, "GRADLE"):
            if not packEmbeddingAPI_gradle(
                    build_json, app_src, app_dest, app_name, app_version):
                return False
        elif BUILD_PARAMETERS.packtype and checkContains(BUILD_PARAMETERS.packtype, "MAVEN"):
            if not packEmbeddingAPI_maven(
                    build_json, app_src, app_dest, app_name, app_version):
                return False
        else:
            if not packEmbeddingAPI_ant(
                    build_json, app_src, app_dest, app_name, app_version):
                return False
    else:
        LOG.error("Got wrong pkg type: %s" % BUILD_PARAMETERS.pkgtype)
        return False

    LOG.info("Success to pack APP: %s" % app_name)
    return True


def createIndexFile(index_file_path=None, hosted_app=None):
    try:
        if hosted_app:
            index_url = "http://127.0.0.1/opt/%s/webrunner/index.html?" \
                "testsuite=../tests.xml&testprefix=../../.." % PKG_NAME
        else:
            index_url = "opt/%s/webrunner/index.html?testsuite=../tests.xml" \
                        "&testprefix=../../.." % PKG_NAME
        html_content = "<!doctype html><head><meta http-equiv='Refresh' " \
                       "content='1; url=%s'></head>" % index_url
        index_file = open(index_file_path, "w")
        index_file.write(html_content)
        index_file.close()
    except Exception as e:
        LOG.error("Fail to create index.html for top-app: %s" % e)
        return False
    LOG.info("Success to create index file %s" % index_file_path)
    return True


def buildSubAPP(app_dir=None, build_json=None, app_dest_default=None):
    app_dir_inside = safelyGetValue(build_json, "app-dir")
    if app_dir_inside:
        app_dir = app_dir_inside
    LOG.info("+Building sub APP(s) from %s ..." % app_dir)
    app_dir = os.path.join(BUILD_ROOT_SRC, app_dir)
    app_name = safelyGetValue(build_json, "app-name")
    if not app_name:
        app_name = os.path.basename(app_dir)

    app_src = os.path.join(BUILD_ROOT_SRC_SUB_APP, app_name)
    if buildSRC(app_dir, app_src, build_json):
        app_dest = safelyGetValue(build_json, "install-path")
        if app_dest:
            app_dest = os.path.join(app_dest_default, app_dest)
        else:
            app_dest = app_dest_default

        if safelyGetValue(build_json, "all-apps") == "true":
            app_dirs = os.listdir(app_src)
            apps_num = 0
            for i_app_dir in app_dirs:
                if os.path.isdir(os.path.join(app_src, i_app_dir)):
                    i_app_name = os.path.basename(i_app_dir)
                    if not packAPP(
                            build_json, os.path.join(app_src, i_app_name),
                            app_dest, i_app_name):
                        return False
                    else:
                        apps_num = apps_num + 1
            if apps_num > 0:
                LOG.info("Totally packed %d apps in %s" % (apps_num, app_dir))
                return True
        else:
            return packAPP(build_json, app_src, app_dest, app_name)
    return False


def buildPKGAPP(build_json=None):
    LOG.info("+Building package APP ...")
    if not doCopy(os.path.join(BUILD_ROOT_SRC, "icon.png"),
                  os.path.join(BUILD_ROOT_SRC_PKG_APP, "icon.png")):
        return False

    if checkContains(BUILD_PARAMETERS.pkgtype, "XPK"):
        if not doCopy(
                os.path.join(BUILD_ROOT_SRC, "manifest.json"),
                os.path.join(BUILD_ROOT_SRC_PKG_APP, "manifest.json")):
            return False
    elif checkContains(BUILD_PARAMETERS.pkgtype, "WGT"):
        if not doCopy(os.path.join(BUILD_ROOT_SRC, "config.xml"),
                      os.path.join(BUILD_ROOT_SRC_PKG_APP, "config.xml")):
            return False

    hosted_app = False
    if safelyGetValue(build_json, "hosted-app") == "true":
        hosted_app = True
    if not createIndexFile(
            os.path.join(BUILD_ROOT_SRC_PKG_APP, "index.html"), hosted_app):
        return False

    if not hosted_app:
        if "blacklist" not in build_json:
            build_json.update({"blacklist": []})
        build_json["blacklist"].extend(PKG_BLACK_LIST)
        if not buildSRC(BUILD_ROOT_SRC, BUILD_ROOT_PKG_APP, build_json):
            return False

        if "subapp-list" in build_json:
            for i_sub_app in build_json["subapp-list"].keys():
                if not buildSubAPP(
                        i_sub_app, build_json["subapp-list"][i_sub_app],
                        BUILD_ROOT_PKG_APP):
                    return False

    if not packAPP(
            build_json, BUILD_ROOT_SRC_PKG_APP, BUILD_ROOT_PKG, PKG_NAME):
        return False

    return True


def buildPKG(build_json=None):
    if "blacklist" not in build_json:
        build_json.update({"blacklist": []})
    build_json["blacklist"].extend(PKG_BLACK_LIST)
    if not buildSRC(BUILD_ROOT_SRC, BUILD_ROOT_PKG, build_json):
        return False

    if "subapp-list" in build_json:
        for i_sub_app in build_json["subapp-list"].keys():
            if not buildSubAPP(
                    i_sub_app, build_json["subapp-list"][i_sub_app],
                    BUILD_ROOT_PKG):
                return False

    if "pkg-app" in build_json:
        if not buildPKGAPP(build_json["pkg-app"]):
            return False

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
            "-c",
            "--cfg",
            dest="pkgcfg",
            help="specify the path of config json file")
        opts_parser.add_option(
            "-t",
            "--type",
            dest="pkgtype",
            help="specify the pkg type, e.g. apk, xpk, wgt ...")
        opts_parser.add_option(
            "-m",
            "--mode",
            dest="pkgmode",
            help="specify the apk mode, not for embeddingapi, cordova version 4.0, e.g. shared, embedded")
        opts_parser.add_option(
            "-a",
            "--arch",
            dest="pkgarch",
            help="specify the apk arch, not for embeddingapi, cordova version 3.6, e.g. x86, arm")
        opts_parser.add_option(
            "-d",
            "--dest",
            dest="destdir",
            help="specify the installation folder for packed package")
        opts_parser.add_option(
            "-s",
            "--src",
            dest="srcdir",
            help="specify the path of pkg resource for packing")
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
            "--sign",
            dest="signature",
            action="store_true",
            help="signature operation will be done when packing wgt")
        opts_parser.add_option(
            "-v",
            "--version",
            dest="bversion",
            action="store_true",
            help="show this tool's version")
        opts_parser.add_option(
            "-u",
            "--user",
            dest="user",
            help="specify the user in inst.py")
        opts_parser.add_option(
            "--sub-version",
            dest="subversion",
            help="specify the embeddingapi, cordova sub version, e.g. v1, v2, v3 ...")
        opts_parser.add_option(
            "--pkg-version",
            dest="pkgversion",
            help="specify the pkg version, e.g. 0.0.0.1")
        opts_parser.add_option(
            "--pack-type",
            dest="packtype",
            help="specify the pack type, e.g. gradle, maven")

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

    if not BUILD_PARAMETERS.srcdir:
        BUILD_PARAMETERS.srcdir = os.getcwd()
    BUILD_PARAMETERS.srcdir = os.path.expanduser(BUILD_PARAMETERS.srcdir)

    if not BUILD_PARAMETERS.user:
        BUILD_PARAMETERS.user = "app"

    if not os.path.exists(
            os.path.join(BUILD_PARAMETERS.srcdir, "..", "..", VERSION_FILE)):
        if not os.path.exists(
                os.path.join(BUILD_PARAMETERS.srcdir, "..", VERSION_FILE)):
            if not os.path.exists(
                    os.path.join(BUILD_PARAMETERS.srcdir, VERSION_FILE)):
                LOG.info(
                    "Not found pkg version file, try to use option --pkg-version")
                pkg_version_file_path = None
            else:
                pkg_version_file_path = os.path.join(
                    BUILD_PARAMETERS.srcdir, VERSION_FILE)
        else:
            pkg_version_file_path = os.path.join(
                BUILD_PARAMETERS.srcdir, "..", VERSION_FILE)
    else:
        pkg_version_file_path = os.path.join(
            BUILD_PARAMETERS.srcdir, "..", "..", VERSION_FILE)

    try:
        pkg_main_version = 0
        pkg_release_version = 1
        if BUILD_PARAMETERS.pkgversion:
            LOG.info("Using %s as pkg version " % BUILD_PARAMETERS.pkgversion)
            pkg_main_version = BUILD_PARAMETERS.pkgversion
        else:
            if pkg_version_file_path is not None:
                LOG.info("Using pkg version file: %s" % pkg_version_file_path)
                with open(pkg_version_file_path, "rt") as pkg_version_file:
                    pkg_version_raw = pkg_version_file.read()
                    pkg_version_file.close()
                    pkg_version_json = json.loads(pkg_version_raw)
                    pkg_main_version = pkg_version_json["main-version"]
                    pkg_release_version = pkg_version_json["release-version"]
    except Exception as e:
        LOG.error("Fail to read pkg version file: %s, exit ..." % e)
        sys.exit(1)

    if not BUILD_PARAMETERS.pkgtype:
        LOG.error("No pkg type provided, exit ...")
        sys.exit(1)
    elif not BUILD_PARAMETERS.pkgtype in PKG_TYPES:
        LOG.error("Wrong pkg type, only support: %s, exit ..." %
                  PKG_TYPES)
        sys.exit(1)

    if BUILD_PARAMETERS.pkgtype == "apk" or \
       BUILD_PARAMETERS.pkgtype == "apk-aio":
        if not BUILD_PARAMETERS.pkgmode:
            LOG.error("No pkg mode option provided, exit ...")
            sys.exit(1)
        elif not BUILD_PARAMETERS.pkgmode in PKG_MODES:
            LOG.error(
                "Wrong pkg mode option provided, only support:%s, exit ..." %
                PKG_MODES)
            sys.exit(1)

        if not BUILD_PARAMETERS.pkgarch:
            LOG.error("No pkg arch option provided, exit ...")
            sys.exit(1)
        elif not BUILD_PARAMETERS.pkgarch in PKG_ARCHS:
            LOG.error(
                "Wrong pkg arch option provided, only support:%s, exit ..." %
                PKG_ARCHS)
            sys.exit(1)

    if BUILD_PARAMETERS.pkgtype == "apk-aio" or \
       BUILD_PARAMETERS.pkgtype == "cordova-aio":
        if not BUILD_PARAMETERS.destdir or not os.path.exists(
                BUILD_PARAMETERS.destdir):
            LOG.error("No all-in-one installation dest dir found, exit ...")
            sys.exit(1)

    elif not BUILD_PARAMETERS.destdir:
        BUILD_PARAMETERS.destdir = BUILD_PARAMETERS.srcdir
    BUILD_PARAMETERS.destdir = os.path.expanduser(BUILD_PARAMETERS.destdir)

    if not BUILD_PARAMETERS.pkgpacktools:
        BUILD_PARAMETERS.pkgpacktools = os.path.join(
            BUILD_PARAMETERS.srcdir, "..", "..", "tools")
    BUILD_PARAMETERS.pkgpacktools = os.path.expanduser(
        BUILD_PARAMETERS.pkgpacktools)

    config_json = None
    if BUILD_PARAMETERS.pkgcfg:
        config_json_file_path = BUILD_PARAMETERS.pkgcfg
    else:
        config_json_file_path = os.path.join(
            BUILD_PARAMETERS.srcdir, "suite.json")
    try:
        LOG.info("Using config json file: %s" % config_json_file_path)
        with open(config_json_file_path, "rt") as config_json_file:
            config_raw = config_json_file.read()
            config_json_file.close()
            config_json = json.loads(config_raw)
    except Exception as e:
        LOG.error("Fail to read config json file: %s, exit ..." % e)
        sys.exit(1)

    global PKG_NAME
    PKG_NAME = safelyGetValue(config_json, "pkg-name")
    if not PKG_NAME:
        PKG_NAME = os.path.basename(BUILD_PARAMETERS.srcdir)
        LOG.warning(
            "Fail to read pkg name from json, "
            "using src dir name as pkg name ...")

    LOG.info("================= %s (%s-%s) ================" %
             (PKG_NAME, pkg_main_version, pkg_release_version))

    if not safelyGetValue(config_json, "pkg-list"):
        LOG.error("Fail to read pkg-list, exit ...")
        sys.exit(1)

    pkg_json = None
    global parameters_type
    parameters_type = None
    cordova_subv_list = ['4.0', '3.6']

    if BUILD_PARAMETERS.pkgtype == "cordova" or BUILD_PARAMETERS.pkgtype == "cordova-aio":

        if BUILD_PARAMETERS.pkgarch and not BUILD_PARAMETERS.pkgarch in PKG_ARCHS:
            LOG.error("Wrong pkg-arch, only support: %s, exit ..." %
                      PKG_ARCHS)
            sys.exit(1)

        if BUILD_PARAMETERS.pkgmode and not BUILD_PARAMETERS.pkgmode in PKG_MODES:
            LOG.error("Wrong pkg-mode, only support: %s, exit ..." %
                      PKG_MODES)
            sys.exit(1)

        if BUILD_PARAMETERS.subversion:
            if not str(BUILD_PARAMETERS.subversion) in cordova_subv_list:
                LOG.error(
                    "The argument of cordova --sub-version can only be '3.6' or '4.0' , exit ...")
                sys.exit(1)
            if BUILD_PARAMETERS.subversion == '4.0' and BUILD_PARAMETERS.pkgmode:
                LOG.error("Command -m is only for cordova version 3.6")
                sys.exit(1)
            parameters_type = BUILD_PARAMETERS.pkgtype + \
                BUILD_PARAMETERS.subversion

        if (BUILD_PARAMETERS.subversion ==
                '3.6' or not BUILD_PARAMETERS.subversion) and BUILD_PARAMETERS.pkgarch:
            LOG.error("Command -a is not for cordova version 3.6")
            sys.exit(1)

    if BUILD_PARAMETERS.pkgtype == "embeddingapi":
        if BUILD_PARAMETERS.packtype and not BUILD_PARAMETERS.packtype in PACK_TYPES:
            LOG.error("embeddingapi packtype can only be gradle, maven or ant")
            sys.exit(1)
        if BUILD_PARAMETERS.subversion:
            BUILD_PARAMETERS.pkgtype = BUILD_PARAMETERS.pkgtype + \
                BUILD_PARAMETERS.subversion

    all_pkg_string = "".join(config_json["pkg-list"].keys())
    if parameters_type and parameters_type in all_pkg_string:
        for i_pkg in config_json["pkg-list"].keys():
            i_pkg_list = i_pkg.replace(" ", "").split(",")
            if parameters_type in i_pkg_list:
                pkg_json = config_json["pkg-list"][i_pkg]
                break
    elif BUILD_PARAMETERS.pkgtype in all_pkg_string:
        for i_pkg in config_json["pkg-list"].keys():
            i_pkg_list = i_pkg.replace(" ", "").split(",")
            if BUILD_PARAMETERS.pkgtype in i_pkg_list:
                pkg_json = config_json["pkg-list"][i_pkg]
                break

    if (pkg_json == config_json['pkg-list'].get('apk') or pkg_json == config_json['pkg-list'].get('apk,cordova')) and int(
            str(pkg_main_version).split('.')[-1]) != 0 and config_json['pkg-list'].get('apk-googleplayer') is not None:
        pkg_json = config_json["pkg-list"]['apk-googleplayer']

    if not pkg_json:
        LOG.error("Fail to read pkg json, exit ...")
        sys.exit(1)

    if not prepareBuildRoot():
        exitHandler(1)

    if "pkg-blacklist" in config_json:
        PKG_BLACK_LIST.extend(config_json["pkg-blacklist"])

    if not buildPKG(pkg_json):
        exitHandler(1)

    LOG.info("+Building package ...")
    if BUILD_PARAMETERS.pkgtype == "apk-aio" or \
       BUILD_PARAMETERS.pkgtype == "cordova-aio":
        pkg_file_list = os.listdir(os.path.join(BUILD_ROOT, "pkg"))
        for i_file in pkg_file_list:
            if not doCopy(
                    os.path.join(BUILD_ROOT, "pkg", i_file),
                    os.path.join(BUILD_PARAMETERS.destdir, i_file)):
                exitHandler(1)
    elif BUILD_PARAMETERS.pkgtype == "embeddingapi" and BUILD_PARAMETERS.subversion:
        pkg_file = os.path.join(
            BUILD_PARAMETERS.destdir,
            "%s-%s-%s-%s.%s.zip" %
            (PKG_NAME,
             pkg_main_version,
             pkg_release_version,
             BUILD_PARAMETERS.subversion,
             BUILD_PARAMETERS.pkgtype))

        LOG.info("pkg_file: %s" % pkg_file)
        if not zipDir(os.path.join(BUILD_ROOT, "pkg"), pkg_file):
            exitHandler(1)
    else:
        pkg_file = os.path.join(
            BUILD_PARAMETERS.destdir,
            "%s-%s-%s.%s.zip" %
            (PKG_NAME,
             pkg_main_version,
             pkg_release_version,
             BUILD_PARAMETERS.pkgtype))

        if not zipDir(os.path.join(BUILD_ROOT, "pkg"), pkg_file):
            exitHandler(1)

if __name__ == "__main__":
    main()
    exitHandler(0)
