#!/bin/bash
source $(dirname $0)/docroot.spec
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


SRC_ROOT=$(cd $(dirname $0);pwd)
BUILD_ROOT=/tmp/${name}_pack
BUILD_DEST=/tmp/${name}

# check precondition
function check_precondition(){
    which $1 > /dev/null 2>&1
    if [ $? -ne 0 ]; then
        echo "Error: no tool: $1"
        exit 1
    fi
}

# clean
function clean_workspace(){
    echo "cleaning workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    rm -rf $BUILD_ROOT $BUILD_DEST
}

clean_workspace
mkdir -p $BUILD_ROOT $BUILD_DEST/opt/$core_name

# copy source code
rm -rf $SRC_ROOT/*.zip
cp -arf $SRC_ROOT/* $BUILD_ROOT/

for list in $LIST;do
    python $SRC_ROOT/../../tools/build/pack.py -t apk-aio -m embedded -a $arch -d $BUILD_DEST/opt/$core_name -s $SRC_ROOT/../../webapi/$list
done

## creat testlist.json ##
echo "[
    {\"category\": \"W3C\", \"tests\":
        [" > $BUILD_ROOT/testlist.json
for suite in `ls $BUILD_DEST/opt/$core_name/opt |grep "\-tests" |grep -v spec$`;do
    echo "\"${suite}\","
done | sed '$s/,//' >>$BUILD_ROOT/testlist.json
echo "        ]
    }
]" >>$BUILD_ROOT/testlist.json


# build
echo "build from workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
cd  $BUILD_ROOT

## copy php files under cgi folder ##
for folder in `find $BUILD_DEST -type d -name cgi`;do
    parent_folder=`dirname $folder`
    cp -ar $folder/* $parent_folder/
done

## creat zip package ##
cp -a $BUILD_ROOT/webrunner/*     $BUILD_DEST/opt/$core_name/
cp -a $BUILD_ROOT/testlist.json     $BUILD_DEST/opt/$core_name/
cd $BUILD_DEST/opt
zip -Drq $BUILD_DEST/$core_name.zip $core_name/
if [ $? -ne 0 ];then
    echo "Create zip package fail... >>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi
rm -rf $BUILD_DEST/opt
cp -ar $BUILD_ROOT/inst.py $BUILD_DEST/inst.py
cd /tmp
zip -Drq $BUILD_DEST/$name-$version-$sub_version.apk.zip $name/

# copy zip file
echo "copy package from workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
cp -f $BUILD_DEST/$name-$version-$sub_version.apk.zip $SRC_ROOT/

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
