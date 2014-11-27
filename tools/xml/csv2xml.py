#!/usr/bin/python
#encoding:utf-8

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
#         Liu, xin <xinx.liu@intel.com>

import os
import csv
import re
import sys
import platform
import logging  
import logging.handlers
from xml.etree import ElementTree

LOG = None
LOG_LEVEL = logging.DEBUG

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

def csv2full(csv_path, split_sign):
    if not os.path.isfile(csv_path):
        print '%s is not a file' % csv_path
        return
    name, ext = os.path.splitext(csv_path)
    if not ext == '.csv':
        print '%s is not a csv' % csv_path
        return
    LOG.info("+Convert csv to xml start ...")
    csv_file = file(csv_path, 'rb')
    csv_file.readline()
    reader = csv.reader(csv_file)
    csv_content = []
    for line in reader:
        csv_content.append(line)

    csv_file.close()
    suite_name = csv_content[0][16].split('/')[2]
    category_name = csv_content[0][12]
    set_name = name.split(split_sign)[-1]
    folder = os.path.dirname(csv_path)
    full_test_path = '%s%stests.full(%s).xml' % (folder, split_sign, set_name)
    make_full_test(csv_content, full_test_path, suite_name, set_name, category_name)
    LOG.info('General %s' % full_test_path)
    test_path = '%s%stests(%s).xml' % (folder, split_sign, set_name)
    make_test(csv_content, test_path, suite_name, set_name, category_name)
    LOG.info('General %s' % test_path)
    LOG.info("== Convert csv to xml finish==")

def make_full_test(csv_content, full_test_name, suite_name, set_name, category_name):
    full_test_file = open(full_test_name, 'w')
    content = '<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>\n<test_definition>\n  <suite name="%s" launcher="WRTLauncher" category="%s">\n    <set name="%s">' % (suite_name, category_name, set_name)
    for line in csv_content:
        content += '\n      <testcase purpose="%s" type="%s" status="%s" component="%s" execution_type="%s" priority="%s" id="%s">\n        <description>\n          <test_script_entry>%s</test_script_entry>\n        </description>\n        <specs>\n          <spec>\n            <spec_assertion element_type="%s" element_name="%s" interface="%s" specification="%s" section="%s" category="%s"/>\n            <spec_url>%s</spec_url>\n            <spec_statement/>\n          </spec>\n        </specs>\n      </testcase>' % (line[1],
         line[17],
         line[15],
         line[2],
         line[4],
         line[6],
         line[0],
         line[16],
         line[7],
         line[8],
         line[9],
         line[10],
         line[11],
         line[12],
         line[13])

    content += '\n    </set>\n  </suite>\n</test_definition>'
    full_test_file.seek(0)
    full_test_file.truncate()
    full_test_file.write(content)
    full_test_file.close()

def make_test(csv_content, test_name, suite_name, set_name, category_name):
    test_file = open(test_name, 'w')
    content = '<?xml version="1.0" encoding="UTF-8"?>\n<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>\n<test_definition>\n  <suite name="%s" category="%s" launcher="WRTLauncher">\n    <set name="%s">' % (suite_name, category_name, set_name)
    for line in csv_content:
        content += '\n      <testcase component="%s" execution_type="%s" id="%s" purpose="%s">\n        <description>\n          <test_script_entry>%s</test_script_entry>\n        </description>\n      </testcase>' % (line[2],
         line[4],
         line[0],
         line[1],
         line[16])

    content += '\n    </set>\n  </suite>\n</test_definition>'
    test_file.seek(0)
    test_file.truncate()
    test_file.write(content)
    test_file.close()

def echo_about():
    """
    This function will print the user guide and stop toolkit.
    """
    about = 'csv2xml V1.0\n-c <path>  |  Convert csv file to tests.full.xml and tests.xml\n'
    print about
    sys.exit()

def main():
    """
    main function will call different functions according to the command line argvs followed the toolkit.
    """
    global LOG
    LOG = logging.getLogger("pack-tool")
    LOG.setLevel(LOG_LEVEL)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(LOG_LEVEL)
    stream_formatter = ColorFormatter("[%(asctime)s] %(message)s")
    stream_handler.setFormatter(stream_formatter)
    LOG.addHandler(stream_handler)

    sys_name = platform.system()
    if sys_name == 'Windows':
        split_sign = '\\'
    elif sys_name == 'Linux':
        split_sign = '/'
    if len(sys.argv) != 3:
        print 'Error: No enough argv!'
        echo_about()
    else:
        {'-c': lambda : csv2full(sys.argv[2], split_sign)}[sys.argv[1]]()

if __name__ == '__main__':
    main()
