#!/usr/bin/env python
#
# Copyright (c) 2016 Intel Corporation.
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
#         Zhu, Yongyong <yongyongx.zhu@intel.com>

import unittest
import os
import sys
import commands
import comm


class TestAppMultipleApkFalse(unittest.TestCase):

    def test_multiple_apk_false(self):
        comm.setUp()
        app_name = "testMultipleApk"
        pkg_name = " com.example." + app_name.lower()
        content = "<a href='http://www.intel.com'>Intel</a>\n</body>"
        key = "</body>"
        replace_index_list = [key, content]
        comm.create(
            app_name,
            pkg_name,
            comm.MODE,
            None,
            replace_index_list,
            self, None, "false")
        comm.build(app_name, 0, self, True, False)
        if comm.MODE == "embedded":
            comm.checkFileSize(os.path.join(comm.testapp_path, "%s.apk" % app_name), 40, 50, self)
        else:
            comm.checkFileSize(os.path.join(comm.testapp_path, "%s.apk" % app_name), 1, 5, self)
        comm.app_install(app_name, pkg_name, self)
        comm.app_launch(app_name, pkg_name, self)
        comm.app_stop(pkg_name, self)
        comm.app_uninstall(pkg_name, self)

if __name__ == '__main__':
    unittest.main()


