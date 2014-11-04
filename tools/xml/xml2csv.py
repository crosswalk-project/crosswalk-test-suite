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

def xml2csv(xml_path, split_sign):
    if not os.path.isfile(xml_path):
        print '%s is not a file' % xml_path
        return
    name, ext = os.path.splitext(xml_path)

    if not ext == '.xml':
        print '%s is not a xml' % xml_path
        return
    if not name.split(split_sign)[-1] == 'tests.full':
        print name
        print '%s is not tests.full.xml' % xml_path
        return
    LOG.info("+Convert xml to csv start ...")
    folder = os.path.dirname(xml_path)
    csv_path = folder + split_sign
    make_csv(xml_path, csv_path)
    LOG.info("===Convert xml to csv finish===")

def make_csv(xml_path, csv_path):
    root_node = ElementTree.parse(xml_path)
    set_node = root_node.find('suite/set')
    csv_file_name = set_node.attrib['name']
    csv_path += csv_file_name + '.csv'
    LOG.info("General: %s" % csv_path)
    writer = csv.writer(file(csv_path, 'wb'))
    writer.writerow(['Name',
     'Description',
     'Component',
     'Onload_Delay',
     'Execution_Type',
     'Package',
     'Priority',
     'ElementType',
     'ElementName',
     'Interface',
     'Specification',
     'Section',
     'Category',
     'SpecURL',
     'SpecStatement',
     'Status',
     'Test_Script_Entry',
     'Type',
     'PreCondition',
     'PostCondition',
     'StepNumber',
     'StepDescription',
     'StepExpectedResult'])
    case_nodes = set_node.findall('testcase')
    for case_node in case_nodes:
        spec_assertion = case_node.find('specs/spec/spec_assertion')
        element_type = ''
        if 'element_type' in spec_assertion.attrib:
            element_type = spec_assertion.attrib['element_type']
        else:
            element_type = 'true'
        element_name = ''
        if 'element_name' in spec_assertion.attrib:
            element_name = spec_assertion.attrib['element_name']
        writer.writerow([case_node.attrib['id'],
         case_node.attrib['purpose'],
         case_node.attrib['component'],
         '',
         case_node.attrib['execution_type'],
         '',
         case_node.attrib['priority'],
         element_type,
         element_name,
         spec_assertion.attrib['interface'],
         spec_assertion.attrib['specification'],
         spec_assertion.attrib['section'],
         spec_assertion.attrib['category'],
         case_node.find('specs/spec/spec_url').text,
         '',
         case_node.attrib['status'],
         case_node.find('description/test_script_entry').text,
         case_node.attrib['type'],
         '',
         '',
         '1',
         '',
         'pass'])

def echo_about():
    """
    This function will print the user guide and stop toolkit.
    """
    about = 'xml2csv V1.0\n-c <path>  |  Convert tests.full.xml to csv file\n'
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
        {
         '-c': lambda : xml2csv(sys.argv[2], split_sign)}[sys.argv[1]]()

if __name__ == '__main__':
    main()
