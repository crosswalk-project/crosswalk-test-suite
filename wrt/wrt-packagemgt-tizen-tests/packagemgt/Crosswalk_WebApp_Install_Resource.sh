#!/bin/bash
# Program:
#       This program install web app
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
# Authors:
#

local_path=$(cd $(dirname $0);pwd)
source $local_path/Common
xpk_path=$local_path/../testapp
pkg_id=`pkgcmd -l | grep "web_app_test" | awk '{print $4}'`
pkg_id=`echo $pkg_id | awk '{print $1}'`
pkg_id=${pkg_id:1:-1}
get_uninstall=`pkgcmd -u -n  webapptest -q`
rm -rf /home/app/.config/xwalk-service/Storage/ext/webapptest.webapptestversion
pkgcmd -i -t wgt -p  $xpk_path/web_app_test.wgt -q
if [[ $? -eq 0 ]]; then
                echo "Install Pass"
        else
                echo "Install Fail"
                exit 1
fi

myPath="/home/app/.config/xwalk-service/Storage/ext/webapptest.webapptestversion"
if [ ! -d $myPath ]; then 
     echo "Pass,webapp have not isolated storage partition before running"
     get_uninstall=`pkgcmd -u -n  webapptest -q`
     exit 0
  else
     echo "Fail,webapp have isolated storage partition"
     exit 1
fi
