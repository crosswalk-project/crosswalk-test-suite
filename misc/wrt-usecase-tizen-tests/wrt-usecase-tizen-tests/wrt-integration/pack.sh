#!/bin/bash
source $(dirname $0)/wrt-integration.spec

#parse params
usage="Usage: ./pack.sh [-t <package type: wgt | apk | crx | xpk>] [-m <apk mode: shared | embedded>] [-a <apk runtime arch: x86 | arm>]
[-t wgt] option was set as default.
[-m shared] option was set as default.
[-a x86] option was set as default.
"

if [[ $1 == "-h" || $1 == "--help" ]]; then
    echo "$usage"
    exit 1
fi

type="wgt"
mode="shared"
arch="x86"
while getopts t:m:a: o
do
    case "$o" in
    t) type=$OPTARG;;
    m) mode=$OPTARG;;
    a) arch=$OPTARG;;
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

SRC_ROOT=$PWD
RESOURCE_DIR=/home/app/content
BUILD_ROOT=/tmp/${name}_pack
BUILD_DEST=/tmp/${name}

# clean
function clean_workspace(){
    echo "cleaning workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    rm -rf $BUILD_ROOT $BUILD_DEST
}

clean_workspace
mkdir -p $BUILD_ROOT $BUILD_DEST

# copy source code
rm -rf *.rpm *.tar.bz2 *.tar.gz *.zip
cp -arf $SRC_ROOT/* $BUILD_ROOT/

## function for create wgt apk xpk ##

function create_wgt(){
    # create wgt
    cd $BUILD_DEST
    cp -af $BUILD_ROOT/index.html $BUILD_DEST/
    cp -af $BUILD_ROOT/config.xml $BUILD_DEST/
    cp -af $BUILD_ROOT/icon.png $BUILD_DEST/
    cp -af $BUILD_ROOT/tests.tizen.xml $BUILD_DEST/tests.xml
    cp -af $BUILD_ROOT/subtestresult.xml $BUILD_DEST/
    cp -af $BUILD_ROOT/js $BUILD_DEST/
    cp -af $BUILD_ROOT/css $BUILD_DEST/
    cp -af $BUILD_ROOT/tests $BUILD_DEST/
    cp -af $BUILD_ROOT/res $BUILD_DEST/
    mkdir -p $BUILD_DEST/opt/$name/res/media
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
        cp -arf $SRC_ROOT/../../../tools/signing $BUILD_ROOT/signing
        if [ $? -ne 0 ];then
            echo "No signing tool found in $SRC_ROOT/../tools.... >>>>>>>>>>>>>>>>>>>>>>>>>"
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
    cd $BUILD_DEST
    cat > index.html << EOF
<!doctype html>
<head>
    <meta http-equiv="Refresh" content="1; url=opt/$name/webrunner/index.html?testsuite=../tests.xml&testprefix=../../..">
</head>
EOF
    cp -r $SRC_ROOT/../../../tools/crosswalk $BUILD_ROOT/crosswalk

    cp -af $BUILD_ROOT/index.html $BUILD_DEST/
    cp -af $BUILD_ROOT/config.xml $BUILD_DEST/
    cp -af $BUILD_ROOT/icon.png $BUILD_DEST/
    cp -af $BUILD_ROOT/tests.android.xml $BUILD_DEST/tests.xml
    cp -af $BUILD_ROOT/subtestresult.xml $BUILD_DEST/
    cp -af $BUILD_ROOT/js $BUILD_DEST/
    cp -af $BUILD_ROOT/css $BUILD_DEST/
    cp -af $BUILD_ROOT/tests $BUILD_DEST/
    cp -af $BUILD_ROOT/res $BUILD_DEST/
    mkdir -p $BUILD_DEST/opt/$name/res/media

    cd $BUILD_ROOT/crosswalk
    python make_apk.py --package=org.xwalk.$appname --name=$appname --app-root=$BUILD_DEST --app-local-path=index.html --icon=$BUILD_DEST/icon.png --mode=$mode --arch=$arch
    if [ $? -ne 0 ];then
        echo "Create $name.apk fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
        clean_workspace
        exit 1
    fi
}

function create_xpk(){
    cp -a $BUILD_ROOT/manifest.json   $BUILD_DEST/
    cp -a $BUILD_ROOT/icon.png     $BUILD_DEST/

    cd $BUILD_DEST
    cat > index.html << EOF
<!doctype html>
<head>
    <meta http-equiv="Refresh" content="1; url=opt/$name/webrunner/index.html?testsuite=../tests.xml&testprefix=../../..">
</head>
EOF

    cp -af $BUILD_ROOT/index.html $BUILD_DEST/
    cp -af $BUILD_ROOT/config.xml $BUILD_DEST/
    cp -af $BUILD_ROOT/icon.png $BUILD_DEST/
    cp -af $BUILD_ROOT/tests.tizen.xml $BUILD_DEST/tests.xml
    cp -af $BUILD_ROOT/subtestresult.xml $BUILD_DEST/
    cp -af $BUILD_ROOT/js $BUILD_DEST/
    cp -af $BUILD_ROOT/css $BUILD_DEST/
    cp -af $BUILD_ROOT/tests $BUILD_DEST/
    cp -af $BUILD_ROOT/res $BUILD_DEST/
    mkdir -p $BUILD_DEST/opt/$name/res/media

    cp $SRC_ROOT/../../../tools/make_xpk.py $BUILD_ROOT/make_xpk.py
    cd $BUILD_ROOT
    # create xpk
    python make_xpk.py /tmp/$name key


    if [ $? -ne 0 ];then
        echo "Create $name.xpk fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
        clean_workspace
        exit 1
    fi
}

function create_crx(){
    echo "crx is not support yet... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
}

## zip function ##
function zip_for_wgt(){
    cd $BUILD_DEST
    # cp inst.sh script and tests.xml #
    cp -af $BUILD_ROOT/inst.sh.wgt $BUILD_DEST/opt/$name/inst.sh
    cp -af $BUILD_ROOT/tests.tizen.xml $BUILD_DEST/opt/$name/tests.xml

    # cp license files #
    cp -af $BUILD_ROOT/LICENSE.Apache-2.0 $BUILD_DEST/opt/$name/LICENSE.Apache-2.0
    cp -af $BUILD_ROOT/LICENSE.BSD-3 $BUILD_DEST/opt/$name/LICENSE.BSD-3
    cp -af $BUILD_ROOT/LICENSE.CC-BY-3.0 $BUILD_DEST/opt/$name/LICENSE.CC-BY-3.0

    # cp res folder #
    cp -a $BUILD_ROOT/res/font $BUILD_DEST/opt/$name/res/font
    cp -a $BUILD_ROOT/res/images $BUILD_DEST/opt/$name/res/images
    cp -a $BUILD_ROOT/res/js $BUILD_DEST/opt/$name/res/js
    cp -a $BUILD_ROOT/js/thirdparty/jquery.js $BUILD_DEST/opt/$name/res/js/
    cp -a $BUILD_ROOT/res/css $BUILD_DEST/opt/$name/res/css
    cp -a $BUILD_ROOT/testresult.xsl $BUILD_DEST/opt/$name/res/css/
    cp -a $BUILD_ROOT/res/media/khronos/red-green.theora.ogv $BUILD_DEST/opt/$name/res/media/

    if [ $src_file -eq 0 ];then
        for file in $(ls opt/$name |grep -v wgt);do
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

function zip_for_apk(){
    cd $BUILD_DEST
    # cp inst.sh script #
    cp -af $BUILD_ROOT/inst.sh.apk $BUILD_DEST/opt/$name/inst.sh
    mv $BUILD_ROOT/crosswalk/*.apk $BUILD_DEST/opt/$name/

    cp -af $BUILD_ROOT/tests.android.xml $BUILD_DEST/opt/$name/tests.xml

    if [ $src_file -eq 0 ];then
        for file in $(ls opt/$name |grep -v apk);do
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

function zip_for_xpk(){
    cd $BUILD_DEST
    cp -af $BUILD_ROOT/inst.sh.xpk $BUILD_DEST/opt/$name/inst.sh

    # mv xpk package
    find $BUILD_ROOT/ -name "*.xpk"| grep -v inst.sh.xpk |xargs -I% mv % $BUILD_DEST/opt/$name/

    cp -af $BUILD_ROOT/tests.tizen.xml $BUILD_DEST/opt/$name/tests.xml

    # cp license files #
    cp -af $BUILD_ROOT/LICENSE.Apache-2.0 $BUILD_DEST/opt/$name/LICENSE.Apache-2.0
    cp -af $BUILD_ROOT/LICENSE.BSD-3 $BUILD_DEST/opt/$name/LICENSE.BSD-3
    cp -af $BUILD_ROOT/LICENSE.CC-BY-3.0 $BUILD_DEST/opt/$name/LICENSE.CC-BY-3.0

    # cp res folder #
    cp -a $BUILD_ROOT/res/font $BUILD_DEST/opt/$name/res/font
    cp -a $BUILD_ROOT/res/images $BUILD_DEST/opt/$name/res/images
    cp -a $BUILD_ROOT/res/js $BUILD_DEST/opt/$name/res/js
    cp -a $BUILD_ROOT/js/thirdparty/jquery.js $BUILD_DEST/opt/$name/res/js/
    cp -a $BUILD_ROOT/res/css $BUILD_DEST/opt/$name/res/css
    cp -a $BUILD_ROOT/testresult.xsl $BUILD_DEST/opt/$name/res/css/
    cp -a $BUILD_ROOT/res/media/khronos/red-green.theora.ogv $BUILD_DEST/opt/$name/res/media/

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
