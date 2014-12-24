#!/bin/bash
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
#Authors:
#
path=$(dirname $(dirname $0))
SLEEP=86400
PACKAGENAME=$path/"3d_test.wgt"
APP_NAME="3d_test"
#source $path/longlasting/xwalk_common.sh
#pkgcmd -u -n thrdoptest -q
#pkgcmd -i -t wgt -p $PACKAGENAME -q

#monitor device info
echo "beging..."
get_pid=`ps aux | grep rscohn2.herokuapp | grep -v "grep" | head -n 1 | awk '{print $2}'`
kill $get_pid
$path/longlasting/sysmon-seperateRun.sh $SLEEP "rscohn2.herokuapp" &
sleep 2
nohup xwalk-launcher  http://rscohn2.herokuapp.com/sbp/ &>/dev/null &
launch_statue=`ps -aux | grep xwalk-launcher | grep -v grep | awk '{print $12}'`
if [[ "$launch_statue" =~ "herokuapp" ]];then
   sleep 86400
   get_pid=`ps -aux | grep rscohn2.herokuapp | grep -v "grep" | head -n 1 | awk '{print $2}'`
   echo "getpid="$get_pid
   kill $get_pid
   echo "end..."
   exit 0
else
    exit 1
fi
exit 1
