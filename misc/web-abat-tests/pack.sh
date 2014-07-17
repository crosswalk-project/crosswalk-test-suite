#!/bin/bash
source $(dirname $0)/$(basename $(pwd)).spec

#parse params
usage="Usage: ./pack.sh [-t <package type: wgt | apk | crx | xpk >] [-m <apk mode: shared | embedded>] [-p <xpk platform: mobile | ivi | generic>] [-a <apk runtime arch: x86 | arm>]
[-t xpk] option was set as default.
[-m shared] option was set as default.
[-a x86] option was set as default.
[-p ivi] option was set as default."

if [[ $1 == "-h" || $1 == "--help" ]]; then
    echo "$usage"
    exit 1
fi

type="xpk"
mode="embedded"
arch="x86"
platform="ivi"
while getopts t:m:a:p: o
do
    case "$o" in
    t) type=$OPTARG;;
    m) mode=$OPTARG;;
    a) arch=$OPTARG;;
    p) platform=$OPTARG;;
    *) echo "$usage"
       exit 1;;
    esac
done

if [[ $type == "wgt" || $type == "apk" || $type == "crx" || $type == "xpk" ]];then
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

SRC_ROOT=$(cd $(dirname $0);pwd)
RESOURCE_DIR=/home/app/content
BUILD_ROOT=/tmp/${name}_pack
BUILD_DEST=/tmp/$name
docroot_dir=/tmp/docroot_pack

# clean
function clean_workspace(){
    echo "cleaning workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    rm -rf $BUILD_DEST $docroot_dir $BUILD_ROOT
}

echo "cleaning workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
clean_workspace
mkdir -p $BUILD_ROOT $BUILD_DEST
rm -rf $SRC_ROOT/*.zip
cp -arf $SRC_ROOT/* $BUILD_ROOT/

## function for create wgt apk xpk ##

function create_wgt(){
# create wgt
cd $BUILD_DEST
mkdir -p $BUILD_DEST/opt/$name/abat
cp -r $BUILD_ROOT/abat/common/* $BUILD_DEST/opt/$name/abat
cp -r $BUILD_ROOT/abat/tizen/* $BUILD_DEST/opt/$name/abat
cp -r $BUILD_ROOT/webrunner $BUILD_DEST/opt/$name
cp -r $BUILD_ROOT/resources $BUILD_DEST/opt/$name/abat

mkdir -p $BUILD_DEST/$name
cp -a $BUILD_ROOT/manifest.json   $BUILD_DEST/$name/
cp -a $BUILD_ROOT/icon.png     $BUILD_DEST/$name/

cat > index.html << EOF
<!doctype html>
<head>
    <meta http-equiv="Refresh" content="1; url=opt/$name/webrunner/index.html?testsuite=../tests.xml&testprefix=../../..">
</head>
EOF
cp -f $BUILD_ROOT/config.xml.wgt $BUILD_DEST/config.xml
zip -rq $BUILD_DEST/opt/$name/$name.wgt *
if [ $? -ne 0 ];then
    echo "Create $name.wgt fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi

# sign wgt
if [ $sign -eq 1 ];then
    # copy signing tool
    echo "copy signing tool... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    cp -arf $SRC_ROOT/../../tools/signing $BUILD_ROOT/signing
    if [ $? -ne 0 ];then
        echo "No signing tool found in $SRC_ROOT/../../tools.... >>>>>>>>>>>>>>>>>>>>>>>>>"
    fi
    wgt=$(find $BUILD_DEST/opt/$name/ -name *.wgt)
    for wgt in $(find $BUILD_DEST/opt/$name/ -name *.wgt);do
        $BUILD_ROOT/signing/sign-widget.sh --dist platform $wgt
        if [ $? -ne 0 ];then
            echo "Please check your signature files... >>>>>>>>>>>>>>>>>>>>>>>>>"
        fi
    done
fi
}

function create_apk(){
    cp -arf $SRC_ROOT/* $BUILD_DEST/
    if [ -f $SRC_ROOT/../../tools/crosswalk/make_apk.py ]; then
        cp -ar $SRC_ROOT/../../tools/crosswalk $BUILD_DEST/crosswalk
    else
        echo "Could not find the pack tool in $SRC_ROOT/../../tools/ for creating apk-package."
        clean_workspace
        exit 1
    fi

    cd $BUILD_DEST/crosswalk
    python make_apk.py --package=org.xwalk.$appname --name=$appname --app-url=http://127.0.0.1:8080/index.html --icon=$BUILD_DEST/icon.png --mode=$mode --arch=$arch
    if [ $? -ne 0 ];then
        echo "Create $name.apk fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
        clean_workspace
        exit 1
    fi
}

function create_xpk(){
    mkdir -p $BUILD_DEST/opt/$name/abat
    cp -r $BUILD_ROOT/abat/common/* $BUILD_DEST/opt/$name/abat
    cp -r $BUILD_ROOT/abat/tizen/* $BUILD_DEST/opt/$name/abat
    cp -r $BUILD_ROOT/webrunner $BUILD_DEST/opt/$name
    cp -r $BUILD_ROOT/resources $BUILD_DEST/opt/$name/abat

    mkdir -p $BUILD_DEST/$name
    cp -a $BUILD_ROOT/manifest.json   $BUILD_DEST/$name/
    cp -a $BUILD_ROOT/icon.png     $BUILD_DEST/$name/

    cd $BUILD_DEST/$name/
    cat > index.html << EOF
<!doctype html>
<head>
    <meta http-equiv="Refresh" content="1; url=http://127.0.0.1/opt/$name/webrunner/index.html?testsuite=../tests.xml&testprefix=../../..">
</head>
EOF

    if [ -f $SRC_ROOT/../../tools/make_xpk.py ]; then
        cp -a $SRC_ROOT/../../tools/make_xpk.py $BUILD_ROOT/make_xpk.py
    else
        echo "Could not find the pack tool in $SRC_ROOT/../../tools/ for creating xpk-package."
        clean_workspace
        exit 1
    fi
    cd $BUILD_ROOT
    python make_xpk.py $BUILD_DEST/$name/ key
    if [ $? -ne 0 ];then
        echo "Create $name.xpk fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
        clean_workspace
        exit 1
    fi
    rm -rf $BUILD_DEST/$name/
}

function create_crx(){
    echo "crx is not support yet... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
}

## zip function ##
function zip_for_wgt(){
    cd $BUILD_DEST
    cp $BUILD_ROOT/tests.xml.xpk $BUILD_DEST/opt/$name/tests.xml

    if [ $platform == "generic" ]; then
        cp -af $BUILD_ROOT/inst.sh.wgt.generic $BUILD_DEST/opt/$name/inst.sh
    else
        cp -af $BUILD_ROOT/inst.sh.wgt $BUILD_DEST/opt/$name/inst.sh
    fi
    cp -af $BUILD_ROOT/COPYING $BUILD_DEST/opt/$name/
    mv $BUILD_ROOT/$name.wgt $BUILD_DEST/opt/$name/

    zip -Drq $BUILD_DEST/$name-$version.wgt.zip opt/
    if [ $? -ne 0 ];then
        echo "Create zip package fail... >>>>>>>>>>>>>>>>>>>>>>>>>"
        clean_workspace
        exit 1
    fi
}

function zip_for_apk(){
    ## cp tests.xml and inst.sh ##
    mkdir -p $BUILD_DEST/opt/$name
    cp $SRC_ROOT/inst.sh.apk $BUILD_DEST/opt/$name/inst.sh
    cp $SRC_ROOT/tests.xml.apk $BUILD_DEST/opt/$name/tests.xml
    cp $SRC_ROOT/COPYING $BUILD_DEST/opt/$name/

    ## creat zip package ##
    mv $BUILD_DEST/crosswalk/*.apk $BUILD_DEST/opt/$name/
    cd $BUILD_DEST
    zip -Drq $BUILD_DEST/$name-$version.apk.zip opt/
    if [ $? -ne 0 ];then
        echo "Create zip package fail... >>>>>>>>>>>>>>>>>>>>>>>>>"
        clean_workspace
        exit 1
    fi

    # copy zip file
    echo "copy package from workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    cp -f $BUILD_DEST/$name-$version.apk.zip $SRC_ROOT/

    mkdir -p $docroot_dir/docroot
    cp $BUILD_DEST/webrunner/* $docroot_dir/docroot
    mkdir -p $docroot_dir/docroot/opt/$name/abat
    cp -r $BUILD_DEST/abat/common/* $docroot_dir/docroot/opt/$name/abat
    cp -r $BUILD_DEST/resources $docroot_dir/docroot/opt/$name/abat
    cp -r $BUILD_DEST/webrunner $docroot_dir/docroot/opt/$name
    cp $BUILD_DEST/tests.xml.apk $docroot_dir/docroot/opt/$name/tests.xml
    cd $docroot_dir
    zip -r docroot.zip docroot
    rm -rf docroot/*
    mv docroot.zip docroot
    cp $BUILD_DEST/inst.sh.docroot docroot/inst.sh
    zip -r $SRC_ROOT/docroot_$version.apk.zip docroot
}

function zip_for_xpk(){
    cd $BUILD_DEST
    cp $BUILD_ROOT/tests.xml.xpk $BUILD_DEST/opt/$name/tests.xml

    if [ $platform == "generic" ]; then
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
}

function zip_for_crx(){
    echo "zip_for_crx not ready yet... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
}

## create wgt crx apk xpk and zip package ##
case $type in
    wgt) create_wgt
         zip_for_wgt;;
    apk) create_apk
         zip_for_apk;;
    xpk) create_xpk
         zip_for_xpk;;
    crx) create_crx
         zip_for_crx;;
esac


# copy zip file
echo "copy package from workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
cp -f $BUILD_DEST/$name*.zip $SRC_ROOT/

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
