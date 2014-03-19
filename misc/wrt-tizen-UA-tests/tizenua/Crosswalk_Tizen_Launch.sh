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
logName=Crosswalk_Tizen_Launch_test_`date '+%Y%m%d%H%M'`.log
reportName="Crosswalk_Tizen_Launch_Test.result"
resultName="Crosswalk_Tizen_Launch_Test.result.log"
function_launch_xwalk $logName
xwalkcmd=`head -1 $local_path/../log/LAUNCH_RESULT`
if [ "${xwalkcmd##* }"x = "found"x ];then
  echo "xwalk launch unsuccessflly" >> $local_path/../log/result/$resultName
  echo "Crosswalk_Tizen_Launch***************************** [Fail]" >> $local_path/../log/result/$resultName
  echo "Crosswalk_Tizen_Launch                               FAIL" >> $local_path/../log/result/$reportName
  exit 1
else
  echo "xwalk install successflly" >> $local_path/../log/result/$resultName
  echo "Crosswalk_Tizen_Launch***************************** [Pass]" >> $local_path/../log/result/$resultName
  echo "Crosswalk_Tizen_Launch                               PASS" >> $local_path/../log/result/$reportName
  exit 0
fi
