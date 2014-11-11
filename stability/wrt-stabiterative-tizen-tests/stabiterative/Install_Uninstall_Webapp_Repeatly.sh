#!/bin/bash
#
# Copyright (C) 2010 Intel Corporation
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
#
# Author:
# 

path=$(dirname $(dirname $0))
PACKAGENAME=$path/"launch_exist_test.wgt"
source $path/stabiterative/xwalk_common.sh
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

