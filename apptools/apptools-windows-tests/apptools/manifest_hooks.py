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
#         Liu, Yun <yunx.liu@intel.com>

import unittest
import os
import comm
import shutil


class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_versionCode_normal(self):
        comm.setUp()
        os.chdir(comm.XwalkPath)
        comm.clear("org.xwalk.test")
        os.mkdir("org.xwalk.test")
        os.chdir('org.xwalk.test')
        shutil.copyfile(comm.ConstPath + "/../testapp/manifest_hooks/XWalkExtensionHooks.js", comm.ConstPath + "/../testapp/xwalk_echo_extension/extension/echo_extension/XWalkExtensionHooks.js")
        cmd = comm.HOST_PREFIX + comm.PackTools + \
            "crosswalk-pkg --platforms=windows --crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk + " " + comm.ConstPath + "/../testapp/xwalk_echo_extension/"
        (return_code, output) = comm.getstatusoutput(cmd)
        os.remove(comm.ConstPath + "/../testapp/extension_permission/contactextension/XWalkExtensionHooks.js")
        comm.clear("org.xwalk.test")
        preline = output[0].index('prePackage windows')
        pkgline = output[0].index('Package:')
        postline = output[0].index('postPackage windows')
        self.assertEquals(return_code, 0)
        self.assertIn("prePackage windows", output[0])
        self.assertIn("postPackage windows", output[0])
        self.assertTrue(postline > pkgline)
        self.assertTrue(pkgline > preline)

if __name__ == '__main__':
    unittest.main()
