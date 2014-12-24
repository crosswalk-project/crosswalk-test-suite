#!/usr/bin/env python
#
# Copyright (c) 2014 Intel Corporation.
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
#         Chen, Xi <xix.a.chen@intel.com>

import json
import os
import sys
import shutil
from optparse import OptionParser

#
# Usage: python copy.py  [-j /path/to/resources.json] [-n specify the file or dir you want to copy,please split them by comma]
#
# This script is used to copy common resource files to each suite as configured in resources.json.
#
# The default directory for test suite is: path/crosswalk-test-suite/webapi.
# The default directory shared files saved at is: path/crosswalk-test-suite/tools/script.
#
# Directory or a single file both can be configured in resources.json.
#
# Resources.json file is saved at path/crosswalk-test-suite/tools/script by default. You can change it by -j option.
# You can specify only copy portion of the shared files by option: -n(if more than one,please them by comma).The default is all #the shared files are all need to copy.
#


def doCopy(src, dest):
    try:
        if not os.path.exists(src):
            print "src %s does not exists." % src
            return
        if not os.path.exists(dest):
            os.mkdir(dest)
        if os.path.isfile(src):
            shutil.copy(src, dest)
        else:
            for filename in os.listdir(src):
                src_name = os.path.join(src, filename)
                shutil.copy(src_name, dest)
    except Exception as e:
        print "Get error when copy file: %s" % e


def safelyGetValue(origin_json=None, key=None):
    if origin_json and key and key in origin_json:
        return origin_json[key]
    return None


def parseJsonFile(json_file=None, node=None):
    try:
        script_path = sys.path[0]
        srcdir = os.path.join(os.path.dirname(script_path), "resources")
        destdir = os.path.dirname(os.path.dirname(script_path))
        if not json_file:
            json_file = os.path.join(srcdir, "resources.json")
        if os.path.isfile(json_file):
            with open(json_file, "rt") as config_json_file:
                config_raw = config_json_file.read()
                config_json_file.close()
                config_json = json.loads(config_raw)
                node_list = config_json.keys()
                if node:
                    tmp_list = node.split(",")
                    for element in tmp_list:
                        if not element in node_list:
                            print "The node you specify is invalid.Please input again."
                            return
                    node_list = tmp_list
                for key in node_list:
                    file_list = safelyGetValue(config_json, key)
                    if file_list:
                        for element in file_list:
                            src = os.path.join(srcdir, key)
                            dest = os.path.join(destdir, element)
                            if not os.path.exists(os.path.dirname(dest)):
                                print "Dest source does not exists: %s" % dest
                                return
                            if not os.path.exists(os.path.dirname(src)):
                                print "Src source does not exists: %s" % src
                                return
                            doCopy(src, dest)
                print "Well done!"
        else:
            print "can not find the file : %s" % json_file
    except Exception as e:
        print "Get error when parse json file: %s" % e


def main():
    try:
        usage = "Usage: python copy.py  -j /path/to/resources.json \
                 -n specify the file or dir you want to copy,please split them by comma"
        opts_parser = OptionParser(usage=usage)
        opts_parser.add_option(
            "-j",
            "--json",
            dest="json",
            help="specify the path of resources.json file saved")
        opts_parser.add_option(
            "-n",
            "--node",
            dest="node",
            help="specify the file or dir you want to copy,please split them by commma")

        (PARAMETERS, args) = opts_parser.parse_args()

        parseJsonFile(PARAMETERS.json, PARAMETERS.node)

    except Exception as e:
        print("Get wrong options: %s, exit ..." % e)
        sys.exit(1)


if __name__ == '__main__':
    main()
