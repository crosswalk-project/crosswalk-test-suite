#!/usr/bin/env python
#coding=utf-8

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
