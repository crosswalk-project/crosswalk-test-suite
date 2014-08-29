#!/bin/bash

local_path=$(cd "$(dirname $0)";pwd)
NAME=$(basename $local_path)
RESOURCE_DIR=/home/app/content

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
    [ -d /home/app/content ] ||  mkdir -p /home/app/content
    [ -d $RESOURCE_DIR/opt/$NAME ] && rm -rf $RESOURCE_DIR/opt/$NAME
    [ -e $RESOURCE_DIR/$NAME.zip ] && rm -rf $RESOURCE_DIR/$NAME.zip
    cp $local_path/$NAME.zip $RESOURCE_DIR/
    cd $RESOURCE_DIR/;unzip $NAME.zip
    echo "Package unzip successfully and push to $RESOURCE_DIR/"
    chmod 777 $RESOURCE_DIR/opt/$NAME/$folderName/*.sh
    echo "Install webapp ..."
    adb install -r $RESOURCE_DIR/opt/$NAME/$folderName/Playvideo*.apk
}

function cleansource()
{
    adb uninstall org.xwalk.playvideo
    [ -d $RESOURCE_DIR/opt/$NAME ] && rm -rf $RESOURCE_DIR/opt/$NAME
    [ -e $RESOURCE_DIR/$NAME.zip ] && rm -rf $RESOURCE_DIR/$NAME.zip
    echo "Clean folder successfully..."
}

case "$1" in
    -h|--help) echo "$USAGE"
               exit ;;
    -u) cleansource;;
    -i) unzippkg;;
    *) unzippkg;;
esac
