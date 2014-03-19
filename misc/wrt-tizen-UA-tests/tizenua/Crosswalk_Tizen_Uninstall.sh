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
source $local_path/Common_Gallery.sh

# Get current time as log file's name
logName=Crosswalk_Tizen_Uninstall_test_`date '+%Y%m%d%H%M'`.log
reportName="Crosswalk_Tizen_Test.result"
resultName="Crosswalk_Tizen_Test.result.log"

xwalk &>$local_path/../log/INSTALL_RESULT &
sleep 2
cat $local_path/../log/INSTALL_RESULT | grep "command not found" &>> $local_path/../log/logName
if [ $? -eq 0 ];then
  function_install_xwalk $logName

  if [ $? -eq 1 ];then
    echo "xwalk install unsuccessflly,install xwalk frist then uninstall it" >> $local_path/../log/result/$resultName
    echo "Crosswalk_Tizen_Launcher_UI_Uninstall***************************** [Fail]" >> $local_path/../log/result/$resultName
    echo "Crosswalk_Tizen_Launcher_UI_Uninstall                                 FAIL" >> $local_path/../log/result/$reportName
    exit 1
  fi
else
  function_kill_process
fi

function_uninstall_xwalk $logName

if [ $? -eq 0 ];then
  echo "xwalk uninstall successflly" >> $local_path/../log/result/$resultName
  echo "Crosswalk_Tizen_Launcher_UI_Uninstall***************************** [Pass]" >> $local_path/../log/result/$resultName
  echo "Crosswalk_Tizen_Launcher_UI_Uninstall                                 PASS" >> $local_path/../log/result/$reportName
  rpm -ivh $local_path/../resources/installer/$CROSSWALK_APK &>> $local_path_source/../log/$logName
  exit 0
else
  echo "xwalk uninstall unsuccessflly" >> $local_path/../log/result/$resultName
  echo "Crosswalk_Tizen_Launcher_UI_Uninstall***************************** [Fail]" >> $local_path/../log/result/$resultName
  echo "Crosswalk_Tizen_Launcher_UI_Uninstall                                 FAIL" >> $local_path/../log/result/$reportName
  exit 1
fi
