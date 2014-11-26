#!/usr/bin/env python

import os
import shutil
import glob
import time
import sys
import subprocess
from optparse import OptionParser, make_option


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PKG_NAME = os.path.basename(SCRIPT_DIR)
TEST_PREFIX = os.environ['HOME']
PARAMETERS = None
ADB_CMD = "adb"


def doCMD(cmd):
    # Do not need handle timeout in this short script, let tool do it
    print "-->> \"%s\"" % cmd
    output = []
    cmd_return_code = 1
    cmd_proc = subprocess.Popen(
        cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True)

    while True:
        output_line = cmd_proc.stdout.readline().strip("\r\n")
        cmd_return_code = cmd_proc.poll()
        if output_line == '' and cmd_return_code != None:
            break
        sys.stdout.write("%s\n" % output_line)
        sys.stdout.flush()
        output.append(output_line)

    return (cmd_return_code, output)


def overwriteCopy(src, dest, symlinks=False, ignore=None):
    if not os.path.exists(dest):
        os.makedirs(dest)
        shutil.copystat(src, dest)
    sub_list = os.listdir(src)
    if ignore:
        excl = ignore(src, sub_list)
        sub_list = [x for x in sub_list if x not in excl]
    for i_sub in sub_list:
        s_path = os.path.join(src, i_sub)
        d_path = os.path.join(dest, i_sub)
        if symlinks and os.path.islink(s_path):
            if os.path.lexists(d_path):
                os.remove(d_path)
            os.symlink(os.readlink(s_path), d_path)
            try:
                s_path_s = os.lstat(s_path)
                s_path_mode = stat.S_IMODE(s_path_s.st_mode)
                os.lchmod(d_path, s_path_mode)
            except Exception, e:
                pass
        elif os.path.isdir(s_path):
            overwriteCopy(s_path, d_path, symlinks, ignore)
        else:
            shutil.copy2(s_path, d_path)


def doCopy(src_item=None, dest_item=None):
    try:
        if os.path.isdir(src_item):
            overwriteCopy(src_item, dest_item, symlinks=True)
        else:
            if not os.path.exists(os.path.dirname(dest_item)):
                os.makedirs(os.path.dirname(dest_item))
            shutil.copy2(src_item, dest_item)
    except Exception, e:
        return False

    return True


def uninstPKGs():
    action_status = True
    for root, dirs, files in os.walk(SCRIPT_DIR):
        for file in files:
            if file.endswith(".apk"):
                cmd = "%s -s %s uninstall org.xwalk.%s" % (
                    ADB_CMD, PARAMETERS.device, os.path.basename(os.path.splitext(file)[0]))
                (return_code, output) = doCMD(cmd)
                for line in output:
                    if "Failure" in line:
                        action_status = False
                        break
    #if os.path.isdir("%s/opt/%s/" % (TEST_PREFIX, PKG_NAME)):
        #shutil.rmtree("%s/opt/%s/" % (TEST_PREFIX, PKG_NAME))
    return action_status


def instPKGs():
    action_status = True
    #for root, dirs, files in os.walk(SCRIPT_DIR):
    #    for file in files:
    #        if file.endswith(".apk"):
    #            cmd = "%s -s %s install %s" % (ADB_CMD,
    #                                           PARAMETERS.device, os.path.join(root, file))
    for item in glob.glob("%s/*" % SCRIPT_DIR):
        if item.endswith(".apk"):
            continue
        elif item.endswith("inst.py"):
            continue
        else:
            item_name = os.path.basename(item)
            if not doCopy(item, "%s/opt/%s/%s" % (TEST_PREFIX, PKG_NAME, item_name)):
                action_status = False
    os.rename("%s/opt/%s/resources/apk/webappintel.apk" % (TEST_PREFIX, PKG_NAME),"%s/opt/%s/resources/apk/WebApp.apk" % (TEST_PREFIX, PKG_NAME))
    print "Package push to host %s/opt/%s successfully!" % (TEST_PREFIX, PKG_NAME)
    path = "/tmp/Crosswalk_sharedmode.conf"
    if os.path.exists(path):
        if not doCopy(path, "%s/opt/%s/Crosswalk_sharedmode.conf" % (TEST_PREFIX, PKG_NAME)):
            action_status = False
        (return_code, output) = doCMD("cat \"%s/opt/%s/Crosswalk_sharedmode.conf\" | grep \"Android_Crosswalk_Path\" | cut -d \"=\" -f 2" % (TEST_PREFIX, PKG_NAME))
        for line in output:
            if "Failure" in line:
                action_status = False
                break
        if not output == []:
            ANDROID_CROSSWALK_PATH = output[0]
            CROSSWALK = os.path.basename(ANDROID_CROSSWALK_PATH)
            if not doCopy(ANDROID_CROSSWALK_PATH, "%s/opt/%s/resources/installer/%s" % (TEST_PREFIX, PKG_NAME, CROSSWALK)):
                action_status = False    
        
    return action_status


def main():
    try:
        global TEST_PREFIX
        usage = "usage: inst.py -i"
        opts_parser = OptionParser(usage=usage)
        opts_parser.add_option(
            "-s", dest="device", action="store", help="Specify device")
        opts_parser.add_option(
            "-i", dest="binstpkg", action="store_true", help="Install package")
        opts_parser.add_option(
            "-u", dest="buninstpkg", action="store_true", help="Uninstall package")
        opts_parser.add_option(
            "-t", dest="testprefix", action="store", help="unzip path prefix", default=os.environ["HOME"])
        global PARAMETERS
        (PARAMETERS, args) = opts_parser.parse_args()
    except Exception, e:
        print "Got wrong option: %s, exit ..." % e
        sys.exit(1)

    if not PARAMETERS.device:
        (return_code, output) = doCMD("adb devices")
        for line in output:
            if str.find(line, "\tdevice") != -1:
                PARAMETERS.device = line.split("\t")[0]
                break

    TEST_PREFIX = PARAMETERS.testprefix

    if not PARAMETERS.device:
        print "No device found"
        sys.exit(1)

    if PARAMETERS.binstpkg and PARAMETERS.buninstpkg:
        print "-i and -u are conflict"
        sys.exit(1)

    if PARAMETERS.buninstpkg:
        os.system("%s -s %s uninstall %s" % (ADB_CMD, PARAMETERS.device, "org.xwalk.runtime.lib"))
        #if not uninstPKGs():
            #sys.exit(1)
    else:
        os.system("%s -s %s install -r %s" % (ADB_CMD, PARAMETERS.device, "resources/installer/XWalkRuntimeLib.apk"))
        #if not instPKGs():
            #sys.exit(1)

if __name__ == "__main__":
    main()
    sys.exit(0)
