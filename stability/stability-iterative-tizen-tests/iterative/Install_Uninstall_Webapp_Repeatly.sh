#!/bin/bash
#
# Copyright (C) 2013 Intel Corporation
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
#

path=$(dirname $(dirname $0))
PACKAGENAME=$path/"launch_exist_test.wgt"

APP_NAME="launch_exist_test"
get_uninstall_status=`pkgcmd -u -n launchandt -q`
for (( i=1; i<=50; i=i+1 ))
do
  get_install_status=`pkgcmd -i -t wgt -p $PACKAGENAME -q`
  get_install_status=` echo $get_install_status | awk '{print $15}'`
  echo $get_install_status
  sleep 1
  if [[ "$get_install_status" =~ "val[ok]" ]];then
       get_uninstall_status=`pkgcmd -u -n launchandt -q`
       sleep 1
       if [[ "$get_install_status" =~ "val[ok]" ]];then
         echo "install/uninstall ok"
       else
         echo "install/uninstall fail"
         exit 1
       fi
  else
    echo "install fail"
    exit 1
  fi
done
exit 0

