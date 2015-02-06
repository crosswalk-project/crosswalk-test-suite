#!/bin/bash
#
#Copyright (c) 2014 Intel Corporation.
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

#Authors:
#        Lin, Wanming <wanmingx.lin@intel.com>

###below functions just for crosswalk ivi testing###

##usage: install_app $app_path(e.g. uninstall_app /home/tizen_user/content/tct/opt/tct-sp02-wrt-tests/tct-sp02-wrt-tests.wgt, note:tizen_user is the current device normal user, "app" user on ivi, "guest" user on tizen commom)##

function get_currentuser(){
    TIZEN_USER=`whoami`
}

function install_app(){
    pkgcmd -i -t wgt -q -p $1
}

##usage: uninstall_app $app_name(e.g. uninstall_app tct-sp02-wrt-tests)##
function uninstall_app(){
    pkgids=`pkgcmd -l |grep $1 |awk -F "pkgid" '{print $2}' |awk -F '[' '{print $2}'|awk -F ']' '{print $1}'`
    for pkgid in $pkgids
    do
        pkgcmd -u -n $pkgid -q
    done
}

##usage: find_app $app_name(e.g. uninstall_app tct-sp02-wrt-tests)##
function find_appid(){
    appids=`app_launcher -l | grep $1 | awk '{print $2}'`
    appids=${appids:1:-1}
}

function find_app(){
    pkgids=`pkgcmd -l |grep $1 |awk -F "pkgid" '{print $2}' |awk -F '[' '{print $2}'|awk -F ']' '{print $1}'`
}


##usage: launch_app $app_name(e.g. launch_app tct-sp02-wrt-tests)##
function launch_app(){
    find_appid $1
    pkgnum=`echo "$appids"|wc -w`
    if [ $pkgnum -eq 1 ]; then
        nohup app_launcher -s $appids &>/dev/null &
    else
        echo "launch error, please check if exists this app or there are more than one app with this app_name"
    fi
}
