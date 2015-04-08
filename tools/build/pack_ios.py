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
#         Wang, Hongjuan <hongjuanx.wang@intel.com>

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
import re
from optparse import OptionParser

reload(sys)
sys.setdefaultencoding('utf8')

TOOL_VERSION = "v0.1"
VERSION_FILE = "VERSION"
DEFAULT_CMD_TIMEOUT = 600
PKG_TYPES = ["ios"]
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


def iterfindfiles(path, fnexp):
    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files, fnexp):
            yield os.path.join(root, filename)

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
    global BUILD_ROOT	# The build root directory, like as "/tmp/randomName"
    global BUILD_ROOT_SRC	# The source code in the tmp directory, like as "/tmp/randomName/crosswalk-test"
    global BUILD_ROOT_SRC_PKG	# The source of the zip operate for all package, like as "/tmp/randomName/pkg" 
    global BUILD_ROOT_SRC_PKG_APP	# The source of the app_package operate for all package, like as "/tmp/randomName/pkg-app"
    global BUILD_ROOT_SRC_SUB_APP	# The source of the sub app_package operate for all package, like as "/tmp/randomName/sub-app"
    global BUILD_ROOT_PKG	# BUILD_ROOT_SRC_PKG + "opt" + PKG_NAME
    global BUILD_ROOT_PKG_APP	# BUILD_ROOT_SRC_PKG_APP + "opt" + PKG_NAME

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
        replaceUserString(BUILD_ROOT_SRC,'*','TESTER-HOME-DIR',"/home/%s"%BUILD_PARAMETERS.user)

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


def createIndexFile(index_file_path=None, hosted_app=None):
    try:
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
	
    pkg_name = app_name
    LOG.info("+Change dir to %s: " % BUILD_ROOT_SRC_SUB_APP)
    if not os.path.exists(BUILD_ROOT_SRC_SUB_APP):
        LOG.info("Create BUILD_ROOT_SRC_SUB_APP dir: %s" %
        BUILD_ROOT_SRC_SUB_APP)
        os.makedirs(BUILD_ROOT_SRC_SUB_APP)
    os.chdir(BUILD_ROOT_SRC_SUB_APP)
    pack_cmd = "crosswalk-app create " + pkg_name
    orig_dir = os.getcwd()
    if not doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
		os.chdir(orig_dir)
		return False
	
	# copy source to  BUILD_ROOT_SRC_SUB_APP/pkg_name/app
    if buildSRC(app_dir, os.path.join(app_src, "app"), build_json):
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

def replaceCopy(readfile,writefile,content,newContent): 
    ffrom=open(readfile,"r")  
    fto=open(writefile,"w")  
    while True:  
        l = ffrom.readline()  
        if not l:  
            break  
        if 'org.xwalk.embedding.test' in l:
            temp = ""
            temp=re.sub(content,newContent,l)
            fto.write(temp)
        else:
            temp1 = l  
            fto.write(temp1)  
    fto.close()

def findVersionFile(pathFile=None):
    if not pathFile:
        pathFile = os.path.join("..", "..", "..")
    if not os.path.exists(
                os.path.join(BUILD_PARAMETERS.srcdir, pathFile, VERSION_FILE)):
        pathFile = pathFile[:-3]
        if pathFile != "..":
            findVersionFile(pathFile)
    else:
        pkg_version_file_path = os.path.join(BUILD_PARAMETERS.srcdir, pathFile, VERSION_FILE)
    	return (pkg_version_file_path)

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
        usage = "Usage: ./%prog -t ios"
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
            help="specify the pkg type, e.g. ios ...")
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
            "-v",
            "--version",
            dest="bversion",
            action="store_true",
            help="show this pack tool's version")
        opts_parser.add_option(
            "-u",
            "--user",
            dest="user",
            help="specify the user in inst.py")
        opts_parser.add_option(
            "--pkg-version",
            dest="pkgversion",
            help="specify the pkg version, e.g. 0.0.0.1")

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

    pkg_version_file_path = findVersionFile()

    try:
        pkg_main_version = 0
        pkg_release_version = 1
        if BUILD_PARAMETERS.pkgversion:
            LOG.info("Using %s as pkg version " % BUILD_PARAMETERS.pkgversion)
            pkg_main_version = BUILD_PARAMETERS.pkgversion
        else:
            if pkg_version_file_path is not None:
                LOG.info("Using pkg version by file: %s" % pkg_version_file_path)
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
            "Due to fail to read pkg name from json that "
            "using src dir name as pkg name ...")

    LOG.info("================= %s (%s-%s) ================" %
             (PKG_NAME, pkg_main_version, pkg_release_version))

    if not safelyGetValue(config_json, "pkg-list"):
        LOG.error("Fail to read pkg-list, exit ...")
        sys.exit(1)

    pkg_json = None
    for i_pkg in config_json["pkg-list"].keys():
        i_pkg_list = i_pkg.replace(" ", "").split(",")
        if BUILD_PARAMETERS.pkgtype in i_pkg_list:
            pkg_json = config_json["pkg-list"][i_pkg]

    if not pkg_json:
        LOG.error("Fail to read pkg json, exit ...")
        sys.exit(1)

    if not prepareBuildRoot():
        exitHandler(1)
    
    global PKG_BLACK_LIST
    PKG_BLACK_LIST = []
    if "pkg-blacklist" in config_json:
        PKG_BLACK_LIST.extend(config_json["pkg-blacklist"])

    if not buildPKG(pkg_json):
        exitHandler(1)

    LOG.info("+Building package ...")
    pkg_file = os.path.join(
        BUILD_PARAMETERS.destdir,
        "%s-%s-%s.%s.zip" %
        (PKG_NAME,
        pkg_main_version,
        pkg_release_version,
        BUILD_PARAMETERS.pkgtype))
        
    if not zipDir(BUILD_ROOT_SRC_PKG, pkg_file):
            exitHandler(1)

if __name__ == "__main__":
    main()
    exitHandler(0)
