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

func_install lifecycle-launch-installed-app.wgt
if [ $? -eq 1 ];then
  echo "The installation of lifecycle-launch-installed-app.wgt is failed"
  exit 1
fi

func_install lifecycle-hide-running-app.wgt
if [ $? -eq 1 ];then
  echo "The installation of lifecycle-hide-running-app.wgt is failed"
  exit 1
fi

func_launch_other lifecycle-launch-installed-app.wgt
if [ $? -eq 1 ];then
  echo "The launch is failed"
  func_uninstall lifecycle-launch-installed-app.wgt
  func_uninstall lifecycle-hide-running-app.wgt
  exit 1
fi

func_uninstall lifecycle-launch-installed-app.wgt
func_uninstall lifecycle-hide-running-app.wgt

exit 0
