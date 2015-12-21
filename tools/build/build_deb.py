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
#         Xu, Kang <kangx.xu@intel.com>

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
LOG = utils.getLogger("build_deb")

def packDeb(build_json=None, app_src=None, app_dest=None, app_name=None):
    BUILD_PARAMETERS = varshop.getValue("BUILD_PARAMETERS")
    BUILD_ROOT = varshop.getValue("BUILD_ROOT")
    BUILD_ROOT_SRC = varshop.getValue("BUILD_ROOT_SRC")
    BUILD_TIME= varshop.getValue("BUILD_TIME")
    DEFAULT_CMD_TIMEOUT= varshop.getValue("DEFAULT_CMD_TIMEOUT")
    app_name = app_name.replace("-", "_")

    files = glob.glob(os.path.join(BUILD_ROOT, "*.deb"))
    if files:
        if not utils.doRemove(files):
            return False

    url_opt = ""
    pkg_opt = ""

    tmp_opt = utils.safelyGetValue(build_json, "apk-pkg-opt")
    if tmp_opt:
        pkg_opt = "%s" % tmp_opt

    tmp_opt = utils.safelyGetValue(build_json, "apk-url-opt")
    if tmp_opt:
        url_opt = "%s" % tmp_opt


    manifest_opt = {}
    manifest_opt["name"] = "%s" % app_name
    print app_name + "test"
    if pkg_opt:
        manifest_opt["xwalk_package_id"] = "org.xwalk.%s" % pkg_opt
    else:
        manifest_opt["xwalk_package_id"] = "org.xwalk.%s" % app_name
    if url_opt:
        manifest_opt["start_url"] = url_opt
    else:
        manifest_opt["start_url"] = "index.html"
    manifest_opt = json.JSONEncoder().encode(manifest_opt)

    if utils.safelyGetValue(build_json, "apk-type") == "MANIFEST":
        pack_cmd = "crosswalk-pkg -p deb %s" % app_src
    else:
        pack_cmd = "crosswalk-pkg --manifest='%s' -p deb %s" % (manifest_opt, app_src)

    orig_dir = os.getcwd()
    os.chdir(os.path.join(BUILD_ROOT))
    if not utils.doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT * 1.5):
        os.chdir(orig_dir)
        return False

    files = glob.glob(os.path.join(BUILD_ROOT, "*.deb"))
    if files:
        rename_app_name = utils.safelyGetValue(build_json, "app-name")
        if not rename_app_name:
            rename_app_name = app_name

        if not utils.doCopy(files[0], os.path.join(app_dest, "%s.deb" % rename_app_name)):
            os.chdir(orig_dir)
            return False
    else:
        LOG.error("Fail to find the deb file")
        os.chdir(orig_dir)
        return False

    os.chdir(orig_dir)
    return True
