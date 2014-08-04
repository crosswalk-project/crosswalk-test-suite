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
source $local_path/Common.sh

#get current time as log file's name
logName=Crosswalk_Tizen_Packaging_Tool_Uninstall_test_`date '+%Y%m%d%H%M'`.log
reportName="Crosswalk_Tizen_Test.result"
resultName="Crosswalk_Tizen_Test.result.log"

#APP_NAME=`function_get_xpm_name $logName`
APP_NAME=$(function_get_xpm_name $logName)

#check if the xpk create successfully
test -f $PACKAGING_TOOL/$APP_NAME.xpk
if [ $? -eq 1 ];then
        function_creat_xpk $logName
fi

#push xpk to device
sdb shell "[ -e /$APP_NAME.xpk ] && rm -rf $APP_NAME.xpk"
sdb push $PACKAGING_TOOL/$APP_NAME.xpk /

#install xwalk web app
sdb shell "xwalkctl --install /$APP_NAME.xpk" &> $local_path/../log/INSTALL_RESULT

function_uninstall_xpk $logName
sleep 5
cat $local_path/../log/UNINSTALL_RESULT | grep "successfully" &>> $local_path/../log/$logName
if [ $? -ne 0 ];then
        rm -f $local_path/../log/UNINSTALL_RESULT
        echo "XPK uninstall unsuccessfully" >> $local_path/../log/result/$resultName
        echo "Crosswalk_Tizen_Packaging_Tool_Uninstall_Packed**************************[Fail]" >> $local_path/../log/result/$resultName
        echo "Crosswalk_Tizen_Packaging_Tool_Uninstall_Packed                            FAIL" >> $local_path/../log/result/$reportName
        exit 1
else
        rm -f $local_path/../log/UNINSTALL_RESULT
        rm $PACKAGING_TOOL/$APP_NAME.xpk
        sdb shell "rm /$APP_NAME.xpk"
        echo "The xpk installed successfully" >> $local_path/../log/result/$resultName
        echo "Crosswalk_Tizen_Packaging_Tool_Uninstall_Packed***************************** [Pass]" >> $local_path/../log/result/$resultName
        echo "Crosswalk_Tizen_Packaging_Tool_Uninstall_Packed                           PASS" >> $local_path/../log/result/$reportName
        exit 0
fi
