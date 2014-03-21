#!/bin/bash

local_path=$(cd "$(dirname $0)";pwd)
NAME=$(basename $local_path)

folderName_tmp=${NAME#*-}
folderName=${folderName_tmp%%-*}

#parse params
USAGE="Usage: ./inst.sh [-i] [-u]
  -i install wgt and config environment
  -u uninstall wgt and remove source file
[-i] option was set as default."

function unzippkg()
{
    #environment clear
    echo "environment clear >>>>>>>>>>>>>>>>>>>>>>>>>>>>>."
    #unzip and push to device
    sdb shell "[ -d /opt/usr/media/tct ] ||  mkdir -p /opt/usr/media/tct"
    sdb shell "[ -d /opt/usr/media/tct/opt/$NAME ] && rm -rf /opt/usr/media/tct/opt/$NAME"
    sdb shell "[ -e /opt/usr/media/tct/$NAME.zip ] && rm -rf /opt/usr/media/tct/$NAME.zip"
    sdb push $local_path/$NAME.zip /opt/usr/media/tct/
    sdb shell "cd /opt/usr/media/tct/;unzip $NAME.zip"
    echo "Package unzip successfully and push to /opt/usr/media/tct/"

}

function cleansource()
{
    sdb shell "[ -d /opt/usr/media/tct/opt/$NAME ] && rm -rf /opt/usr/media/tct/opt/$NAME"
    sdb shell "[ -e /opt/usr/media/tct/$NAME.zip ] && rm -rf /opt/usr/media/tct/$NAME.zip"
    echo "Clean folder successfully..."
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
