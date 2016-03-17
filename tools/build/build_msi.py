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
#         Zhu, Yongyong <yongyongx.zhu@intel.com>

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
import varshop
import utils
from optparse import OptionParser

global LOG
LOG = utils.getLogger("build_msi")

def packMsi(build_json=None, app_src=None, app_dest=None, app_name=None):

    if os.path.exists(os.path.join(app_src, "icon.png")):
        if not utils.doCopy(os.path.join(app_src, "icon.png"),
                os.path.join(app_src, "icon.ico")):
            return False

    pkg_name = "org.xwalk." + app_name.replace("-", "")

    BUILD_PARAMETERS = varshop.getValue("BUILD_PARAMETERS")
    BUILD_ROOT = varshop.getValue("BUILD_ROOT")
    BUILD_ROOT_SRC = varshop.getValue("BUILD_ROOT_SRC")
    BUILD_TIME= varshop.getValue("BUILD_TIME")
    CROSSWALK_VERSION = varshop.getValue("CROSSWALK_VERSION")
    DEFAULT_CMD_TIMEOUT= varshop.getValue("DEFAULT_CMD_TIMEOUT")
    PKG_MODES= varshop.getValue("PKG_MODES")
    PKG_ARCHS= varshop.getValue("PKG_ARCHS")
    get_real_arch = {"x86": "x86",
                     "x86_64": "x86_64",
                     "arm": "armeabi-v7a",
                     "arm64": "arm64-v8a"}

    windows_opt = ""
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

    tmp_opt = utils.safelyGetValue(build_json, "google-api-key")
    if tmp_opt:
        source_keys_file = os.path.join(BUILD_PARAMETERS.pkgpacktools, "resources", "keys", "crosswalk-app-tools-keys.json")
        userName = os.getenv("USERNAME")
        dest_keys_file = "C:\\Users\\%s\\.crosswalk-app-tools-keys.json" % userName
        if not utils.doCopy(
                source_keys_file,
                dest_keys_file):
            return False
        windows_opt = "-w google-api-key:%s" % tmp_opt

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
    #common_opts = common_opts.replace(' -r ','')

    tmp_opt = utils.safelyGetValue(build_json, "apk-ext-opt")
    if tmp_opt:
        ext_opt = tmp_opt

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

    if not arch_opt:
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
        icon_opt = "icon.ico"
        icon_set = {}
        icon_set["src"] = icon_opt
        icon_set["sizes"] = "72x72"
        icons_opt = [icon_set]

    manifest_opt = {}
    manifest_opt["name"] = "%s" % app_name
    if pkg_opt:
        manifest_opt["xwalk_package_id"] = "org.xwalk.%s" % pkg_opt
    else:
        manifest_opt["xwalk_package_id"] = pkg_name
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

    manifest_opt = manifest_opt.replace("\"", "\"\"\"")
    manifest_opt = manifest_opt.replace("\"\"\"src\"\"\"", "\"\"src\"\"")
    manifest_opt = manifest_opt.replace("\"\"\"icon.ico\"\"\"", "\"\"icon.ico\"\"")
    manifest_opt = manifest_opt.replace("\"\"\"sizes\"\"\"", "\"\"sizes\"\"")
    manifest_opt = manifest_opt.replace("\"\"\"72x72\"\"\"", "\"\"72x72\"\"")
    manifest_opt = manifest_opt.replace("{\"\"\"", "\"{\"\"\"")
    manifest_opt = manifest_opt.replace("\"\"\"}", "\"\"\"}\"")
    print manifest_opt

    orig_dir = os.getcwd()
    if not os.path.exists(
           os.path.join(BUILD_ROOT, "crosswalk-%s.zip" % CROSSWALK_VERSION)):
        if not utils.doCopy(os.path.join(BUILD_PARAMETERS.pkgpacktools, "crosswalk-%s.zip" % CROSSWALK_VERSION),
                      os.path.join(BUILD_ROOT, "crosswalk-%s.zip" % CROSSWALK_VERSION)):
            return False

    os.chdir(BUILD_ROOT)
    crosswalk_app_tools = os.getenv("CROSSWALK_APP_TOOLS")
    if crosswalk_app_tools == None:
        LOG.error("Pls add an environment variable named 'CROSSWALK_APP_TOOLS', and set the crosswalk-app-tools path to this environment variable")
        os.chdir(orig_dir)
        return False

    if not utils.safelyGetValue(build_json, "apk-type") or utils.safelyGetValue(build_json, "apk-type") != "MANIFEST":
        if os.path.exists(os.path.join(app_src, "manifest.json")):
            if not utils.doRemove([os.path.join(app_src, "manifest.json")]):
                os.chdir(orig_dir)
                return False

        build_cmd = "node %s/src/crosswalk-pkg -c crosswalk-%s.zip --platforms=windows -m  %s %s %s %s" \
            % (crosswalk_app_tools, CROSSWALK_VERSION, manifest_opt, common_opts, windows_opt, app_src)
    else:
        build_cmd = "node %s/src/crosswalk-pkg -c crosswalk-%s.zip --platforms=windows %s %s %s" % (crosswalk_app_tools, CROSSWALK_VERSION, common_opts, windows_opt, app_src)


    print build_cmd
    if not utils.doCMD(build_cmd, DEFAULT_CMD_TIMEOUT):
        LOG.error("Fail to pack: %s" % build_cmd)


    # After build successfully, copy the .msi file from project_root to app_dest
    time.sleep(5)
    files = glob.glob(os.path.join(BUILD_ROOT, "*.msi"))
    if not utils.doCopy(
            files[0],
            os.path.join(app_dest, "%s.msi" % app_name)):
        return False

    if not utils.doRemove([files[0]]):
        return False

    os.chdir(orig_dir)
    return True

