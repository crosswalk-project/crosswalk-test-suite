#!/bin/bash
# Program:
#       This program check data path
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
#
local_path=$(dirname $0)
source $local_path/Common.sh

#get current time as log file's name
logName=Crosswalk_Tizen_Data_Path_test_`date '+%Y%m%d%H%M'`.log
reportName="Crosswalk_Tizen_Test.result"
resultName="Crosswalk_Tizen_Test.result.log"

#run xwalk and use --data-path create folder in local
xwalk --run-as-service --data-path=mydata_path &> $local_path/log/INSTALL_RESULT &
sleep 5
#kill process
function_kill_process
cat $local_path/log/INSTALL_RESULT | grep "command not found"
if [ $? -eq 0 ];then
        echo "xwalk can not installed" >> $local_path/log/result/$resultName
        echo "Crosswalk_Tizen_Data_Path**************************[Fail]" >> $local_path/log/result/$resultName
        echo "Crosswalk_Tizen_Data_Path                     FAIL" >> $local_path/log/result/$reportName
        exit 1
else
        ls | grep mydata_path &>/dev/null
        if [ $? -eq 0 ];then
                echo "Use xwalk --run-as-service --data-path=mydata can create mydata folder successfully" >> $local_path/log/result/$resultName
                echo "Crosswalk_Tizen_Data_Path**************************************** [Pass]" >> $local_path/log/result/$resultName
                echo "Crosswalk_Tizen_Data_Path                                  PASS" >> $local_path/log/result/$reportName
                #delete mydata folder
                rm -rf mydata_path
                exit 0
        else
                echo "Use xwalk --run-as-service --data-path=mydata can not create mydata folder" >> $local_path/log/result/$resultName
                echo "Crosswalk_Tizen_Data_Path************************************* [Fail]" >> $local_path/log/result/$resultName
                echo "Crosswalk_Tizen_Data_Path                                   FAIL" >> $local_path/log/result/$reportName
                exit 1
        fi
fi
