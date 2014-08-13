#!/bin/bash

path=$(dirname $(dirname $0))
PACKAGENAME="$path/$1"
Result="Pass"


#1.**** install app
pkgids=`xwalkctl --install /home/app/content/tct/diffid_same_version_tests.xpk`
if [ $? -eq 1 ];then
  echo "Install Fail"
  exit 1
else
  echo "Install ok"
  webapp_id=`sqlite3 /home/app/.applications/dbspace/.app_info.db "select package from app_info where name like \"%diffid_same_version_tests%\";"`
  echo $webapp_id
  xwalkctl -u $webapp_id
  if [ $? -eq 0 ];then
      echo "Unintall Pass"
      exit 0
  else
      echo "Unintall Fail"
      exit 1
  fi
fi



