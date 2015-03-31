#!/usr/bin/python
#!encoding:utf-8

import os
import sys
import re
import commands
import glob
import fnmatch
import string
import json
from xml.etree import ElementTree as ET
from optparse import OptionParser

usecase_list = ["usecase-cordova-android-tests", "usecase-embedding-android-tests", "usecase-litewrt-android-tests", "usecase-webapi-xwalk-tests", "usecase-wrt-android-tests", "usecase-wrt-tizen-tests", "behavior"]

def iterfindfiles(path, fnexp):
    for root, dirs, files in os.walk(path):
	    for filename in fnmatch.filter(files, fnexp):
		    yield os.path.join(root, filename)

def iterfinddirs(path, fnexp):
    for root, dirs, files in os.walk(path):
        mdirlist = fnmatch.filter(dirs, fnexp)
        #if len(mdirlist) > 0:
        for dirname in mdirlist:
            yield os.path.join(root, dirname)
        #else:
        #    print "%s was not found !!!"%fnexp

def count_upstream (string = None, str_entry=None ):
    if str(string).find('/%s/' % str_entry) >= 0:
        return 1
    else:
        return 0


def get_specinfo(path):
    spec_maturity = ""
    spec_url = ""
    sub_file_name = os.path.basename(str(path)).split('-')[1]
    spec_jsfile_list = list(iterfindfiles(path,'spec.json'))
    if len(spec_jsfile_list) == 1:
        with open(spec_jsfile_list[0]) as spec_ff:
            spec_dict = json.load(spec_ff)
        spec_url = str(spec_dict.get(sub_file_name).get('spec_url'))
        spec_maturity = str(spec_dict.get(sub_file_name).get('spec_maturity'))


    sepc_info_string = spec_maturity + "|" + spec_url
    return sepc_info_string

def analy_test_file(file_path = None):
    if not PARAMETERS.inplatform:
        platform_type = "all"
    else:
        platform_type = PARAMETERS.inplatform
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
    s_component = ""
    s_component_list = []
    app_num = 0
    other_num = 0
    list_ename = []
    list_tname = []
    spec_category = ""
    spec_sub_category = ""
    spec = ""
    spec_maturify_url = ""
    usecase_flag = 0
    for usecase_suite in usecase_list:
        if usecase_suite in file_path:
            usecase_flag = 1
            break
    try:
        suite_root_dir = os.path.dirname(file_path)
        spec_maturify_url = get_specinfo(suite_root_dir)
        suite_name = os.path.basename(suite_root_dir)
        tree = ET.parse(file_path)
        root = tree.getroot()
        for set_node in root.findall('suite/set'):
            flag = 0
            #uiauto_flag = 0
            #s_type = set_node.get('type')
            s_uiauto = set_node.get('ui-auto')
            
            if s_uiauto:
                flag = 1
            #print s_type
            #if s_type == 'ref' or s_type == 'script' :
            #   if os.path.split(file_path)[0].split('/')[-1].find("wrt") > -1:
            #      flag = 0
            #   else:
            #      flag = 1
            for tc_node in set_node.findall('testcase'):
              subcase = 1
              s_status = tc_node.get('status')
              s_execution_type = tc_node.get('execution_type')
              s_priority = tc_node.get('priority')
              s_subcase = tc_node.get('subcase')
              s_component_list.append(tc_node.get('component'))
              s_platform = tc_node.get('platform')
              if s_status == 'designed' :
                 continue

              if not platform_type == "all":
                 if s_platform:
                   if not (s_platform == platform_type or s_platform == "all"):
                     continue
                 
              if s_subcase:
                 subcase = string.atoi(s_subcase)
              if s_priority == 'P0' :
                 if usecase_flag == 1:
                   if flag == 1 and s_execution_type == "auto" and platform_type != "tizen" :
                     p0_auto_webdriver += 1*subcase
                   if flag == 1 and s_execution_type == "manual":
                     p0_manual += 1*subcase
                 else:
                   if flag == 1:
                     p0_auto_webdriver += 1*subcase
                 if flag == 0:
                   if s_execution_type == "auto" :
                     p0_auto += 1*subcase
                   else:
                     p0_manual += 1*subcase
              elif s_priority == 'P1' :
                 if usecase_flag == 1:
                   if flag == 1 and s_execution_type == "auto" and platform_type != "tizen" : 
                     p1_auto_webdriver += 1*subcase
                   if flag == 1 and s_execution_type == "manual":
                     p1_manual += 1*subcase
                 else:
                   if flag == 1:
                     p1_auto_webdriver += 1*subcase
                 if flag == 0: 
                   if s_execution_type == "auto" :
                     p1_auto += 1*subcase
                   else:
                     p1_manual += 1*subcase
              elif s_priority == 'P2' :
                 if usecase_flag == 1:
                   if flag == 1 and s_execution_type == "auto" and platform_type != "tizen" :
                     p2_auto_webdriver += 1*subcase
                   if flag == 1 and s_execution_type == "manual":
                     p2_manual += 1*subcase
                 else:
                   if flag == 1:
                     p2_auto_webdriver += 1*subcase
                 if flag == 0:
                   if s_execution_type == "auto" :
                     p2_auto += 1*subcase
                   else:
                     p2_manual += 1*subcase
              elif s_priority == 'P3' :
                 if usecase_flag == 1:
                   if flag == 1 and s_execution_type == "auto" and platform_type != "tizen" :
                     p3_auto_webdriver += 1*subcase
                   if flag == 1 and s_execution_type == "manual":
                     p3_manual += 1*subcase
                 else:
                   if flag == 1:
                     p3_auto_webdriver += 1*subcase
                 if flag == 0:
                   if s_execution_type == "auto" :
                     p3_auto += 1*subcase
                   else:
                     p3_manual += 1*subcase
        for spec_node in root.findall('suite/set/testcase/specs/spec/spec_assertion'):
            if str(spec_node.get('element_type')).lower() == 'true' or str(spec_node.get('element_type')).lower() == 'tbd':
                list_ename.append(spec_node.get('element_name'))
            else:
                list_tname.append(spec_node.get('element_name'))
    except Exception, e:
         print "Got error when get case status: %s" % e
         print file_path

    p0_number = p0_auto + p0_manual + p0_auto_webdriver
    p1_number = p1_auto + p1_manual + p1_auto_webdriver
    p2_number = p2_auto + p2_manual + p2_auto_webdriver
    p3_number = p3_auto + p3_manual + p3_auto_webdriver
    total_auto = p0_auto + p1_auto + p2_auto + p3_auto  
    total_auto_webdriver = p0_auto_webdriver + p1_auto_webdriver + p2_auto_webdriver + p3_auto_webdriver 
    total_manual = p0_manual + p1_manual + p2_manual + p3_manual  
    total_number = total_auto + total_manual + total_auto_webdriver
    app_num = len(set(list_tname))
    other_num = len(set(list_ename))
    final_component_list = sorted(list(set(s_component_list)))
    if len(final_component_list) > 0:
        for ss in final_component_list:
            if len(s_component) > 0:
                s_component = s_component + ";" + ss
            else:
                s_component = ss

        component_string_list = final_component_list[0].split('/')
        if len(component_string_list) >= 3: 
            spec_category = component_string_list[0]
            spec_sub_category = component_string_list[1]
            spec = component_string_list[2]
        elif len(component_string_list) == 2:
            spec_category = component_string_list[0]
            spec = component_string_list[1]
        elif len(component_string_list) == 1:
            spec_category = component_string_list[0]
    
    case_message = Component + "|" + Platforminfo + "|" + suite_name + "|" + s_component + "|"+ str(spec_category) + "|" + str(spec_sub_category) + "|" + str(spec) + "|" + str(spec_maturify_url) + "|" + str(total_number) + "|" + str(total_auto) + "|" + str(total_auto_webdriver) + "|" + str(total_manual) + "|" + str(p0_number) + "|" + str(p0_auto) + "|" + str(p0_auto_webdriver) + "|" + str(p0_manual) + "|" + str(p1_number) + "|" + str(p1_auto) + "|" + str(p1_auto_webdriver) + "|" + str(p1_manual) + "|" + str(p2_number) + "|" + str(p2_auto) + "|" + str(p2_auto_webdriver) + "|" + str(p2_manual) + "|" + str(p3_number) + "|" + str(p3_auto) + "|" + str(p3_auto_webdriver) + "|" + str(p3_manual) + "|" + str(app_num) + "|" + str(other_num) + "|"

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
    return str(n_upstream) + "|" + upstream[: -1]


def get_case_status(file_path):

    #if "tct-widget02-w3c-tests" in file_path:
    #    return
    if "tct-manual-w3c-tests" in file_path:
        return
    if "tct-testconfig" in file_path:
        return
    if "xwalk-system-tests" in file_path:
        return
    
    try:
        case_message = analy_test_file(file_path)
        upstream = get_upstream(file_path)
        content = case_message + upstream
        print content
        #fp = open("analy_result.csv",'a')
        #fp.write(content)
        #fp.write("\n")
        #fp.close()
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
    
    rootdir = os.getcwd()
    global Component
    global Platforminfo
    Component = ""
    Platforminfo=""
    
    try:
        usage = "copy stats_all.py and projects.json to the root directory of crosswalk-test-suite, ./stat.py [-p <platform: all | android | tizen] [-f <apk tests.full.xml>] [-r <direction name>]"
        opts_parser = OptionParser(usage=usage)
        opts_parser.add_option(
            "-r",
            dest="suitesdir",
            help="specify the path of folder which tests.full.xml located in.")
        opts_parser.add_option(
            "-f",
            dest="xmlfile",
            help="specify the path of tests.full.xml file")
        opts_parser.add_option(
            "-p",
            dest="inplatform",
            help="specify the platform name,It will list the case number of all packages on the platform,Three platform name you can choose: all, android, tizen .")
        
        #init_result_file()
        if len(sys.argv) == 1:
		    sys.argv.append("-h")
        
        global PARAMETERS
        (PARAMETERS, args) = opts_parser.parse_args()
        if PARAMETERS.suitesdir:
            for filename in iterfindfiles("%s" % PARAMETERS.suitesdir, "tests.full.xml"):
                get_case_status(filename)

        if PARAMETERS.xmlfile:
            get_case_status(PARAMETERS.xmlfile)   

        if PARAMETERS.inplatform:

            pkgdict = {'tct_webapi':'TCT Web APIs','crosswalk_webapi':'Crosswalk Web APIs','tct_wrt':'TCT WRT','crosswalk_wrt':'Crosswalk WRT','usecase':'Crosswalk Use Cases','stability':'Stability','cordova':'Cordova Feature','bat':'BAT','sampleapp':'Sample App','cordovausecase':'Cordova Use case'}
            
            platformlist = ('all','android','tizen')
            
            with open('projects.json') as ffjson:
                allpkgdict = json.load(ffjson) 
            
            androidpkglist = []
            tienpkglist = []
            
            for list1 in allpkgdict['android'].keys():
                androidpkglist = allpkgdict['android'][list1] + androidpkglist
            for list2 in allpkgdict['tizen'].keys():
                tienpkglist = allpkgdict['tizen'][list2] + tienpkglist


            if PARAMETERS.inplatform not in platformlist:
                print "platform '%s' not exists,only three platform can be chosed: all, android, tizen."
                sys.exit(1)
            with open('projects.json') as fjson: 
                pkginfodic = json.load(fjson)
                
            for pkggroup in pkginfodic[PARAMETERS.inplatform].keys():
                print "*************%s start ...****************"%pkggroup
                 
                for pkgname in pkginfodic[PARAMETERS.inplatform].get(pkggroup):
                    for dirname in iterfinddirs(rootdir,str(pkgname)):
                        if pkgname in set(androidpkglist) and pkgname in set(tienpkglist):
                            Platforminfo = "Common"
                        elif pkgname in set(androidpkglist) and pkgname not in set(tienpkglist):
                            Platforminfo = "Android"
                        elif pkgname in set(tienpkglist) and pkgname not in set(androidpkglist):
                            Platforminfo = "Tizen"
                            
                        xmlf = str(dirname) + '/tests.full.xml'
                        #if str(os.path.dirname(dirname)) == "wrt-manifest-tizen-tests" or str(os.path.dirname(dirname)) == "wrt-manifest-android-tests" :
                        #    xmlf = str(dirname) + '/tests.xml'
                        Component = pkgdict.get(pkggroup)
                        if os.path.exists(xmlf):
                            get_case_status(xmlf)
                        else:
                            print "##################%s is not exists###################"%xmlf
            
    except Exception as e:
        print "Got error: %s, exit" % e

if __name__ == '__main__':
	main()

