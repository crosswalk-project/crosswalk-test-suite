#!/usr/bin/env python

# Author:
#         Li, Jiajia <jiajiax.li@intel.com>

import sys, os, os.path, shutil, time
import commands, traceback, glob
import threading
import time
import logging
import subprocess
from optparse import OptionParser

SCRIPT_PATH = os.path.realpath(__file__)
ConstPath = os.path.dirname(SCRIPT_PATH)

LOG = None
LOG_LEVEL = logging.DEBUG
BUILD_TIME = time.strftime('%Y%m%d',time.localtime(time.time()))
DEFAULT_CMD_TIMEOUT = 1200
#RES_STDICT = {"positive":0,"negative":1}
RESULT_DIR = os.path.join(ConstPath,"apks")
MAX_RUNNING_THREAD_NUM = 12


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


def doCMDWithOutput(cmd, time_out=DEFAULT_CMD_TIMEOUT):
    LOG.info("Doing CMD: [ %s ]" % cmd)
    pre_time = time.time()
    output = []
    cmd_return_code = 1 
    cmd_proc = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

    while True:
        output_line = cmd_proc.stdout.readline().strip("\r\n")
        cmd_return_code = cmd_proc.poll()
        elapsed_time = time.time() - pre_time
        if cmd_return_code is None:
            if elapsed_time >= time_out:
                killProcesses(ppid=cmd_proc.pid)
                LOG.error("Timeout to exe CMD")
                return False
        elif output_line == '' and cmd_return_code is not None:
            break

        sys.stdout.write("%s\n" % output_line)
        sys.stdout.flush()
        output.append(output_line)
    if cmd_return_code != 0:
        LOG.error("Fail to exe CMD")

    return (cmd_return_code, output)



def init_env(arch_arg):

    global RES_FILE
    global RES_ARCH_DIR

    RES_ARCH_DIR = os.path.join(RESULT_DIR,arch_arg)
    RES_FILE = os.path.join(RESULT_DIR,arch_arg,"Pkg_result.txt")

    if os.path.exists(RES_ARCH_DIR):
        shutil.rmtree(RES_ARCH_DIR)

    
    os.makedirs(RES_ARCH_DIR)
    os.mknod(RES_FILE)


def ge_apks(suite_dir, arch_arg, res_arch_dir):

    max_num.acquire()

    suite_name = suite_dir.split('/')[-1]
    suitename_without_flag = suite_name.split('-')[0]
    flag = suite_name.split('-')[-1]

    #cmd ="python " + os.path.join(BUILD_PARAMETERS.pkgpacktools, 'crosswalk', 'make_apk.py') +" --package=org.xwalk.test --app-versionCode=123 --arch=" + arch_arg + " --manifest="
    with open(suite_dir + '/cmd.txt') as cmdfile:
        cmd_origin = cmdfile.read()
    cmd = cmd_origin.replace('make_apk.py', pkg_script)
    #manifest_path = os.path.join(suite_dir, "manifest.json")
    res_suite_dir = os.path.join(res_arch_dir, suitename_without_flag)

    #if not os.path.exists(manifest_path):
    #    LOG.error("%s not exists !!!" % manifest_path)
    #    ores_file.write(suitename_without_flag + "\t" + flag + "\t" + "Manifest not exists !!!" + "\n")
    #    return
    if os.path.exists(res_suite_dir):
        shutil.rmtree(res_suite_dir)
    os.makedirs(res_suite_dir)

    os.chdir(res_suite_dir)

    resdir_name = None
    if 'target-dir' in cmd_origin:
        for command in cmd_origin.split():
            if 'target-dir' in command:
                resdir_name = command.split('"')[-2]

    if resdir_name != None and resdir_name != './' and os.path.exists(resdir_name + "/Intel_" + BUILD_PARAMETERS.pkgarch + ".apk"):
        #for eapk in glob.glob(resdir_name + "/*.apk"):
        os.remove(resdir_name + "/Intel_" + BUILD_PARAMETERS.pkgarch + ".apk")
    
    status, info = doCMDWithOutput(cmd)

    if (status == 0 and flag == 'positive') or (status != 0 and flag == 'negative'):
        result = "PASS"
    else:
        result = "FAIL"

    if status != 0:
        shutil.rmtree(res_suite_dir)
    else:
        if resdir_name != None and resdir_name != './' and os.path.exists(resdir_name + "/Intel_" + BUILD_PARAMETERS.pkgarch + ".apk"):
            shutil.move(resdir_name + "/Intel_" + BUILD_PARAMETERS.pkgarch + ".apk", res_suite_dir)
        
    

    ores_file.write(suitename_without_flag + "\t"  + flag + "\t" + result + "\n")

    if result == "PASS":
        LOG.info("Built Done: [ %s %s %s %s ] !!! "%(suitename_without_flag, flag, result, status))
    else:
        LOG.error("Built Done: [ %s %s %s %s ] !!! "%(suitename_without_flag, flag, result, status))
        
    if threading.activeCount() >= MAX_RUNNING_THREAD_NUM:
        max_num.release()

    

if __name__ == "__main__":

    #global LOG
    LOG = logging.getLogger("pack-tool")
    LOG.setLevel(LOG_LEVEL)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(LOG_LEVEL)
    stream_formatter = ColorFormatter("[%(asctime)s] %(message)s")
    stream_handler.setFormatter(stream_formatter)
    LOG.addHandler(stream_handler)
    pack_threads = []
    global max_num
    global ores_file
    global pkg_script

    try:
        usage = "Usage: ./gen_apks.py -a x86 --tools=<tools path>"
        opts_parser = OptionParser(usage=usage)
        opts_parser.add_option(
            "-a",
            "--arch",
            dest="pkgarch",
            help="specify the apk arch, e.g. x86, arm")
        opts_parser.add_option(
            "--tools",
            dest="pkgpacktools",
            help="specify the parent folder of pack tools")

        if len(sys.argv) == 1:
            sys.argv.append("-h")

        global BUILD_PARAMETERS
        (BUILD_PARAMETERS, args) = opts_parser.parse_args()
    except Exception as e:
        LOG.error("Got wrong options: %s, exit ..." % e)
        sys.exit(1)

    if not BUILD_PARAMETERS.pkgarch:
        BUILD_PARAMETERS.pkgarch = "x86"

    if not BUILD_PARAMETERS.pkgpacktools:
        BUILD_PARAMETERS.pkgpacktools = os.path.join(
            ConstPath, "..", "..", "tools")
    BUILD_PARAMETERS.pkgpacktools = os.path.expanduser(
        BUILD_PARAMETERS.pkgpacktools)
    pkg_script = os.path.join(BUILD_PARAMETERS.pkgpacktools, 'crosswalk', 'make_apk.py')


    init_env(BUILD_PARAMETERS.pkgarch)

    ores_file = open(RES_FILE,'w')

    max_num = threading.Semaphore(MAX_RUNNING_THREAD_NUM)
    for suite in os.listdir(os.path.join(ConstPath, 'tcs', BUILD_PARAMETERS.pkgarch)):
        suite_abspath = os.path.join(ConstPath, 'tcs', BUILD_PARAMETERS.pkgarch, suite)
        pack_threads.append(threading.Thread(target=ge_apks, args=(suite_abspath, BUILD_PARAMETERS.pkgarch, RES_ARCH_DIR)))

    for sthread in pack_threads:
        #if max_num.acquire():
        sthread.daemon = True
        sthread.start()
        #if len(threading.enumerate()) < 3:
        #    max_num.release()

    for sthread in pack_threads:
        sthread.join()

    ores_file.flush()
    ores_file.close()
