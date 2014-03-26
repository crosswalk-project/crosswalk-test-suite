#!/bin/bash
#
# Copyright (c) 2014 Intel Corporation.
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
#         Jiehua.Xiong <jiehuax.xiong@intel.com>

source $(dirname $0)/suite-list.sh

#parse params
usage="Usage: ./pack.sh [-t <package type: wgt | apk | crx | xpk>] [-m <apk mode: shared | embedded>] [-p <xpk platform: mobile | ivi>] [-a <apk runtime arch: x86 | arm>]
[-t apk] option was set as default.
[-m shared] option was set as default.
[-a x86] option was set as default.
[-p mobile] option was set as default"

if [[ $1 == "-h" || $1 == "--help" ]]; then
    echo "$usage"
    exit 1
fi

type="apk"
mode="shared"
arch="x86"
platform="mobile"
while getopts t:m:a:p: o
do
    case "$o" in
    t) type=$OPTARG;;
    m) mode=$OPTARG;;
    a) arch=$OPTARG;;
    p) platform=$OPTARG;;
    *) echo "$usage"
       exit 1;;
    esac
done

if [[ $type == "wgt" || $type == "apk" || $type == "crx" || $type == "xpk" ]];then
    echo "Create package with $type and raw source"
else
    echo "Sorry,$type is not support... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    echo "$usage"
    exit 1
fi

if [ $type == "apk" ];then
    pkg_folder="$type-$mode"
    SUITE=$APKSUITE
elif [ $type == "xpk" ];then
    SUITE=$XPKSUITE
    pkg_folder="$type"
else
    SUITE=$WGTSUITE
    pkg_folder="$type"
fi

root_dir=$PWD
rm -rf $pkg_folder
mkdir $pkg_folder

for suite in $SUITE;do
    cd $suite
    ./pack.sh -t $type -m $mode -p $platform -a $arch
    mv *.zip $root_dir/$pkg_folder
    cd $root_dir
done
