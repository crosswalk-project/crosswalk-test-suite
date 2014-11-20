#!/bin/bash

path=$(dirname $(dirname $0))
xpksuite_name=wrt-manifest-tizen-tests
PACKAGENAME="$path/$1"
Result="Pass"


#2.**** launcher the app
pkgnum=`echo "$1"|wc -w`
if [ $pkgnum -eq 1 ]; then
   app_launcher -s $1 &>/dev/null &
 if [ $? -eq 1 ];then
  echo Launch Fail
  exit 1
 fi
 sleep 2s
 echo Launch ok
else
 echo no or more than one app launch failed
 exit 1
fi

pkgids=""
pkgnum=0

