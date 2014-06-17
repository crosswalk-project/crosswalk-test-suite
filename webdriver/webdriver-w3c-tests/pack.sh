#!/bin/bash

#parse params
usage="Usage: ./pack.sh"

if [[ $1 == "-h" || $1 == "--help" ]]; then
    echo "$usage"
    exit 1
fi

SRC_ROOT=$PWD
BUILD_ROOT=/tmp/webdriver_pack
BUILD_DEST=/tmp/webdriver

# check precondition
function check_precondition(){
    which $1 > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo "Error: no tool: $1"
        exit 1
    fi
}
check_precondition autoreconf
check_precondition gcc
check_precondition make

# clean
function clean_workspace(){
echo "cleaning workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
rm -rf $BUILD_ROOT $BUILD_DEST
}

clean_workspace
mkdir -p $BUILD_ROOT $BUILD_DEST

# copy source code
rm -rf *.apk *.tar.bz2 *.tar.gz *.zip
cp -arf $SRC_ROOT/* $BUILD_ROOT/


function create_apk(){
cd $BUILD_ROOT

# copy html to apk folder
find -name *.html |grep -v support |xargs -I% cp --parents % $BUILD_ROOT/support/XwalkDriverTest

cp -r $SRC_ROOT/../../tools/crosswalk $BUILD_ROOT/crosswalk

# enable remote debugging
temp=$BUILD_ROOT/crosswalk/app_src/src/org/xwalk/app/template/AppTemplateActivity.java
line=`sed -n '/super.onCreate/=' $temp | tail -n1`
sed -i "${line}s/.*/setRemoteDebugging(true);\n&/" $temp

cd $BUILD_ROOT/crosswalk
python make_apk.py --manifest=$BUILD_ROOT/support/XwalkDriverTest/manifest.json

if [ $? -ne 0 ];then
    echo "Create $name.apk fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi
}

# create apk
create_apk

# copy apk file
echo "copy package from workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
mv $BUILD_ROOT/crosswalk/*.apk $SRC_ROOT/


# clean workspace
clean_workspace

# validate
echo "checking result... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
if [ -z "`ls $SRC_ROOT | grep "\.apk"`" ];then
    echo "------------------------------ FAILED to build $name packages --------------------------"
    exit 1
fi

echo "------------------------------ Done to build $name packages --------------------------"
cd $SRC_ROOT
ls *.apk 2>/dev/null
