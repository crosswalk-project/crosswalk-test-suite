#!/bin/bash

local_path=$(cd "$(dirname $0)";pwd)
NAME=$(basename $local_path)
RESOURCE_DIR=/home/app/content

folderName_tmp=${NAME#*-}
folderName=${folderName_tmp%%-*}

#parse params
USAGE="Usage: ./inst.sh [-i] [-u]
  -i install wgt and config environment
  -u uninstall wgt and remove source file
[-i] option was set as default."

function installpkg()
{
    #environment clear
    echo "environment clear >>>>>>>>>>>>>>>>>>>>>>>>>>>>>."

    oldFolder=OldSysmon_`date '+%Y%m%d%H%M'`
    [ -e /tmp/sysmon.xml ] && mkdir /tmp/$oldFolder
    [ -d /tmp/$oldFolder ] && mv /tmp/sysmon* /tmp/$oldFolder/
}

function uninstallpkg()
{
#clear resouce
if [ -d $RESOURCE_DIR/tct/opt/$NAME ];then
    rm -rf $RESOURCE_DIR/tct/opt/$NAME
else
    echo "Remove source file fail,please check if the source file exist: $RESOURCE_DIR/tct/opt/$NAME ..."
fi
}

case "$1" in
    -h|--help) echo "$USAGE"
               exit ;;
    ""|-i) installpkg;;
    -u) uninstallpkg;;
    *) echo "Unknown option: $1"
       echo "$USAGE"
       exit ;;
esac
