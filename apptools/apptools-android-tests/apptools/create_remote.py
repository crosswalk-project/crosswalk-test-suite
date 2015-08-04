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
#         Hongjuan, Wang<hongjuanx.wang@intel.com>
#         Yun, Liu<yunx.liu@intel.com>

import unittest
import os
import comm
import shutil
import urllib2
import re
from bs4 import BeautifulSoup


class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_normal_with_downloadCrosswalk(self):
        comm.setUp()
        comm.clear("org.xwalk.test")
        os.chdir(comm.XwalkPath)
        createcmd = comm.HOST_PREFIX + comm.PackTools + "crosswalk-app create org.xwalk.test"
        return_code = os.system(createcmd)
        htmlDoc = urllib2.urlopen(
            'https://download.01.org/crosswalk/releases/crosswalk/android/stable/').read()
        soup = BeautifulSoup(htmlDoc)
        alist = soup.find_all('a')
        version = ''
        for  index in range(-1, -len(alist)-1, -1):
            aEle = alist[index]
            version = aEle['href'].strip('/')
            if re.search('[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*', version):
                break
        crosswalk = 'crosswalk-{}.zip'.format(version)
        namelist = os.listdir(os.getcwd())
        comm.clear("org.xwalk.test")
        self.assertIn(crosswalk, namelist)
        self.assertEquals(return_code, 0)

if __name__ == '__main__':
    unittest.main()
