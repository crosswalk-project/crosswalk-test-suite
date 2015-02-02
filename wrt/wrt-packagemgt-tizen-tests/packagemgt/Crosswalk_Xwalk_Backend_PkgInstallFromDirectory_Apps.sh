#!/bin/bash
#
# Copyright (C) 2015 Intel Corporation
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

path=$(cd $(dirname $0);pwd)
source $local_path/Common
webapptest="web_app_test"
PACKAGENAME=$path/../testapp/"$webapptest.wgt"

getPkgid $webapptest
get_uninstall_status=`pkgcmd -u -n $pkg_id -q`
get_install_status=`pkgcmd -i -t wgt -p $PACKAGENAME -q`
get_install_status=` echo $get_install_status | awk '{print $15}'`
echo $get_install_status
sleep 1
if [[ "$get_install_status" =~ "val[ok]" ]];then
     get_backend_status=`/usr/lib/xwalk/xwalk_backend -i $path/../testapp/ 2>&1`
     if [[ "$get_backend_status" =~ "Cannot install from directory" ]];then
        echo "Installation from directory is unsupported, ok"
        sleep 1
        getPkgid $webapptest
        get_uninstall_status=`pkgcmd -u -n $pkg_id -q`
        exit 0
     else
        echo "Installation from directory is supported, fail"
        exit 1
     fi
else
  echo "install fail"
  exit 1
fi
