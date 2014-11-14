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
PACKAGENAME=$path/"test_app.wgt"
APP_NAME="test_app"
get_uninstall_status=`pkgcmd -u -n testapp001 -q`
get_install_status=`pkgcmd -i -t wgt -p $PACKAGENAME -q`
get_install_status=` echo $get_install_status | awk '{print $15}'`
echo $get_install_status
sleep 1
if [[ "$get_install_status" =~ "val[ok]" ]];then
     get_uninstall_status=`pkgcmd -u -n testapp001 -q`
     sleep 1
     if [[ "$get_uninstall_status" =~ "val[ok]" ]];then
       echo "uninstall webapp ok"
     else
       echo "uninstall webapp fail"
       exit 1
     fi
else
  echo "uninstall fail"
  exit 1
fi
