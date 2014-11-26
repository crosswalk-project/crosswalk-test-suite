#!/bin/bash
# Program:
#       This program install & uninstall Crosswalk

# Copyright (c) 2013 Intel Corporation.

# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:

# * Redistributions of works must retain the original copyright notice, this list
#   of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# * Neither the name of Intel Corporation nor the names of its contributors
#   may be used to endorse or promote products derived from this work without
#   specific prior written permission.

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

# Author:
#        IVAN CHEN <yufeix.chen@intel.com>

local_path=$(dirname $0)
source $local_path/common

if [ "${command}""x" == "x" ];then
    exit 1
fi

CROSSWALK_APK=`cat $local_path/../Crosswalk_sharedmode.conf | grep "Crosswalk_Library_Name" | cut -d "=" -f 2`
CROSSWALK_PACKAGE=`cat $local_path/../Crosswalk_sharedmode.conf | grep "Crosswalk_Library_Package" | cut -d "=" -f 2`

test -f $local_path/../resources/installer/$CROSSWALK_APK &>/dev/null
#install
if [ $? -eq 0 ];then
    echo "XwalkRuntimeLibrary install"
    $command install -r $local_path/../resources/installer/$CROSSWALK_APK &>/dev/null
    $command shell pm list packages |grep $CROSSWALK_PACKAGE &>/dev/null
    if [ $? -eq 0 ];then
        echo "XwalkRuntimeLibrary install successflly"
        $command uninstall $CROSSWALK_PACKAGE &>/dev/null
        $command shell pm list packages |grep $CROSSWALK_PACKAGE &>/dev/null
        if [ $? -ne 0 ];then
            echo "XwalkRuntimeLibrary uninstall successflly"
            $command install -r $local_path/../resources/installer/$CROSSWALK_APK &>/dev/null
            exit 0
        else
            echo "XwalkRuntimeLibrary uninstall fail"
            exit 1
        fi
    else
        echo "XwalkRuntimeLibrary install fail"
        exit 1
    fi
else
    echo "XwalkRuntimeLibrary APK not found in $local_path/../resources/installer/"
    exit 1
fi
