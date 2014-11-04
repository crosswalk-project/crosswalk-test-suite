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


def verify_xml(xml_dir, split_sign):
    if not os.path.isdir(xml_dir):
        if not os.path.isfile(xml_dir):
            LOG.error("Not dir and not file error")
            return
        else:
            name, ext = os.path.splitext(xml_dir)
            if not ext == '.xml':
                print '%s is not a xml' % xml_path
                return
            else:
                verify_path(xml_dir, split_sign)
            
    paths = [ item for item in os.walk(xml_dir) ]
    for path, dirs, files in paths:
        for filename in files:
            if filename == "tests.full.xml":
                verify_path(path + split_sign + filename, split_sign)

def verify_path(xml_path, split_sign):
    LOG.info("+Verify xml: " + xml_path)
    try:
        root_node = ElementTree.parse(xml_path)
    except Exception as e:
        LOG.error("xml parse error")
        return False
    suite_node = root_node.find('suite')
    set_nodes = suite_node.findall('set')
    id_list = []
    purpose_list = []
    set_type = ['js', 'wrt', 'ref', 'qunit', 'script', 'pyunit', 'androidunit']
    for set_node in set_nodes:
        try:
            if set_node.attrib['type'] not in set_type:
                LOG.info("set wrong type: " + set_node.attrib['name'])
                break
        except Exception as e:
            LOG.error("set no type: " + set_node.attrib['name'])
            return False
        if set_node.attrib['type'] == 'script':
            break
        case_nodes = set_node.findall('testcase')
        for case_node in case_nodes:
            verify_path =  os.path.dirname(xml_path)
            casepath = case_node.find('description/test_script_entry').text
            if casepath is None:
                break
            id_list.append(case_node.attrib['id'])
            purpose_list.append(case_node.attrib['purpose'])
            arraypath =  casepath.split('?')[0].split(split_sign)
            if len(arraypath) < 3:
                break
            if arraypath.count('http:') > 0:
                del arraypath[0:5]
            else:
                del arraypath[0:3]
            for i in range(len(arraypath)):
                verify_path += split_sign + arraypath[i]
            
            if not os.path.exists(verify_path):
                LOG.info("path no found: " + verify_path)
    temp_array = []
    for xid in range(len(id_list)):
        if id_list.count(id_list[xid]) > 1 and id_list[xid] not in temp_array: 
            LOG.info(str(id_list.count(id_list[xid])) + " same id : " + id_list[xid])
            temp_array.append(id_list[xid])
    del temp_array[:]
    for xpurpose in range(len(purpose_list)):
        if purpose_list.count(purpose_list[xpurpose]) > 1 and purpose_list[xpurpose] not in temp_array: 
            LOG.info(str(purpose_list.count(purpose_list[xpurpose])) + " same purpose: " + purpose_list[xpurpose])
            temp_array.append(purpose_list[xpurpose])
    del temp_array[:]
    LOG.info("===Verify case path, id and purpose finish===")

def echo_about():
    """
    This function will print the user guide and stop toolkit.
    """
    about = 'xmlverifier V1.0\n-v <path>  |  Verify case path, id, purpose and set type are right\n'
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
        {'-v': lambda : verify_xml(sys.argv[2], split_sign)}[sys.argv[1]]()

if __name__ == '__main__':
    main()
