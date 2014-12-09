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
#        Yue, jianhui <jianhuix.a.yue@intel.com>

if [ $# != 1 ];then
    echo "Need to add the parameter"
    exit 1
fi

path=$(dirname $(dirname $0))
PACKAGENAME="$path/$1"
p_name=$1
APP_NAME=${p_name%.*}
source $path/scripts/xwalk_common.sh
find_app $APP_NAME

pkgnum=`echo "$pkgids"|wc -w`
if [ $pkgnum -ge 1 ]; then
  uninstall_app $APP_NAME
  find_app $APP_NAME
pkgnum=`echo "$pkgids"|wc -w`
if [ $pkgnum -ge 1 ]; then
    echo "fail to uninstall widget"
    exit 1
  fi
fi
install_app $PACKAGENAME
find_app $APP_NAME
pkgnum=`echo "$pkgids"|wc -w`
if [ $pkgnum -ge 1 ]; then
  echo "The widget should not be installed"
  uninstall_app $APP_NAME
  exit 1
else
  echo "The widget is not installed successfully"
  exit 0
fi
