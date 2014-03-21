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
source $(dirname $0)/Common
source $path/scripts/xwalk_common.sh
func_install Sample-widget.wgt
if [ $? -eq 1 ];then
  echo "The installation is failed"
  exit 1
fi

find_app Sample-widget
uninstall_app Sample-widget
if [ $? -eq 1 ];then
  echo "The uninstallation is failed"
  exit 1
fi

for pkgid in $pkgids
do
  xwalkctl --uninstall $pkgid 1>>/tmp/uninstaller.log 2>&1
done

RET3=`grep "invalid application id" /tmp/uninstaller.log `
if [ -z "$RET3"  ]; then
  echo -e  "informed failure of uninstallation failed!"
  rm -f /tmp/uninstaller.log
  exit 1
else
  echo -e  "informed failure of uninstallation successfully!"
  rm -f /tmp/uninstaller.log
  exit 0
fi
