#!/bin/bash
# Copyright (c) 2014 Intel Corporation.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# * Redistributions of works must retain the original copyright notice, this list
#   of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
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
#        Shen, Lin <linx.a.shen@intel.com>
#

local_path=$(dirname $0)
# Get current time as log file's name
logName=Android_SampleApp_Gallery_Install_Test_`date '+%Y%m%d%H%M'`.log
reportName="Android_SampleApp_Gallery_Install.result"
resultName="Android_SampleApp_Gallery_Install.result.log"

Gallery_APK=`cat $local_path/../SampleApp_Android.conf | grep "Sampleapp_Gallery_Android_name" | cut -d "=" -f 2`

test -f $local_path/../resources/$Gallery_APK

# Install
if [ $? -eq 0 ];then
   adb install -r $local_path/../resources/$Gallery_APK &> $local_path/../log/INSTALL_RESULT
   echo "install apk" 2>&1 >> $local_path/../log/$logName
   grep "Success" $local_path/../log/INSTALL_RESULT 2>&1 >> $local_path/../log/$logName
   if [ $? -eq 0 ];then
        echo "Gallery install successflly" >> $local_path/../log/result/$resultName
        echo "Crosswalk_SampleApp_Gallery_Install***************************** [Pass]" >> $local_path/../log/result/$resultName
        echo "Crosswalk_SampleApp_Gallery_Install                                 PASS" >> $local_path/../log/result/$reportName
        exit 0
   else
        echo "Gallery install fail" >> $local_path/../log/result/$resultName
        echo "Crosswalk_SampleApp_Gallery_Install***************************** [Fail]" >> $local_path/../log/result/$resultName
        echo "Crosswalk_SampleApp_Gallery_Install                                 FAIL" >> $local_path/../log/result/$reportName
        exit 1
   fi
else
   echo "Gallery APK not found in $local_path/../resources/installer/" >> $local_path/../log/result/$resultName
   echo "Crosswalk_SampleApp_Gallery_Install***************************** [Fail]" >> $local_path/../log/result/$resultName
   echo "Crosswalk_SampleApp_Gallery_Install                                FAIL" >> $local_path/../log/result/$reportName
   exit 1
fi
