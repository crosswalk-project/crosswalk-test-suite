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
import urllib2
import json
import shutil

class TestCrosswalkApptoolsFunctions(unittest.TestCase):
    def test_target_create(self):
        comm.setUp()
        if comm.SHELL_FLAG == "False":
            cmd = "where android"
        else:
            cmd = "which android"
        (return_code, androidpath) = comm.getstatusoutput(cmd)
        targetversionpath = os.path.dirname(os.path.dirname(androidpath[0]))
        os.chdir(targetversionpath)
        if os.path.exists(os.path.dirname(os.path.dirname(targetversionpath)) + "/platforms/"):
            shutil.rmtree(os.path.dirname(os.path.dirname(targetversionpath)) + "/platforms/")
        os.mkdir(os.path.dirname(os.path.dirname(targetversionpath)) + "/platforms/")
        movepath = os.path.dirname(os.path.dirname(targetversionpath))
        if comm.SHELL_FLAG == "False":
            os.system("xcopy /s /e /i /y platforms\* " + movepath + "\platforms")
        else:
            os.system("mv platforms/* " + movepath + "/platforms/")
        shutil.rmtree("platforms")
        comm.clear("org.xwalk.test")
        os.chdir(comm.XwalkPath)
        createcmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-app create org.xwalk.test" + comm.MODE + " --android-crosswalk=" + \
            comm.crosswalkzip
        (return_create_code, output) = comm.getstatusoutput(createcmd)
        os.chdir(movepath)
        os.mkdir(targetversionpath + "/platforms")
        if comm.SHELL_FLAG == "False":
            os.system("xcopy /s /e /i /y platforms\* " + targetversionpath + "\platforms")
        else:
            os.system("mv platforms/* " + targetversionpath + "/platforms/")
        shutil.rmtree("platforms")
        comm.clear("org.xwalk.test")
        self.assertNotEquals(return_create_code, 0)

    def test_target_build(self):
        comm.setUp()
        comm.clear("org.xwalk.test")
        os.chdir(comm.XwalkPath)
        comm.create(self)
        if comm.SHELL_FLAG == "False":
            cmd = "where android"
        else:
            cmd = "which android"
        (return_code, androidpath) = comm.getstatusoutput(cmd)
        targetversionpath = os.path.dirname(os.path.dirname(androidpath[0]))
        os.chdir(targetversionpath)
        if os.path.exists(os.path.dirname(os.path.dirname(targetversionpath)) + "/platforms/"):
            shutil.rmtree(os.path.dirname(os.path.dirname(targetversionpath)) + "/platforms/")
        os.mkdir(os.path.dirname(os.path.dirname(targetversionpath)) + "/platforms/")
        movepath = os.path.dirname(os.path.dirname(targetversionpath))
        if comm.SHELL_FLAG == "False":
            os.system("xcopy /s /e /i /y platforms\* " + movepath + "\platforms")
        else:
            os.system("mv platforms/* " + movepath + "/platforms/")
        shutil.rmtree("platforms")
        os.chdir(comm.XwalkPath)
        os.chdir('org.xwalk.test')
        buildcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app build"
        (return_build_code, buildstatus) = comm.getstatusoutput(buildcmd)
        os.chdir(movepath)
        os.mkdir(targetversionpath + "/platforms")
        if comm.SHELL_FLAG == "False":
            os.system("xcopy /s /e /i /y platforms\* " + targetversionpath + "\platforms")
        else:
            os.system("mv platforms/* " + targetversionpath + "/platforms/")
        shutil.rmtree("platforms")
        comm.clear("org.xwalk.test")
        self.assertNotEquals(return_build_code, 0)
        self.assertIn("project target", buildstatus[0])

if __name__ == '__main__':
    unittest.main()
