#!/bin/bash

local_path=$(cd "$(dirname $0)";pwd)
NAME=$(basename $local_path)
RESOURCE_DIR=/home/app/content

#parse params
USAGE="Usage: ./inst.sh [-u] [-e]
  -i install wgt and config environment
  -u clean source file
  -e unzip package
[-e] option was set as default."

function unzippkg()
{
    #environment clear
    echo "environment clear >>>>>>>>>>>>>>>>>>>>>>>>>>>>>."
    sdb root on
    sdb shell "rpm -qa | grep cross  |xargs -I%  rpm -e %" &> /dev/null
    sdb shell "rpm -qa | grep extensions-crosswalk  |xargs -I%  rpm -e %" &> /dev/null
    unzip and push to device
    sdb shell "[ -d $RESOURCE_DIR/tct ] ||  mkdir -p $RESOURCE_DIR/tct"
    sdb shell "[ -d $RESOURCE_DIR/tct/opt/$NAME ] && rm -rf $RESOURCE_DIR/tct/opt/$NAME"
    sdb shell "[ -e $RESOURCE_DIR/tct/$NAME.zip ] && rm -rf $RESOURCE_DIR/tct/$NAME.zip"
    sdb push $local_path/$NAME.zip $RESOURCE_DIR/tct/
    sdb shell "cd $RESOURCE_DIR/tct/;unzip $NAME.zip"
    echo "Package unzip successfully and push to device $RESOURCE_DIR/tct/"
}

function cleansource()
{
    ### remove source file ###
    sdb root on
    sdb shell "rpm -qa | grep cross  |xargs -I%  rpm -e %" &> /dev/null
    sdb shell "rpm -qa | grep extensions-crosswalk  |xargs -I%  rpm -e %" &> /dev/null
    sdb shell "[ -d $RESOURCE_DIR/tct/opt/$NAME ] && rm -rf $RESOURCE_DIR/tct/opt/$NAME"
    sdb shell "[ -e $RESOURCE_DIR/tct/$NAME.zip ] && rm -rf $RESOURCE_DIR/tct/$NAME.zip"
    echo "Clean folder successfully..."
}

case "$1" in
    -h|--help) echo "$USAGE"
               exit ;;
    -u) cleansource;;
    -e) unzippkg;;
    *) unzippkg;;
esac
