#!/bin/bash
source $(dirname $0)/$(basename $(pwd)).spec

#parse params
usage="Usage: ./pack.sh [-t <package type: wgt | apk | crx | xpk | pure>] [-m <apk mode: shared | embedded>] [-p <xpk platform: mobile | ivi>]
[-t pure] option was set as default.
[-m shared] option was set as default.
[-p mobile] option was set as default."

if [[ $1 == "-h" || $1 == "--help" ]]; then
    echo "$usage"
    exit 1
fi

name_tmp=${name#*-}
name_xpk=${name_tmp%%-*}

type="xpk"
mode="shared"
platform="mobile"
while getopts t:m:p: o
do
    case "$o" in
    t) type=$OPTARG;;
    m) mode=$OPTARG;;
    p) platform=$OPTARG;;
    *) echo "$usage"
       exit 1;;
    esac
done

if [[ $type == "wgt" || $type == "apk" || $type == "crx" || $type == "xpk" || $type == "pure" ]];then
    echo "Create package with raw source"
    #echo "Create package with $type and raw source"
else
    echo "Sorry,$type is not support... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    echo "$usage"
    exit 1
fi

if [ $type == "xpk" ]; then
    xpkpacktooldir=$PWD/resources
fi

if [[ -z $name || -z $version || -z $appname ]];then
    echo "Package name or version not specified in setting file"
    exit 1
fi

SRC_ROOT=$PWD
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
check_precondition autoreconf
check_precondition gcc
check_precondition make

# clean
function clean_workspace(){
echo "cleaning workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
rm -rf $BUILD_ROOT $BUILD_DEST $OPT
}

clean_workspace
mkdir -p $BUILD_ROOT $BUILD_DEST

# copy source code
rm -rf *.rpm *.tar.bz2 *.tar.gz *.zip
cp -arf $SRC_ROOT/* $BUILD_ROOT/

# build
echo "build from workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
cd  $BUILD_ROOT
./autogen && ./configure --prefix=/usr && make && make install DESTDIR=$BUILD_DEST
if [ $? -ne 0 ];then
    echo "build fail,please check Makefile.am and cofigure.ac... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi
find $BUILD_DEST -name "Makefile*" -delete

## function for create wgt apk xpk ##
function create_xpk(){
cd $xpkpacktooldir
./bad_xpk_generator.sh $BUILD_ROOT/$name_xpk key
if [ $? -eq 0 ];then
    mv $name_xpk.xpk "bad_"$name_xpk.xpk
fi
rm key
./xpk_generator.sh $BUILD_ROOT/$name_xpk ee
if [ $? -ne 0 ];then
    echo "Create $name.xpk fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi
#clean middle files
rm ee
}

function zip_for_xpk(){
mv $xpkpacktooldir/"bad_"$name_xpk.xpk $BUILD_DEST/opt/$name/
mv $xpkpacktooldir/$name_xpk.xpk $BUILD_DEST/opt/$name/
cd $BUILD_DEST
if [ $src_file -eq 0 ];then
    for file in $(ls opt/$name |grep -v xpk);do
        if [[ "${whitelist[@]}" =~ $file ]];then
            echo "$file in whitelist,keep it..."
        else
            echo "Remove unnessary file:$file..."
            rm -rf opt/$name/$file
        fi
    done
fi
zip -Drq $BUILD_DEST/$name-$version.$type.zip opt/
if [ $? -ne 0 ];then
    echo "Create zip package fail... >>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi
}

## create wgt crx apk xpk and zip package ##
case $type in
    xpk) create_xpk
         zip_for_xpk;;
esac


# copy zip file
echo "copy package from workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
cp -f $BUILD_DEST/$name-$version.$type.zip $SRC_ROOT/$name-$version.$type.zip

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
