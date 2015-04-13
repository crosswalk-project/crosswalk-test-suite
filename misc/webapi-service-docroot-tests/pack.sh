#!/bin/bash
source $(dirname $0)/docroot.spec
usage="Usage: ./pack.sh [-t <package type: apk | cordova>] [-a <apk runtime arch: x86 | arm>] [-m <package mode: embedded | shared>]
[-t apk] option was set as default.
[-a x86] option was set as default.
[-m embedded] option was set as default.
"

SRC_ROOT=$(cd $(dirname $0);pwd)
BUILD_ROOT=/tmp/${name}-${path_flag}_pack
BUILD_DEST=/tmp/${name}-${path_flag}

dest_dir=$SRC_ROOT
pack_type="apk"
arch="x86"
pack_mode="embedded"
while getopts a:t:m:d: o
do
    case "$o" in
    a) arch=$OPTARG;;
    t) pack_type=$OPTARG;;
    m) pack_mode=$OPTARG;;
    d) dest_dir=$OPTARG;;
    *) echo "$usage"
       exit 1;;
    esac
done


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
rm -rf $dest_dir/$name-$version-$sub_version.$pack_type.zip
rm -rf $SRC_ROOT/*.zip
cp -arf $SRC_ROOT/* $BUILD_ROOT/

if [ $pack_type == "cordova" ]; then
    for list in $LIST;do
        python $SRC_ROOT/../../tools/build/pack.py -t ${pack_type}-aio -m $pack_mode -d $BUILD_DEST/opt/$core_name -s $SRC_ROOT/../../webapi/$list
    done
else
    for list in $LIST;do
        python $SRC_ROOT/../../tools/build/pack.py -t ${pack_type}-aio -m $pack_mode -a $arch -d $BUILD_DEST/opt/$core_name -s $SRC_ROOT/../../webapi/$list
    done

fi

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
mkdir $path_flag
cp -a $BUILD_DEST $path_flag/${name}
cd $path_flag
zip -Drq $BUILD_DEST/$name-$version-$sub_version.$pack_type.zip ${name}
cd -
rm -rf $path_flag

# copy zip file
echo "copy package from workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
cd $SRC_ROOT
mkdir -p $dest_dir
cp -f $BUILD_DEST/$name-$version-$sub_version.$pack_type.zip $dest_dir

# clean workspace
clean_workspace

# validate
echo "checking result... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
if [ ! -f $dest_dir/$name-$version-$sub_version.$pack_type.zip ];then
    echo "------------------------------ FAILED to build $name packages --------------------------"
    exit 1
fi

echo "------------------------------ Done to build $name packages --------------------------"
cd $dest_dir
ls $name-$version-$sub_version.$pack_type.zip 2>/dev/null
