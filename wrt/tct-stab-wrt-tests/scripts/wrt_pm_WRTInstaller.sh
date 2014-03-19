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
#        Yue, jianhui <jianhuix.a.yue@intel.com>
path=$(dirname $(dirname $0))
source $path/scripts/xwalk_common.sh
if [ $# != 1 ];then
    echo "Need to add the parameter"
    exit 1
fi

path=$(dirname $(dirname $0))
PACKAGENAME="$path/$1"
p_name=$1
APP_NAME=${p_name%.*}
find_app $APP_NAME
for i in `seq 100`;do
    pkgnum=`echo "$pkgids"|wc -w`
    if [ $pkgnum -ge 1 ]; then
      uninstall_app $pkgids
      find_app $APP_NAME
      pkgnum=`echo "$pkgids"|wc -w`
      if [ $pkgnum -ge 1 ]; then
        echo "fail to uninstall widget"
        exit 1
      fi
    fi
    install_app $PACKAGENAME
    find_app $APP_NAME
    pkgnum=`echo "$pkgids"|wc -w`
    if [ $pkgnum -lt 1 ]; then
      echo "The installation is failed"
      exit 1
    else
      echo "The widget is installed successfully"
      if [ $i -eq 30 ];then
          uninstall_app $pkgids
          exit 0
      fi
    fi
done
