#!/bin/bash
# Program:
#       This program install & uninstall Crosswalk
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
local_path_source=$(dirname $0)
WEB_APP_1_PATH=`cat $local_path_source/../Crosswalk_wrt_BFT.conf | grep "Tizen_WebApp_1" | cut -d "=" -f 2`
CROSSWALK_RPM=`cat $local_path_source/../Crosswalk_wrt_BFT.conf | grep "Tizen_Crosswalk_Name" | cut -d "=" -f 2`
PACKAGING_TOOL=`cat $local_path_source/../Crosswalk_wrt_BFT.conf | grep "Tizen_Packaging_tool_path" | cut -d "=" -f 2`

function function_kill_process()
{
        #kill xwalk process
        sdb shell "ps -ef | grep xwalk" &> $local_path_source/../log/PROCESS_FILE1
        awk '{print $2}' $local_path_source/../log/PROCESS_FILE1 &> $local_path_source/../log/PROCESS_FILE
        cat $local_path_source/../log/PROCESS_FILE | while read allline
        do
                sdb shell "kill -9 $allline" &>/dev/null
        done
        rm -rf $local_path_source/../log/PROCESS_FILE1
        rm -rf $local_path_source/../log/PROCESS_FILE
}

function function_install_xwalk()
{
        sdb shell "rpm -qa | grep cross  |xargs -I%  rpm -e %" &> /dev/null
        sdb shell "[ -e $CROSSWALK_RPM ] && rm -rf $CROSSWALK_RPM"
        sdb push $local_path_source/../resources/installer/$CROSSWALK_RPM /
        sdb shell "rpm -ivh /$CROSSWALK_RPM" &>> $local_path_source/../log/$1
}

function function_get_xpm_name()
{
        #get xpk's name
        APP_NAME=${WEB_APP_1_PATH##*/}
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
        NAME=$(function_get_xpm_name $1 delete_old_xpm)

        #packaging XPK
        cd $PACKAGING_TOOL
        python make_xpk.py $WEB_APP_1_PATH key.pem &>> $local_path_source/../log/$1
        sleep 5
        test -f $PACKAGING_TOOL/$NAME.xpk
        if [ $? -eq 0 ];then
                rm key.pem
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
        echo $install_id &>> $local_path_source/../log/$logName
        ID=${install_id##* }
        rm -f $local_path_source/../log/INSTALL_RESULT.log &> /dev/null

        echo "The web app id is:$ID" &>> $local_path_source/../log/$1
        #install xwalk web app
        sdb shell "xwalkctl --uninstall $ID" &> $local_path_source/../log/UNINSTALL_RESULT
}
