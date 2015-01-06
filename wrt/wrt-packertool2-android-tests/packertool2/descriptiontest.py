#!/usr/bin/env python
#coding=utf-8
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

import unittest
import os, sys, commands, filecmp
import comm
reload(sys)
sys.setdefaultencoding( "utf-8" )

class TestPackertoolsFunctions(unittest.TestCase):
  def test_description(self):
      descPara = " --description=YourApplicationDescription"
      desc = '<string name="description">YourApplicationDescription</string>'
      comm.description(descPara, desc, self)

  def test_description_backslashSingleQuote(self):
      descPara = ' --description="\\\'description\\\'"'
      desc = '<string name="description">\\\'description\\\'</string>'
      comm.description(descPara, desc, self)

  def test_description_chinese(self):
      descPara = " --description='中文描述'"
      desc = '<string name="description">中文描述</string>'
      comm.description(descPara, desc, self)

  def test_description_doubleQuote(self):
      descPara = " --description=\'\"description\"\'"
      desc = '<string name="description">&quot;description&quot;</string>'
      comm.description(descPara, desc, self)

  def test_description_longString(self):
      descPara = " --description='abcdefghijklmnopqrstuvwxyznnnnabcdefghijklmnopqrstuvwxyznnnnabcdefghijklmnopqrstuvwxyznnnnabcdefghijklmnopqrstuvwxyznnnnabcdefghijklmnopqrstuvwxyznnnnabcdefghijklmnopqrstuvwxyznnnnabcdefghijklmnopqrstuvwxyznnnn'"
      desc = '<string name="description">abcdefghijklmnopqrstuvwxyznnnnabcdefghijklmnopqrstuvwxyznnnnabcdefghijklmnopqrstuvwxyznnnnabcdefghijklmnopqrstuvwxyznnnnabcdefghijklmnopqrstuvwxyznnnnabcdefghijklmnopqrstuvwxyznnnnabcdefghijklmnopqrstuvwxyznnnn</string>'
      comm.description(descPara, desc, self)

  def test_description_numOtherSymbol(self):
      descPara = " --description='0123456()[]{}-_=+:;,./?|<>'"
      desc = '<string name="description">0123456()[]{}-_=+:;,./?|&lt;&gt;</string>'
      comm.description(descPara, desc, self)

  def test_description_numSpace(self):
      descPara = " --description='0123456 '"
      desc = '<string name="description">0123456 </string>'
      comm.description(descPara, desc, self)

  def test_description_numSymbol(self):
      descPara = " --description='0123456()[]{}-_=+:;,./?|'"
      desc = '<string name="description">0123456()[]{}-_=+:;,./?|</string>'
      comm.description(descPara, desc, self)

  def test_description_symbol(self):
      descPara = " --description='~!@#$%^&*'"
      desc = '<string name="description">~!@#$%^&amp;*</string>'
      comm.description(descPara, desc, self)

  def test_description_singleQuote(self):
      comm.setUp()
      descPara = ' --description=\"\'description\'\"'
      appRoot = comm.ConstPath + "/../testapp/example/"
      os.chdir(appRoot)
      cmd = "python %smake_apk.py --package=org.xwalk.example --name=example --arch=%s --mode=%s --app-root=%s --app-local-path=index.html --project-dir=example" % \
            (comm.Pck_Tools, comm.ARCH, comm.MODE, appRoot)
      print cmd + descPara
      packstatus = commands.getstatusoutput(cmd + descPara)
      errorInfo = "exited with non-zero exit code 1"
      self.assertIn(errorInfo, packstatus[1])

if __name__ == '__main__':  
    unittest.main()
