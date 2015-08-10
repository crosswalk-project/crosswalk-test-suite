#!/usr/bin/python
# encoding:utf-8

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
#         Li, Hao <haox.li@intel.com>

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

class Set():
    set_name = ""
    set_type = ""
    ui_auto = ""
    testcase = []

    def __init__(self, setname, settype, uiauto):
        self.set_name = setname
        self.set_type = settype
        self.ui_auto = uiauto
        self.testcase = []

    def __init__(self, setname, settype, uiauto, testcase):
        self.set_name = setname
        self.set_type = settype
        self.ui_auto = uiauto
        self.testcase = testcase



class TestCase():
    case_id = ""
    purpose = ""
    component = ""
    priority = ""
    execution_type = ""
    status = ""
    case_type = ""
    onload_delay = ""
    subcase = ""
    pre_condition = ""
    post_condition = ""
    steps = []
    test_script_entry = ""
    refer_test_script_entry = ""
    bdd_test_script_entry = ""
    spec_category = ""
    spec_section = ""
    spec_specification = ""
    spec_interface = ""
    spec_element_name = ""
    spec_element_type = ""
    spec_url = ""
    spec_statement = ""

    def __init__(self, caseid, purpose, component, priority, executiontype, status, casetype,\
                 onloaddelay, subcase, precondition, postcondition, steps, testscriptentry,\
                 refertestscriptentry, bddtestscriptentry, speccategory, specsection,\
                 specification, specinterface, specelementname, specelementtype, specurl):
        self.case_id = caseid
        self.purpose = purpose
        self.component = component
        self.priority = priority
        self.execution_type = executiontype
        self.status = status
        self.case_type = casetype
        self.onload_delay = onloaddelay
        self.subcase = subcase
        self.pre_condition = precondition
        self.post_condition = postcondition
        self.steps = steps
        self.test_script_entry = testscriptentry
        self.refer_test_script_entry = refertestscriptentry
        self.bdd_test_script_entry = bddtestscriptentry
        self.spec_category = speccategory
        self.spec_section = specsection
        self.spec_specification = specification
        self.spec_interface = specinterface
        self.spec_element_name = specelementname
        self.spec_element_type = specelementtype
        self.spec_url = specurl


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
    LOG.info("+Convert csv to test.full.xml start ...")
    csv_file = file(csv_path, 'rb')
    csv_file.readline()
    reader = csv.reader(csv_file)
    test_suite = {}
    for line in reader:
        if test_suite.get(line[0]) is None:
            testset = Set(line[0], line[1], line[2], [])
            test_suite[line[0]] = testset

        testcase = TestCase(line[3], line[4], line[5], line[8], line[7], line[17], line[22],\
                            str(line[6]), str(line[21]), line[23], line[24], line[25], line[18], line[19],\
                            line[20], line[14], line[13], line[12], line[11], line[10], line[9], line[15])
        test_suite[line[0]].testcase.append(testcase)

    csv_file.close()

    suite_name = test_suite.values()[0].testcase[0].test_script_entry.split('/')[2]
    category_name = test_suite.values()[0].testcase[0].component.split('/')[0]
    folder = os.path.dirname(csv_path)
    full_test_path = '%s%s%s-tests.full.xml' % (folder, split_sign, suite_name)
    make_full_test(
        test_suite,
        full_test_path,
        suite_name,
        category_name)
    LOG.info('General %s' % full_test_path)


def make_full_test(test_suite, full_test_name, suite_name, category_name):
    full_test_file = open(full_test_name, 'w')
    content = '<?xml version="1.0" encoding="UTF-8"?>\n'\
            + '<?xml-stylesheet type="text/xsl" href="./testcase.xsl"?>\n'\
            + '<test_definition>\n'\
            + '  <suite category="%s" name="%s">\n' % (category_name, suite_name)
    for testset in test_suite.values():
        set_ui_auto = ""
        if testset.ui_auto is not "":
            set_ui_auto = ' ui-auto="%s"' % testset.ui_auto
        content += '    <set name="%s" type="%s"%s>\n' % (testset.set_name, testset.set_type, set_ui_auto)
        testcasestr = ""
        for testcase in testset.testcase:
            onload_delay = ' onload_delay="%s"' % testcase.onload_delay if testcase.onload_delay is not "" else ""
            subcase = ' subcase="%s"' % testcase.subcase if testcase.subcase is not "" else ""
            pre_condition = '\
          <pre_condition>\n\
              %s\n\
          </pre_condition>\n' % testcase.pre_condition if testcase.pre_condition is not "" else ""

            post_condition = '\
          <post_condition>\n\
              %s\n\
          </post_condition>\n' % testcase.post_condition if testcase.post_condition is not "" else ""

            refer_test_script_entry = "          <refer_test_script_entry>%s</refer_test_script_entry>\n" \
                                      % testcase.post_condition if testcase.post_condition is not "" else ""
            bdd_test_script_entry = "          <bdd_test_script_entry>%s</bdd_test_script_entry>\n" \
                                      % testcase.bdd_test_script_entry if testcase.bdd_test_script_entry is not "" else ""

            testcasestr += '\
      <testcase purpose="%s" component="%s" type="%s" status="%s" execution_type="%s" priority="%s" id="%s"%s%s>\n\
        <description>\n%s%s\
          <test_script_entry>%s</test_script_entry>\n%s%s\
        </description>\n\
        <specs>\n\
          <spec>\n\
            <spec_assertion element_type="%s" element_name="%s" interface="%s" specification="%s" section="%s" category="%s"/>\n\
            <spec_url>%s</spec_url>\n\
            <spec_statement/>\n\
          </spec>\n\
        </specs>\n\
      </testcase>\n' % (testcase.purpose, testcase.component, testcase.case_type, testcase.status, testcase.execution_type,\
                        testcase.priority, testcase.case_id, onload_delay, subcase, pre_condition, post_condition,\
                        testcase.test_script_entry, refer_test_script_entry, bdd_test_script_entry, testcase.spec_element_type,\
                        testcase.spec_element_name, testcase.spec_interface, testcase.spec_specification, testcase.spec_section,\
                        testcase.spec_category, testcase.spec_url)
        content += testcasestr\
                 + '    </set>\n'

    content += '  </suite>\n</test_definition>'
    full_test_file.seek(0)
    full_test_file.truncate()
    full_test_file.write(content)
    full_test_file.close()


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
        {'-c': lambda: csv2full(sys.argv[2], split_sign)}[sys.argv[1]]()

if __name__ == '__main__':
    main()
