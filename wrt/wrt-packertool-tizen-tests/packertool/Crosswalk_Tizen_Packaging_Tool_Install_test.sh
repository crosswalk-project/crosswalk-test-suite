#!/bin/bash
# Program:
#       This program xwalk install web app
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
logName=Crosswalk_Tizen_Packaging_Tool_Install_test_`date '+%Y%m%d%H%M'`.log
reportName="Crosswalk_Tizen_Test.result"
resultName="Crosswalk_Tizen_Test.result.log"
PACKAGING_TOOL=`cat $local_path/../Crosswalk_wrt_BFT.conf | grep "Tizen_Packaging_tool_path" | cut -d "=" -f 2`

#APP_NAME=`function_get_xpm_name $logName`
APP_NAME=$(function_get_xpm_name $logName)
echo "APP=$APP_NAME"

function_creat_xpk $logName

#function_install_xwalk $logName

#push xpk to device
sdb shell "[ -e /$APP_NAME.xpk ] && rm -rf $APP_NAME.xpk"
sdb push $PACKAGING_TOOL/$APP_NAME.xpk /

#install xwalk web app
sdb shell "xwalkctl --install /$APP_NAME.xpk" &> $local_path/../log/INSTALL_RESULT
sleep 5
cat $local_path/../log/INSTALL_RESULT | grep "successfully" &>> $local_path/../log/$logName
if [ $? -eq 0 ];then
        echo "The xpk installed successfully" >> $local_path/../log/result/$resultName
        echo "Crosswalk_Tizen_Packaging_Tool_Install_Packed***************************** [Pass]" >> $local_path/../log/result/$resultName
        echo "Crosswalk_Tizen_Packaging_Tool_Install_Packed                             PASS" >> $local_path/../log/result/$reportName
        function_uninstall_xpk $logName
        rm $PACKAGING_TOOL/$APP_NAME.xpk
        sdb shell "rm /$APP_NAME.xpk"
        exit 0
else
        echo "The xpk installed unsuccessfully" >> $local_path/../log/result/$resultName
        echo "Crosswalk_Tizen_Packaging_Tool_Install_Packed**************************[Fail]" >> $local_path/../log/result/$resultName
        echo "Crosswalk_Tizen_Packaging_Tool_Install_Packed                            FAIL" >> $local_path/../log/result/$reportName
        exit 1
fi
