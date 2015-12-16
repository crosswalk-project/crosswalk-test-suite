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
import shutil


class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_setup_cache_dir(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        if os.path.exists("cache"):
            shutil.rmtree("cache")
        os.mkdir("cache")
        os.environ["CROSSWALK_APP_TOOLS_CACHE_DIR"] = comm.XwalkPath + "cache"
        os.chdir(comm.XwalkPath + "cache")
        createcmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-app create org.xwalk.test" + comm.MODE + " --android-crosswalk=" + comm.crosswalkVersion + comm.ANDROID_TARGETS
        return_code = os.system(createcmd)
        crosswalklist = os.listdir(os.getcwd())
        os.environ["CROSSWALK_APP_TOOLS_CACHE_DIR"] = comm.XwalkPath
        os.chdir(comm.XwalkPath)
        shutil.rmtree("cache")
        self.assertEquals(return_code, 0)
        self.assertIn("crosswalk-13.42.319.5.zip", crosswalklist)

if __name__ == '__main__':
    unittest.main()
