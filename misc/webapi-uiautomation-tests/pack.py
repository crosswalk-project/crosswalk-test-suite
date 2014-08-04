#!/usr/bin/env python
#
# Copyright (c) 2014 Intel Corporation.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# * Redistributions of works must retain the original copyright notice, this list
#   of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
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
import random
import json
import logging
import zipfile
import signal
import subprocess
from optparse import OptionParser, make_option

reload(sys)
sys.setdefaultencoding('utf8')

TOOL_VERSION = "v0.01"
VERSION_FILE = "VERSION"
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPT_DIR_NAME = os.path.basename(SCRIPT_DIR)
DEFAULT_CMD_TIMEOUT = 600
PKG_NAME = None
PKG_TYPE = ["apk", "xpk", "wgt", "apk-aio", "cordova"]
PKG_MODE = ["shared", "embedded"]
PKG_ARCH = ["x86", "arm"]
PKG_BLACK_LIST = []
BUILD_PARAMETERS = None
BUILD_ROOT = None
BUILD_ROOT_SRC = None
BUILD_ROOT_PKG = None
BUILD_ROOT_PKG_APP = None
LOG = None
LOG_LEVEL = logging.DEBUG


def pidExists(pid):
    if pid < 0:
        return False
    try:
        os.kill(pid, 0)
    except OSError as e:
        return False
    else:
        return True


def IsWindows():
    return sys.platform == "cygwin" or sys.platform.startswith("win")


def KillAllProcesses(ppid=None):
    if IsWindows():
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
                except:
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
        z_file = zipfile.ZipFile(zip_file, "w")
        orig_dir = os.getcwd()
        os.chdir(dir_path)
        for root, dirs, files in os.walk("."):
            for file in files:
                LOG.info("zip %s" % os.path.join(root, file))
                z_file.write(os.path.join(root, file))
        z_file.close()
        os.chdir(orig_dir)
    except Exception, e:
        LOG.error("Fail to pack %s to %s" % (dir_path, zip_file))
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
            except Exception, e:
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
    except Exception, e:
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
        except Exception, e:
            LOG.error("Fail to remove file %s: %s" % (i_file, e))
            return False
    return True


def buildSRC(src=None, dest=None, build_json=None):
    if not doCopy(src, dest):
        return False
    if build_json.has_key("blacklist"):
        if build_json["blacklist"].count("") > 0:
            build_json["blacklist"].remove("")
        black_file_list = []
        for i_black in build_json["blacklist"]:
            black_file_list = black_file_list + \
                glob.glob(os.path.join(dest, i_black))

        black_file_list = list(set(black_file_list))
        if not doRemove(black_file_list):
            return False

    if build_json.has_key("copylist"):
        for i_s_key in build_json["copylist"].keys():
            if i_s_key != "" and build_json["copylist"][i_s_key] != "":
                if not doCopy(os.path.join(src, i_s_key), os.path.join(
                        dest, build_json["copylist"][i_s_key])):
                    return False

    return True


def exitHandler(return_code=1):
    if not BUILD_PARAMETERS.bnotclean and os.path.exists(BUILD_ROOT):
        if not doRemove([BUILD_ROOT]):
            LOG.error("Fail to clean build root: %s, exit ..." % e)
            sys.exit(1)

    if return_code == 0:
        LOG.info("================ DONE ================")
    else:
        LOG.error(
            "================ Found Something Wrong !!! ================")
    sys.exit(return_code)


def perpareBuildRoot():
    global BUILD_ROOT
    global BUILD_ROOT_SRC
    global BUILD_ROOT_PKG
    global BUILD_ROOT_PKG_APP

    if IsWindows():
        build_root_parent = "c:\web-test-tmp"
    else:
        build_root_parent = "/tmp"

    while True:
        BUILD_ROOT = os.path.join("/tmp", getRandomStr())
        if os.path.exists(BUILD_ROOT):
            continue
        else:
            break

    BUILD_ROOT_SRC = os.path.join(BUILD_ROOT, SCRIPT_DIR_NAME)
    BUILD_ROOT_PKG = os.path.join(BUILD_ROOT, "pkg", "opt", PKG_NAME)
    BUILD_ROOT_PKG_APP = os.path.join(BUILD_ROOT, "pkg-app", "opt", PKG_NAME)

    try:
        if not doCopy(SCRIPT_DIR, BUILD_ROOT_SRC):
            return False
        if not doRemove(glob.glob(os.path.join(BUILD_ROOT_SRC, "%s*.zip" % PKG_NAME))):
            return False
    except Exception, e:
        LOG.error("Fail to copy source to build root dir: %s" % e)
        return False

    return True


def doCMD(cmd, time_out=DEFAULT_CMD_TIMEOUT, no_check_return=False):
    LOG.info("Doing CMD: %s" % cmd)
    pre_time = time.time()
    cmd_proc = subprocess.Popen(args=cmd, shell=True)
    while True:
        cmd_exit_code = cmd_proc.poll()
        elapsed_time = time.time() - pre_time
        if cmd_exit_code == None:
            if elapsed_time >= time_out:
                killAllProcesses(ppid=pe_proc.pid)
                LOG.error("Timeout to exe CMD")
                return False
        else:
            if not no_check_return and cmd_exit_code != 0:
                LOG.error("Fail to exe CMD")
                return False
            break
        time.sleep(2)
    return True


def packAPP(app_name=None, app_dir=None, dest_dir=None, sign_flag=False):
    LOG.info("Packing %s(%s)" % (app_name, app_dir))
    try:
        if not os.path.exists(dest_dir):
            os.makedirs(dest_dir)
        if BUILD_PARAMETERS.pkgtype == "xpk":
            xpk_pack_tool = os.path.join(BUILD_ROOT, "make_xpk.py")
            if not os.path.exists(xpk_pack_tool):
                if not doCopy(os.path.join(BUILD_PARAMETERS.pkgpacktools, "make_xpk.py"), xpk_pack_tool):
                    return False
            orig_dir = os.getcwd()
            os.chdir(BUILD_ROOT)
            if os.path.exists("key.file"):
                if not doRemove(["key.file"]):
                    os.chdir(orig_dir)
                    return False
            pack_cmd = "python make_xpk.py %s key.file -o %s" % (
                app_dir, os.path.join(dest_dir, "%s.xpk" % app_name))
            if not doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
                os.chdir(orig_dir)
                return False

        elif BUILD_PARAMETERS.pkgtype == "wgt":
            if not zipDir(app_dir, os.path.join(dest_dir, "%s.wgt" % app_name)):
                return False
            if sign_flag:
                if not os.path.exists(os.path.join(BUILD_ROOT, "signing")):
                    if not doCopy(os.path.join(BUILD_PARAMETERS.pkgpacktools, "signing"), os.path.join(BUILD_ROOT, "signing")):
                        return False
                signing_cmd = "%s --dist platform %s" % (os.path.join(
                    BUILD_ROOT, "signing", "sign-widget.sh"), os.path.join(dest_dir, "%s.wgt" % app_name))
                if not doCMD(signing_cmd, DEFAULT_CMD_TIMEOUT):
                    os.chdir(orig_dir)
                    return False
        elif BUILD_PARAMETERS.pkgtype == "apk" or BUILD_PARAMETERS.pkgtype == "apk-aio":
            app_name = app_name.replace("-", "_")
            #activity_name = ''.join([i.capitalize() for i in app_name.split('_') if i])
            activity_name = app_name

            if not os.path.exists(os.path.join(BUILD_ROOT, "crosswalk")):
                if not doCopy(os.path.join(BUILD_PARAMETERS.pkgpacktools, "crosswalk"), os.path.join(BUILD_ROOT, "crosswalk")):
                    return False
            pack_cmd = "python make_apk.py --package=org.xwalk.%s --name=%s --app-root=%s --app-local-path=index.html --icon=%s/icon.png --mode=%s --arch=%s" % (
                app_name, app_name, app_dir, app_dir, BUILD_PARAMETERS.pkgmode, BUILD_PARAMETERS.pkgarch)
            orig_dir = os.getcwd()
            os.chdir(os.path.join(BUILD_ROOT, "crosswalk"))
            if not doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
                os.chdir(orig_dir)
                return False

            files = glob.glob(
                os.path.join(BUILD_ROOT, "crosswalk", "%s[._]*apk" % activity_name))
            if files:
                if not doCopy(files[0], os.path.join(dest_dir, "%s.apk" % app_name)):
                    os.chdir(orig_dir)
                    return False
            else:
                LOG.error("Fail to find the apk file")
                os.chdir(orig_dir)
                return False

            os.chdir(orig_dir)
        elif BUILD_PARAMETERS.pkgtype == "cordova":
            cordova_tool_path = os.path.join(BUILD_ROOT, "cordova")
            app_name = app_name.replace("-", "_")
            if not os.path.exists(cordova_tool_path):
                if not doCopy(os.path.join(BUILD_PARAMETERS.pkgpacktools, "cordova"), cordova_tool_path):
                    return False
            orig_dir = os.getcwd()
            os.chdir(cordova_tool_path)
            pack_cmd = "bin/create %s org.xwalk.%s %s" % (
                app_name, app_name, app_name)
            if not doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
                os.chdir(orig_dir)
                return False
            if not doRemove([os.path.join(cordova_tool_path, app_name, "assets", "www")]):
                os.chdir(orig_dir)
                return False
            if not doCopy(app_dir, os.path.join(cordova_tool_path, app_name, "assets", "www")):
                os.chdir(orig_dir)
                return False
            os.chdir(os.path.join(BUILD_ROOT, "cordova", app_name))
            pack_cmd = "./cordova/build"
            if not doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
                os.chdir(orig_dir)
                return False

            if not doCopy(os.path.join(BUILD_ROOT, "cordova", app_name, "bin", "%s-debug.apk" % app_name), os.path.join(dest_dir, "%s.apk" % app_name)):
                os.chdir(orig_dir)
                return False
            os.chdir(orig_dir)
    except Exception, e:
        LOG.error("Fail to pack pkg: %s" % e)
        return False

    LOG.info("Success to pack pkg: %s" % app_name)
    return True


def createIndexFile(index_file_path=None, hosted_app=None):
    try:
        if hosted_app:
            index_url = "http://127.0.0.1/opt/%s/webrunner/index.html?testsuite=../tests.xml&testprefix=../../.." % PKG_NAME
        else:
            index_url = "opt/%s/webrunner/index.html?testsuite=../tests.xml&testprefix=../../.." % PKG_NAME
        html_content = "<!doctype html><head><meta http-equiv='Refresh' content='1; url=%s'></head>" % index_url
        index_file = open(index_file_path, "w")
        index_file.write(html_content)
        index_file.close()
    except Exception, e:
        LOG.error("Fail to create index.html for top-app: %s" % e)
        return False
    LOG.info("Success to create index file %s" % index_file_path)
    return True


def createPKGAPP(hosted_app=False, sign_flag=False):
    build_root_pkg_app = os.path.join(BUILD_ROOT, "pkg-app")
    if not doCopy(os.path.join(BUILD_ROOT_SRC, "icon.png"),
                  os.path.join(build_root_pkg_app, "icon.png")):
        return False

    if BUILD_PARAMETERS.pkgtype == "xpk":
        if not doCopy(os.path.join(BUILD_ROOT_SRC, "manifest.json"), os.path.join(build_root_pkg_app, "manifest.json")):
            return False
    elif BUILD_PARAMETERS.pkgtype == "wgt":
        if not doCopy(os.path.join(BUILD_ROOT_SRC, "config.xml"),
                      os.path.join(build_root_pkg_app, "config.xml")):
            return False

    if createIndexFile(os.path.join(build_root_pkg_app, "index.html"), hosted_app):
        if packAPP(PKG_NAME, build_root_pkg_app, BUILD_ROOT_PKG, sign_flag):
            return True
    return False


def buildSubAPP(app_path=None, build_json=None, sub_app_install_root=None):
    sign_flag = False
    if build_json.has_key("sign-flag") and build_json["sign-flag"] == "true":
        sign_flag = True

    src = os.path.join(BUILD_ROOT_SRC, app_path)
    if not build_json.has_key("app-name"):
        app_name = os.path.basename(src)
    else:
        app_name = build_json["app-name"]

    dest = os.path.join(BUILD_ROOT, app_name)
    if buildSRC(src, dest, build_json):
        if build_json.has_key("install-path") and build_json["install-path"] != "":
            sub_app_install_path = os.path.join(
                sub_app_install_root, build_json["install-path"])
        else:
            sub_app_install_path = sub_app_install_root
        if build_json.has_key("all-apps") and build_json["all-apps"] == "true":
            files = os.listdir(dest)
            apps_num = 0
            for i_file in files:
                if os.path.isdir(os.path.join(dest, i_file)):
                    i_app_name = os.path.basename(i_file)
                    if not packAPP(i_app_name, os.path.join(dest, i_app_name), sub_app_install_path, sign_flag):
                        return False
                    else:
                        apps_num = apps_num + 1
            if apps_num > 0:
                LOG.info("Totally found %d apps in %s" % (apps_num, app_path))
                return True
        else:
            return packAPP(app_name, dest, sub_app_install_path, sign_flag)
    return False


def buildPKGAPP(build_json=None):
    sign_flag = False
    if build_json.has_key("sign-flag") and build_json["sign-flag"] == "true":
        sign_flag = True

    if build_json.has_key("hosted-app") and build_json["hosted-app"] == "true":
        if not createPKGAPP(True, sign_flag):
            return False
    else:
        if not build_json.has_key("blacklist"):
            build_json.update({"blacklist": []})
        build_json["blacklist"].extend(PKG_BLACK_LIST)
        if not buildSRC(BUILD_ROOT_SRC, BUILD_ROOT_PKG_APP, build_json):
            return False

        if build_json.has_key("subapp-list"):
            for i_sub_app in build_json["subapp-list"].keys():
                if not buildSubAPP(i_sub_app, build_json["subapp-list"][i_sub_app], BUILD_ROOT_PKG_APP):
                    return False

        if not createPKGAPP(False, sign_flag):
            return False

    return True


def buildPKG(build_json=None):
    if not build_json.has_key("blacklist"):
        build_json.update({"blacklist": []})
    build_json["blacklist"].extend(PKG_BLACK_LIST)
    if not buildSRC(BUILD_ROOT_SRC, BUILD_ROOT_PKG, build_json):
        return False

    if build_json.has_key("subapp-list"):
        for i_sub_app in build_json["subapp-list"].keys():
            if not buildSubAPP(i_sub_app, build_json["subapp-list"][i_sub_app], BUILD_ROOT_PKG):
                return False

    if build_json.has_key("pkg-app"):
        if not buildPKGAPP(build_json["pkg-app"]):
            return False

    return True


def main():
    global LOG
    LOG = logging.getLogger("pack-tool")
    LOG.setLevel(LOG_LEVEL)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(LOG_LEVEL)
    stream_formatter = logging.Formatter("-->> %(asctime)s - %(message)s")
    stream_handler.setFormatter(stream_formatter)
    LOG.addHandler(stream_handler)

    try:
        usage = "Usage: ./pack.py -t apk -m shared -a x86"
        opts_parser = OptionParser(usage=usage)
        opts_parser.add_option(
            "-c", "--cfg", dest="pkgcfg", help="Specify the path of config json file")
        opts_parser.add_option(
            "-t", "--type", dest="pkgtype", help="Specify the pkg type, e.g. apk, xpk, wgt ...")
        opts_parser.add_option(
            "-m", "--mode", dest="pkgmode", help="Specify the apk mode, e.g. shared, embedded")
        opts_parser.add_option(
            "-a", "--arch", dest="pkgarch", help="Specify the apk arch, e.g. x86, arm")
        opts_parser.add_option(
            "-d", "--dest", dest="destdir", help="Specify the installaion path of all in one pkg resource")
        opts_parser.add_option(
            "--tools", dest="pkgpacktools", help="Specify the path of tools of crosswalk, signing ...")
        opts_parser.add_option(
            "--notclean", dest="bnotclean", action="store_true", help="Disable the build root clean after the packing")
        opts_parser.add_option(
            "-v", "--version", dest="bversion", action="store_true", help="Show this tool's version")

        if len(sys.argv) == 1:
            sys.argv.append("-h")

        global BUILD_PARAMETERS
        (BUILD_PARAMETERS, args) = opts_parser.parse_args()
    except Exception, e:
        LOG.error("Got wrong options: %s, exit ..." % e)
        sys.exit(1)

    if BUILD_PARAMETERS.bversion:
        print "Version: %s" % TOOL_VERSION
        sys.exit(0)

    if not os.path.exists(os.path.join(SCRIPT_DIR, "..", "..", VERSION_FILE)):
        if not os.path.exists(os.path.join(SCRIPT_DIR, "..", VERSION_FILE)):
            if not os.path.exists(os.path.join(SCRIPT_DIR, VERSION_FILE)):
                LOG.error("No found pkg version file, exit ...")
                sys.exit(1)
            else:
                pkg_version_file_path = os.path.join(SCRIPT_DIR, VERSION_FILE)
        else:
            pkg_version_file_path = os.path.join(
                SCRIPT_DIR, "..", VERSION_FILE)
    else:
        pkg_version_file_path = os.path.join(
            SCRIPT_DIR, "..", "..", VERSION_FILE)

    try:
        LOG.error("Using pkg version file: %s" % pkg_version_file_path)
        with open(pkg_version_file_path, "rt") as pkg_version_file:
            pkg_version_raw = pkg_version_file.read()
            pkg_version_file.close()
            pkg_version_json = json.loads(pkg_version_raw)
            pkg_main_version = pkg_version_json["main-version"]
            pkg_release_version = pkg_version_json["release-version"]
    except Exception, e:
        LOG.error("Fail to read pkg version file: %s, exit ..." % e)
        sys.exit(1)

    if not BUILD_PARAMETERS.pkgtype:
        LOG.error("No pkg type provided, exit ...")
        sys.exit(1)
    elif not BUILD_PARAMETERS.pkgtype in PKG_TYPE:
        LOG.error("Wrong pkg type, only support: %s, exit ..." %
                  PKG_TYPE)
        sys.exit(1)

    if BUILD_PARAMETERS.pkgtype == "apk" or BUILD_PARAMETERS.pkgtype == "apk-aio":
        if not BUILD_PARAMETERS.pkgmode:
            LOG.error("No pkg mode option provided, exit ...")
            sys.exit(1)
        elif not BUILD_PARAMETERS.pkgmode in PKG_MODE:
            LOG.error(
                "Wrong pkg mode option provided, only support:%s, exit ..." % PKG_MODE)
            sys.exit(1)

        if not BUILD_PARAMETERS.pkgarch:
            LOG.error("No pkg arch option provided, exit ...")
            sys.exit(1)
        elif not BUILD_PARAMETERS.pkgarch in PKG_ARCH:
            LOG.error(
                "Wrong pkg arch option provided, only support:%s, exit ..." % PKG_ARCH)
            sys.exit(1)

    if BUILD_PARAMETERS.pkgtype == "apk-aio":
        if not BUILD_PARAMETERS.destdir or not os.path.exists(BUILD_PARAMETERS.destdir):
            LOG.error("No all-in-one installation dest dir found, exit ...")
            sys.exit(1)

    if not BUILD_PARAMETERS.pkgpacktools:
        BUILD_PARAMETERS.pkgpacktools = os.path.join(
            SCRIPT_DIR, "..", "..", "tools")

    config_json = None
    if BUILD_PARAMETERS.pkgcfg:
        config_json_file_path = BUILD_PARAMETERS.pkgcfg
    else:
        config_json_file_path = os.path.join(
            SCRIPT_DIR, "suite.json")
    try:
        LOG.error("Using config json file: %s" % config_json_file_path)
        with open(config_json_file_path, "rt") as config_json_file:
            config_raw = config_json_file.read()
            config_json_file.close()
            config_json = json.loads(config_raw)
    except Exception, e:
        LOG.error("Fail to read config json file: %s, exit ..." % e)
        sys.exit(1)

    if config_json.has_key("pkg-name") and config_json["pkg-name"] != "":
        global PKG_NAME
        PKG_NAME = config_json["pkg-name"]
        LOG.info("================ %s (%s-%s) ================" %
                 (PKG_NAME, pkg_main_version, pkg_release_version))
    else:
        LOG.error("Fail to read pkg name, exit ...")
        sys.exit(1)

    if not config_json.has_key("pkg-list") or config_json["pkg-list"] == "":
        LOG.error("Fail to read pkg-list, exit ..." % e)
        sys.exit(1)

    pkg_json = None
    for i_pkg in config_json["pkg-list"].keys():
        i_pkg_list = i_pkg.replace(" ", "").split(",")
        if BUILD_PARAMETERS.pkgtype in i_pkg_list:
            pkg_json = config_json["pkg-list"][i_pkg]

    if not pkg_json or pkg_json == "":
        LOG.error("Fail to read pkg json, exit ...")
        sys.exit(1)

    if not perpareBuildRoot():
        exitHandler(1)

    if config_json.has_key("pkg-blacklist"):
        PKG_BLACK_LIST.extend(config_json["pkg-blacklist"])

    if not buildPKG(pkg_json):
        exitHandler(1)

    if BUILD_PARAMETERS.pkgtype == "apk-aio":
        pkg_file_list = os.listdir(os.path.join(BUILD_ROOT, "pkg"))
        for i_file in pkg_file_list:
            if not doCopy(os.path.join(BUILD_ROOT, "pkg", i_file), os.path.join(BUILD_PARAMETERS.destdir, i_file)):
                exitHandler(1)
    else:
        pkg_file = os.path.join(SCRIPT_DIR, "%s-%s-%s.%s.zip" % (PKG_NAME,
                                                                 pkg_main_version, pkg_release_version, BUILD_PARAMETERS.pkgtype))
        if not zipDir(os.path.join(BUILD_ROOT, "pkg"), pkg_file):
            exitHandler(1)

if __name__ == "__main__":
    main()
    exitHandler(0)
