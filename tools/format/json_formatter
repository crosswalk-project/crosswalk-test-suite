#!/usr/bin/env python
#
# Copyright (c) 2014 Intel Corporation.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of works must retain the original copyright notice, this
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright notice
#   , this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
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

import sys
import os
import json
import logging
from optparse import OptionParser

VERSION = "v0.1"
LOG = None
LOG_LEVEL = logging.DEBUG
FORMAT_ERROR_STATUS = False


class color_formatter(logging.Formatter):

    def __init__(self, msg):
        logging.Formatter.__init__(self, msg)

    def format(self, record):
        red, green, yellow, blue = range(4)
        colors = {'INFO': green, 'DEBUG': blue,
                  'WARNING': yellow, 'ERROR': red}
        msg = record.msg
        levelname = record.levelname
        if levelname in colors:
            msg_color = "\033[0;%dm" % (
                31 + colors[levelname]) + msg + "\033[0m"
            record.msg = msg_color

        return logging.Formatter.format(self, record)


def get_file_list(format_list=None, recursive=False, symlinks=True):
    global FORMAT_ERROR_STATUS
    file_list = []
    for format_item in format_list:
        if not os.path.exists(format_item):
            LOG.error("%s is not existing" % format_item)
            FORMAT_ERROR_STATUS = True
            continue
        elif os.path.islink(format_item):
            if symlinks:
                format_item = os.path.join(
                    os.path.dirname(format_item),
                    os.readlink(format_item))
            else:
                LOG.warning("%s is link, skip it" % format_item)
                continue

        if os.path.isdir(format_item):
            if not recursive:
                LOG.error("%s is not a file" % format_item)
                FORMAT_ERROR_STATUS = True
                continue
            for dirpath, dirnames, files in os.walk(format_item):
                for i_file in files:
                    if i_file.endswith(".json"):
                        i_file_path = os.path.join(dirpath, i_file)
                        if os.path.islink(i_file_path):
                            if symlinks:
                                file_list = file_list + [
                                    os.path.join(
                                        os.path.dirname(i_file_path),
                                        os.readlink(i_file_path))]
                            else:
                                LOG.warning(
                                    "%s is link, skip it" %
                                    i_file_path)
                                continue
                        else:
                            file_list = file_list + [i_file_path]
        else:
            file_list = file_list + [format_item]

    if not file_list:
        LOG.error("No json file found for formatting ...")
    return file_list


def main():
    global LOG
    global FORMAT_ERROR_STATUS

    LOG = logging.getLogger("json-formater")
    LOG.setLevel(LOG_LEVEL)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(LOG_LEVEL)
    stream_formatter = color_formatter("%(message)s")
    stream_handler.setFormatter(stream_formatter)
    LOG.addHandler(stream_handler)

    try:
        usage = "Usage: \n\tjson_formatter -i file.json\n\t" \
                "json_formatter -r json_dir\n\tjson_formatter file.json"
        opts_parser = OptionParser(usage=usage, version=VERSION)
        opts_parser.add_option(
            "-i",
            "--in-place",
            dest="inplace",
            action="store_true",
            help="make changes to json files in place")
        opts_parser.add_option(
            "-r",
            "--recursive",
            dest="recursive",
            action="store_true",
            help="run recursively over directories, "
                 "force the formatter to use \"--in-place\"")
        opts_parser.add_option(
            "-n",
            "--indent",
            dest="indent",
            action="store",
            type="int",
            help="json indent, default value is 4")
        opts_parser.add_option(
            "-u",
            "--unsort-keys",
            dest="unsortkeys",
            action="store_true",
            help="not sort json keys")
        opts_parser.add_option(
            "-s",
            "--symlinks",
            dest="symlinks",
            action="store_true",
            help="follow symlinks")
        opts_parser.add_option(
            "-m",
            "--minimize",
            dest="minimize",
            action="store_true",
            help="minimize the json file")

        if len(sys.argv) == 1:
            sys.argv.append("-h")
        (options, args) = opts_parser.parse_args()
    except Exception as e:
        LOG.error("Got options error: %s" % e)
        sys.exit(1)

    files_list = []
    format_list = [os.getcwd()]

    if options.symlinks:
        follow_symlinks = True
    else:
        follow_symlinks = False

    if args:
        format_list = args

    if options.recursive:
        options.inplace = True
        follow_recursive = True
    else:
        follow_recursive = False

    json_indent = 4
    if options.indent:
        json_indent = options.indent

    json_sort = True
    if options.unsortkeys:
        json_sort = False

    files_list = get_file_list(
        format_list,
        recursive=follow_recursive,
        symlinks=follow_symlinks)
    for i_file in files_list:
        LOG.info("-->> Formatting %s" % i_file)
        try:
            with open(i_file, "rt") as original_json_file:
                original_json_raw = original_json_file.read()
                original_json_file.close()
                original_json = json.loads(original_json_raw)
                if options.minimize:
                    updated_json_tmp = json.dumps(
                        original_json,
                        separators=(',', ':'),
                        sort_keys=json_sort)
                else:
                    updated_json_tmp = json.dumps(
                        original_json,
                        indent=json_indent,
                        sort_keys=json_sort)
                updated_json = None
                for i_line in updated_json_tmp.splitlines():
                    i_line = i_line.rstrip()
                    if i_line:
                        if updated_json:
                            updated_json = "%s\n%s" % (updated_json, i_line)
                        else:
                            updated_json = i_line
                if not updated_json:
                    LOG.error("Got empty json string from %s" % i_file)
                    FORMAT_ERROR_STATUS = True
                    continue
                if options.inplace:
                    os.rename(i_file, "%s.json-formatter" % i_file)
                    try:
                        with open(i_file, "w") as original_json_file:
                            original_json_file.write(updated_json)
                            original_json_file.close()
                            os.remove("%s.json-formatter" % i_file)
                    except Exception as e:
                        LOG.error("Fail to format %s: %s" % (i_file, e))
                        FORMAT_ERROR_STATUS = True
                        if os.path.exists(i_file):
                            os.remove(i_file)
                        os.rename("%s.json-formatter" % i_file, i_file)
                else:
                    print updated_json
        except Exception as e:
            LOG.error("Fail to format %s: %s" % (i_file, e))
            FORMAT_ERROR_STATUS = True
            continue
        LOG.info("Done")

    if FORMAT_ERROR_STATUS:
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()
