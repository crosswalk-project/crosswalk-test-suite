#!/bin/bash

#Copyright (c) 2013 Intel Corporation.
#
#Redistribution and use in source and binary forms, with or without modification,
#are permitted provided that the following conditions are met:
#
#* Redistributions of works must retain the original copyright notice, this list
# of conditions and the following disclaimer.
#* Redistributions in binary form must reproduce the original copyright notice,
#  this list of conditions and the following disclaimer in the documentation
# and/or other materials provided with the distribution.
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
#Authors:
#       IVAN CHEN <yufeix.chen@intel.com>

local_path=$(cd $(dirname $0);pwd)
source $local_path/Common
get_currentuser
func_check_xwalkservice

pkgcmd -i -t xpk -p $local_path/../source/signature.xpk -q
app_name=`sqlite3 /home/$TIZEN_USER/.applications/dbspace/.app_info.db "select name from app_info where name like \"%signature%\";"`
app_id=`sqlite3 /home/$TIZEN_USER/.applications/dbspace/.app_info.db "select package from app_info where name like \"%signature%\";"`
if [[ $app_name =~ "signature" ]]; then
    echo "The signature.xpk install successfully"
    # uninstall xpk
    app_id=`pkgcmd -l | grep wrt-signature-tizen-tests | awk '{print $4}'`
    app_id=`echo $app_id | awk '{print $1}'`
    app_id=${app_id:1:-1}
    pkgcmd -u -n $app_id -q
    exit 0
else
   echo "Fail"
   exit 1
fi
