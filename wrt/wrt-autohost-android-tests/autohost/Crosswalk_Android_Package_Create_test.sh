#!/bin/bash
# Program:
#       This program check package tools

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
logName=Crosswalk_Android_Package_Create_test_`date '+%Y%m%d%H%M'`.log
reportName="Crosswalk_Android_Test.result"
resultName="Crosswalk_Android_Test.result.log"

PACKAGE_TOOL_PATH=`cat $local_path/../Crosswalk_wrt_BFT.conf | grep "Android_Packaging_tool_path" | cut -d "=" -f 2` &>> $local_path/../log/$logName
echo "package tools path is " $PACKAGE_TOOL_PATH &>> $local_path/../log/$logName

#apk name
apk_name="TestApp"
#package name
package_name="com.xwalk.testapp"

#delete files
test -f $PACKAGE_TOOL_PATH/$apk_name*.apk
if [ $? -eq 0 ];then
    files=`ls $PACKAGE_TOOL_PATH/$apk_name*.apk` &>> $local_path/../log/$logName
    #echo $files
    rm -rf $files
    rm -rf $PACKAGE_TOOL_PATH/$apk_name*
fi

cd $PACKAGE_TOOL_PATH
python make_apk.py --name=$apk_name --package=$package_name --app-url=http://www.baidu.com &>> $local_path/../log/$logName

#clean middle files
rm *.pyc
rm *.stam*
rm -r $apk_name

ls $PACKAGE_TOOL_PATH/$apk_name*.apk
if [ $? -eq 0 ];then
   echo "Package generated successfully." >> $local_path/../log/result/$resultName
   echo "Crosswalk_Android_Packaging_Tool_Create_Package***************************** [Pass]" >> $local_path/../log/result/$resultName
   echo "Crosswalk_Android_Packaging_Tool_Create_Package                     PASS" >> $local_path/../log/result/$reportName
   rm -rf $PACKAGE_TOOL_PATH/$apk_name*.apk
   exit 0
else
  echo "Package generated Failure,the apk can't exist." >> $local_path/../log/result/$resultName
  echo "Crosswalk_Android_Packaging_Tool_Create_Package***************************** [Fail]" >> $local_path/../log/result/$resultName
  echo "Crosswalk_Android_Packaging_Tool_Create_Package                      FAIL" >> $local_path/../log/result/$reportName
  exit 1
fi
