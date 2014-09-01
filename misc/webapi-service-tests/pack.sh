#!/bin/bash
source $(dirname $0)/webapi-service-tests.spec
SRC_ROOT=$(cd $(dirname $0);pwd)
BUILD_ROOT=/tmp/$name

usage="Usage: ./pack.sh [-a <apk runtime arch: x86 | arm>]"

arch="x86"
while getopts a: o
do
    case "$o" in
    a) arch=$OPTARG;;
    *) echo "$usage"
       exit 1;;
    esac
done

rm -rf $SRC_ROOT/*.zip

# clean
function clean_workspace(){
    echo "cleaning workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    rm -rf $BUILD_ROOT
}

echo "cleaning workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
clean_workspace
mkdir -p $BUILD_ROOT

## creat apk ##
cp -a $SRC_ROOT/icon.png     $BUILD_ROOT/
cp -ar $SRC_ROOT/../../tools/crosswalk $BUILD_ROOT/crosswalk

cd $BUILD_ROOT/crosswalk
python make_apk.py --package=org.xwalk.$appname --name=$appname --app-url=http://127.0.0.1:8080/index.html --icon=$BUILD_ROOT/icon.png --mode=embedded --arch=$arch
if [ $? -ne 0 ];then
    echo "Create $name.apk fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi

## cp tests.xml and inst.sh ##
mkdir -p $BUILD_ROOT/opt/$name
cp $SRC_ROOT/inst.py $BUILD_ROOT/opt/$name/inst.py

for list in $LIST;do
    suite=`basename $list`
    cp $SRC_ROOT/../../../crosswalk-test-suite/webapi/$list/tests.xml  $BUILD_ROOT/opt/$name/$suite.tests.xml
    sed -i "s/<suite/<suite widget=\"$name\"/g" $BUILD_ROOT/opt/$name/$suite.tests.xml
    cp $SRC_ROOT/../../../crosswalk-test-suite/webapi/$list/tests.full.xml  $BUILD_ROOT/opt/$name/$suite.tests.full.xml
    sed -i "s/<suite/<suite widget=\"$name\"/g" $BUILD_ROOT/opt/$name/$suite.tests.full.xml
done

## creat zip package ##
mv $BUILD_ROOT/crosswalk/*.apk $BUILD_ROOT/opt/$name/
cd $BUILD_ROOT

if [ -f $BUILD_ROOT/opt/$name/WebapiServiceTests_$arch.apk ];then
    mv $BUILD_ROOT/opt/$name/WebapiServiceTests_$arch.apk $BUILD_ROOT/opt/$name/webapi_service_tests.apk
fi

zip -Drq $BUILD_ROOT/$name-$version-$sub_version.apk.zip opt/
if [ $? -ne 0 ];then
    echo "Create zip package fail... >>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi

# copy zip file
echo "copy package from workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
cp -f $BUILD_ROOT/$name-$version-$sub_version.apk.zip $SRC_ROOT/

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
