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

import os
import sys
import commands
import shutil
import comm

def generate_cmd():
    comm.setUp()
    positive_data = ['org.xwalk.tests', 'org.xwalk.t1234', 'org.example._xwalk', 'org.example.xwal_', 'org.example.te_st', 'org.xwalk.Tests', 'or_g.example.xwalk', 'org000.example.xwalk', '_org.example.xwalk', 'org.example123.xwalk']
    negative_data = ['org.xwalk', 'test', 'org.example.1234test', 'org.example.1234', '123org.example.xwalk', 'org.123example.xwalk']
    flag = ''
    num = 0
    os.chdir(comm.ConstPath + '/../')
    if os.path.exists(comm.ConstPath + '/../report'):
        shutil.rmtree(comm.ConstPath + '/../report')
    os.mkdir('report')
    fp = open(comm.ConstPath + '/../report/cmd.txt', 'a+')
    for i in positive_data:
        num = num + 1
        flag = 'positive' + str(num)
        cmd = flag + '\tcrosswalk-app create ' + i + ' --crosswalk=/opt/wrt-apptools-android-tests/tools/crosswalk*.zip\n'
        #print cmd
        fp.write(cmd)
    for j in negative_data:
        num = num + 1
        flag = 'negative' + str(num)
        cmd = flag + '\tcrosswalk-app create ' + j + ' --crosswalk=/opt/wrt-apptools-android-tests/tools/crosswalk*.zip\n'
        #print cmd
        fp.write(cmd)

def generate_unittest():
    try:
        generate_cmd()
        fp = open(comm.ConstPath + '/../report/cmd.txt')
        if os.path.exists(comm.ConstPath + "/pkgNametest.py"):
            os.remove(comm.ConstPath + "/pkgNametest.py")
        testfile = open(comm.ConstPath + "/pkgNametest.py" ,'a+')
        testfile.write("#!/usr/bin/env python \n# coding=utf-8 \nimport random,os,sys,unittest,allpairs \nreload(sys) \nsys.setdefaultencoding( \"utf-8\" ) \nclass TestCaseUnit(unittest.TestCase): \n ")
        lines = fp.readlines()
        for line in lines:
            item = line.strip('\t\n')
            flag = item[:10].strip()
            cmd = item[10:].strip()
            #print flag, cmd[cmd.index("create")+6:].strip()[-5:]
            casenum = "\n  def test_pkgName_" + flag + "(self):\n     self.assertEqual(\"PASS\", allpairs.tryRunApp(\"" + flag +"\", \"" + cmd+ "\"))"+ "\n"
            testfile.write(casenum)
            testfile.flush()
        testfile.write("\nif __name__ == '__main__':\n    unittest.main()")
        testfile.close()
        os.system("chmod +x " + comm.ConstPath + "/pkgNametest.py")
    except Exception,e:
        print Exception,"Generate pkgNametest.py error:",e
        sys.exit(1)

def tryRunApp(item, cmd):
    try:
        comm.setUp()
        ToolsPath = comm.XwalkPath + comm.XwalkName
        fp = open(comm.ConstPath + '/../report/cmd.txt')
        lines = fp.readlines()
        for line in lines:
            item = line.strip('\t\n')
            flag = item[:10].strip()
            cmd = item[10:].strip()
            package = cmd[cmd.index("create")+6:cmd.index("--crosswalk")].strip()
            exec_cmd = comm.PackTools + cmd[:cmd.index("crosswalk=")+10].strip() + ToolsPath
            #print exec_cmd
            if 'negative' in flag:
                packstatus = commands.getstatusoutput(exec_cmd)
                if packstatus[0] != 0:
                    print "Genarate APK ---------------->O.K"
                    comm.clear(package)
                    result = 'PASS'
                    return result
                else:
                    print "Genarate APK ---------------->Error"
                    comm.clear(package)
                    return result
                    result = 'FILE'
            elif 'positive' in flag:
                packstatus = commands.getstatusoutput(exec_cmd)
                if packstatus[0] == 0:
                    print "Genarate APK ---------------->O.K"
                    comm.clear(package)
                    result = 'PASS'
                    return result
                else:
                    print "Genarate APK ---------------->Error"
                    comm.clear(package)
                    result = 'FILE'
                    return result
    except Exception,e:
        print Exception,"Generate pkgNametest.py error:",e
        sys.exit(1)

if __name__ == '__main__':
    generate_unittest()
