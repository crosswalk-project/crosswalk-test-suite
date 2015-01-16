#!/bin/bash
#
# Copyright (C) 2015 Intel Corporation
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
#        Mengli Zhang <mengli.zhang@samsung.com>
#

function existbh()
{
  echo $1
  pkgcmd -u -q -t wgt -n YD4zU83rK8
  exit $2
}
$(dirname $0)/wrt_appwgt_installer.sh sp-widget-only-author-signature.wgt YD4zU83rK8
if [ $? -ne 0 ]
then
  exit 1
fi
app_launcher -s YD4zU83rK8.spWidgetOnlyAuthorSignatur
sleep 2
widgetpath="/home/app/.config/xwalk-service/applications/YD4zU83rK8.spWidgetOnlyAuthorSignatur"
if [ ! -d $widgetpath ]
then
  existbh "The path of the application does not exist." 1
fi
filecount=$(ls -lR $widgetpath|grep "^-"|wc -l)
name=("config.xml" "icon.png" "index.html" "author-signature.xml")
if [ $filecount -eq 4  ]
then
  filename=$(ls $widgetpath)
  for var in ${filename[@]};do
    echo ${name[@]}|grep -q "$var"
    if [ $? -ne 0 ]
    then
      existbh "WRT does not support Web AppWidget installation." 1
    fi
  done
  indexcount=$(find $widgetpath -name index.html|wc -l)
  if [ $indexcount -ne 1  ]
  then
    existbh "WRT does not support Web AppWidget installation." 1
  fi
  existbh "WRT supports Web AppWidget installation." 0
else
  existbh "WRT does not support Web AppWidget installation." 1
fi
