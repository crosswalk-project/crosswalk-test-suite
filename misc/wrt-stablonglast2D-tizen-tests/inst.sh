#!/bin/bash

local_path=$(cd "$(dirname $0)";pwd)
NAME=$(basename $local_path)

folderName_tmp=${NAME#*-}
folderName=${folderName_tmp%%-*}

#parse params
USAGE="Usage: ./inst.sh [-i] [-u]
  -i install wgt and config environment
  -u uninstall wgt and remove source file
[-i] option was set as default."

function installpkg()
{
    #environment clear
    echo "environment clear >>>>>>>>>>>>>>>>>>>>>>>>>>>>>."
    pkgid=`pkgcmd -l | grep -i dynamic | grep -v Box | cut -d '[' -f3 | cut -d ']' -f1`
    xwalkctl --uninstall $pkgid > /dev/null 2>&1
    chmod 777 $local_path/$folderName/*.sh
    chmod 777 $local_path/$folderName/sysmon
    echo "Install webapp ..."
    [ -e /opt/usr/media/tct/opt/$NAME/$folderName/*.xpk ] || echo Not found xpk to install && xwalkctl --install /opt/usr/media/tct/opt/$NAME/$folderName/*.xpk 1> /tmp/installer.log 2>&1
    RET=`grep "Application installed" /tmp/installer.log`
    if [ -z "$RET"  ]
    then
      echo "Dynamic webapp installed failed!"
      exit 1
    else
      echo "Dynamic webapp installed successfully!"
    fi

    oldFolder=OldSysmon_`date '+%Y%m%d%H%M'`
    [ -e /tmp/sysmon.xml ] && mkdir /tmp/$oldFolder
    [ -d /tmp/$oldFolder ] && mv /tmp/sysmon* /tmp/$oldFolder/
}

function uninstallpkg(){
#clear resouce
if [ -d /opt/usr/media/tct/opt/$NAME ];then
    rm -rf /opt/usr/media/tct/opt/$NAME
else
    echo "Remove source file fail,please check if the source file exist: /opt/usr/media/tct/opt/$NAME ..."
fi
}

case "$1" in
    -h|--help) echo "$USAGE"
               exit ;;
    ""|-i) installpkg;;
    -u) uninstallpkg;;
    *) echo "Unknown option: $1"
       echo "$USAGE"
       exit ;;
esac
