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
#       Xu,Yuhan <yuhanx.xu@intel.com>

local_path=$(dirname $0)

function checkps()
{
    adb shell "ps | grep "$1"" > /tmp/check.txt
    process_info9=`awk '{print $9}' /tmp/check.txt |tr -d [[:space:]]`
    #echo "sencod=$process_info9"
    if [ "${process_info9}" == "$1" ];then
        return 0
    else
        return 1
    fi
}

#install webapp
adb install -r $local_path/../source/packagemgt*.apk > /tmp/install.txt
grep "Success" /tmp/install.txt

if [ $? -eq 0 ];then
    #launch app by terminal
    adb shell am start -a android.intent.action.View -n org.xwalk.packagemgt/.packagemgtActivity
    sleep 4
    checkps "org.xwalk.packagemgt"

    if [ $? -eq 0 ];then
        #install webapp2
        adb install -r $local_path/../source/apk2packagemgt*.apk > /tmp/install.txt
        grep "Success" /tmp/install.txt

        if [ $? -eq 0 ];then
            #launch app by terminal
            adb shell am start -a android.intent.action.View -n org.xwalk.apk2packagemgt/.apk2packagemgtActivity
            sleep 4
            checkps "org.xwalk.apk2packagemgt"

            if [ $? -eq 0 ];then
                adb uninstall org.xwalk.packagemgt
                adb uninstall org.xwalk.apk2packagemgt
                exit 0
            else
                exit 1
            fi
        else
            exit 1
        fi
    else
        exit 1
    fi
else
    exit 1
fi
