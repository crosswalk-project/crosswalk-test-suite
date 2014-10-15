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

local_path_source=$(dirname $0)
WEB_APP_Gallery_PATH=`cat $local_path_source/../Crosswalk_wrt_BFT.conf | grep "Sampleapp_Gallery_Tizen_name" | cut -d "=" -f 2`
CROSSWALK_APK=`cat $local_path_source/../Crosswalk_wrt_BFT.conf | grep "Tizen_Crosswalk_Name" | cut -d "=" -f 2`
PACKAGING_TOOL=`cat $local_path_source/../Crosswalk_wrt_BFT.conf | grep "Tizen_Packaging_tool_path" | cut -d "=" -f 2`

function function_launch_xwalk()
{
  rm -rf $local_path_source/../log/LAUNCH_RESULT
  pkgcmd -l &> $local_path_source/../log/LAUNCH_RESULT &
  sleep 5
  cat $local_path_source/../log/LAUNCH_RESULT | grep "xwalk: command not found" &
}

function function_exit_xwalk()
{
  #ps xwalk process
  ps -ef | grep xwalk &>$local_path_source/../resources/PROCESS_FILE1
  awk '{print $2}' $local_path_source/../resources/PROCESS_FILE1 &> $local_path_source/../resources/PROCESS_FILE
  cat $local_path_source/../resources/PROCESS_FILE | while read allline
  do
    kill -9 $allline &>/dev/null
  done
  sleep 2
  ps -ef | grep xwalk
  rm -rf $local_path_source/../resources/PROCESS_FILE1
  rm -rf $local_path_source/../resources/PROCESS_FILE
}

function function_kill_process()
{
  #kill xwalk process
  ps -ef | grep xwalk &>$local_path_source/../resources/PROCESS_FILE1
  awk '{print $2}' $local_path_source/../resources/PROCESS_FILE1 &> $local_path_source/../resources/PROCESS_FILE
  cat $local_path_source/../resources/PROCESS_FILE | while read allline
  do
    kill -9 $allline &>/dev/null
  done
  rm -rf $local_path_source/../resources/PROCESS_FILE1
  rm -rf $local_path_source/../resources/PROCESS_FILE
}

function function_install_xwalk()
{
  #local_path_source=$(dirname $0)
  #get current time as log file's name
  #CROSSWALK_APK=`cat $local_path_source/../Crosswalk_wrt_BFT.conf | grep "Tizen_Crosswalk_Name" | cut -d "=" -f 2`
  #install xwalk rpm
  rpm -qa | grep cross  |xargs -I%  rpm -e % &> /dev/null
  rpm -ivh $local_path_source/../resources/$CROSSWALK_APK &>> $local_path_source/../log/$1
  sleep 2
  xwalk &> $local_path_source/../log/INSTALL_RESULT &
  sleep 5

  cat $local_path_source/../log/INSTALL_RESULT | grep "command not found" &>> $local_path_source/../log/$1
  if [ $? -eq 0 ];then
    return 1
  else
    function_kill_process
    return 0
  fi
}

function function_uninstall_xwalk()
{
  #local_path_source=$(dirname $0)
  #CROSSWALK_APK=`cat $local_path_source/../Crosswalk_wrt_BFT.conf | grep "Tizen_Crosswalk_Name" | cut -d "=" -f 2`
  #uninstall crosswalk
  rpm -qa | grep cross &> $local_path_source/../log/INSTALL_RESULT
  xwalk_rpm=`sed -n 1p $local_path_source/../log/INSTALL_RESULT` &>> $local_path_source/../log/$1
  #echo "Installed rpm is "$xwalk_rpm
  #echo "file name is "${CROSSWALK_APK%.*}
  rpm -e ${CROSSWALK_APK%.*}
  #RUN xwalk in background
  xwalk &>$local_path_source/../log/INSTALL_RESULT &
  sleep 2
  cat $local_path_source/../log/INSTALL_RESULT | grep "command not found" &>> $local_path_source/../log/$1
  #echo $?
  if [ $? -eq 0 ];then
    return 0
  else
    return 1
  fi
}

function function_get_xpm_name()
{
  #local_path_source=$(dirname $0)
  #WEB_APP_Gallery_PATH=`cat $local_path_source/../Crosswalk_wrt_BFT.conf | grep "Tizen_WebApp_1" | cut -d "=" -f 2`
  #get xpk's name
  APP_NAME=${WEB_APP_Gallery_PATH##*/}
  if [ -z "$APP_NAME" ];then
    temp=${APP_PATH%/*}
    APP_NAME=${temp##*/}
    echo "web app 1 name is $APP_NAME" &>> $local_path_source/../log/$1
  fi

  if [[ $# > 1 ]];then
    #delete files
    test -f $PACKAGING_TOOL/$APP_NAME.xpk
    if [ $? -eq 0 ];then
      files=`ls $PACKAGING_TOOL/$APP_NAME.xpk` &>> $local_path_source/../log/$1
      rm -rf $PACKAGING_TOOL/x.pem
      rm -rf $files
    fi
  fi
  echo "$APP_NAME"
}

function function_creat_xpk()
{
  #local_path_source=$(dirname $0)
  #PACKAGING_TOOL=`cat $local_path_source/../Crosswalk_wrt_BFT.conf | grep "Tizen_Packaging_tool_path" | cut -d "=" -f 2`
  #WEB_APP_Gallery_PATH=`cat $local_path_source/../Crosswalk_wrt_BFT.conf | grep "Tizen_WebApp_1" | cut -d "=" -f 2`

  #NAME=`function_get_xpm_name $1 delete_old_xpm`
  NAME=$(function_get_xpm_name $1 delete_old_xpm)

  #packaging XPK
  cd $PACKAGING_TOOL
  python make_xpk.py $WEB_APP_Gallery_PATH key.pem &>> $local_path_source/../log/$1
  sleep 5
  test -f $PACKAGING_TOOL/$NAME.xpk
  rm key.pem
  if [ $? -eq 0 ];then
    return 0
  else
    return 1
  fi
}

function function_uninstall_xpk()
{
  #local_path_source=$(dirname $0)
  #get app id
  cat $local_path_source/../log/INSTALL_RESULT | grep "OK" &> $local_path_source/../log/INSTALL_RESULT.log
  install_id=`head -1 $local_path_source/../log/INSTALL_RESULT.log`
  echo $install_id &>> $local_path_source/../log/$1
  ID=${install_id##* }
  rm -f $local_path_source/../log/INSTALL_RESULT.log &> /dev/null

  echo "$ID"

  #echo "The web app id is:$ID" &>> $local_path_source/../log/$1
  #install xwalk web app
  #xwalkctl --uninstall $ID &> $local_path_source/../log/UNINSTALL_RESULT
}
