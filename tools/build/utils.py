#!/usr/bin/env python
#
# Copyright (c) 2015 Intel Corporation.
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
#         Fan, Yugang <yugang.fan@intel.com>
#         Hao, Yunfei <yunfeix.hao@intel.com>

import os
import shutil
import time
import sys
import stat
import random
import logging
import zipfile
import signal
import fnmatch
import subprocess
import re
from optparse import OptionParser
import varshop

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


def iterfindfiles(path, fnexp):
    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files, fnexp):
            yield os.path.join(root, filename)


def replaceUserString(path, fnexp, old_s, new_s):
    for sub_file in iterfindfiles(path, fnexp):
        try:
            with open(sub_file, 'r') as sub_read_obj:
                read_string = sub_read_obj.read()
        except IOError as err:
            LOG.error("Read %s Error : " % sub_file + str(err))
            continue
        if read_string.find(old_s) >= 0:
            try:
                with open(sub_file, 'w') as sub_write_obj:
                    sub_write_obj.write(re.sub(old_s, new_s, read_string))
            except IOError as err:
                LOG.error("Modify %s Error : " % sub_file + str(err))
                continue


def pidExists(pid):
    if pid < 0:
        return False
    try:
        os.kill(pid, 0)
    except OSError:
        return False
    else:
        return True


def isWindows():
    return sys.platform == "cygwin" or sys.platform.startswith("win")


def killProcesses(ppid=None):
    if isWindows():
        subprocess.check_call("TASKKILL /F /PID %s /T" % ppid)
    else:
        ppid = str(ppid)
        pidgrp = []

        def GetChildPids(ppid):
            command = "ps -ef | awk '{if ($3 ==%s) print $2;}'" % str(ppid)
            pids = os.popen(command).read()
            pids = pids.split()
            return pids

        pidgrp.extend(GetChildPids(ppid))
        for pid in pidgrp:
            pidgrp.extend(GetChildPids(pid))

        pidgrp.insert(0, ppid)
        while len(pidgrp) > 0:
            pid = pidgrp.pop()
            try:
                os.kill(int(pid), signal.SIGKILL)
                return True
            except OSError:
                try:
                    os.popen("kill -9 %d" % int(pid))
                    return True
                except Exception:
                    return False


def safelyGetValue(origin_json=None, key=None):
    if origin_json and key and key in origin_json:
        return origin_json[key]
    return None


def checkContains(origin_str=None, key_str=None):
    if origin_str.upper().find(key_str.upper()) >= 0:
        return True
    return False


def getRandomStr():
    str_pool = list("abcdefghijklmnopqrstuvwxyz1234567890")
    random_str = ""
    for i in range(15):
        index = random.randint(0, len(str_pool) - 1)
        random_str = random_str + str_pool[index]

    return random_str


def zipDir(dir_path, zip_file):
    try:
        if os.path.exists(zip_file):
            if not doRemove([zip_file]):
                return False
        if not os.path.exists(os.path.dirname(zip_file)):
            os.makedirs(os.path.dirname(zip_file))
        z_file = zipfile.ZipFile(zip_file, "w")
        orig_dir = os.getcwd()
        os.chdir(dir_path)
        
        # Remove the .git directory to reduce the size of cordova packages
        os.system('find . -name ".git" | xargs rm -fr')
        for root, dirs, files in os.walk("."):
            for i_file in files:
                LOG.info("zip %s" % os.path.join(root, i_file))
                z_file.write(os.path.join(root, i_file))
        z_file.close()
        os.chdir(orig_dir)
    except Exception as e:
        LOG.error("Fail to pack %s to %s: %s" % (dir_path, zip_file, e))
        return False
    LOG.info("Done to zip %s to %s" % (dir_path, zip_file))
    return True


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
            except Exception:
                pass
        elif os.path.isdir(s_path):
            overwriteCopy(s_path, d_path, symlinks, ignore)
        else:
            shutil.copy2(s_path, d_path)


def doCopy(src_item=None, dest_item=None):
    LOG.info("Copying %s to %s" % (src_item, dest_item))
    try:
        if os.path.isdir(src_item):
            overwriteCopy(src_item, dest_item, symlinks=True)
        else:
            if not os.path.exists(os.path.dirname(dest_item)):
                LOG.info("Create non-existent dir: %s" %
                         os.path.dirname(dest_item))
                os.makedirs(os.path.dirname(dest_item))
            shutil.copy2(src_item, dest_item)
    except Exception as e:
        LOG.error("Fail to copy file %s: %s" % (src_item, e))
        return False

    return True


def doRemove(target_file_list=None):
    for i_file in target_file_list:
        LOG.info("Removing %s" % i_file)
        try:
            if os.path.isdir(i_file):
                shutil.rmtree(i_file)
            else:
                os.remove(i_file)
        except Exception as e:
            LOG.error("Fail to remove file %s: %s" % (i_file, e))
            return False
    return True


def doCMD(cmd, time_out, no_check_return=False):
    if time_out is None:
        time_out = varshop.getValue("DEFAULT_CMD_TIMEOUT")
    LOG.info("Doing CMD: [ %s ]" % cmd)
    pre_time = time.time()
    cmd_proc = subprocess.Popen(args=cmd, shell=True)
    while True:
        cmd_exit_code = cmd_proc.poll()
        elapsed_time = time.time() - pre_time
        if cmd_exit_code is None:
            if elapsed_time >= time_out:
                killProcesses(ppid=cmd_proc.pid)
                LOG.error("Timeout to exe CMD")
                return False
        else:
            if not no_check_return and cmd_exit_code != 0:
                LOG.error("Fail to exe CMD")
                return False
            break
        time.sleep(2)
    return True


def doCMDWithOutput(cmd, time_out):
    if time_out is None:
        time_out = varshop.getValue("DEFAULT_CMD_TIMEOUT")
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


def getLogger(flg):
    LOG_LEVEL = logging.DEBUG
    LOGGER = logging.getLogger(flg)
    LOGGER.setLevel(LOG_LEVEL)
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(LOG_LEVEL)
    stream_formatter = ColorFormatter("[%(asctime)s] %(message)s")
    stream_handler.setFormatter(stream_formatter)
    LOGGER.addHandler(stream_handler)
    return LOGGER


global LOG
LOG = getLogger("utils")
