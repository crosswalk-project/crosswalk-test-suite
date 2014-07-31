#!/bin/bash

local_path=$(cd "$(dirname $0)";pwd)
NAME=$(basename $local_path)
RESOURCE_DIR=/home/app/content

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
    [ -d $RESOURCE_DIR/tct ] ||  mkdir -p $RESOURCE_DIR/tct
    [ -e $RESOURCE_DIR/tct/$NAME.zip ] && rm $RESOURCE_DIR/tct/$NAME.zip
    [ -e $RESOURCE_DIR/tct/opt/$NAME ] && rm -rf $RESOURCE_DIR/tct/opt/$NAME
    cp -arf $local_path/$NAME.zip $RESOURCE_DIR/tct/
    cd $RESOURCE_DIR/tct/
    unzip $NAME.zip
    echo "Package unzip successfully and push to host $RESOURCE_DIR/tct/"

    if [ -e /tmp/Crosswalk_wrt_BFT.conf ];then
        cp /tmp/Crosswalk_wrt_BFT.conf $RESOURCE_DIR/tct/opt/$NAME/
        #copy crosswalk to install folder:$RESOURCE_DIR/opt/$NAME/resources/installer
        ANDROID_CROSSWALK_PATH=`cat $RESOURCE_DIR/tct/opt/$NAME/Crosswalk_wrt_BFT.conf | grep "Tizen_Crosswalk_Path" | cut -d "=" -f 2`
        cp $ANDROID_CROSSWALK_PATH $RESOURCE_DIR/tct/opt/$NAME/resources/installer
    else
        echo "Error: Not found Crosswalk_wrt_BFT.conf >>>>>>>>>>>>>>>>>>>>>>>>."
        exit 1
    fi
}

function cleansource()
{
    [ -e $RESOURCE_DIR/tct/opt/$NAME/Crosswalk_wrt_BFT.conf ]
    if [ $? -ne 0 ];then
         echo "Please running "./inst.sh" to unzip package to local first ..."
         exit 1
    fi
    CROSSWALK_APK_NAME=`cat $RESOURCE_DIR/tct/opt/$NAME/Crosswalk_wrt_BFT.conf  | grep "Tizen_Crosswalk_Name" | cut -d "=" -f 2 | sed s/\.rpm//g`
    sdb shell "rpm -e $CROSSWALK_APK_NAME" &> /dev/null
    sdb shell "rpm -e tizen-extensions-crosswalk" &> /dev/null
    sdb shell "rm -rf $CROSSWALK_APK_NAME.rpm"
    [ -d $RESOURCE_DIR/tct/opt/$NAME ] && rm -rf $RESOURCE_DIR/tct/opt/$NAME
    [ -e $RESOURCE_DIR/tct/$NAME.zip ] && rm $RESOURCE_DIR/tct/$NAME.zip
    echo "Clean folder successfully..."
}

case "$1" in
    -h|--help) echo "$USAGE"
               exit ;;
    -u) cleansource;;
    -e) unzippkg;;
    *) unzippkg;;
esac
