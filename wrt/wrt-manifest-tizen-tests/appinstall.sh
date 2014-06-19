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
  #get installed app id
  pkgids=${pkgids:(-33):32}
  echo $pkgids
  pkgids=""
  pkgnum=0
  exit 0
fi



