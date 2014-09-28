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
  uninstall_app $APP_NAME
  exit $2
}
$(dirname $0)/wrt_sp02_installer.sh $APP_NAME.wgt
find_app $APP_NAME
if [ $? -ne 0 ]
then
  exit 1
fi
widgetpath="/home/app/.config/xwalk-service/applications/$pkgids"
if [ ! -d $widgetpath ]
then
  existbh "The path of the application does not exist." 1
fi
filecount=$(ls -lR $widgetpath|grep "^-"|wc -l)
name=("config.xml" "icon.png" "index.html")
if [ $filecount -eq 3  ]
then
  filename=$(ls -l $widgetpath | grep "^_")
  for var in ${filename[@]};do
    echo ${name[@]}|grep -q "$var"
    if [ $? -ne 0 ]
    then
      existbh "Application does not have its own localStorage space" 1
    fi
  done
  existbh "Application has its own localStorage space" 0
else
  existbh "Application does not have its own localStorage space" 1
fi
