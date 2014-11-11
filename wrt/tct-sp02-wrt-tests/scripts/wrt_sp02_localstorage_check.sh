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
APP_NAME="private_localstorage_check"
function existbh()
{
  echo $1
  pkgcmd -u -n wrt5plc001 -q
  exit $2
}
$(dirname $0)/wrt_sp02_installer.sh $APP_NAME.wgt
find_app $APP_NAME
if [ $? -ne 0 ]
then
  exit 1
fi
open_app wrt5plc001.privatelocalstoragecheck
sleep 2
widgetpath="/home/app/.config/xwalk-service/Storage/ext/wrt5plc001.privatelocalstoragecheck"
if [ -d $widgetpath ]
then
  existbh "Application has its own localStorage space" 0
else
  existbh "Application does not have its own localStorage space" 1
fi
