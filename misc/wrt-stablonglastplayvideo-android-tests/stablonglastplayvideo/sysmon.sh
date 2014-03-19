#!/bin/bash
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

# Authors:
#    IVAN CHEN <yufeix.chen@intel.com>

sysmonFolder=$1"_sysmon_"`date '+%Y%m%d%H%M'`
mkdir /tmp/$sysmonFolder
echo "Create result folder: /tmp/$sysmonFolder"

times=`expr $2 / 10`
while [ $times -ne "0" ]
do
	echo `date` >> /tmp/$sysmonFolder/cpu.res
	echo `date` >> /tmp/$sysmonFolder/mem.res
	adb shell "dumpsys cpuinfo |grep $3" >> /tmp/$sysmonFolder/cpu.res
	adb shell "dumpsys meminfo |grep $3" | head -n 1 >> /tmp/$sysmonFolder/mem.res
	echo >> /tmp/$sysmonFolder/cpu.res
	echo >> /tmp/$sysmonFolder/mem.res
	echo "sysmon times = "$times >> /tmp/$sysmonFolder/times
	times=$(($times - 1))
	sleep 10
done

#kill self
kill -9 $$
