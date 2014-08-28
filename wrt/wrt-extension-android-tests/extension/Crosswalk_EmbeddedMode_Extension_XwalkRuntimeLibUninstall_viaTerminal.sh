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
    adb shell "ps | grep "org.xwalk.extension_permission_contacts_tests"" > /tmp/check.txt
    process_info9=`awk '{print $9}' /tmp/check.txt |tr -d [[:space:]]`
    #echo "sencod=$process_info9"
    if [ "${process_info9}" == "org.xwalk.extension_permission_contacts_tests" ];then
        return 0
    else
        return 1
    fi
}

if [ ! -f adb install $local_path/../resources/XWalkRuntimeLib.apk ];then
    echo "XWalk Runtime Library not found"
    exit 1
fi

adb install -r $local_path/../source/extension_*.apk > /tmp/install.txt
grep "Success" /tmp/install.txt

if [ $? -eq 0 ];then
    #Uninstall apk
    adb uninstall org.xwalk.runtime.lib > /tmp/uninstall.txt
    grep "Success" /tmp/uninstall.txt

    if [ $? -eq 0 ];then
        #launcher app by terminal
        adb shell am start -a android.intent.action.View -n org.xwalk.extension_permission_contacts_tests/.ExtensionPermissionContactsTestsActivity
        sleep 8
        checkps

        if [ $? -eq 0 ];then
            adb uninstall org.xwalk.extension_permission_contacts_tests
            adb install $local_path/../resources/XWalkRuntimeLib.apk
            exit 0
        else
            adb install $local_path/../resources/XWalkRuntimeLib.apk
            exit 1
        fi
    else
        exit 1
    fi
else
   exit 1
fi
