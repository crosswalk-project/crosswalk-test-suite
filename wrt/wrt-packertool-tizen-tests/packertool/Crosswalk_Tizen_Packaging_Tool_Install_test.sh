#!/bin/bash
# Program:
#       This program xwalk install web app
#
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
# Author:
#        IVAN CHEN <yufeix.chen@intel.com>
#
source $(dirname $0)/Common.sh
userid=`id -u`

local_path=$(dirname $0)
python $local_path/../make_xpk.py $local_path/../diffid_same_version_tests/ key.pem 
sleep 5
test -f diffid_same_version_tests.xpk
if [ $? -eq 0 ];then
                rm key.pem
                echo "Pass"
else
                echo "Fail"
                exit 1
fi

#push xpk to device
if [ $connect_type == "sdb" ];then
    sdb -s $device_id push diffid_same_version_tests.xpk /home/$TIZEN_USER/content/tct
    sdb -s $device_id push ./packertool/appinstall.sh /home/$TIZEN_USER/content/tct
    sdb -s $device_id root on
    sdb -s $device_id shell "su - $TIZEN_USER -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$userid/dbus/user_bus_socket;/home/$TIZEN_USER/content/tct/appinstall.sh'"
    echo $TIZEN_USER,$userid
    if [ $? -eq 0 ];then
      echo "Install xpk Pass"
      exit 0
    else
      exit 1
    fi
else
    scp diffid_same_version_tests.xpk $device_id:/home/$TIZEN_USER/content/tct
    scp ./packertool/appinstall.sh $device_id:/home/$TIZEN_USER/content/tct
    ssh $device_id "su - $TIZEN_USER -c 'export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/$userid/dbus/user_bus_socket;/home/$TIZEN_USER/content/tct/appinstall.sh'"
    if [ $? -eq 0 ];then
      echo "Install xpk Pass"
      exit 0
    else
      exit 1
    fi
fi





