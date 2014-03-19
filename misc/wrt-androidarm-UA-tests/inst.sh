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
    [ -d /opt/usr/media ] ||  mkdir -p /opt/usr/media
    [ -e /opt/usr/media/$NAME.zip ] && rm -rf /opt/usr/media/$NAME.zip
    [ -e /opt/usr/media/opt/$NAME ] && rm -rf /opt/usr/media/opt/$NAME
    cp -arf $local_path/$NAME.zip /opt/usr/media/
    cd /opt/usr/media/
    unzip $NAME.zip
    echo "Package unzip successfully and push to host /opt/usr/media/"
}

function cleansource()
{
    [ -e /opt/usr/media/opt/$NAME ] && rm -rf /opt/usr/media/opt/$NAME
    [ -e /opt/usr/media/$NAME.zip ] && rm -rf /opt/usr/media/$NAME.zip
    echo "Clean folder successfully..."
}

case "$1" in
    -h|--help) echo "$USAGE"
               exit ;;
    -u) cleansource;;
    -e) unzippkg;;
    *) unzippkg;;
esac
