#!/usr/bin/python
#!encoding:utf-8

import os
import sys
import re
import commands
import glob
import fnmatch
from xml.etree import ElementTree as ET
from optparse import OptionParser


def iterfindfiles (path, fnexp):
    for root, dirs, files in os.walk(path):
	    for filename in fnmatch.filter(files, fnexp):
		    yield os.path.join(root, filename)

def count_total (status = None, execution_type = None, priority = None, tec = None, flag = None):
    n_total = 0
    n_total_auto = 0
    n_total_manual = 0
    n_total_driver = 0
    if status == "approved" or status == "ready":
        n_total += 1
        if execution_type == "auto":
            n_total_auto += 1
            if flag == 1:
                n_total_driver += 1
            elif flag == 2:
                if count_bddrunner(tec) == 1:
                    n_total_driver += 1
        else:
            n_total_manual += 1
    return (n_total, n_total_auto, n_total_driver, n_total_manual)

def count_priority (string = None, status = None, execution_type = None, priority = None, tec = None, flag = None):
    n_total = 0
    n_auto = 0
    n_manual = 0
    n_driver = 0
    if status == "approved" or status == "ready":
        if priority == string:
            n_total += 1
            if execution_type == "auto":
                n_auto += 1
                if flag == 1:
                    n_driver += 1
                elif flag ==2:
                    if count_bddrunner(tec) == 1:
                        n_driver += 1
            else:
                n_manual += 1
    return (n_total, n_auto, n_driver, n_manual)

def count_upstream (string = None, str_entry=None ):
    if string.find('/%s/' % str_entry) >= 0:
        return 1
    else:
        return 0

def count_bddrunner (string = None):
    if string.find('bddrunner') >= 0:
        return 1
    else:
        return 0

def create_source_upstream (source_upstream = None, string = None):
    if source_upstream.find(string) >= 0:
        return source_upstream
    else:
        source_upstream += "%s " % string
        return source_upstream

def get_case_status (file_path = None):
    if "tct-fonts-css3-tests" in file_path:
        return
    if "tct-widget02-w3c-tests" in file_path:
        return
    if "tct-manual-w3c-tests" in file_path:
        return
    if "tct-batterystatus-w3c-tests" in file_path:
        return
    if "tct-testconfig" in file_path:
        return
    if "tct-canvas-html5-tests" in file_path:
        return
    if "xwalk-system-tests" in file_path:
        return

    suite_name = os.path.basename(os.path.dirname(file_path))
    tree = ET.parse(file_path)
    root = tree.getroot()
    list_t = [0, 0, 0, 0]
    list_p0 = [0, 0, 0, 0]
    list_p1 = [0, 0, 0, 0]
    list_p2 = [0, 0, 0, 0]
    list_p3 = [0, 0, 0, 0]
    flag_driver = 0
    n_driver_total = 0
    n_driver_p0 = 0
    n_driver_p1 = 0
    n_driver_p2 = 0
    n_driver_p3 = 0
    n_upstream = 0
    source_upstream = ""
    for set_node in root.findall('suite/set'):
        flag_driver = 0
        if set_node.get('type') == "ref":
            flag_driver = 1
        if set_node.get('type') == "script":
            flag_driver = 2
        for tc_node in set_node.findall('testcase'):
            s_status = tc_node.get('status')
            s_execution_type = tc_node.get('execution_type')
            s_priority = tc_node.get('priority')
            l_tse = tc_node.findall('description/test_script_entry')
            if l_tse:
                s_tsc = l_tse[0].text
            else:
                s_tsc = "null"
            array_t = count_total(s_status, s_execution_type, s_priority, s_tsc, flag_driver)
            list_t[0] += array_t[0]
            list_t[1] += array_t[1]
            list_t[2] += array_t[2]
            list_t[3] += array_t[3]
            array_p0 = count_priority("P0", s_status, s_execution_type, s_priority, s_tsc, flag_driver)
            list_p0[0] += array_p0[0]
            list_p0[1] += array_p0[1]
            list_p0[2] += array_p0[2]
            list_p0[3] += array_p0[3]
            array_p1 = count_priority("P1", s_status, s_execution_type, s_priority, s_tsc, flag_driver)
            list_p1[0] += array_p1[0]
            list_p1[1] += array_p1[1]
            list_p1[2] += array_p1[2]
            list_p1[3] += array_p1[3]
            array_p2 = count_priority("P2", s_status, s_execution_type, s_priority, s_tsc, flag_driver)
            list_p2[0] += array_p2[0]
            list_p2[1] += array_p2[1]
            list_p2[2] += array_p2[2]
            list_p2[3] += array_p2[3]
            array_p3 = count_priority("P3", s_status, s_execution_type, s_priority, s_tsc, flag_driver)
            list_p3[0] += array_p3[0]
            list_p3[1] += array_p3[1]
            list_p3[2] += array_p3[2]
            list_p3[3] += array_p3[3]
        for entry_node in set_node.findall('testcase/description/test_script_entry'):
            if count_upstream(entry_node.text, "w3c") == 1:
                n_upstream += 1
                source_upstream = create_source_upstream(source_upstream, "csswg")
                continue
            if count_upstream(entry_node.text, "csswg") == 1:
                n_upstream += 1
                source_upstream = create_source_upstream(source_upstream, "csswg")
                continue
            if count_upstream(entry_node.text, "webkit") == 1:
                n_upstream += 1
                source_upstream = create_source_upstream(source_upstream, "csswg")
                continue
            if count_upstream(entry_node.text, "khronos") == 1:
                n_upstream += 1
                source_upstream = create_source_upstream(source_upstream, "csswg")
                continue
            if count_upstream(entry_node.text, "blink") == 1:
                n_upstream += 1
                source_upstream = create_source_upstream(source_upstream, "csswg")
                continue
            if count_upstream(entry_node.text, "ecmascript_simd") == 1:
                n_upstream += 1
                source_upstream = create_source_upstream(source_upstream, "csswg")
                
    print "%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s|%s" % \
            (suite_name,
             list_t[0], list_t[1], list_t[2], list_t[3],
             list_p0[0], list_p0[1], list_p0[2], list_p0[3],
             list_p1[0], list_p1[1], list_p1[2], list_p1[3],
             list_p2[0], list_p2[1], list_p2[2], list_p2[3],
             list_p3[0], list_p3[1], list_p3[2], list_p3[3],
             n_upstream, source_upstream)

def main():
    try:
        usage = "./stats.py -f ../../webapi/tct-2dtransforms-css3-tests/tests.full.xml"
        opts_parser = OptionParser(usage=usage)
        opts_parser.add_option(
            "-r",
            dest="suitesdir",
            help="specify the path of folder which tests.full.xml located in.")
        opts_parser.add_option(
            "-f",
            dest="xmlfile",
            help="specify the path of tests.full.xml file")

        if len(sys.argv) == 1:
		    sys.argv.append("-h")
        (PARAMETERS, args) = opts_parser.parse_args()
        if PARAMETERS.suitesdir:
			for filename in iterfindfiles("%s" % PARAMETERS.suitesdir, "tests.full.xml"):
			    get_case_status(filename)

        if PARAMETERS.xmlfile:
            print "Suite Name|Total|Total_auto|Total_auto_webdriver|Total_manual|P0|P0_auto|Total_auto_webdriver|P0_manual|P1|P1_auto|P1_auto_webdriver|P1_manual|P2|P2_auto|P2_auto_webdriver|P2_manual|P3|P3_auto|P3_auto_webdriver|P3_manual|Integrated Upstream TCs|Upstream Resource"
            get_case_status(PARAMETERS.xmlfile)   
    except Exception as e:
        print "Got error: %s, exit" % e

if __name__ == '__main__':
	main()

