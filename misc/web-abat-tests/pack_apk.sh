#!/bin/bash
#parse params
usage="Usage: ./pack.sh [-l <pack apk-package tool's location>]"

if [[ $1 == "-h" || $1 == "--help" ]]; then
    echo $usage
    exit 1
fi

toollocation=''
while getopts l: o
do
    case "$o" in
    l) toollocation=$OPTARG;;
    *) echo $usage
       exit 1;;
    esac
done

if [ ! -e "$toollocation"/xwalk_app_template/make_apk.py ];then
    echo "Could not find the pack tool in $toollocation for creating apk-package."
    echo "$usage"
    exit 1
fi

source $(dirname $0)/web-abat-tests.spec
SRC_ROOT=$(cd $(dirname $0);pwd)
BUILD_ROOT=/tmp/$name
docroot_dir=/tmp/docroot_pack
rm -rf $SRC_ROOT/*.zip

# clean
function clean_workspace(){
    echo "cleaning workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    rm -rf $BUILD_ROOT $docroot_dir
}

echo "cleaning workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
clean_workspace
mkdir -p $BUILD_ROOT
cp -arf $SRC_ROOT/* $BUILD_ROOT/
## creat apk ##
cp -a $SRC_ROOT/icon.png     $BUILD_ROOT/
cp -ar $toollocation/xwalk_app_template $BUILD_ROOT/xwalk_app_template

cd $BUILD_ROOT/xwalk_app_template
python make_apk.py --package=org.xwalk.$appname --name=$appname --app-url=http://127.0.0.1:8080/index.html --icon=$BUILD_ROOT/icon.png --mode=embedded
if [ $? -ne 0 ];then
    echo "Create $name.apk fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi

## cp tests.xml and inst.sh ##
mkdir -p $BUILD_ROOT/opt/$name
cp $SRC_ROOT/inst.sh.apk $BUILD_ROOT/opt/$name/inst.sh
cp $SRC_ROOT/tests.xml.apk $BUILD_ROOT/opt/$name/tests.xml
cp $SRC_ROOT/COPYING $BUILD_ROOT/opt/$name/
#sed -i "s/<suite/<suite widget=\"$name\"/g" $BUILD_ROOT/opt/$name/tests.xml

## creat zip package ##
mv $BUILD_ROOT/xwalk_app_template/*.apk $BUILD_ROOT/opt/$name/
cd $BUILD_ROOT
zip -Drq $BUILD_ROOT/$name-$version.apk.zip opt/
if [ $? -ne 0 ];then
    echo "Create zip package fail... >>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi

# copy zip file
echo "copy package from workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
cp -f $BUILD_ROOT/$name-$version.apk.zip $SRC_ROOT/

mkdir -p $docroot_dir/docroot
cp $BUILD_ROOT/testkit/web/* $docroot_dir/docroot
mkdir -p $docroot_dir/docroot/opt/$name/abat
cp -r $BUILD_ROOT/abat/common/* $docroot_dir/docroot/opt/$name/abat
cp -r $BUILD_ROOT/resources $docroot_dir/docroot/opt/$name/abat
cp -r $BUILD_ROOT/testkit $docroot_dir/docroot/opt/$name
cp $BUILD_ROOT/tests.xml.apk $docroot_dir/docroot/opt/$name/tests.xml
cd $docroot_dir
zip -r docroot.zip docroot
rm -rf docroot/*
mv docroot.zip docroot
cp $BUILD_ROOT/inst.sh.docroot docroot/inst.sh
zip -r $SRC_ROOT/docroot_$version.apk.zip docroot


# clean workspace
clean_workspace

# validate
echo "checking result... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
if [ -z "`ls $SRC_ROOT | grep "\.zip"`" ];then
    echo "------------------------------ FAILED to build $name packages --------------------------"
    exit 1
fi

echo "------------------------------ Done to build $name packages --------------------------"
cd $SRC_ROOT
ls *.zip 2>/dev/null
