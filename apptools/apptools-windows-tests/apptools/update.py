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
import re
from bs4 import BeautifulSoup


class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_update_no_argument(self):
        comm.setUp()
        comm.create(self)
        updatecmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app update org.xwalk.test --windows-crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk
        (return_update_code, update_output) = comm.getstatusoutput(updatecmd)
        comm.clear("org.xwalk.test")
        self.assertIn("ERROR:", update_output[0])

    def test_update_beta(self):
        comm.setUp()
        comm.create(self)
        updatecmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app update beta org.xwalk.test --windows-crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk
        comm.update(self, updatecmd)
        comm.clear("org.xwalk.test")

    def test_update_canary(self):
        comm.setUp()
        comm.create(self)
        updatecmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app update canary org.xwalk.test --windows-crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk
        comm.update(self, updatecmd)
        comm.clear("org.xwalk.test")

    def test_update_stable(self):
        comm.setUp()
        comm.create(self)
        updatecmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app update stable org.xwalk.test --windows-crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk
        comm.update(self, updatecmd)
        comm.clear("org.xwalk.test")

    def test_update_invalid_channel(self):
        comm.setUp()
        comm.create(self)
        updatecmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app update channel org.xwalk.test --windows-crosswalk=" + comm.XwalkPath + comm.windowsCrosswalk
        (return_update_code, update_output) = comm.getstatusoutput(updatecmd)
        comm.clear("org.xwalk.test")
        self.assertIn("ERROR:", update_output[0])

if __name__ == '__main__':
    unittest.main()
