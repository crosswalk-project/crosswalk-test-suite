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

func_install_changename widget-version-1.wgt
if [ $? -eq 1 ];then
  echo "The installation is failed"
  exit 1
fi

func_launch widget-version.wgt
if [ $? -eq 1 ];then
  echo "The launch is failed"
  func_uninstall_changename widget-version-1.wgt
  exit 1
fi

find_app widget-version
mkdir /opt/home/app/.config/xwalk/applications/$pkgids/data
myPath="/opt/home/app/.config/xwalk/applications/$pkgids/data"
if [ ! -d $myPath ];then
  echo -e  "created folder data failed!"
  exit 1
fi

func_install_changename widget-version-1-1.wgt
if [ $? -eq 1 ];then
  echo "The installation is failed"
  func_uninstall_changename widget-version-1.wgt
  exit 1
fi

if [ -d $myPath ];then
  echo -e  "the case is fail because the folder data exist!"
  exit 1
else
  echo -e  "the case is pass because the folder data dose not exist!"
  func_uninstall_changename widget-version-1.wgt
  func_uninstall_changename widget-version-1-1.wgt
  echo "The two widgets are uninstalled successfully"
  exit 0
fi
