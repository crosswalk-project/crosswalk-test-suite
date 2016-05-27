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

import os
import glob
import time
import sys
import json
import subprocess
import commands
import platform
from optparse import OptionParser

import build_android
import build_cordova
import build_embeddingapi
import build_extension
import build_deb
import build_msi
import varshop
import utils
import resource_only

reload(sys)
if platform.system() == "Windows":
    sys.setdefaultencoding('gbk')
else:
    sys.setdefaultencoding('utf8')

TOOL_VERSION = "v0.1"
VERSION_FILE = "VERSION"
PKG_TYPES = [
    "apk",
    "apk-aio",
    "cordova-aio",
    "cordova",
    "embeddingapi",
    "deb",
    "msi",
    "ios"]
PKG_BLACK_LIST = []
PACK_TYPES = ["ant", "gradle", "maven"]
CORDOVA_PACK_TYPES = ["npm", "local"]
PKG_NAME = None
BUILD_ROOT_SRC_PKG = None
BUILD_ROOT_SRC_PKG_APP = None
BUILD_ROOT_SRC_SUB_APP = None
BUILD_ROOT_PKG = None
BUILD_ROOT_PKG_APP = None

# Variables which store in config.py
BUILD_PARAMETERS = None
BUILD_ROOT = None
BUILD_ROOT_SRC = None
BUILD_TIME = time.strftime('%Y%m%d', time.localtime(time.time()))
CROSSWALK_BRANCH = ""
CROSSWALK_VERSION = ""
DEFAULT_CMD_TIMEOUT = 600
PKG_MODES = ["shared", "embedded", "lite"]
PKG_ARCHS = ["x86", "arm", "x86_64", "arm64"]


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

    if not utils.doCopy(src, dest):
        return False
    if "blacklist" in build_json:
        if build_json["blacklist"].count("") > 0:
            build_json["blacklist"].remove("")
        black_file_list = []
        for i_black in build_json["blacklist"]:
            black_file_list = black_file_list + \
                glob.glob(os.path.join(dest, i_black))

        black_file_list = list(set(black_file_list))
        if not utils.doRemove(black_file_list):
            return False
    if "copylist" in build_json:
        for i_s_key in build_json["copylist"].keys():
            if i_s_key and build_json["copylist"][i_s_key]:
                (src_updated, dest_updated) = updateCopylistPrefix(
                    src, dest, i_s_key, build_json["copylist"][i_s_key])
                if not utils.doCopy(src_updated, dest_updated):
                    return False

    return True


def exitHandler(return_code=1):
    LOG.info("+Cleaning build root folder ...")
    if not BUILD_PARAMETERS.bnotclean and os.path.exists(BUILD_ROOT):
        if not utils.doRemove([BUILD_ROOT]):
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
        BUILD_ROOT = os.path.join("/tmp", utils.getRandomStr())
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

    if not utils.doCopy(BUILD_PARAMETERS.srcdir, BUILD_ROOT_SRC):
        return False
    else:
        utils.replaceUserString(
            BUILD_ROOT_SRC,
            '*',
            'TESTER-HOME-DIR',
            "/home/%s" %
            BUILD_PARAMETERS.user)

    if not utils.doRemove(
            glob.glob(os.path.join(BUILD_ROOT_SRC, "%s*.zip" % PKG_NAME))):
        return False

    return True


def packAPP(build_json=None, app_src=None, app_dest=None, app_name=None):
    LOG.info("Packing %s(%s)" % (app_name, app_src))
    if not os.path.exists(app_dest):
        try:
            os.makedirs(app_dest)
        except Exception as e:
            LOG.error("Fail to init package install dest dir: %s" % e)
            return False

    app_tpye = utils.safelyGetValue(build_json, 'app-type')

    if utils.checkContains(BUILD_PARAMETERS.pkgtype, "APK") and app_tpye == "EXTENSION":
        if not build_extension.packExtension(build_json, app_src, app_dest, app_name):
            return False
        if not build_android.packAPK(build_json, app_src, app_dest, app_name):
            return False
    elif utils.checkContains(BUILD_PARAMETERS.pkgtype, "APK") and app_tpye != "EMBEDDINGAPI":
        if not build_android.packAPK(build_json, app_src, app_dest, app_name):
            return False
    elif utils.checkContains(BUILD_PARAMETERS.pkgtype, "CORDOVA"):
        if not build_cordova.packCordova(build_json, app_src, app_dest, app_name):
            return False
    elif utils.checkContains(BUILD_PARAMETERS.pkgtype, "EMBEDDINGAPI") or app_tpye == "EMBEDDINGAPI":
        app_version = None
        if "_" in app_name:
            index_flag = app_name.index("_")
            app_version = app_name[index_flag + 1:]
        if app_version:
            utils.replaceUserString(
                app_src,
                'AndroidManifest.xml',
                'org.xwalk.embedding.test',
                "org.xwalk.embedding.test." +
                app_version)
            utils.replaceUserString(
                app_src,
                'AndroidManifest.xml',
                'EmbeddingApiTestUnit',
                "EmbeddingApiTestUnit" +
                app_version)
            if app_version != "v6":
                utils.replaceUserString(
                    app_src,
                    'AndroidManifest.xml',
                    '<provider android:name=\"org.xwalk.embedding.base.TestContentProvider\"' +
                    ' android:authorities=\"org.xwalk.embedding.base.TestContentProvider\" />',
                    "")
            main_dest = os.path.join(app_src, "src/org/xwalk/embedding")
            utils.replaceUserString(
                main_dest,
                'MainActivity.java',
                'org.xwalk.embedding.test',
                "org.xwalk.embedding.test." +
                app_version)
        if BUILD_PARAMETERS.packtype and utils.checkContains(
                BUILD_PARAMETERS.packtype, "GRADLE"):
            if not build_embeddingapi.packEmbeddingAPI_gradle(
                    build_json, app_src, app_dest, app_name, app_version):
                return False
        elif BUILD_PARAMETERS.packtype and utils.checkContains(BUILD_PARAMETERS.packtype, "MAVEN"):
            if not build_embeddingapi.packEmbeddingAPI_maven(
                    build_json, app_src, app_dest, app_name, app_version):
                return False
        else:
            if not build_embeddingapi.packEmbeddingAPI_ant(
                    build_json, app_src, app_dest, app_name, app_version):
                return False
    elif utils.checkContains(BUILD_PARAMETERS.pkgtype, "DEB"):
        if not build_deb.packDeb(build_json, app_src, app_dest, app_name):
            return False
    elif utils.checkContains(BUILD_PARAMETERS.pkgtype, "MSI"):
        if not build_msi.packMsi(build_json, app_src, app_dest, app_name):
            return False
    elif utils.checkContains(BUILD_PARAMETERS.pkgtype, "ios"):
        if not build_ios.packIOS(build_json, app_src, app_dest, app_name):
            return False
    else:
        LOG.error("Got wrong pkg type: %s" % BUILD_PARAMETERS.pkgtype)
        return False

    LOG.info("Success to pack APP: %s" % app_name)
    return True


def createIndexFile(index_file_path=None, hosted_app=None):
    try:
        if hosted_app:
            index_url = "http://127.0.0.1:8080/opt/%s/webrunner/index.html?" \
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
    app_dir_inside = utils.safelyGetValue(build_json, "app-dir")
    if app_dir_inside:
        app_dir = app_dir_inside
    LOG.info("+Building sub APP(s) from %s ..." % app_dir)
    app_dir = os.path.join(BUILD_ROOT_SRC, app_dir)
    app_name = utils.safelyGetValue(build_json, "app-name")
    if not app_name:
        app_name = os.path.basename(app_dir)

    app_src = os.path.join(BUILD_ROOT_SRC_SUB_APP, app_name)
    if buildSRC(app_dir, app_src, build_json):
        app_dest = utils.safelyGetValue(build_json, "install-path")
        if app_dest:
            app_dest = os.path.join(app_dest_default, app_dest)
        else:
            app_dest = app_dest_default

        if utils.safelyGetValue(build_json, "all-apps") == "true":
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
    if utils.safelyGetValue(build_json, "apk-type") == "MANIFEST":
        if not os.path.exists(os.path.join(BUILD_ROOT_SRC, "manifest.json")):
            LOG.error("Not found manifest.json in suite folder, please check!")
            sys.exit(1)
        if not utils.doCopy(os.path.join(BUILD_ROOT_SRC, "manifest.json"),
                      os.path.join(BUILD_ROOT_SRC_PKG_APP, "manifest.json")):
            return False
    if os.path.exists(os.path.join(BUILD_ROOT_SRC, "icon.png")):
        if not utils.doCopy(os.path.join(BUILD_ROOT_SRC, "icon.png"),
                      os.path.join(BUILD_ROOT_SRC_PKG_APP, "icon.png")):
            return False
    if os.path.exists(os.path.join(BUILD_ROOT_SRC, "icon.ico")):
        if not utils.doCopy(os.path.join(BUILD_ROOT_SRC, "icon.ico"),
                      os.path.join(BUILD_ROOT_SRC_PKG_APP, "icon.ico")):
            return False

    hosted_app = False
    if utils.safelyGetValue(build_json, "hosted-app") == "true":
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

    if BUILD_PARAMETERS.docrootonly:
        return True

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
    LOG = utils.getLogger("pack-tool")
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
            help="specify the pkg type, e.g. apk, cordova ...")
        opts_parser.add_option(
            "-m",
            "--mode",
            dest="pkgmode",
            help="specify the apk mode, not for embeddingapi, e.g. shared, embedded")
        opts_parser.add_option(
            "-a",
            "--arch",
            dest="pkgarch",
            help="specify the apk arch, not for embeddingapi, e.g. x86, arm")
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
            help="specify the crosswalk version, e.g. 18.48.477.13 " \
                 "or the absolute path of the specific crosswalk binary")
        opts_parser.add_option(
            "--pack-type",
            dest="packtype",
            help="specify the pack type, e.g. gradle, maven")
        opts_parser.add_option(
            "--notdebug",
            dest="bnotdebug",
            action="store_true",
            help="specify the packed pkg is not debug mode")
        opts_parser.add_option(
            "--resource-only",
            dest="resourceonly",
            action="store_true",
            help="only restore resources to project root")
        opts_parser.add_option(
            "--docroot-only",
            dest = "docrootonly",
            action = "store_true",
            default = False,
            help = "pack docroot only for webtestingservice")

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
            CROSSWALK_BRANCH = "master"
        else:
            if pkg_version_file_path is not None:
                LOG.info("Using pkg version file: %s" % pkg_version_file_path)
                with open(pkg_version_file_path, "rt") as pkg_version_file:
                    pkg_version_raw = pkg_version_file.read()
                    pkg_version_file.close()
                    pkg_version_json = json.loads(pkg_version_raw)
                    pkg_main_version = pkg_version_json["main-version"]
                    pkg_release_version = pkg_version_json["release-version"]
                    CROSSWALK_BRANCH = pkg_version_json["crosswalk-branch"]
    except Exception as e:
        LOG.error("Fail to read pkg version file: %s, exit ..." % e)
        sys.exit(1)
    CROSSWALK_VERSION = pkg_main_version

    if not BUILD_PARAMETERS.pkgtype:
        LOG.error("No pkg type provided, exit ...")
        sys.exit(1)
    elif not BUILD_PARAMETERS.pkgtype in PKG_TYPES:
        LOG.error("Wrong pkg type, only support: %s, exit ..." %
                  PKG_TYPES)
        sys.exit(1)

    if BUILD_PARAMETERS.resourceonly:
        LOG.info("Starting copy resource only")
        resource_only.copy_resource(BUILD_PARAMETERS.pkgtype)
        sys.exit(0)

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
    PKG_NAME = utils.safelyGetValue(config_json, "pkg-name")
    if not PKG_NAME:
        PKG_NAME = os.path.basename(BUILD_PARAMETERS.srcdir)
        LOG.warning(
            "Fail to read pkg name from json, "
            "using src dir name as pkg name ...")

    LOG.info("================= %s (%s-%s) ================" %
             (PKG_NAME, pkg_main_version, pkg_release_version))

    if not utils.safelyGetValue(config_json, "pkg-list"):
        LOG.error("Fail to read pkg-list, exit ...")
        sys.exit(1)

    pkg_json = None
    global parameters_type
    parameters_type = None

    if BUILD_PARAMETERS.pkgtype == "cordova" or BUILD_PARAMETERS.pkgtype == "cordova-aio":

        if BUILD_PARAMETERS.pkgarch and not BUILD_PARAMETERS.pkgarch in PKG_ARCHS:
            LOG.error("Wrong pkg-arch, only support: %s, exit ..." %
                      PKG_ARCHS)
            sys.exit(1)

        if BUILD_PARAMETERS.pkgmode and not BUILD_PARAMETERS.pkgmode in PKG_MODES:
            LOG.error("Wrong pkg-mode, only support: %s, exit ..." %
                      PKG_MODES)
            sys.exit(1)

        if BUILD_PARAMETERS.packtype and not BUILD_PARAMETERS.packtype in CORDOVA_PACK_TYPES:
            LOG.error("cordova packtype can only be npm, local")
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

    if pkg_json == config_json['pkg-list'].get('apk') and BUILD_PARAMETERS.subversion is not None:
        pkg_json = config_json["pkg-list"][BUILD_PARAMETERS.subversion]

    if not pkg_json:
        LOG.error("Fail to read pkg json, exit ...")
        sys.exit(1)

    if not prepareBuildRoot():
        exitHandler(1)

    if "pkg-blacklist" in config_json:
        PKG_BLACK_LIST.extend(config_json["pkg-blacklist"])

    try:
        varshop.setValue("BUILD_PARAMETERS", BUILD_PARAMETERS)
        varshop.setValue("BUILD_ROOT", BUILD_ROOT)
        varshop.setValue("BUILD_ROOT_SRC", BUILD_ROOT_SRC)
        varshop.setValue("BUILD_TIME", BUILD_TIME)
        varshop.setValue("CROSSWALK_BRANCH", CROSSWALK_BRANCH)
        varshop.setValue("CROSSWALK_VERSION", CROSSWALK_VERSION)
        varshop.setValue("DEFAULT_CMD_TIMEOUT", DEFAULT_CMD_TIMEOUT)
        varshop.setValue("PKG_MODES", PKG_MODES)
        varshop.setValue("PKG_ARCHS", PKG_ARCHS)
    except Exception as e:
        LOG.error("Fail to set global vars: %s, exit ..." % e)
        sys.exit(1)

    if not buildPKG(pkg_json):
        exitHandler(1)


    LOG.info("+Building package ...")
    if BUILD_PARAMETERS.pkgtype == "apk-aio" or \
       BUILD_PARAMETERS.pkgtype == "cordova-aio":
        pkg_file_list = os.listdir(os.path.join(BUILD_ROOT, "pkg"))
        for i_file in pkg_file_list:
            if not utils.doCopy(
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
        if not utils.zipDir(os.path.join(BUILD_ROOT, "pkg"), pkg_file):
            exitHandler(1)
    elif BUILD_PARAMETERS.pkgtype.startswith("embeddingapi") and BUILD_PARAMETERS.packtype:
        pkg_file = os.path.join(
            BUILD_PARAMETERS.destdir,
            "%s-%s-%s.%s-%s.zip" %
            (PKG_NAME,
             pkg_main_version,
             pkg_release_version,
             BUILD_PARAMETERS.pkgtype,
             BUILD_PARAMETERS.packtype))

        if not utils.zipDir(os.path.join(BUILD_ROOT, "pkg"), pkg_file):
            exitHandler(1)
    else:
        pkg_file = os.path.join(
            BUILD_PARAMETERS.destdir,
            "%s-%s-%s.%s.zip" %
            (PKG_NAME,
             pkg_main_version,
             pkg_release_version,
             BUILD_PARAMETERS.pkgtype))

        if not utils.zipDir(os.path.join(BUILD_ROOT, "pkg"), pkg_file):
            exitHandler(1)

if __name__ == "__main__":
    main()
    exitHandler(0)
