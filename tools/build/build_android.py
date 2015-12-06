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
#         Hao, Yunfei <yunfeix.hao@intel.com>

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
import varshop
import utils

global LOG
LOG = utils.getLogger("build_android")

def getNameById(filename=None):
    '''
    According to the rule defined in crosswalk-pkg tool,
    package built name will be org.xwalk.extensions_ad-0.1-debug.shared.apk,
    so here we get the name "extension_ad" as apk's name
    '''
    try:
        lst_name_dot = filename.split('.', 2)
        lst_name_hyphen = lst_name_dot[2].split('-')
        return lst_name_hyphen[0]
    except Exception as e:
        LOG.error("Cannot get apk's name, error is: %s" % e)
        sys.exit(1)


def packAPK(build_json=None, app_src=None, app_dest=None, app_name=None):
    BUILD_PARAMETERS = varshop.getValue("BUILD_PARAMETERS")
    BUILD_ROOT = varshop.getValue("BUILD_ROOT")
    BUILD_ROOT_SRC = varshop.getValue("BUILD_ROOT_SRC")
    BUILD_TIME= varshop.getValue("BUILD_TIME")
    CROSSWALK_VERSION = varshop.getValue("CROSSWALK_VERSION")
    DEFAULT_CMD_TIMEOUT= varshop.getValue("DEFAULT_CMD_TIMEOUT")
    PKG_MODES= varshop.getValue("PKG_MODES")
    PKG_ARCHS= varshop.getValue("PKG_ARCHS")
    app_name = app_name.replace("-", "_")
    get_real_arch = {"x86": "x86",
                     "x86_64": "x86_64",
                     "arm": "armeabi-v7a",
                     "arm64": "arm64-v8a"}

    #Use crosswalk zip in local mode
    #if not os.path.exists(os.path.join(BUILD_ROOT, "crosswalk-%s.zip" % CROSSWALK_VERSION)):
    #    if not utils.doCopy(
    #            os.path.join(BUILD_PARAMETERS.pkgpacktools, "crosswalk-%s.zip" % CROSSWALK_VERSION),
    #            os.path.join(BUILD_ROOT, "crosswalk-%s.zip" % CROSSWALK_VERSION)):
    #        return False

    files = glob.glob(os.path.join(BUILD_ROOT, "*.apk"))
    if files:
        if not utils.doRemove(files):
            return False

    ext_opt = []
    cmd_opt = ""
    url_opt = ""
    mode_opt = ""
    arch_opt = ""
    icon_opt = ""
    icons_opt = []
    version_opt = ""
    pkg_opt = ""
    version_code_opt = ""
    fullscreen_opt = ""
    orientation_opt = ""
    screenOn_opt = ""
    animatableView_opt = ""
    webp_opt = ""
    shortName_opt = ""
    permissions_opt = []

    common_opts = utils.safelyGetValue(build_json, "apk-common-opts")
    if common_opts is None:
        common_opts = " -r "
    else:
        common_opts_array = common_opts.split()
        if "-r" in common_opts_array:
            pass
        elif "--enable-remote-debugging" in common_opts_array:
            common_opts = common_opts.replace('--enable-remote-debugging', '')
        else:
            common_opts += " -r "
    #workaround for XWALK-4042
    common_opts = common_opts.replace(' -r ','')

    tmp_opt = utils.safelyGetValue(build_json, "apk-ext-opt")
    if tmp_opt:
        ext_opt = [os.path.join(BUILD_ROOT_SRC, tmp_opt)]

    tmp_opt = utils.safelyGetValue(build_json, "apk-version-opt")
    if tmp_opt:
        version_opt = "%s" % tmp_opt

    tmp_opt = utils.safelyGetValue(build_json, "apk-fullscreen-opt")
    if tmp_opt:
        fullscreen_opt = "%s" % tmp_opt

    tmp_opt = utils.safelyGetValue(build_json, "apk-pkg-opt")
    if tmp_opt:
        pkg_opt = "%s" % tmp_opt

    tmp_opt = utils.safelyGetValue(build_json, "apk-cmd-opt")
    if tmp_opt:
        cmd_opt = "%s" % tmp_opt

    tmp_opt = utils.safelyGetValue(build_json, "apk-url-opt")
    if tmp_opt:
        url_opt = "%s" % tmp_opt

    tmp_opt = utils.safelyGetValue(build_json, "apk-orientation-opt")
    if tmp_opt:
        orientation_opt = "%s" % tmp_opt

    tmp_opt = utils.safelyGetValue(build_json, "apk-screenOn-opt")
    if tmp_opt:
        screenOn_opt = "%s" % tmp_opt

    tmp_opt = utils.safelyGetValue(build_json, "apk-animatableView-opt")
    if tmp_opt:
        animatableView_opt = "%s" % tmp_opt

    tmp_opt = utils.safelyGetValue(build_json, "apk-webp-opt")
    if tmp_opt:
        webp_opt = "%s" % tmp_opt

    tmp_opt = utils.safelyGetValue(build_json, "apk-shortName-opt")
    if tmp_opt:
        shortName_opt = "%s" % tmp_opt

    tmp_opt = utils.safelyGetValue(build_json, "apk-permissions-opt")
    if tmp_opt:
        permissions_opt = [tmp_opt]

    tmp_opt = utils.safelyGetValue(build_json, "apk-mode-opt")
    if tmp_opt:
        if tmp_opt in PKG_MODES:
            mode_opt = "--android=\"%s\"" % tmp_opt
            if tmp_opt == "embedded":
                mode_opt = ""
        else:
            LOG.error("Got wrong app mode: %s" % tmp_opt)
            return False
    else:
        mode_opt = "--android=\"%s\"" % BUILD_PARAMETERS.pkgmode
        if BUILD_PARAMETERS.pkgmode == "embedded":
            mode_opt = ""

    tmp_opt = utils.safelyGetValue(build_json, "apk-arch-opt")
    if tmp_opt:
        if tmp_opt in PKG_ARCHS:
            arch_opt = "%s" % tmp_opt
        else:
            LOG.error("Got wrong app arch: %s" % tmp_opt)
            return False
    else:
        arch_opt = "%s" % BUILD_PARAMETERS.pkgarch
    arch_opt = get_real_arch[arch_opt]

    tmp_opt = utils.safelyGetValue(build_json, "apk-icon-opt")
    if tmp_opt:
        icon_opt = "%s" % tmp_opt
        icon_set = {}
        icon_set["src"] = icon_opt
        icon_set["sizes"] = "72x72"
        icons_opt = [icon_set]
    elif tmp_opt == "":
        pass
    else:
        icon_opt = "icon.png"
        icon_set = {}
        icon_set["src"] = icon_opt
        icon_set["sizes"] = "72x72"
        icons_opt = [icon_set]

    manifest_opt = {}
    manifest_opt["name"] = "%s" % app_name
    if pkg_opt:
        manifest_opt["xwalk_package_id"] = "org.xwalk.%s" % pkg_opt
    else:
        manifest_opt["xwalk_package_id"] = "org.xwalk.%s" % app_name
    if url_opt:
        manifest_opt["start_url"] = url_opt
    else:
        manifest_opt["start_url"] = "index.html"
    if ext_opt:
        manifest_opt["xwalk_extensions"] = ext_opt
    if cmd_opt:
        manifest_opt["xwalk_command_line"] = cmd_opt
    if fullscreen_opt:
        manifest_opt["display"] = fullscreen_opt
    if version_opt:
        manifest_opt["xwalk_app_version"] = version_opt
    if icons_opt and \
           utils.safelyGetValue(build_json, "apk-type") != "MANIFEST":
        manifest_opt["icons"] = icons_opt
    if orientation_opt:
        manifest_opt["orientation"] = orientation_opt
    if screenOn_opt:
        manifest_opt["xwalk_android_keep_screen_on"] = screenOn_opt
    if animatableView_opt:
        manifest_opt["xwalk_android_animatable_view"] = animatableView_opt
    if webp_opt:
        manifest_opt["xwalk_android_webp"] = webp_opt
    if shortName_opt:
        manifest_opt["short_name"] = shortName_opt
    if permissions_opt:
        manifest_opt["xwalk_android_permissions"] = permissions_opt 

    manifest_opt = json.JSONEncoder().encode(manifest_opt)

    if utils.safelyGetValue(build_json, "apk-type") == "MANIFEST":
        pack_cmd = "crosswalk-pkg %s --crosswalk=%s " \
                   "-p android --targets=\"%s\" %s %s" % (
                       mode_opt, CROSSWALK_VERSION, arch_opt, common_opts,
                       app_src)
    else:
        pack_cmd = "crosswalk-pkg %s --crosswalk=%s --manifest='%s' " \
                   "-p android --targets=\"%s\" %s %s" % (
                       mode_opt, CROSSWALK_VERSION, manifest_opt, arch_opt,
                       common_opts, app_src)

    orig_dir = os.getcwd()
    os.chdir(os.path.join(BUILD_ROOT))
    if not utils.doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    files = glob.glob(os.path.join(BUILD_ROOT, "*.apk"))
    if files:
        rename_app_name = utils.safelyGetValue(build_json, "app-name")
        if not rename_app_name:
            rename_app_name = getNameById(files[0])
        if not utils.doCopy(files[0], os.path.join(app_dest, "%s.apk" % rename_app_name)):
            os.chdir(orig_dir)
            return False
    else:
        LOG.error("Fail to find the apk file")
        os.chdir(orig_dir)
        return False

    os.chdir(orig_dir)
    return True
