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
#         Yang, Yunlong <yunlongx.yang@intel.com>


import os
import glob
import subprocess
import varshop
import utils

global LOG
LOG = utils.getLogger("build_extension")

def packExtension(build_json=None, app_src=None, app_dest=None, app_name=None):
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

    ext_src = ""
    ext_output = ""
    ext_jar_name = ""

    tmp_opt = utils.safelyGetValue(build_json, "apk-ext-src")
    if tmp_opt:
        ext_src = os.path.join(BUILD_ROOT_SRC, tmp_opt)
        if not os.path.exists(os.path.join(ext_src, "libs")):
            try:
                os.makedirs(os.path.join(ext_src, "libs"))
            except Exception as e:
                LOG.error("Fail to init extension libs dir: %s" % e)
                return False

    tmp_opt = utils.safelyGetValue(build_json, "apk-ext-opt")
    if tmp_opt:
        ext_output = os.path.join(app_src, tmp_opt)
        if not os.path.exists(ext_output):
            try:
                os.makedirs(ext_output)
            except Exception as e:
                LOG.error("Fail to init extension output dir: %s" % e)
                return False
        ext_jar_name = ext_output.split("/")[-1]


    if not os.path.exists(os.path.join(BUILD_ROOT, "crosswalk", "xwalk_core_library", "libs", "xwalk_core_library_java.jar")):
        return False

    if not utils.doCopy(
            os.path.join(BUILD_ROOT, "crosswalk", "xwalk_core_library", "libs", "xwalk_core_library_java.jar"),
            os.path.join(ext_src, "libs")):
        return False

    orig_dir = os.getcwd()
    os.chdir(ext_src)

    (return_code, output) = utils.doCMDWithOutput("android list target", DEFAULT_CMD_TIMEOUT)
    api_level = ""
    for line in output:
        if "API level:" in line:
            api_level = line.split(":")[1].strip()
    if not api_level:
        LOG.error("Fail to get Android API Level")
        os.chdir(orig_dir)
        return False

    android_project_cmd = "android update project --target android-%s --path %s" % (
                            api_level, ext_src)
    if not utils.doCMD(android_project_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    LOG.info("Extension release extension jar start ...")
    ant_cmd = "ant release -Dandroid.library=true"
    if not utils.doCMD(ant_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    if not os.path.exists(os.path.join(ext_src, "bin", "classes.jar")):
        LOG.error("Fail to release the extension jar file")
        os.chdir(orig_dir)
        return False

    if not utils.doCopy(
            os.path.join(ext_src, "bin", "classes.jar"),
            os.path.join(ext_output, "%s.jar" % ext_jar_name)):
        os.chdir(orig_dir)
        return False

    if not os.path.exists(os.path.join(ext_src, "%s.json" % ext_jar_name)):
        os.chdir(orig_dir)
        return False
    if not utils.doCopy(
            os.path.join(ext_src, "%s.json" % ext_jar_name),
            os.path.join(ext_output, "%s.json" % ext_jar_name)):
        os.chdir(orig_dir)
        return False

    if os.path.exists(os.path.join(ext_src, "js", "%s.js" % ext_jar_name)):
        if not utils.doCopy(
                os.path.join(ext_src, "js", "%s.js" % ext_jar_name),
                os.path.join(ext_output, "%s.js" % ext_jar_name)):
            os.chdir(orig_dir)
            return False

    os.chdir(orig_dir)
    return True
