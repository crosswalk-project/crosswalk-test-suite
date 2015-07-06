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
import os.path
import glob
import sys
import shutil
from optparse import OptionParser

#
# Usage: python copy.py  [-j /path/to/xxxx.json] [-s webapi-xxxx-tests]
#
# This script is used to deploy common resources to corresponding test suite and sub app as configured in json files.
#
# Json files for configure is located at /path/to/crosswalk-test-suite/tools/resources as default. You can change it by option -j like "-j /path/to/xxxx.json".
#
# Common resources will be deployed to all suites and sub apps configured in json files as default. You can deploy resources to the specified suite by option -s like "-s webapi-xxxx-tests".

def doCopy(src, dest):
    try:
        if os.path.isdir(src) and not os.path.isdir(dest):
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


def parseJsonFile(json_file=None, suite=None):
    try:
        jsons = []
        toolsdir = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        srcdir = os.path.join(toolsdir, "resources")
        destdir = os.path.dirname(toolsdir)
        if not json_file:
            jsons.extend(glob.glob(os.path.join(srcdir, "*json")))
        else:
            jsons.append(json_file)

        for json_file in jsons:
            if os.path.isfile(json_file):
                with open(json_file, "rt") as config_json_file:
                    config_raw = config_json_file.read()
                    config_json = json.loads(config_raw)
                    node_list = config_json.keys()
                    for key in node_list:
                        file_list = safelyGetValue(config_json, key)
                        if file_list:
                            for element in file_list:
                                if not suite:
                                    pass
                                elif element.find(suite) == -1:
                                    continue
                                src = os.path.join(srcdir, key)
                                dest = os.path.join(destdir, element)
                                if not os.path.exists(src):
                                    print "Src source does not exists: %s" % src
                                    return
                                doCopy(src, dest)
            else:
                print "can not find the file : %s" % json_file
        print "Well done!"
    except Exception as e:
        print "Get error when parse json file: %s" % e


def main():
    try:
        usage = "Usage: python copy.py -j /path/to/xxxx.json -n webapi-xxxx-tests"
        opts_parser = OptionParser(usage=usage)
        opts_parser.add_option(
            "-j",
            "--json",
            dest="json",
            help="specify the path to json file")
        opts_parser.add_option(
            "-s",
            "--suite",
            dest="suite",
            help="specify the suite which need to deploy common resources")

        (PARAMETERS, args) = opts_parser.parse_args()

        parseJsonFile(PARAMETERS.json, PARAMETERS.suite)
    except Exception as e:
        print "Get wrong options: %s, exit ..." % e
        sys.exit(1)

if __name__ == '__main__':
    main()
