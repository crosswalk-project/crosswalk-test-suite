#!/bin/bash
#
# Copyright (C) 2013 Intel Corporation
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# * Redistributions of works must retain the original copyright notice, this list
#   of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright notice,
#   this list of conditions and the following disclaimer in the documentation
#   and/or other materials provided with the distribution.
# * Neither the name of Intel Corporation nor the names of its contributors
#   may be used to endorse or promote products derived from this work without
#   specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors:
#        Zhang Ge <gex.zhang@intel.com>
#        Yin,Haichao <haichaox.yin@intel.com>

path=$(dirname $(dirname $0))
source $path/scripts/xwalk_common.sh
APP_NAME="app-widget-sample"
get_currentuser
function existbh()
{
  echo $1
  exit $2
}
$(dirname $0)/wrt_appwgt_installer.sh $APP_NAME.wgt
find_app $APP_NAME
if [ $? -ne 0 ];then
  exit 1
fi
widgetpath="/home/$TIZEN_USER/apps_rw/xwalk/applications/$appid"
if [ ! -d $widgetpath ];then
  uninstall_app $APP_NAME
  existbh "The path of the application does not exist." 1
fi
$(dirname $0)/wrt_appwgt_uninstaller.sh $APP_NAME.wgt
if [ $? -ne 0 ];then
  exit 1
fi
if [ -d $widgetpath ];then
  existbh "The WRT does not support Web AppWidget uninstallation." 1
else
  existbh "The WRT supports Web AppWidget uninstallation." 0
fi
