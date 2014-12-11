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
#       Wang, Hongjuan <hongjuanx.wang@intel.com>

local_path=$(dirname $0)
source $local_path/common

if [ "${command}""x" == "x" ];then
    exit 1
fi

#install webapp
cd $local_path
cd ../tools/crosswalk
for((i=0; i<100; i++)); do
echo $i
python make_apk.py --package=org.xwalk.test$i  --app-url=https://crosswalk-project.org --arch=x86 --name=test$i > /tmp/install.txt
$command install -r Test$i*.apk > /tmp/install.txt
$command shell am start -n org.xwalk.test$i/."Test"$i"Activity" > /tmp/install.txt
grep "Success" /tmp/install.txt
$command shell "top -n 1" | grep org.xwalk.test0 > /tmp/install.txt
grep "org.xwalk.test0" /tmp/install.txt
if [ $? -eq 0 ];then
    echo "Continue"
else
    echo "Finish test"
    for((j=0; j<$i+1; j++)); do
        $command uninstall org.xwalk.test$j
    done
    exit 0
fi
sleep 3
done
