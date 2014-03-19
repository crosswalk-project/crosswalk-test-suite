#!/bin/bash

local_path=$(cd "$(dirname $0)";pwd)
NAME=$(basename $local_path)

#parse params
USAGE="Usage: ./inst.sh [-u] [-e]
  -u clean source file
  -e unzip package
[-e] option was set as default."

function unzippkg()
{
    #environment clear
    echo "environment clear >>>>>>>>>>>>>>>>>>>>>>>>>>>>>."
    adb uninstall org.xwalk.runtime.lib &> /dev/null
    [ -d /opt/usr/media ] ||  mkdir -p /opt/usr/media
    [ -e /opt/usr/media/$NAME.zip ] && rm -rf /opt/usr/media/$NAME.zip
    [ -e /opt/usr/media/opt/$NAME ] && rm -rf /opt/usr/media/opt/$NAME
    cp -arf $local_path/$NAME.zip /opt/usr/media/
    cd /opt/usr/media/
    unzip $NAME.zip
    echo "Package unzip successfully and push to host /opt/usr/media/"

    if [ -e /tmp/Crosswalk_wrt_BFT.conf ];then
        cp -f /tmp/Crosswalk_wrt_BFT.conf /opt/usr/media/opt/$NAME/
        #copy crosswalk to install folder:/opt/usr/media/opt/$NAME/resources/installer
        ANDROID_CROSSWALK_PATH=`cat /opt/usr/media/opt/$NAME/Crosswalk_wrt_BFT.conf | grep "Android_Crosswalk_Path" | cut -d "=" -f 2`
        cp $ANDROID_CROSSWALK_PATH /opt/usr/media/opt/$NAME/resources/installer
    else
        echo "Error: Not found Crosswalk_wrt_BFT.conf >>>>>>>>>>>>>>>>>>>>>>>>."
        exit 1
    fi
}

function cleansource()
{
    [ -e /opt/usr/media/opt/$NAME/Crosswalk_wrt_BFT.conf ]
    if [ $? -ne 0 ];then
         echo "Please running "./inst.sh" to unzip package to local first ..."
         exit 1
    fi
    [ -e /opt/usr/media/opt/$NAME ] && rm -rf /opt/usr/media/opt/$NAME
    [ -e /opt/usr/media/$NAME.zip ] && rm -rf /opt/usr/media/$NAME.zip
    adb uninstall org.xwalk.runtime.lib
    echo "Clean folder successfully..."
}

case "$1" in
    -h|--help) echo "$USAGE"
               exit ;;
    -u) cleansource;;
    -e) unzippkg;;
    *) unzippkg;;
esac
