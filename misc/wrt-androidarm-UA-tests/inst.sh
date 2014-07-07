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
    [ -d /home/app/content ] ||  mkdir -p /home/app/content
    [ -e $RESOURCE_DIR/$NAME.zip ] && rm -rf $RESOURCE_DIR/$NAME.zip
    [ -e $RESOURCE_DIR/opt/$NAME ] && rm -rf $RESOURCE_DIR/opt/$NAME
    cp -arf $local_path/$NAME.zip $RESOURCE_DIR/
    cd $RESOURCE_DIR/
    unzip $NAME.zip
    echo "Package unzip successfully and push to host $RESOURCE_DIR/"
}

function cleansource()
{
    [ -e $RESOURCE_DIR/opt/$NAME ] && rm -rf $RESOURCE_DIR/opt/$NAME
    [ -e $RESOURCE_DIR/$NAME.zip ] && rm -rf $RESOURCE_DIR/$NAME.zip
    echo "Clean folder successfully..."
}

case "$1" in
    -h|--help) echo "$USAGE"
               exit ;;
    -u) cleansource;;
    -e) unzippkg;;
    *) unzippkg;;
esac
