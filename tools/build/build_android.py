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

def packAPK(build_json=None, app_src=None, app_dest=None, app_name=None):
    BUILD_PARAMETERS = varshop.getValue("BUILD_PARAMETERS")
    BUILD_ROOT = varshop.getValue("BUILD_ROOT")
    BUILD_ROOT_SRC = varshop.getValue("BUILD_ROOT_SRC")
    BUILD_TIME= varshop.getValue("BUILD_TIME")
    DEFAULT_CMD_TIMEOUT= varshop.getValue("DEFAULT_CMD_TIMEOUT")
    PKG_MODES= varshop.getValue("PKG_MODES")
    PKG_ARCHS= varshop.getValue("PKG_ARCHS")
    app_name = app_name.replace("-", "_")

    if not os.path.exists(os.path.join(BUILD_ROOT, "crosswalk")):
        if not utils.doCopy(
                os.path.join(BUILD_PARAMETERS.pkgpacktools, "crosswalk"),
                os.path.join(BUILD_ROOT, "crosswalk")):
            return False

    files = glob.glob(os.path.join(BUILD_ROOT, "crosswalk", "*.apk"))
    if files:
        if not utils.doRemove(files):
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

    common_opts = utils.safelyGetValue(build_json, "apk-common-opts")
    if common_opts is None:
        common_opts = ""

    tmp_opt = utils.safelyGetValue(build_json, "apk-ext-opt")
    if tmp_opt:
        ext_opt = "--extensions='%s'" % os.path.join(BUILD_ROOT_SRC, tmp_opt)

    tmp_opt = utils.safelyGetValue(build_json, "apk-version-opt")
    if tmp_opt:
        version_opt = "--app-version='%s'" % ''.join([tmp_opt, BUILD_TIME])
        version_code_opt = "--app-versionCode='%s'" % ''.join(
            ['6', BUILD_TIME])

    tmp_opt = utils.safelyGetValue(build_json, "apk-fullscreen-opt")
    if tmp_opt:
        ext_opt = "--%s" % tmp_opt

    tmp_opt = utils.safelyGetValue(build_json, "apk-pkg-opt")
    if tmp_opt:
        pkg_opt = "--package='org.xwalk.%s'" % tmp_opt

    tmp_opt = utils.safelyGetValue(build_json, "apk-cmd-opt")
    if tmp_opt:
        cmd_opt = "--xwalk-command-line='%s'" % tmp_opt

    tmp_opt = utils.safelyGetValue(build_json, "apk-url-opt")
    if tmp_opt:
        url_opt = "--app-url='%s'" % tmp_opt

    tmp_opt = utils.safelyGetValue(build_json, "apk-mode-opt")
    if tmp_opt:
        if tmp_opt in PKG_MODES:
            mode_opt = "--mode=%s" % tmp_opt
        else:
            LOG.error("Got wrong app mode: %s" % tmp_opt)
            return False
    else:
        mode_opt = "--mode=%s" % BUILD_PARAMETERS.pkgmode

    tmp_opt = utils.safelyGetValue(build_json, "apk-arch-opt")
    if tmp_opt:
        if tmp_opt in PKG_ARCHS:
            arch_opt = "--arch=%s" % tmp_opt
        else:
            LOG.error("Got wrong app arch: %s" % tmp_opt)
            return False
    else:
        arch_opt = "--arch=%s" % BUILD_PARAMETERS.pkgarch

    tmp_opt = utils.safelyGetValue(build_json, "apk-icon-opt")
    if tmp_opt:
        icon_opt = "--icon=%s" % tmp_opt
    elif tmp_opt == "":
        icon_opt = ""
    else:
        icon_opt = "--icon=%s/icon.png" % app_src

    if utils.safelyGetValue(build_json, "apk-type") == "MANIFEST":
        pack_cmd = "python make_apk.py --package=org.xwalk.%s " \
            "--manifest=%s/manifest.json  %s %s %s %s %s %s %s %s %s" % (
                app_name, app_src, mode_opt, arch_opt,
                ext_opt, cmd_opt, common_opts, version_opt, pkg_opt, version_code_opt, fullscreen_opt)
    elif utils.safelyGetValue(build_json, "apk-type") == "HOSTEDAPP":
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
    if not utils.doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    files = glob.glob(os.path.join(BUILD_ROOT, "crosswalk", "*.apk"))
    if files:
        if not utils.doCopy(files[0], os.path.join(app_dest, "%s.apk" % app_name)):
            os.chdir(orig_dir)
            return False
    else:
        LOG.error("Fail to find the apk file")
        os.chdir(orig_dir)
        return False

    os.chdir(orig_dir)
    return True
