import sys, os
import itertools, shutil

 
path = os.getcwd()
path_tcs = path + "/tcs"
path_result= path + "/result"
path_allpairs = path + "/allpairs"
path_resource = path + "/resource"
seed_file = path_allpairs + "/positive/input_seed.txt"
seed_negative = path_allpairs + "/negative"
seed_positive =path_allpairs + "/positivee"
seed_file_na = seed_negative + "/input_seed_negative.txt"
selfcomb_file = path_allpairs + "/selfcomb.txt"
output_file = path_allpairs + "/output.txt"
output_file_ne = path_allpairs + "/output_negative.txt"
report_path = path + "/report"
report_file = report_path + "/wrt-manifest-tizen-tests.xml"
report_summary_file = report_path + "/summary.xml"
sh_path = path + "/script"
log_path = report_path + "/log.txt"
device_path = "/home/app/content/tct/"
run_times = 3
version="6.35.1.2"
name="wrt-manifest-tizen-tests"
