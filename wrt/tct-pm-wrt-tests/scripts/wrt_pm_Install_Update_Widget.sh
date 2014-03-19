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

func_install_changename WIdgetIDAppID-same1.wgt
if [ $? -eq 1 ];then
  echo "The installation is failed"
  exit 1
fi

func_install_changename WIdgetIDAppID-same2.wgt
if [ $? -eq 1 ];then
  echo "The installation is failed"
  exit 1
fi
echo "The widget is able to be updated when the widget has been installed."

func_uninstall_changename WIdgetIDAppID-same1.wgt
func_uninstall_changename WIdgetIDAppID-same2.wgt
echo "The two widgets are uninstalled successfully"

exit 0
