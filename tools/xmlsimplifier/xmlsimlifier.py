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
#         Li, Hao <haox.li@intel.com>
#         Xu, Jianfeng <jianfengx.xu@intel.com>

import os
import sys
import logging
import glob
import json
import ConfigParser
import commands
import xml.etree.ElementTree as etree
from optparse import OptionParser

reload(sys)

LOG = None
LOG_LEVEL = logging.DEBUG
PARAMETERS = None
ROOT_DIR = None
PLATFORM = None
EXECUTION = None
CONFIG = None

JOIN = os.path.join
EXISTS = os.path.exists
DIRNAME = os.path.dirname
BASENAME = os.path.basename
ABSPATH = os.path.abspath
SPLIT = os.path.split

CURENT_DIR = DIRNAME(ABSPATH(__file__))
CONFIG_FILE = JOIN(CURENT_DIR, "config")
try:
    CONFIG = ConfigParser.ConfigParser()
    CONFIG.read(CONFIG_FILE)
    auto_attribute = CONFIG.get('auto', 'attribute').split(',')
    auto_description = CONFIG.get('auto', 'description').split(',')
    manual_attribute = CONFIG.get('manual', 'attribute').split(',')
    manual_description = CONFIG.get('manual', 'description').split(',')
    auto_capability =  CONFIG.get('auto', 'capability').split(',')
    manual_capability =  CONFIG.get('manual', 'capability').split(',')

except ConfigParser.Error, err:
    LOGGER.error(
        "[ Error: fail to parse version info, error: %s ]\n" % err)

class ColorFormatter(logging.Formatter):
    def __init__(self, msg):
        logging.Formatter.__init__(self, msg)

    def format(self, record):
        red, green, yellow, blue = range(4)
        colors = {'INFO': green, 'DEBUG': blue,
                  'WARNING': yellow, 'ERROR': red}
        msg = record.msg
        if msg[0] == "+":
            msg = "\33[01m" + msg[1:] + "\033[0m"
        elif msg[0] == "=":
            msg = "\33[07m" + msg + "\033[0m"
        levelname = record.levelname
        if levelname in colors:
            msg_color = "\033[0;%dm" % (
                31 + colors[levelname]) + msg + "\033[0m"
            record.msg = msg_color

        return logging.Formatter.format(self, record)


def simplify(inputfile, outputfile, plat, execu):
    try:
        ep = etree.parse(inputfile)
        suiteparent = ep.getroot()
        for suite in ep.getiterator('suite'):
            for tset in suite.getiterator('set'):
                for testcase in tset.getiterator('testcase'):
                    if (testcase.get('status') == 'approved') or (testcase.get('status') == 'ready'):
                        if (testcase.get('platform') == 'all') or (testcase.get('platform') == plat) or (testcase.get('platform') == None) or (plat == None):
                            if (testcase.get('execution_type') ==
execu) or (execu == None):
                                if testcase.get('execution_type') =='auto':
                                    for key in testcase.keys():
                                        if key not in auto_attribute:
                                            del testcase.attrib[key]
                                    removeitem(testcase,'auto')
                                if testcase.get('execution_type') =='manual':
                                    for key in testcase.keys():
                                        if key not in manual_attribute:
                                            del testcase.attrib[key]
                                    removeitem(testcase,'manual')
                            else:
                                tset.remove(testcase)
                        else:
                            tset.remove(testcase)
                    else:
                        tset.remove(testcase)

        for suite in ep.getiterator('suite'):
            for tset in suite.getiterator('set'):
                if not tset.getiterator('testcase'):
                   suite.remove(tset)     

    except IOError, err:
        print "[ no xml case found]\n"
        sys.exit(1)

    declaration_text = """<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>\n"""

    try:
        print outputfile
        with open(outputfile, 'w') as output:
            output.write(declaration_text)
            tree = etree.ElementTree(element=suiteparent)
            tree.write(output)
        cmd = """xmllint --format '%s' > '%s'""" % (outputfile, outputfile+".bak")
        xmllint = os.popen(cmd).read()
        if xmllint == "":
            os.remove(outputfile)
            os.rename(outputfile+".bak", outputfile)
            print "Finished simplified tests.xml,pls check: %s" % outputfile
        else:
            print xmllint

    except IOError, err:
        print "[ Error: create filtered total result file: %s failed, error: %s ]\n" % (outputfile, err)

def removeitem(testcase,execution_type):
    if execution_type =='auto':
        defin_description =auto_description
        defin_capability =auto_capability
    if execution_type =='manual':
        defin_description =manual_description
        defin_capability =manual_capability

    remove_case_childitem = []
    for case_child in testcase.getchildren():
        if case_child.tag in defin_description :
            remove_child_em =[]
            for child in case_child.getchildren():
                if child.tag not in defin_description:
                    remove_child_em.append(child)
            for re_item in remove_child_em:
                case_child.remove(re_item)

        elif case_child.tag  in defin_capability :
            remove_child_em =[]
            for child in case_child.getchildren():
                if child.tag not in defin_capability:
                    remove_child_em.append(child)
            for re_item in remove_child_em:
                case_child.remove(re_item)
        else:
             remove_case_childitem.append(case_child)

    for re_case_item in remove_case_childitem:
        testcase.remove(re_case_item)


def main():
    global LOG, ROOT_DIR, CONFIG_FILE
    LOG = logging.getLogger("log")
    LOG.setLevel(LOG_LEVEL)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(LOG_LEVEL)
    stream_formatter = ColorFormatter("[%(asctime)s] %(message)s")
    stream_handler.setFormatter(stream_formatter)
    LOG.addHandler(stream_handler)

    ROOT_DIR = os.getcwd()
    CONFIG_FILE = os.path.join(ROOT_DIR, "config")

    try:
        usage = "Usage: ./xmlsimplifier.py -f <file> [-o <output>] [-p <platform>] [-e <execution>]"
        opts_parser = OptionParser(usage=usage)
        opts_parser.add_option(
            "-f",
            dest="file",
            help="Specify a test definition file (tests.xml)")
        opts_parser.add_option(
            "-o",
            dest="output",
            help="Specify an output file")
        opts_parser.add_option(
            "-p",
            dest="platform",
            help="Specify a platform")
        opts_parser.add_option(
            "-e",
            dest="execution",
            help="Specify a execution type")

        if len(sys.argv) == 1:
            sys.argv.append("-h")
     
        global PARAMETERS
        (PARAMETERS, args) = opts_parser.parse_args(sys.argv[1:])

        if not PARAMETERS.output:
            PARAMETERS.output = PARAMETERS.file

        simplify(PARAMETERS.file, PARAMETERS.output, PARAMETERS.platform, PARAMETERS.execution)


    except Exception as e:
        LOG.error("Got wrong options: %s, exit ..." % e)
        sys.exit(1)


if __name__ == "__main__":
    main()
