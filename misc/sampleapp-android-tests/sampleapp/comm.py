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
#         Cici,Li<cici.x.li@intel.com>
#         Li, Hao<haox.li@intel.com>

import unittest
import os
import sys
import commands
import shutil
import json
import glob
reload(sys)
sys.setdefaultencoding("utf-8")

script_path = os.path.realpath(__file__)
const_path = os.path.dirname(script_path)
sample_src_pref = "/tmp/crosswalk-samples/"
build_app_dest = const_path + "/../testapp/"
pack_tools = const_path + "/../tools/crosswalk/"
index_path = "index.html"


def setUp():
    global ARCH, MODE, device

    device = os.environ.get('DEVICE_ID')

    if not device:
        print (" get device id error\n")
        sys.exit(1)


    tests_conf_json = os.path.join(const_path, "../tests-conf.json")
    if os.path.exists(tests_conf_json):
        with open(tests_conf_json) as tests_conf_file:
            tests_conf_str = tests_conf_file.read()
            tests_conf_file.close()
            tests_conf = json.loads(tests_conf_str)
            ARCH = tests_conf.get("arch")
            MODE = tests_conf.get("mode")
    else:
        print ("Not find tests.conf.json\n")
        sys.exit(1)


def pack(cmd, appname, self):
    setUp()
    os.chdir(build_app_dest)
    print "Generate APK %s ----------------> START" % appname
    print cmd
    packstatus = commands.getstatusoutput(cmd)
    self.assertEquals(0, packstatus[0])
    print "\nGenerate APK %s ----------------> OK\n" % appname
    apk_file = commands.getstatusoutput("ls %s| grep %s" % (build_app_dest, appname))[1]
    self.assertTrue(apk_file.endswith(".apk"))
    os.chdir("../..")
