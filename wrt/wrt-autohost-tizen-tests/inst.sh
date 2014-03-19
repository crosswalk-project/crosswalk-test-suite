#!/bin/bash

local_path=$(cd "$(dirname $0)";pwd)
NAME=$(basename $local_path)

#parse params
USAGE="Usage: ./inst.sh [-u] [-e]
  -u clean srouce file
  -e unzip package
[-e] option was set as default."

function unzippkg()
{
    #environment clear
    echo "environment clear >>>>>>>>>>>>>>>>>>>>>>>>>>>>>."
    sdb root on
    sdb shell "rpm -qa | grep cross  |xargs -I%  rpm -e %" &> /dev/null
    sdb shell "rpm -qa | grep extensions-crosswalk  |xargs -I%  rpm -e %" &> /dev/null
    [ -d /opt/usr/media/tct ] ||  mkdir -p /opt/usr/media/tct
    [ -e /opt/usr/media/tct/$NAME.zip ] && rm /opt/usr/media/tct/$NAME.zip
    [ -e /opt/usr/media/tct/opt/$NAME ] && rm -rf /opt/usr/media/tct/opt/$NAME
    cp -arf $local_path/$NAME.zip /opt/usr/media/tct/
    cd /opt/usr/media/tct/
    unzip $NAME.zip
    echo "Package unzip successfully and push to host /opt/usr/media/tct/"

    if [ -e /tmp/Crosswalk_wrt_BFT.conf ];then
        cp /tmp/Crosswalk_wrt_BFT.conf /opt/usr/media/tct/opt/$NAME/
        #copy crosswalk to install folder:/opt/usr/media/opt/$NAME/resources/installer
        ANDROID_CROSSWALK_PATH=`cat /opt/usr/media/tct/opt/$NAME/Crosswalk_wrt_BFT.conf | grep "Tizen_Crosswalk_Path" | cut -d "=" -f 2`
        cp $ANDROID_CROSSWALK_PATH /opt/usr/media/tct/opt/$NAME/resources/installer
    else
        echo "Error: Not found Crosswalk_wrt_BFT.conf >>>>>>>>>>>>>>>>>>>>>>>>."
        exit 1
    fi
}

function cleansource()
{
    [ -e /opt/usr/media/tct/opt/$NAME/Crosswalk_wrt_BFT.conf ]
    if [ $? -ne 0 ];then
         echo "Please running "./inst.sh" to unzip package to local first ..."
         exit 1
    fi
    CROSSWALK_APK_NAME=`cat /opt/usr/media/tct/opt/$NAME/Crosswalk_wrt_BFT.conf  | grep "Tizen_Crosswalk_Name" | cut -d "=" -f 2 | sed s/\.rpm//g`
    sdb shell "rpm -e $CROSSWALK_APK_NAME" &> /dev/null
    sdb shell "rpm -e tizen-extensions-crosswalk" &> /dev/null
    sdb shell "rm -rf $CROSSWALK_APK_NAME.rpm"
    [ -d /opt/usr/media/tct/opt/$NAME ] && rm -rf /opt/usr/media/tct/opt/$NAME
    [ -e /opt/usr/media/tct/$NAME.zip ] && rm /opt/usr/media/tct/$NAME.zip
    echo "Clean folder successfully..."
}

case "$1" in
    -h|--help) echo "$USAGE"
               exit ;;
    -u) cleansource;;
    -e) unzippkg;;
    *) unzippkg;;
esac
