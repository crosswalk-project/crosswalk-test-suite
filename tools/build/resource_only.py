#!/usr/bin/env python
#
# Copyright (c) 2016 Intel Corporation.
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
#         Li, Hao <haox.li@intel.com>

import os
import json
import glob
import sys
import utils

ROOT_DIR = os.getcwd()

def copy_resource(pkgtype):
    try:
        json_file = os.path.join(ROOT_DIR, "suite.json")
        if not os.path.exists(json_file):
            print "%s does not exist" % json_file
            sys.exit(1)

        print ">>>> suite.json: %s" % json_file
        print ">>>>   pkg type: %s" % pkgtype

        suite_json = None
        pkg_json = None
        try:
            with open(json_file, "rt") as suite_json_file:
                suite_json_raw = suite_json_file.read()
                suite_json_file.close()
                suite_json = json.loads(suite_json_raw)
        except Exception as e:
            print "Fail to read json file: %s, exit ..." % json_file
            sys.exit(1)

        all_pkg_string = suite_json["pkg-list"].keys()
        for i_pkg in all_pkg_string:
            i_pkg_list = i_pkg.strip().split(",")
            if pkgtype in i_pkg_list:
                pkg_json = suite_json["pkg-list"][i_pkg]
        if pkg_json is None:
            print "No %s type config in %s" % (pkgtype, json_file)

        # package copylist
        if "copylist" in pkg_json:
            main_copylist = pkg_json["copylist"]
            for i_s_key in main_copylist.keys():
                src_path = os.path.join(ROOT_DIR, i_s_key).replace("PACK-TOOL-ROOT", "../../tools")
                dest_path = os.path.join(ROOT_DIR, main_copylist[i_s_key])
                utils.doCopy(src_path, dest_path)

        # pkg-app copylist
        if "pkg-app" in pkg_json:
            pkg_app_json = pkg_json["pkg-app"]
            if "copylist" in pkg_app_json:
                pkg_app_copylist = pkg_app_json["copylist"]
                for i_s_key in pkg_app_copylist.keys():
                    src_path = os.path.join(ROOT_DIR, i_s_key).replace("PACK-TOOL-ROOT", "../../tools")
                    dest_path = os.path.join(ROOT_DIR, pkg_app_copylist[i_s_key])
                    utils.doCopy(src_path, dest_path)

        # subapp-list copylist
        if "subapp-list" in pkg_json:
            subapp_list_json = pkg_json["subapp-list"]
            for subapp_str in subapp_list_json.keys():
                subapp_json = subapp_list_json[subapp_str]
                subapp_path = os.path.join(ROOT_DIR, subapp_str)
                if "copylist" in subapp_json and os.path.exists(subapp_path):
                    subapp_copylist = subapp_json["copylist"]
                    for i_s_key in subapp_copylist.keys():
                        src_path = os.path.join(subapp_path, i_s_key).replace("PACK-TOOL-ROOT", "../../tools")
                        dest_path = os.path.join(subapp_path, subapp_copylist[i_s_key])
                        utils.doCopy(src_path, dest_path)
    except Exception as e:
        print "Get Exception: %s, exit ..." % e
        sys.exit(1)


