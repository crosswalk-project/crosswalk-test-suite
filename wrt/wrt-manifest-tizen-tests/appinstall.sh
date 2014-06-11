#!/bin/bash

path=$(dirname $(dirname $0))
xpksuite_name=wrt-manifest-tizen-tests
PACKAGENAME="$path/$1"
Result="Pass"


#1.**** install app
pkgids=`xwalkctl --install $path/$xpksuite_name/$1`
if [ $? -eq 1 ];then
  echo Install Fail
  exit 1
else
  echo Install ok
fi

#get installed app id
pkgids=${pkgids:(-33):32}

#2.**** launcher the app
pkgnum=`echo "$pkgids"|wc -w`
if [ $pkgnum -eq 1 ]; then
 nohup xwalk-launcher $pkgids &>/dev/null &
 if [ $? -eq 1 ];then
  echo Launch Fail
  exit 1
 fi
 sleep 15s
 echo Launch ok
else
 echo no or more than one app launch failed
 exit 1
fi

#3.****uninstall app
xwalkctl --uninstall $pkgids
if [ $? -eq 1 ];then
  echo Uninstall Fail
  exit 1
else
  echo Uninstall $Result
  exit 0
fi
pkgids=""
pkgnum=0

