#!/bin/bash

local_path=$(cd "$(dirname $0)";pwd)
NAME=$(basename $local_path)
RESOURCE_DIR=/home/app/content

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
    [ -d /home/app/content ] ||  mkdir -p /home/app/content
    [ -e $RESOURCE_DIR/$NAME.zip ] && rm -rf $RESOURCE_DIR/$NAME.zip
    [ -e $RESOURCE_DIR/opt/$NAME ] && rm -rf $RESOURCE_DIR/opt/$NAME
    cp -arf $local_path/$NAME.zip $RESOURCE_DIR/
    cd $RESOURCE_DIR/
    unzip $NAME.zip
    echo "Package unzip successfully and push to host $RESOURCE_DIR/"

    if [ -e /tmp/Crosswalk_wrt_BFT.conf ];then
        cp -f /tmp/Crosswalk_wrt_BFT.conf $RESOURCE_DIR/opt/$NAME/
        #copy crosswalk to install folder:$RESOURCE_DIR/opt/$NAME/resources/installer
        ANDROID_CROSSWALK_PATH=`cat $RESOURCE_DIR/opt/$NAME/Crosswalk_wrt_BFT.conf | grep "Android_Crosswalk_Path" | cut -d "=" -f 2`
        cp $ANDROID_CROSSWALK_PATH $RESOURCE_DIR/opt/$NAME/resources/installer
    else
        echo "Error: Not found Crosswalk_wrt_BFT.conf >>>>>>>>>>>>>>>>>>>>>>>>."
        exit 1
    fi
}

function cleansource()
{
    [ -e $RESOURCE_DIR/opt/$NAME/Crosswalk_wrt_BFT.conf ]
    if [ $? -ne 0 ];then
         echo "Please running "./inst.sh" to unzip package to local first ..."
         exit 1
    fi
    [ -e $RESOURCE_DIR/opt/$NAME ] && rm -rf $RESOURCE_DIR/opt/$NAME
    [ -e $RESOURCE_DIR/$NAME.zip ] && rm -rf $RESOURCE_DIR/$NAME.zip
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
