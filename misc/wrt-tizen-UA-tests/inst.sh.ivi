#!/bin/bash

local_path=$(cd "$(dirname $0)";pwd)
NAME=$(basename $local_path)

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
    sdb shell "[ -d /opt/usr/media/tct ] ||  mkdir -p /opt/usr/media/tct"
    sdb shell "[ -d /opt/usr/media/tct/opt/$NAME ] && rm -rf /opt/usr/media/tct/opt/$NAME"
    sdb shell "[ -e /opt/usr/media/tct/$NAME.zip ] && rm -rf /opt/usr/media/tct/$NAME.zip"
    sdb push $local_path/$NAME.zip /opt/usr/media/tct/
    sdb shell "cd /opt/usr/media/tct/;unzip $NAME.zip"
    echo "Package unzip successfully and push to device /opt/usr/media/tct/"
}

function cleansource()
{
    ### remove source file ###
    sdb root on
    sdb shell "rpm -qa | grep cross  |xargs -I%  rpm -e %" &> /dev/null
    sdb shell "rpm -qa | grep extensions-crosswalk  |xargs -I%  rpm -e %" &> /dev/null
    sdb shell "[ -d /opt/usr/media/tct/opt/$NAME ] && rm -rf /opt/usr/media/tct/opt/$NAME"
    sdb shell "[ -e /opt/usr/media/tct/$NAME.zip ] && rm -rf /opt/usr/media/tct/$NAME.zip"
    echo "Clean folder successfully..."
}

case "$1" in
    -h|--help) echo "$USAGE"
               exit ;;
    -u) cleansource;;
    -e) unzippkg;;
    *) unzippkg;;
esac
