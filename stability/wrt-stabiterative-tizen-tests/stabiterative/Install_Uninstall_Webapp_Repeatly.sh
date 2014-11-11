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
PACKAGENAME="play_test.wgt"
source $path/stabiterative/xwalk_common.sh
APP_NAME="play_test"
uninstall_app $APP_NAME
for (( i=1; i<=50; i=i+1 ))
do
  install_app $PACKAGENAME
  sleep 1
  find_app $APP_NAME
  pkgnum=`echo "$pkgids"|wc -w`
  if [ $pkgnum -ge 1 ]; then
      uninstall_app $APP_NAME
  else
      exit 1
  fi
done
exit 0

