#!/usr/bin/env python
# coding=utf-8
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
#         Li, Hao<haox.li@intel.com>

import sys
import os
import re
import os.path
import commands
import subprocess
import shutil

from log import *
reload(sys)
sys.setdefaultencoding('utf-8')

SCRIPT_PATH = os.path.realpath(__file__)
CONST_PATH = os.path.dirname(SCRIPT_PATH)
DEST_DIR = "/work/webapi/ww/ww43/crosswalk-test-suite/webapi/tct-webgl-nonw3c-tests/webgl/khronos"
ORIGIN_DIR = "/work/webapi/ww/ww43/KhronosGroup/WebGL/conformance-suites/1.0.2"
ORIGIN_TMP= ORIGIN_DIR + "_tmp"

global LOG
LOG = Log.getLogger("logger")
LOG.setLevel(logging.DEBUG)


def doCMD(cmd):
    # Do not need handle timeout in this short script, let tool do it
    LOG.info("-->> \"%s\"" % cmd)
    output = []
    cmd_return_code = 1
    cmd_proc = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

    while True:
        output_line = cmd_proc.stdout.readline().strip("\r\n")
        cmd_return_code = cmd_proc.poll()
        if output_line == '' and cmd_return_code is not None:
            break
        sys.stdout.write("%s\n" % output_line)
        sys.stdout.flush()
        output.append(output_line)

    return (cmd_return_code, output)


def getOptimum(output, expect):
    optimum = ""
    if len(output) == 1:
        optimum = output[0]
    else:
        for line in output:
            if line.endswith(expect):
                optimum = line
    return optimum


def search():
    # Clear envrionment
    if os.path.exists(ORIGIN_TMP):
        shutil.rmtree(ORIGIN_TMP)
    shutil.copytree(ORIGIN_DIR, ORIGIN_TMP)
    # Access search dir
    os.chdir(ORIGIN_TMP)
    not_found_list = []
    # Search all files and directory
    for root,dirs,files in os.walk(DEST_DIR):
        for f in files:
            dest_path = root + os.sep + f
            ff = dest_path.replace(DEST_DIR + os.sep, "")
            cmd = "find -name %s" % f
            (return_code, output) = doCMD(cmd)
            if output[0] == "":
                # Cannot find file
                not_found_list.append(ff)
                #LOG.warning(">>>> Not found: " + dest_path)
            else:
                # Found
                origin_file = getOptimum(output, ff) if getOptimum(output, ff) != ""\
                                                           else getOptimum(output, f)
                origin_path = ORIGIN_TMP + os.sep + origin_file
                LOG.info(">>>> Found: " + origin_path)
                # Update found origin file to dest directory
                shutil.copyfile(origin_path, dest_path)
                os.remove(origin_path)
                # Replace resource in copyed {dest_path}
                with open(dest_path) as fb:
                    d = fb.read()
                    rewrited = False
                    # Replace all '../' to './'
                    if d.find("../resources/"):
                        d = re.sub(r'\.\./.*?resources/', './resources/', d)
                        rewrited = True
                    if d.find("../unit."):
                        d = re.sub(r'\.\./.*?unit.', './resources/unit.', d)
                        rewrited = True
                    if d.find("../util."):
                        d = re.sub(r'\.\./.*?util.', './resources/util.', d)
                        rewrited = True
                    if rewrited:
                        newfile = open(dest_path, "w+")
                        newfile.write(d)
                        newfile.close()
    for items in not_found_list:
        LOG.warning(">>>> Not found in origin directory: " + items)


def main():
    search()


if __name__ == '__main__':
    main()







