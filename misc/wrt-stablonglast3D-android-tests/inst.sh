#!/bin/bash

local_path=$(cd "$(dirname $0)";pwd)
NAME=$(basename $local_path)

folderName_tmp=${NAME#*-}
folderName=${folderName_tmp%%-*}

#parse params
USAGE="Usage: ./inst.sh [-i] [-u]
  -u clean srouce file
  -i unzip package
[-i] option was set as default."

function unzippkg()
{
    #environment clear
    echo "environment clear >>>>>>>>>>>>>>>>>>>>>>>>>>>>>."
    #unzip and push to device
    [ -d /opt/usr/media ] ||  mkdir -p /opt/usr/media
    [ -d /opt/usr/media/opt/$NAME ] && rm -rf /opt/usr/media/opt/$NAME
    [ -e /opt/usr/media/$NAME.zip ] && rm -rf /opt/usr/media/$NAME.zip
    cp $local_path/$NAME.zip /opt/usr/media/
    cd /opt/usr/media/;unzip $NAME.zip
    echo "Package unzip successfully and push to /opt/usr/media/"
    chmod 777 /opt/usr/media/opt/$NAME/$folderName/*.sh
    echo "Install webapp ..."
    adb install -r /opt/usr/media/opt/$NAME/$folderName/dynamicddd*.apk
}

function cleansource()
{
    adb uninstall org.xwalk.dynamicddd
    [ -d /opt/usr/media/opt/$NAME ] && rm -rf /opt/usr/media/opt/$NAME
    [ -e /opt/usr/media/$NAME.zip ] && rm -rf /opt/usr/media/$NAME.zip
    echo "Clean folder successfully..."
}

case "$1" in
    -h|--help) echo "$USAGE"
               exit ;;
    -u) cleansource;;
    -i) unzippkg;;
    *) unzippkg;;
esac
