#!/bin/bash
# Program:
#       This program check packed apk install and basic function

# Copyright (c) 2013 Intel Corporation.

# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:

# * Redistributions of works must retain the original copyright notice, this list
#   of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# * Neither the name of Intel Corporation nor the names of its contributors
#   may be used to endorse or promote products derived from this work without
#   specific prior written permission.

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

# Author:
#        IVAN CHEN <yufeix.chen@intel.com>

local_path=$(dirname $0)

#get current time as log file's name
logName=Crosswalk_Android_Multiple_Packed_Install_Uninstall_test_`date '+%Y%m%d%H%M'`.log
reportName="Crosswalk_Android_Test.result"
resultName="Crosswalk_Android_Test.result.log"

PACKAGE_TOOL_PATH=`cat $local_path/../Crosswalk_wrt_BFT.conf | grep "Android_Packaging_tool_path" | cut -d "=" -f 2`
WEBAPP_1_HTML=`cat $local_path/../Crosswalk_wrt_BFT.conf | grep "Android_WebApp_1" | cut -d "=" -f 2`
WEBAPP_1=${WEBAPP_1_HTML%/*}
WEBAPP_2_HTML=`cat $local_path/../Crosswalk_wrt_BFT.conf | grep "Android_WebApp_2" | cut -d "=" -f 2`
WEBAPP_2=${WEBAPP_2_HTML%/*}

#apk name
apk_name_1="WebApp1"
#package name
package_name_1="com.xwalk.multiple.webapp1"

cd $PACKAGE_TOOL_PATH
python make_apk.py --name=$apk_name_1 --package=$package_name_1 --app-root=$WEBAPP_1 --app-local-path=$WEBAPP_1_HTML &>> $local_path/../log/$logName
#clean middle files
rm *.pyc
rm *.stam*
rm -r $apk_name_1

adb install -r $PACKAGE_TOOL_PATH/$apk_name_1*.apk &> $local_path/../log/INSTALL_RESULT
echo "install "$apk_name_1.apk &>> $local_path/../log/$logName
grep "Success" $local_path/../log/INSTALL_RESULT &>> $local_path/../log/$logName
if [ $? -ne 0 ];then
   echo "First packed apk install Failure" >> $local_path/../log/result/$resultName
   echo "Crosswalk_Android_Packaging_Tool_Install_Multople_Packed***************************** [Fail]" >> $local_path/../log/result/$resultName
   echo "Crosswalk_Android_Packaging_Tool_Install_Multople_Packed             FAIL" >> $local_path/../log/result/$reportName
   exit 1
fi

#apk name
apk_name_2="WebApp2"
#package name
package_name_2="com.xwalk.multiple.webapp2"

#cd $PACKAGE_TOOL_PATH
echo "build webapp2" &>> $local_path/../log/$logName
python make_apk.py --name=$apk_name_2 --package=$package_name_2 --app-root=$WEBAPP_2 --app-local-path=$WEBAPP_2_HTML &>> $local_path/../log/$logName
#clean middle files
rm *.pyc
rm *.stam*
rm -r $apk_name_2

adb install -r $PACKAGE_TOOL_PATH/$apk_name_2*.apk &> $local_path/../log/INSTALL_RESULT
echo "install $apk_name_2.apk" &>> $local_path/../log/$logName
grep "Success" $local_path/../log/INSTALL_RESULT &>>$local_path/../log/$logName
if [ $? -ne 0 ];then
   echo "Second packed apk install Failure">> $local_path/../log/result/$resultName
   echo "Crosswalk_Android_Packaging_Tool_Install_Multople_Packed***************************** [Fail]" >> $local_path/../log/result/$resultName
   echo "Crosswalk_Android_Packaging_Tool_Install_Multople_Packed             FAIL" >> $local_path/../log/result/$reportName
   exit 1
fi

#uninstall packed apk
adb uninstall $package_name_1 &> $local_path/../log/INSTALL_RESULT
adb uninstall $package_name_2 &> $local_path/../log/INSTALL_RESULT
grep "Success" $local_path/../log/INSTALL_RESULT &>>$local_path/../log/$logName
if [ $? -eq 0 ];then
    echo "Multiple packed APK installed successfully" >> $local_path/../log/result/$resultName
    echo "Crosswalk_Android_Packaging_Tool_Install_Multople_Packed***************************** [Pass]" >> $local_path/../log/result/$resultName
    echo "Crosswalk_Android_Packaging_Tool_Install_Multople_Packed             PASS" >> $local_path/../log/result/$reportName
    rm -rf $PACKAGE_TOOL_PATH/$apk_name_1*.apk
    rm -rf $PACKAGE_TOOL_PATH/$apk_name_2*.apk
    exit 0
else
    echo "Packed apk Uninstall Failure" >> $local_path/../log/result/$resultName
    echo "Crosswalk_Android_Packaging_Tool_Install_Multople_Packed***************************** [Fail]" >> $local_path/../log/result/$resultName
    echo "Crosswalk_Android_Packaging_Tool_Install_Multople_Packed             FAIL" >> $local_path/../log/result/$reportName
    exit 1
fi
