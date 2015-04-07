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
#         Yin, Haichao<haichaox.yin@intel.com>

import os
import sys
import commands
import shutil
import time

SCRIPT_FILE_PATH = os.path.realpath(__file__)
SCRIPT_DIR_NAME = os.path.dirname(SCRIPT_FILE_PATH)
TEMP_DATA_PATH = os.path.join(SCRIPT_DIR_NAME, "../tempdata/")
TEST_PROJECT_COMM = "org.xwalk.testlinux"

def setUp():
    if not 'crosswalk-app' in os.environ.get('PATH'):
        print "Please set environment path for crosswalk-app"
        sys.exit(1)

    if not os.path.exists(TEMP_DATA_PATH):
        os.mkdir(TEMP_DATA_PATH)
        os.system("chmod +x " + TEMP_DATA_PATH)
    
def cleanTempData(removeFolder):
    removeFolder = os.path.join(TEMP_DATA_PATH, removeFolder)
    if os.path.exists(removeFolder):
        shutil.rmtree(removeFolder)

def delete():
    if os.path.exists(TEMP_DATA_PATH):
        os.chdir(SCRIPT_DIR_NAME)
        os.system("rm -R " + TEMP_DATA_PATH)

def create(self):
    try:
		setUp()
		os.chdir(TEMP_DATA_PATH)
		cleanTempData(TEST_PROJECT_COMM)
		cmd = "crosswalk-app create " + TEST_PROJECT_COMM
		packstatus = commands.getstatusoutput(cmd)
		self.assertEquals(packstatus[0], 0)
		self.assertIn(TEST_PROJECT_COMM, os.listdir(TEMP_DATA_PATH))
    except Exception,e:
        print Exception,"Create org.xwalk.testlinux error:",e
        sys.exit(1)

def build(self, cmd):
    buildstatus = commands.getstatusoutput(cmd)
    self.assertEquals(buildstatus[0], 0)
    self.assertIn("pkg", os.listdir(os.path.join(TEMP_DATA_PATH, TEST_PROJECT_COMM)))
    os.chdir('pkg')
    debs = os.listdir(os.getcwd())
    for deb in debs:
        print "The pkg deb is " + deb
        self.assertIn(".deb", deb)

def run(self):
    setUp()
    debs = os.listdir(os.getcwd())
    for deb in debs:
        project_name = deb.split("_")[0]

        print "Begin install deb file ", project_name
        status, output = commands.getstatusoutput("sudo dpkg -i " + deb)
        self.assertEquals(status, 0)
        
        print "Begin search deb file ", project_name
        status = commands.getstatusoutput("dpkg -l " + project_name)
        self.assertTrue(status)

        print "Begin launch deb file ", project_name
        os.system(project_name + " & sleep 5")
        # wait 3 second, then check application is running
        time.sleep(3)

        status, output = commands.getstatusoutput("ps -ef | grep " \
            + project_name + " | grep -v \"grep\" | wc -l")
        self.assertEquals(status, 0)

        # kill application
        status, output = commands.getstatusoutput("ps aux | grep xwalk | grep " + project_name + " | grep -v \"grep\"")
        for ps in output.split("\n"):
            for pid in ps.split(" "):
                if pid.isdigit():
                    os.kill(int(pid), 9)
                    break

        print "Begin uninstall deb file ", project_name
        status, output = commands.getstatusoutput("sudo dpkg -P " \
            + project_name)
        self.assertEquals(status, 0)
