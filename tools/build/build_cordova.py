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
LOG = utils.getLogger("build_cordova")

def packCordova(
        build_json=None, app_src=None, app_dest=None, app_name=None):
    BUILD_PARAMETERS = varshop.getValue("BUILD_PARAMETERS")
    BUILD_ROOT = varshop.getValue("BUILD_ROOT")
    CROSSWALK_BRANCH= varshop.getValue("CROSSWALK_BRANCH")
    CROSSWALK_VERSION= varshop.getValue("CROSSWALK_VERSION")
    DEFAULT_CMD_TIMEOUT= varshop.getValue("DEFAULT_CMD_TIMEOUT")
    app_name = app_name.replace("-", "_")
    project_root = os.path.join(BUILD_ROOT, app_name)

    output = commands.getoutput("cordova -v")
    output_version = int(output[0])
    if output_version < 5:
        LOG.error(
            "Cordova build requires the latest Cordova CLI, and must >= 5.0.0, install with command: '$ sudo npm install cordova -g'")
        return False

    plugin_tool = os.path.join(BUILD_ROOT, "cordova_plugins")
    plugin_source = os.path.join(BUILD_PARAMETERS.pkgpacktools, "cordova_plugins")
    if not os.path.exists(plugin_tool):
        if os.path.exists(plugin_source):
            if not utils.doCopy(
                    os.path.join(BUILD_PARAMETERS.pkgpacktools, "cordova_plugins"),
                    plugin_tool):
                return False
    extra_plugins = os.path.join(BUILD_ROOT, "extra_plugins")
    if os.path.exists(extra_plugins):
        if not utils.doCopy(extra_plugins, plugin_tool):
            return False

    orig_dir = os.getcwd()
    os.chdir(BUILD_ROOT)
    pack_cmd = "cordova create %s org.xwalk.%s %s" % (
        app_name, app_name, app_name)
    if not utils.doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    version_opt = utils.safelyGetValue(build_json, "apk-version-opt")
    if version_opt:
        utils.replaceUserString(
            project_root,
            'config.xml',
            'id="org.xwalk.%s" version="0.0.1"' % app_name,
            'id="org.xwalk.%s" version="%s"' %
            (app_name, version_opt))

    # Set activity name as app_name
    utils.replaceUserString(
        project_root,
        'config.xml',
        '<widget',
        '<widget android-activityName="%s"' %
        app_name)
    # Workaround for XWALK-3679
    utils.replaceUserString(
        project_root,
        'config.xml',
        '</widget>',
        '    <allow-navigation href="*" />\n</widget>')

    if not utils.doRemove([os.path.join(project_root, "www")]):
        return False
    if not utils.doCopy(app_src, os.path.join(project_root, "www")):
        os.chdir(orig_dir)
        return False

    os.chdir(project_root)
    pack_cmd = "cordova platform add android"
    if not utils.doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    pkg_mode_tmp = "shared"
    if BUILD_PARAMETERS.pkgmode == "embedded":
        pkg_mode_tmp = "core"

    xwalk_version = "%s" % CROSSWALK_VERSION
    if CROSSWALK_BRANCH == "beta":
        xwalk_version = "org.xwalk:xwalk_%s_library_beta:%s" % (pkg_mode_tmp, CROSSWALK_VERSION)

    webview_plugin_name = "cordova-plugin-crosswalk-webview"
    plugin_dirs = os.listdir(plugin_tool)
    for i_dir in plugin_dirs:
        install_variable_cmd = ""
        i_plugin_dir = os.path.join(plugin_tool, i_dir)
        plugin_crosswalk_source = i_plugin_dir
        if i_dir == webview_plugin_name:
            if BUILD_PARAMETERS.packtype == "npm":
                plugin_crosswalk_source = webview_plugin_name
            install_variable_cmd = "--variable XWALK_MODE=\"%s\" --variable XWALK_VERSION=\"%s\"" \
                    % (BUILD_PARAMETERS.pkgmode, xwalk_version)

        plugin_install_cmd = "cordova plugin add %s %s" % (plugin_crosswalk_source, install_variable_cmd)
        if not utils.doCMD(plugin_install_cmd, DEFAULT_CMD_TIMEOUT):
            os.chdir(orig_dir)
            return False

    ANDROID_HOME = "echo $(dirname $(dirname $(which android)))"
    os.environ['ANDROID_HOME'] = commands.getoutput(ANDROID_HOME)

    apk_name_arch = "armv7"
    pack_arch_tmp = "arm"
    if BUILD_PARAMETERS.pkgarch and BUILD_PARAMETERS.pkgarch != "arm":
        apk_name_arch = BUILD_PARAMETERS.pkgarch
        if BUILD_PARAMETERS.pkgarch == "x86":
            pack_arch_tmp = "x86"
        elif BUILD_PARAMETERS.pkgarch == "x86_64":
            pack_arch_tmp = "x86 --xwalk64bit"
        elif BUILD_PARAMETERS.pkgarch == "arm64":
            pack_arch_tmp = "arm --xwalk64bit"

    pack_cmd = "cordova build android -- --gradleArg=-PcdvBuildArch=%s" % pack_arch_tmp

    if not utils.doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    outputs_dir = os.path.join(
        project_root,
        "platforms",
        "android",
        "build",
        "outputs",
        "apk")

    cordova_tmp_path = os.path.join(
        outputs_dir,
        "android-%s-debug.apk" %
            apk_name_arch)
    if not os.path.exists(cordova_tmp_path):
        cordova_tmp_path = os.path.join(
            outputs_dir,
            "%s-%s-debug.apk" %
            (app_name, apk_name_arch))
        if not os.path.exists(cordova_tmp_path):
            cordova_tmp_path = os.path.join(
                outputs_dir,
                "android-debug.apk")
            if not os.path.exists(cordova_tmp_path):
                cordova_tmp_path = os.path.join(
                    outputs_dir,
                    "%s-debug.apk" %
                    app_name)
    if not utils.doCopy(
            cordova_tmp_path, os.path.join(app_dest, "%s.apk" % app_name)):
        os.chdir(orig_dir)
        return False
    os.chdir(orig_dir)
    return True
