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
#        Cao, Jenny <jenny.q.cao@intel.com>
#        Yue, jianhui <jianhuix.a.yue@intel.com>
#        Lin, Wanmnig <wanmingx.lin@intel.com>

path=$(dirname $(dirname $0))
source $path/scripts/xwalk_common.sh
if [ $# != 1 ];then
    echo "Please add parameter packagename!"
    exit 1
fi
PACKAGENAME="$path/widgetpackaging/w3c/$1"
p_name=$1
APP_NAME=${p_name%%.wgt}
find_app $APP_NAME
if [ ! -z "$pkgids"  ]
then
  uninstall_app $APP_NAME
  find_app $APP_NAME
  if [ ! -z "$pkgids"  ]
  then
    echo -e  "Fail to uninstall the existed widget!"
    exit 1
  fi
fi
install_app $PACKAGENAME
find_app $APP_NAME
if [ -z "$pkgids" ]
then
  echo -e  "Fail to install the widget!"
  exit 1
fi
launch_app $pkgids
App_Status=`xwalk-launcher -r $APPID | grep "not running"`
if [ -z $App_Status ];then
  echo "The widget is launched successfully"
  uninstall_app $APP_NAME
  exit 0
else
  echo "The widget is not launched"
  uninstall_app $APP_NAME
  exit 1
fi
