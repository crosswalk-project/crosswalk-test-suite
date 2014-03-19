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

func_install Sample-widget.wgt
if [ $? -eq 1 ];then
  echo "The installation is failed"
  exit 1
fi

func_launch Sample-widget.wgt
if [ $? -eq 1 ];then
  echo "The launch is failed"
  uninstall_app Sample-widget
  exit 1
fi

uninstall_app Sample-widget
if [ $? -eq 1 ];then
  echo "The uninstallation is failed"
  exit 1
fi

exit 0
