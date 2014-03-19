#!/bin/bash
# Program:
#       This program install web app
#
#Copyright (c) 2013 Intel Corporation.
#
#Redistribution and use in source and binary forms, with or without modification,
#are permitted provided that the following conditions are met:
#
#* Redistributions of works must retain the original copyright notice, this list
#  of conditions and the following disclaimer.
#* Redistributions in binary form must reproduce the original copyright notice,
#  this list of conditions and the following disclaimer in the documentation
#  and/or other materials provided with the distribution.
#* Neither the name of Intel Corporation nor the names of its contributors
#  may be used to endorse or promote products derived from this work without
#  specific prior written permission.
#
#THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
#AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
#INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
#BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
#OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
#EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Author:
#        IVAN CHEN <yufeix.chen@intel.com>

local_path=$(dirname $0)
source $local_path/Common.sh

#get current time as log file's name
logName=Crosswalk_Tizen_WebApp_Install_test_`date '+%Y%m%d%H%M'`.log
reportName="Crosswalk_Tizen_Test.result"
resultName="Crosswalk_Tizen_Test.result.log"
webapp1result=1

xwalkctl --install $local_path/sources/WebApp1.xpk &> $local_path/log/INSTALL_RESULT
echo "install WebApp1.xpk" 2>&1 >> $local_path/log/$logName
grep "successfully" $local_path/log/INSTALL_RESULT 2>&1 >> $local_path/log/$logName
if [ $? -eq 0 ];then
    webapp1result=0
    echo "WebApp1.xpk Installed successflly" >> $local_path/log/result/$resultName
fi

webapp1ID=$(function_uninstall_xpk $logName)

if [ $webapp1result -eq 0  ];then
    echo "Web APP Installed successfully" >> $local_path/log/result/$resultName
    echo "Crosswalk_Tizen_WebApp_Install****************************************** [Pass]" >> $local_path/log/result/$resultName
    echo "Crosswalk_Tizen_WebApp_Install                                  PASS" >> $local_path/log/result/$reportName
    xwalkctl --uninstall $webapp1ID
    exit 0
else
   echo "Web APP Installed failure" >> $local_path/log/result/$resultName
   echo "Crosswalk_Tizen_WebApp_Install******************************************* [Fail]" >> $local_path/log/result/$resultName
   echo "Crosswalk_Tizen_WebApp_Install                                   FAIL" >> $local_path/log/result/$reportName
   exit 1
fi
