#!/usr/bin/python
#!encoding:utf-8

import os
import sys
import re
import commands
import glob
import fnmatch
import string
from xml.etree import ElementTree as ET
from optparse import OptionParser


def iterfindfiles (path, fnexp):
    for root, dirs, files in os.walk(path):
	    for filename in fnmatch.filter(files, fnexp):
		    yield os.path.join(root, filename)

def count_upstream (string = None, str_entry=None ):
    if string.find('/%s/' % str_entry) >= 0:
        return 1
    else:
        return 0

def analy_test_file(file_path = None):
    total_number = 0
    total_auto = 0
    total_auto_webdriver = 0
    total_manual = 0
    p0_number = 0
    p0_auto   = 0
    p0_auto_webdriver = 0
    p0_manual = 0
    p1_number = 0
    p1_auto   = 0
    p1_auto_webdriver = 0
    p1_manual = 0
    p2_number = 0
    p2_auto   = 0
    p2_auto_webdriver = 0
    p2_manual = 0
    p3_number = 0
    p3_auto   = 0
    p3_auto_webdriver = 0
    p3_manual = 0
    try:
        suite_name = os.path.basename(os.path.dirname(file_path))
        tree = ET.parse(file_path)
        root = tree.getroot()
        for set_node in root.findall('suite/set'):
            flag = 0
            s_type = set_node.get('type')
            if s_type == 'ref' or s_type == 'script' :
               if os.path.split(file_path)[0].split('/')[-1].find("wrt") > -1:
                  flag = 0
               else:
                  flag = 1
            for tc_node in set_node.findall('testcase'):
              subcase = 1
              s_status = tc_node.get('status')
              s_subcase = tc_node.get('subcase')
              s_priority = tc_node.get('priority')
              s_execution_type = tc_node.get('execution_type')
              if s_status == 'designed' :
                 continue
              if s_subcase:
                 subcase = string.atoi(s_subcase)
              if s_priority == 'P0' :
                 if s_execution_type == "auto" :
                   p0_auto += 1*subcase
                   if flag == 1:
                     p0_auto_webdriver += 1*subcase
                 else:
                   p0_manual += 1*subcase
              elif s_priority == 'P1' :
                 if s_execution_type == "auto" :
                   p1_auto += 1*subcase
                   if flag == 1:
                     p1_auto_webdriver += 1*subcase
                 else:
                   p1_manual += 1*subcase
              elif s_priority == 'P2' :
                 if s_execution_type == "auto" :
                   p2_auto += 1*subcase
                   if flag == 1:
                     p2_auto_webdriver += 1*subcase
                 else:
                   p2_manual += 1*subcase
              elif s_priority == 'P3' :
                 if s_execution_type == "auto" :
                   p3_auto += 1*subcase
                   if flag == 1:
                     p3_auto_webdriver += 1*subcase
                 else:
                   p3_manual += 1*subcase
    except Exception, e:
         print "Got error when analy test files: %s" % e
         print file_path

    p0_number = p0_auto + p0_manual
    p1_number = p1_auto + p1_manual
    p2_number = p2_auto + p2_manual
    p3_number = p3_auto + p3_manual
    total_auto = p0_auto + p1_auto + p2_auto + p3_auto  
    total_auto_webdriver = p0_auto_webdriver + p1_auto_webdriver + p2_auto_webdriver + p3_auto_webdriver 
    total_manual = p0_manual + p1_manual + p2_manual + p3_manual  
    total_number = total_auto + total_manual

    case_message = suite_name + " " + str(total_number) + " " + str(total_auto) + " " + str(total_auto_webdriver) + " " + str(total_manual) + " " + str(p0_number) + " " + str(p0_auto) + " " + str(p0_auto_webdriver) + " " + str(p0_manual) + " " + str(p1_number) + " " + str(p1_auto) + " " + str(p1_auto_webdriver) + " " + str(p1_manual) + " " + str(p2_number) + " " + str(p2_auto) + " " + str(p2_auto_webdriver) + " " + str(p2_manual) + " " + str(p3_number) + " " + str(p3_auto) + " " + str(p3_auto_webdriver) + " " + str(p3_manual) + " "

    return case_message

def get_upstream(file_path):
    n_upstream = 0
    upstream_name = ["w3c","csswg","webkit","khronos","blink","ecmascript_simd"]
    exist_upstream = []
    try:
        suite_name = os.path.basename(os.path.dirname(file_path))
        tree = ET.parse(file_path)
        root = tree.getroot()
        for entry_node in root.findall('suite/set/testcase/description/test_script_entry'):
           for element in upstream_name :
             if count_upstream(entry_node.text, element) == 1:
                    n_upstream += 1
                    if element not in exist_upstream :
                       exist_upstream.append(element)
    except Exception, e:
        print e

    upstream = ""
    for element in exist_upstream:
      upstream += element + "/"
    return str(n_upstream) + " " + upstream[: -1]


def get_case_status(file_path):

    if "tct-widget02-w3c-tests" in file_path:
        return
    if "tct-testconfig" in file_path:
        return
    if "xwalk-system-tests" in file_path:
        return
    
    try:
        case_message = analy_test_file(file_path)
        upstream = get_upstream(file_path)
        content = case_message + upstream
        fp = open("analy_result.csv",'a')
        fp.write(content)
        fp.write("\n")
        fp.close()
    except Exception, e:
        print "Got error when get case status: %s" % e

def init_result_file():
    title = "Suite_name,Total,Total_auto,Total_auto_webdriver,Total_manual,P0,P0_auto,P0_auto_webdriver,P0_manual,P1,P1_auto,\
P1_auto_webdriver,P1_manual,P2,P2_auto,P2_auto_webdriver,P2_manual,P3,P3_auto,P3_auto_webdriver,P3_manual,\
Integrated_Upstream_TCs,Upstream_Resource"
    try:
        file_path = os.getcwd() + "/analy_result.csv"
        if os.path.exists(file_path):
           os.remove(file_path)
        fp = open("analy_result.csv",'a')
        fp.write(title)
        fp.write("\n")
        fp.close()
    except Exception, e:
        print "Got error when init analy file : %s" % e

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
        
        init_result_file()
        if len(sys.argv) == 1:
		    sys.argv.append("-h")
        (PARAMETERS, args) = opts_parser.parse_args()
        if PARAMETERS.suitesdir:
            for filename in iterfindfiles("%s" % PARAMETERS.suitesdir, "tests.full.xml"):
                get_case_status(filename)

        if PARAMETERS.xmlfile:
            get_case_status(PARAMETERS.xmlfile)   
    except Exception as e:
        print "Got error: %s, exit" % e

if __name__ == '__main__':
	main()

