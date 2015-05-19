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
import comm
import commands
import shutil

class TestCrosswalkApptoolsFunctions(unittest.TestCase):
    def test_setup_cache_dir(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        os.mkdir("cache")
        comm.create(self)
        os.environ["CROSSWALK_APP_TOOLS_CACHE_DIR"] = comm.XwalkPath + "cache"
        os.chdir('org.xwalk.test')
        updatecmd =  comm.PackTools + "crosswalk-app update 13.42.319.5"
        comm.update(self, updatecmd)
        namelist = os.listdir(os.getcwd())
        os.chdir(comm.XwalkPath + "cache")
        crosswalklist = os.listdir(os.getcwd())
        os.environ["CROSSWALK_APP_TOOLS_CACHE_DIR"] = comm.XwalkPath
        os.chdir(comm.XwalkPath)
        shutil.rmtree("cache")
        comm.clear("org.xwalk.test")
        self.assertNotIn("crosswalk-13.42.319.5.zip", namelist)
        self.assertIn("crosswalk-13.42.319.5.zip", crosswalklist)

if __name__ == '__main__':
    unittest.main()
