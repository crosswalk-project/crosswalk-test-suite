#!/bin/bash

path=$(dirname $(dirname $0))
xpksuite_name=wrt-manifest-tizen-tests
PACKAGENAME="$path/$1"
Result="Pass"


#1.**** install app
pkgids=`pkgcmd -i -t xpk -p $1 -q`
if [ $? -eq 1 ];then
  echo Install Fail
  exit 1
else
  echo Install ok
  #get installed app id
  p=`pkgcmd -i -t xpk -p $1 -q`
  appid=`echo $p | awk '{print $7}'`
  pkgid=${appid:6:-1}
  echo $pkgids
  pkgids=""
  pkgnum=0
  exit 0
fi



