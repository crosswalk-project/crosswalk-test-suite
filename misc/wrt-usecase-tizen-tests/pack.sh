#!/bin/bash
suiteName=$(basename $(pwd))
source $(dirname $0)/$suiteName.spec

#parse params
usage="Usage: ./pack.sh [-t <package type: wgt | apk | crx | xpk | pure>] [-m <apk mode: shared | embedded>] [-a <apk runtime arch: x86 | arm>]
[-t apk] option was set as default.
[-m shared] option was set as default.
[-a x86] option was set as default.
"

if [[ $1 == "-h" || $1 == "--help" ]]; then
    echo "$usage"
    exit 1
fi

if [[ $1 == "-h" || $1 == "--help" ]]; then
    echo $usage
    exit 1
fi

#get spec name
folderName_tmp=${suiteName%-*}
folderName=usecase

type="apk"
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

if [ $type == "apk" ]; then
    apkpacktooldir=$PWD/../../tools/crosswalk
fi

if [ $type == "wgt" ]; then
    xpkpacktooldir=$PWD/../../tools
fi

if [[ -z $name || -z $version || -z $appname ]];then
    echo "Package name or version not specified in setting file"
    exit 1
fi

SRC_ROOT=$PWD
RESOURCE_DIR=/home/app/content
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
rm -rf $BUILD_ROOT $BUILD_DEST $OPT
}

clean_workspace
mkdir -p $BUILD_ROOT $BUILD_DEST

# copy source code
rm -rf *.rpm *.tar.bz2 *.tar.gz *.zip
cp -arf $SRC_ROOT/* $BUILD_ROOT/

# build
echo "build from workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

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
cd $BUILD_ROOT/$folderName
mkdir $BUILD_DEST/opt/
mkdir $BUILD_DEST/opt/$folderName
for buildfolder in `ls`
do
    if [ -d $buildfolder ];then
        if [ "${buildfolder:0:27}" == "crosswalk_support_xpk_tests" ];then
            echo "Pack xpk....................."
            cd $xpkpacktooldir
            python make_xpk.py $BUILD_ROOT/$folderName/$buildfolder/crosswalk_support_xpk_tests k.pem
            python make_xpk.py $BUILD_ROOT/$folderName/$buildfolder/update_version_one_tests k.pem
            python make_xpk.py $BUILD_ROOT/$folderName/$buildfolder/update_version_two_tests k.pem
            rm -rf $xpkpacktooldir/*.pem        
            zip -rq $buildfolder.xpk.zip *.xpk             
            mv *.zip $BUILD_DEST/opt/$folderName
            rm -rf $xpkpacktooldir/*.xpk 
            cd $BUILD_ROOT/$folderName
            continue
        fi
        if [ "${buildfolder:0:27}" == "crosswalk_support_wgt_tests" ];then
            echo "Pack wgt....................."
            cd $buildfolder
            cd crosswalk_support_wgt_tests
            zip -rq crosswalk_support_wgt_tests.wgt *
            cp crosswalk_support_wgt_tests.wgt ../
            cd ..
            cd wgt_sample_one
            zip -rq wgt_sample_one.wgt *
            cp wgt_sample_one.wgt ../
            cd ..
            cd wgt_sample_two
            zip -rq wgt_sample_two.wgt *
            cp wgt_sample_two.wgt ../
            cd ..
            
            zip -rq crosswalk_support_wgt_tests.wgt.zip *.wgt
            ls
            cp crosswalk_support_wgt_tests.wgt.zip $BUILD_DEST/opt/$folderName
            cd ..
            continue
        fi
        echo $buildfolder
        cd   $buildfolder
        zip -rq $buildfolder.wgt *
        cp $buildfolder.wgt $BUILD_DEST/opt/$folderName
        cd ..
        sleep 2
    fi
done

}


function create_apk(){
echo "only support wgt"
}

function rmfile(){
rm *.pyc
rm *.stam*
rm -r ${1//-/_}
}

function create_xpk(){
echo "please use pack.sh -t wgt to pack"
}

function create_crx(){
echo "crx is not support yet... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
clean_workspace
exit 1
}

## zip function ##
function zip_for_wgt(){
cd $BUILD_DEST

echo $BUILD_DEST/$name-$version.$type.zip
cp $BUILD_ROOT/inst.sh  $BUILD_DEST/opt/usecase
zip -Drq $BUILD_DEST/$name-$version.$type.zip ./
if [ $? -ne 0 ];then
    echo "Create zip package fail... >>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi
}

function create_inwgt(){
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

function zip_for_apk(){
echo "no for apk"
}

function zip_for_xpk(){
echo "no for xpk"
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
         create_pure
         zip_for_pure;;
esac


# copy zip file
echo "copy package from workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
cp -f $BUILD_DEST/$name-$version.$type.zip $SRC_ROOT/$name-$version.$type.zip

# clean workspace
#clean_workspace

# validate
echo "checking result... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
if [ -z "`ls $SRC_ROOT | grep "\.zip"`" ];then
    echo "------------------------------ FAILED to build $name packages --------------------------"
    exit 1
fi

echo "------------------------------ Done to build $name packages --------------------------"
cd $SRC_ROOT
ls *.zip 2>/dev/null
