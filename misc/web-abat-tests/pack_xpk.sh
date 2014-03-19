#!/bin/bash
#parse params
usage="Usage: ./pack.sh [-l <pack xpk-package tool's location>]  [-p <platform: mobile | ivi | generic>]
[-p mobile] option was set as default."

if [[ $1 == "-h" || $1 == "--help" ]]; then
    echo $usage
    exit 1
fi

toollocation=''
platform="mobile"
while getopts l:p: o
do
    case "$o" in
    l) toollocation=$OPTARG;;
    p) platform=$OPTARG;;
    *) echo $usage
       exit 1;;
    esac
done

if [ -z $toollocation ];then
    echo "$usage"
    exit 1
fi

if [ ! -e "$toollocation"/make_xpk.py ];then
    echo "Could not find the pack tool in $toollocation for creating xpk-package."
    echo "$usage"
    exit 1
fi

source $(dirname $0)/web-abat-tests.spec
SRC_ROOT=$(cd $(dirname $0);pwd)
BUILD_ROOT=/tmp/${name}_pack
BUILD_DEST=/tmp/${name}

rm -rf $SRC_ROOT/*.zip

# clean
function clean_workspace(){
    echo "cleaning workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    rm -rf $BUILD_ROOT $BUILD_DEST
}

echo "cleaning workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
clean_workspace
mkdir -p $BUILD_ROOT
cp -arf $SRC_ROOT/* $BUILD_ROOT/
mkdir -p $BUILD_DEST/opt/$name/abat
cp -r $BUILD_ROOT/abat/common/* $BUILD_DEST/opt/$name/abat
cp -r $BUILD_ROOT/abat/tizen/* $BUILD_DEST/opt/$name/abat
cp -r $BUILD_ROOT/testkit $BUILD_DEST/opt/$name
cp -r $BUILD_ROOT/resources $BUILD_DEST/opt/$name/abat



mkdir -p $BUILD_DEST/$name
cp -a $BUILD_ROOT/manifest.json   $BUILD_DEST/$name/
cp -a $BUILD_ROOT/icon.png     $BUILD_DEST/$name/

cd $BUILD_DEST/$name/
cat > index.html << EOF
<!doctype html>
<head>
    <meta http-equiv="Refresh" content="1; url=http://127.0.0.1/opt/$name/testkit/web/index.html?testsuite=../../tests.xml&testprefix=../../../..">
</head>
EOF

cp $toollocation/make_xpk.py $BUILD_ROOT/make_xpk.py
cd $BUILD_ROOT
python make_xpk.py $BUILD_DEST/$name/ key
if [ $? -ne 0 ];then
    echo "Create $name.xpk fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi
rm -rf $BUILD_DEST/$name/

cd $BUILD_DEST
cp $BUILD_ROOT/tests.xml.xpk $BUILD_DEST/opt/$name/tests.xml

if [ $platform == "ivi" ]; then
    cp -af $BUILD_ROOT/inst.sh.ivi $BUILD_DEST/opt/$name/inst.sh
elif [ $platform == "generic" ]; then
    cp -af $BUILD_ROOT/inst.sh.generic $BUILD_DEST/opt/$name/inst.sh
else
    cp -af $BUILD_ROOT/inst.sh.xpk $BUILD_DEST/opt/$name/inst.sh
fi
cp -af $BUILD_ROOT/COPYING $BUILD_DEST/opt/$name/
mv $BUILD_ROOT/$name.xpk $BUILD_DEST/opt/$name/

zip -Drq $BUILD_DEST/$name-$version.xpk.zip opt/
if [ $? -ne 0 ];then
    echo "Create zip package fail... >>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi

# copy zip file
echo "copy package from workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
cp -f $BUILD_DEST/$name-$version.xpk.zip $SRC_ROOT/

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
