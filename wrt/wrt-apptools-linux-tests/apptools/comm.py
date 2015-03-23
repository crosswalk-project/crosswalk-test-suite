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

SCRIPT_FILE_PATH = os.path.realpath(__file__)
SCRIPT_DIR_NAME = os.path.dirname(SCRIPT_FILE_PATH)
TEMP_DATA_PATH = os.path.join(SCRIPT_DIR_NAME, "../tempdata/")
TEST_PROJECT_COMM = "org.xwalk.testlinux"

def setUp():
    if not 'crosswalk-app' in os.environ.get('PATH'):
        print "Please set environment path for crosswalk-app"
        sys.exit(1)
    
def cleanTempData(removeForder):
    removeForder = os.path.join(TEMP_DATA_PATH, removeForder)
    if os.path.exists(removeForder):
		shutil.rmtree(removeForder)

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
        projectName = deb.split('_')[0]
        cmdInstall = 'sudo dpkg -i ' + deb
        cmdSearchList = 'dpkg -l ' + projectName
        cmdLaunch = projectName
        cmdUninstall = 'sudo dpkg -P ' + projectName

        print "Begin install deb file " + deb
        instStatus = commands.getstatusoutput(cmdInstall)
        self.assertEquals(instStatus[0], 0)
        print "Begin search deb file " + projectName
        listStatus = commands.getstatusoutput(cmdSearchList)
        self.assertTrue(listStatus)
        print "Begin launch deb file " + projectName
        launchStatus = commands.getstatusoutput(cmdLaunch)
        self.assertEquals(launchStatus[0], 0)
        print "Begin uninstall deb file " + projectName
        uninstStatus = commands.getstatusoutput(cmdUninstall)
        self.assertEquals(uninstStatus[0], 0)

