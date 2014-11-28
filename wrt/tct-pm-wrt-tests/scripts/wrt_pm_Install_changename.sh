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

source $(dirname $0)/Common
origin_name=test-widget.wgt
change_name=test-widget-testing.wgt
if [ -f $path/$origin_name ];then
  mv $path/$origin_name $path/$change_name
else
  echo "The widget is not exist"
  exit 1
fi

func_install_changename test-widget-testing.wgt
if [ $? -eq 1 ];then
  echo "The installation is failed"
  mv $path/$change_name $path/$origin_name
  exit 1
fi

func_uninstall_changename test-widget-testing.wgt
mv $path/$change_name $path/$origin_name
echo "The widget is installed successfully"

exit 0
