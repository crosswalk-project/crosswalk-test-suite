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
}

function cleansource()
{
    [ -e $RESOURCE_DIR/tct/opt/$NAME ]
    if [ $? -ne 0 ];then
         echo "Please running "./inst.sh" to unzip package to local first ..."
         exit 1
    fi
}

case "$1" in
    -h|--help) echo "$USAGE"
               exit ;;
    -u) cleansource;;
    -e) unzippkg;;
    *) unzippkg;;
esac
