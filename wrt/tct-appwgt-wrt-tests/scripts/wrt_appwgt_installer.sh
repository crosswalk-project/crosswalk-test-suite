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
#        Zhang Ge <gex.zhang@intel.com>

path=$(dirname $(dirname $0))
source $path/scripts/xwalk_common.sh
if [ $# != 1 ];then
    echo "Please add parameters packagename."
    exit 1
fi
PACKAGENAME="$path/$1"
p_name=$1
APP_NAME=${p_name%%.wgt}
find_app $APP_NAME
pkgnum=`echo "$pkgids"|wc -w`
if [ $pkgnum -ge 1 ]; then
then
  uninstall_app $APP_NAME
  find_app $APP_NAME
  pkgnum=`echo "$pkgids"|wc -w`
  if [ $pkgnum -ge 1 ]; then
  then
    echo -e  "Fail to uninstall the existed widget."
    exit 1
  fi
fi
install_app $PACKAGENAME
find_app $APP_NAME
pkgnum=`echo "$pkgids"|wc -w`
if [ $pkgnum -ge 1 ]; then
then
  echo -e  "The widget is installed successfully!"
  exit 0
else
  echo -e  "Fail to install the widget!"
  exit 1
fi
