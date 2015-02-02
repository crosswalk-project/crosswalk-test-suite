#!/bin/bash
# Program:
#       This program install multiple web app
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
#        Yin, Haichao <haichaox.yin@intel.com>

local_path=$(cd $(dirname $0);pwd)
source $local_path/Common
xpk_path=$local_path/../testapp
firstApp="diffid_same_version_tests"
secondApp="update_original_versionOne_tests"

# install first xpk,if exists,uninstall first
getPkgid $firstApp
get_uninstall=`pkgcmd -u -n  $pkg_id -q`
pkgcmd -i -t xpk -p $xpk_path/$firstApp.xpk -q
getAppid $firstApp
if [[ -n $app_id ]]; then
                echo "Install $firstApp.xpk Pass"
        else
                echo "Install $firstApp.xpk Fail"
                exit 1
fi

# install second xpk,if exists,uninstall first
getPkgid $secondApp
get_uninstall=`pkgcmd -u -n  $pkg_id -q`
pkgcmd -i -t xpk -p $xpk_path/$secondApp.xpk -q
getAppid $secondApp
if [[ -n $app_id ]]; then
                echo "Install $secondApp.xpk Pass"
        else
                echo "Install $secondApp.xpk Fail"
                exit 1
fi

# uninstall above xpk no matter install successfully or failed for the two xpks
getPkgid $firstApp
get_uninstall=`pkgcmd -u -n  $pkg_id -q`
getAppid $firstApp
if [[ ! -n $app_id ]]; then
                echo "Uninstall $firstApp.xpk Pass"
        else
                echo "Uninstall $firstApp.xpk Fail"
                exit 1
fi
getPkgid $secondApp
get_uninstall=`pkgcmd -u -n  $pkg_id -q`
getAppid $secondApp
if [[ ! -n $app_id ]]; then
                echo "Uninstall $secondApp.xpk Pass"
                exit 0
        else
                echo "Uninstall $secondApp.xpk Fail"
                exit 1
fi

