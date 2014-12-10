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
# Author:
#        IVAN CHEN <yufeix.chen@intel.com>

# install original xpk
local_path=$(cd $(dirname $0);pwd)
source $local_path/Common
xpk_path=$local_path/../testapp
app_id=`pkgcmd -l | grep "diffid_same_version_tests" | awk '{print $4}'`
app_id=`echo $app_id | awk '{print $1}'`
app_id=${app_id:1:-1}

get_uninstall=`pkgcmd -u -n  $app_id -q`
pkgcmd -i -t xpk -p  $xpk_path/diffid_same_version_tests.xpk -q
if [[ $? -eq 0 ]]; then
                echo "Install Pass"
        else
                echo "Install Fail"
                exit 1
fi
app_id1=`pkgcmd -l | grep "diffid_same_version_tests" | awk '{print $4}'`
app_id1=`echo $app_id1 | awk '{print $1}'`
app_id1=${app_id1:1:-1}

get_uninstall=`pkgcmd -u -n  $app_id1 -q`
if [[ $? -eq 0 ]]; then
                echo "Uninstall Pass"
        else
                echo "Unistall Fail"
                exit 1
fi
