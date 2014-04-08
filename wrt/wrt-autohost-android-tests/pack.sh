#!/bin/bash
source $(dirname $0)/$(basename $(pwd)).spec

#parse params
usage="Usage: ./pack.sh [-t <package type: wgt | apk | crx | xpk | pure>] [-m <apk mode: shared | embedded>] [-a <apk runtime arch: x86 | arm>]
[-t pure] option was set as default.
[-m shared] option was set as default.
[-a x86] option was set as default.
"

if [[ $1 == "-h" || $1 == "--help" ]]; then
    echo "$usage"
    exit 1
fi

type="pure"
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

if [[ $type == "wgt" || $type == "apk" || $type == "crx" || $type == "xpk" || $type == "pure" ]];then
    echo "Create package with raw source"
    #echo "Create package with $type and raw source"
else
    echo "Sorry,$type is not support... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    echo "$usage"
    exit 1
fi

if [ $type == "pure" ]; then
    apkpacktooldir=$PWD/../../tools/crosswalk
fi

if [ $type == "xpk" ]; then
    xpkpacktooldir=$PWD/../../tools
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

function create_pure()
{
# create wgt
    cd $BUILD_DEST
    zip -rq $BUILD_DEST/opt/$name/$name.zip *
    if [ $? -ne 0 ];then
        echo "Create $name.zip fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
        clean_workspace
        exit 1
    fi
}

## function for create wgt apk xpk ##

function create_wgt(){
# create wgt
cd $BUILD_DEST
cp -a $BUILD_ROOT/manifest.json   $BUILD_DEST/
cp -a $BUILD_ROOT/icon.png     $BUILD_DEST/
cat > index.html << EOF
<!doctype html>
<head>
    <meta http-equiv="Refresh" content="1; url=opt/$name/testkit/web/index.html?testsuite=/opt/usr/media/tct/opt/$name/tests.xml">
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
cd $apkpacktooldir
python make_apk.py --name=WebApp1 --package=com.xwalk.webapp1 --app-url="http://www.hao123.com" --mode=$mode --arch=$arch
python make_apk.py --name=WebApp2 --package=com.xwalk.webapp2 --app-url="http://www.baidu.com" --mode=$mode --arch=$arch
if [ $? -ne 0 ];then
    echo "Create $name.apk fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi
#clean middle files
rm *.pyc
rm *.stam*
mv *.apk $BUILD_DEST/opt/$name/resources/apk/
rm -r WebApp*
}

function create_xpk(){
cp -a $BUILD_ROOT/manifest.json   $BUILD_DEST/
cp -a $BUILD_ROOT/icon.png     $BUILD_DEST/

cd $BUILD_DEST
cat > index.html << EOF
<!doctype html>
<head>
    <meta http-equiv="Refresh" content="1; url=opt/$name/testkit/web/index.html?testsuite=../../tests.xml&testprefix=../../../..">
</head>
EOF

cd $xpkpacktooldir
python make_xpk.py tmp/$name key
if [ $? -ne 0 ];then
    echo "Create $name.xpk fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi

#clean middle files
rm key
}

function create_crx(){
echo "crx is not support yet... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
clean_workspace
exit 1
}

## zip function ##
function zip_for_wgt(){
cd $BUILD_DEST
# cp inst.sh script #
cp -af $BUILD_ROOT/inst.sh.wgt $BUILD_DEST/opt/$name/inst.sh

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
mv $apkpacktooldir/*.apk $BUILD_DEST/opt/$name/

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
mv $xpkpacktooldir/$name.xpk $BUILD_DEST/opt/$name/

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
cp -af $BUILD_ROOT/inst.sh $BUILD_DEST/opt/$name/inst.sh
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
    pure)
         create_apk
         create_pure
         zip_for_pure;;
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
