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

import unittest
import sys
import os
import commands
import comm


class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_dir_exist(self):
        try:
            comm.setUp()
            os.chdir(comm.TEMP_DATA_PATH)
            os.mkdir(comm.TEST_PROJECT_COMM)
            cmd = "crosswalk-app create " + comm.TEST_PROJECT_COMM
            packstatus = commands.getstatusoutput(cmd)
            '''
            2048 return from packstatus, is directory already exist
            '''
            self.assertNotEquals(packstatus[0], 0)
            comm.cleanTempData(comm.TEST_PROJECT_COMM)
        except Exception as e:
            print Exception, "Create org.xwalk.testlinux error:", e
            sys.exit(1)

if __name__ == '__main__':
    unittest.main()
