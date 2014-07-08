#!/bin/bash

path=$(dirname $(dirname $0))
xpksuite_name=wrt-manifest-tizen-tests
PACKAGENAME="$path/$1"
Result="Pass"

#3.****uninstall app
xwalkctl --uninstall $1
if [ $? -eq 1 ];then
  echo Uninstall Fail
  exit 1
else
  echo Uninstall $Result
  exit 0
fi
pkgids=""
pkgnum=0

