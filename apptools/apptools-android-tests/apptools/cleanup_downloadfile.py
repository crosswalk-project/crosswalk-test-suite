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
#         Yun, Liu<yunx.liu@intel.com>

import unittest
import os
import commands
import comm
import thread
import time

result = 0

def update_project():
    global result
    updatecmd = comm.PackTools + "crosswalk-app update 11.40.268.0"
    updatestatus = commands.getstatusoutput(updatecmd)
    result = updatestatus[0]

def kill_ps():
    commands.getstatusoutput("ps -ef |grep update |grep 'crosswalk-app' |grep -v grep |awk '{print $2}' |xargs -I% kill -9 %")

def set_http():
    commands.getstatusoutput("export http_proxy=''")
    commands.getstatusoutput("export https_proxy=''")

class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_abort_download(self):
        global result
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        oldnamelist = len(os.listdir(os.getcwd()))
        thread.start_new_thread(update_project, ())
        time.sleep(15)
        thread.start_new_thread(kill_ps, ())
        newnamelist = len(os.listdir(os.getcwd()))
        comm.clear("org.xwalk.test")
        self.assertNotEquals(result, 0)
        self.assertEquals(oldnamelist, newnamelist)

    def test_download_fail(self):
        global result
        comm.setUp()
        comm.create(self)
        os.chdir('org.xwalk.test')
        oldnamelist = len(os.listdir(os.getcwd()))
        thread.start_new_thread(update_project, ())
        time.sleep(15)
        thread.start_new_thread(set_http, ())
        newnamelist = len(os.listdir(os.getcwd()))
        comm.clear("org.xwalk.test")
        self.assertNotEquals(result, 0)
        self.assertEquals(oldnamelist, newnamelist)

if __name__ == '__main__':
    unittest.main()
