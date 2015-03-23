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

import os
import sys
import commands
import shutil
import comm

def generate_unittest():
    try:
        flag = ''
        num = 0
        reportPath = os.path.join(comm.SCRIPT_DIR_NAME, '../report')
        comm.setUp()
        positive_datas = ['org.xwalk.tests', 'org.xwalk.t1234', 'org.example._xwalk', 'org.example.xwal_', 'org.example.te_st', 'org.xwalk.Tests', 'or_g.example.xwalk', 'org000.example.xwalk', '_org.example.xwalk', 'org.example123.xwalk']  
        negative_datas = ['org.xwalk', 'test', 'org.example.1234test', 'org.example.1234', '123org.example.xwalk', 'org.123example.xwalk']

        if os.path.exists(reportPath):
            shutil.rmtree(reportPath)
        os.mkdir(reportPath)
        pkgNameTestPath = os.path.join(comm.SCRIPT_DIR_NAME, "pkgName.py")
        if os.path.exists(pkgNameTestPath):
                os.remove(pkgNameTestPath)
        testfile = open(pkgNameTestPath,'a+')
        testfile.write(
            "#!/usr/bin/env python \n# coding=utf-8 \nimport random,os,sys,unittest,allpairs \nreload(sys) \nsys.setdefaultencoding( \"utf-8\" ) \nclass TestCaseUnit(unittest.TestCase): \n "
        )
                
        for positive_data in positive_datas:
            num += 1
            flag = 'positive' + str(num)
            cmd = positive_data
            casenum = "\n  def test_pkgName_" + flag + "(self):\n     self.assertEqual(\"PASS\", allpairs.tryRunApp(\"" + flag +"\", \"" + cmd+ "\"))"+ "\n"
            testfile.write(casenum)
        for negative_data in negative_datas:
            num += 1
            flag = 'negative' + str(num)
            cmd = negative_data
            casenum = "\n  def test_pkgName_" + flag + "(self):\n     self.assertEqual(\"PASS\", allpairs.tryRunApp(\"" + flag +"\", \"" + cmd+ "\"))"+ "\n"
            testfile.write(casenum)
        testfile.write("\nif __name__ == '__main__':\n    unittest.main()")
        testfile.close()
        os.system("chmod +x " + pkgNameTestPath)
    except Exception,e:
        print Exception,"Generate pkgName.py error:",e
        sys.exit(1)

def tryRunApp(item, projectName):
    try:
        comm.setUp()
        os.system("chmod 777 " + comm.TEMP_DATA_PATH)
        os.chdir(comm.TEMP_DATA_PATH)
        cmd = "crosswalk-app create " + projectName
        packstatus = commands.getstatusoutput(cmd)
        if 'ERROR' in packstatus[1]:
            print cmd + " deb file [Error]"
            print "Error message: ", packstatus[1] 
            result = 'FILE'
        else:
            print cmd + " deb file [O.K]"
            result = 'PASS'
        comm.cleanTempData(projectName)
        print '---------------------------------------------------------------'
        return result
    except Exception,e:
        print Exception,"Run pkgName.py error:",e
        sys.exit(1)

if __name__ == '__main__':
    generate_unittest()
