#!/bin/bash
# Program:
#       This program xwalk uninstall web app
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

#get current time as log file's name
logName=Crosswalk_Tizen_Uninstall_WithAppRuning_test_`date '+%Y%m%d%H%M'`.log
reportName="Crosswalk_Tizen_Test.result"
resultName="Crosswalk_Tizen_Test.result.log"

#install xwalk web app
xwalkctl --install $local_path/sources/WebApp2.xpk &> $local_path/log/INSTALL_RESULT

#get app id
cat $local_path/log/INSTALL_RESULT | grep "OK" &> $local_path/log/INSTALL_RESULT.log
if [ $? -eq 0 ];then
        install_id=`head -1 $local_path/log/INSTALL_RESULT.log`
        echo $install_id &>> $local_path/log/$logName
        ID=${install_id##* }
        rm -f $local_path/log/INSTALL_RESULT.log &> /dev/null
else
        rm -f $local_path/log/INSTALL_RESULT.log &> /dev/null
        echo "The XPK installed Failure,so can not execute uninstall script" >> $local_path/log/result/$resultName
        echo "Crosswalk_Tizen_Uninstall_WithAppRuning************************************* [Fail]" >> $local_path/log/result/$resultName
        echo "Crosswalk_Tizen_Uninstall_WithAppRuning                                   FAIL" >> $local_path/log/result/$reportName
        exit 1
fi

echo "The web app id is:$ID" &>> $local_path/log/$logName
#run web app
xwalk-launcher $ID &> /dev/null &
sleep 3
#uninstall when web app running
xwalkctl --uninstall $ID &> $local_path/log/UNINSTALL_RESULT
sleep 5
cat $local_path/log/UNINSTALL_RESULT | grep "Application uninstalled successfully" &>> $local_path/log/$logName
if [ $? -ne 0 ];then
        rm -f $local_path/log/UNINSTALL_RESULT
        echo "XPK uninstall with app running unsuccessfully" >> $local_path/log/result/$resultName
        echo "Crosswalk_Tizen_Uninstall_WithAppRuning**********************************[Fail]" >> $local_path/log/result/$resultName
        echo "Crosswalk_Tizen_Uninstall_WithAppRuning                                    FAIL" >> $local_path/log/result/$reportName
        exit 1
else
        rm -f $local_path/log/UNINSTALL_RESULT
        echo "The xpk installed successfully and the interface display normally" >> $local_path/log/result/$resultName
        echo "Crosswalk_Tizen_Uninstall_WithAppRuning************************************* [Pass]" >> $local_path/log/result/$resultName
        echo "Crosswalk_Tizen_Uninstall_WithAppRuning                                  PASS" >> $local_path/log/result/$reportName
        exit 0
fi
