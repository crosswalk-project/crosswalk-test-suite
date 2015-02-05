#!/bin/bash

path=$(dirname $(dirname $0))
PACKAGENAME="$path/$1"
Result="Pass"


#1.**** install app
pkgids=`pkgcmd -i -t xpk -p /home/$TIZEN_USER/content/tct/diffid_same_version_tests.xpk -q`
if [ $? -eq 1 ];then
  echo "Install Fail"
  exit 1
else
  echo "Install ok"
  app_id=`pkgcmd -l | grep diffid_same_version_tests | head -n 1 | awk '{print $4}'`
  app_id=`echo $app_id | awk '{print $1}'`
  app_id=${app_id:1:-1}
  pkgcmd -u -n  $app_id -q
  if [ $? -eq 0 ];then
      echo "Unintall Pass"
      exit 0
  else
      echo "Unintall Fail"
      exit 1
  fi
fi



