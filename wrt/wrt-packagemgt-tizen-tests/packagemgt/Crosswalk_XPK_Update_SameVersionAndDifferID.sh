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
xpk_path=$local_path/../testapp

func_check_xwalkservice

# install original xpk
install_origin_xpk  $xpk_path/update_original_versionOne_tests.xpk

#update valid xpk and check DB
exist_id=`xwalkctl | grep "diffid_same_version_tests" | awk '{print $1}'`
[ -n $exist_id ] & xwalkctl --uninstall $exist_id
xwalkctl --install $xpk_path/diffid_same_version_tests.xpk &> /tmp/install
cat /tmp/install | grep "Application installed"
if [[ $? -ne 0 ]]; then
    echo "The diffid_same_version_tests xpk  install failure."  
    exit 1
fi
 uninstall_xpk $app_id
 #get app id
 get_app_id

 uninstall_xpk $app_id

 exit 0
