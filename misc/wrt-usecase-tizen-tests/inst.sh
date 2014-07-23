#!/bin/bash

#parse params
USAGE="Usage: ./inst.sh [-i] [-u]
  -i install xpk and config environment
  -u uninstall xpk and remove source file
[-i] option was set as default."

PACKAGENAME=
XPKNAME=${PACKAGENAME}.wgt
RESOURCE_DIR=/home/app/content

function installpkg(){
#unzip -o crosswalk_support_wgt_tests.wgt.zip
#unzip -o crosswalk_support_xpk_tests.xpk.zip
for xpkfile in $(ls *.wgt)
do
 if [ ${xpkfile:0:14} = "update_version" ];then
    continue
 fi
 xwalkctl --install $(dirname $0)/$xpkfile
done
    #TODO: copy resource
    #eg:cp xx $RESOURCE_DIR
}

function uninstallpkg(){
    echo "Please uninstall by typing  xwalkctl --uninstall pkgid"

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
