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
LOG = utils.getLogger("build_tizen")

def packWGT(build_json=None, app_src=None, app_dest=None, app_name=None):
    BUILD_PARAMETERS = varshop.getValue("BUILD_PARAMETERS")
    BUILD_ROOT = varshop.getValue("BUILD_ROOT")
    DEFAULT_CMD_TIMEOUT= varshop.getValue("DEFAULT_CMD_TIMEOUT")
    if not utils.zipDir(app_src, os.path.join(app_dest, "%s.wgt" % app_name)):
        return False

    if BUILD_PARAMETERS.signature == True:
        if utils.safelyGetValue(build_json, "sign-flag") == "true":
            if not os.path.exists(os.path.join(BUILD_ROOT, "signing")):
                if not utils.doCopy(
                        os.path.join(BUILD_PARAMETERS.pkgpacktools, "signing"),
                        os.path.join(BUILD_ROOT, "signing")):
                    return False
            signing_cmd = "%s --dist platform %s" % (
                os.path.join(BUILD_ROOT, "signing", "sign-widget.sh"),
                os.path.join(app_dest, "%s.wgt" % app_name))
            if not utils.doCMD(signing_cmd, DEFAULT_CMD_TIMEOUT):
                return False

    return True


def packXPK(build_json=None, app_src=None, app_dest=None, app_name=None):
    BUILD_PARAMETERS = varshop.getValue("BUILD_PARAMETERS")
    BUILD_ROOT = varshop.getValue("BUILD_ROOT")
    DEFAULT_CMD_TIMEOUT= varshop.getValue("DEFAULT_CMD_TIMEOUT")
    pack_tool = os.path.join(BUILD_ROOT, "make_xpk.py")
    if not os.path.exists(pack_tool):
        if not utils.doCopy(
                os.path.join(BUILD_PARAMETERS.pkgpacktools, "make_xpk.py"),
                pack_tool):
            return False
    orig_dir = os.getcwd()
    os.chdir(BUILD_ROOT)
    if os.path.exists("key.file"):
        if not utils.doRemove(["key.file"]):
            os.chdir(orig_dir)
            return False

    key_file = utils.safelyGetValue(build_json, "key-file")
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
    if not utils.doCMD(pack_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    os.chdir(orig_dir)
    return True
