#!/bin/bash

path=$(dirname $(dirname $0))
xpksuite_name=wrt-manifest-tizen-tests
PACKAGENAME="$path/$1"
Result="Pass"
#1.**** install app
back=`pkgcmd -i -t xpk -p $1 -q`
if [ $? -eq 1 ];then
echo Install Fail
exit 1
else
echo $back
#get installed app id
pkgids=`pkgcmd -l | grep $1 | awk '{print $4}'`
pkgids=`echo $pkgids | awk '{print $1}'`
pkgids=${pkgids:1:-1}
echo $pkgids
pkgids=""
pkgnum=0
exit 0
fi
