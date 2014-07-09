#!/bin/bash
source $(dirname $0)/$(basename $(pwd)).spec

#parse params
usage="Usage: ./pack.sh [-t <package type: pure>]
[-t pure] option was set as default.
"

if [[ $1 == "-h" || $1 == "--help" ]]; then
    echo "$usage"
    exit 1
fi

type="pure"
while getopts t:m:a: o
do
    case "$o" in
    t) type=$OPTARG;;
    *) echo "$usage"
       exit 1;;
    esac
done

if [[ $type=="pure" ]];then
    echo "Create package with $type and raw source"
else
    echo "Sorry,$type is not support... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    echo "$usage"
    exit 1
fi

if [[ -z $name || -z $version || -z $appname ]];then
    echo "Package name or version not specified in setting file"
    exit 1
fi

SRC_ROOT=$PWD
BUILD_ROOT=/tmp/${name}_pack
BUILD_DEST=/tmp/$name

# clean
function clean_workspace(){
echo "cleaning workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
rm -rf $BUILD_DEST
}

clean_workspace
mkdir -p $BUILD_ROOT $BUILD_DEST/opt/$name

# copy source code
rm -rf *.rpm *.tar.bz2 *.tar.gz *.zip
cp -arf $SRC_ROOT/* $BUILD_ROOT

function create_pure(){
cp -r $BUILD_ROOT/allpairs $BUILD_DEST/opt/$name/allpairs
cp -r $BUILD_ROOT/metacomm $BUILD_DEST/opt/$name/metacomm
cp -r $BUILD_ROOT/report $BUILD_DEST/opt/$name/report
cp -r $BUILD_ROOT/tools $BUILD_DEST/opt/$name/tools
cp -r ../../tools/crosswalk $BUILD_DEST/opt/$name/tools/
cp -r $BUILD_ROOT/test.py $BUILD_DEST/opt/$name
cp -r $BUILD_ROOT/*.xml $BUILD_DEST/opt/$name
cd $BUILD_DEST
zip -rq $BUILD_DEST/opt/$name/$name.zip *
if [ $? -ne 0 ];then
    echo "Create $name.zip fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi
}

function zip_for_pure()
{
[ -e $SRC_ROOT/$name-$version.$type.zip ] && rm -rf $SRC_ROOT/$name-$version.$type.zip
cd $BUILD_DEST
if [ $src_file -eq 0 ];then
    for file in $(ls opt/$name | grep -v zip);do
        if [[ "${whitelist[@]}" =~ $file ]];then
            echo "$file in whitelist,keep it..."
        else
            echo "Remove unnessary file:$file..."
            rm -rf opt/$name/$file
        fi
    done
fi
cp -af $BUILD_ROOT/inst.sh.pure $BUILD_DEST/opt/$name/inst.sh
cp -af $BUILD_ROOT/tests.xml $BUILD_DEST/opt/$name/
zip -Drq $BUILD_DEST/$name-$version.$type.zip opt/
if [ $? -ne 0 ];then
    echo "Create zip package fail... >>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi
}

## create  pure and zip package ##
create_pure
zip_for_pure

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
