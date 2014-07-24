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
folderName_tmp=${suiteName#*-}
folderName=${folderName_tmp%%-*}

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

if [ $type == "xpk" ]; then
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
cd $BUILD_ROOT/$folderName

for buildfolder in `ls`
do
    cd $BUILD_ROOT/$folderName/$buildfolder
    for build_subfolder in `ls`
    do
        if [ -d $BUILD_DEST/opt/$name/$folderName/$buildfolder/$build_subfolder ];then
            cd $apkpacktooldir
            if [ "${build_subfolder:0:8}" == "manifest" ];then
                echo "Use --manifest to build..."
                python make_apk.py --manifest=$BUILD_DEST/opt/$name/$folderName/$buildfolder/$build_subfolder/manifest.json --mode=$mode --arch=$arch
                rmfile $build_subfolder
                mv *.apk $BUILD_DEST/opt/$name/$folderName/$buildfolder
                rm -rf $BUILD_DEST/opt/$name/$folderName/$buildfolder/$build_subfolder
                continue
            fi
            if [ "${build_subfolder:0:34}" == "crosswalk_remote_debugging_default" ];then
                echo "Use --debugging to build..."
                python make_apk.py --name=$build_subfolder --package=org.xwalk.$build_subfolder --app-root=$BUILD_DEST/opt/$name/$folderName/$buildfolder/$build_subfolder --app-local-path=index.html --enable-remote-debugging
                rmfile $build_subfolder
                mv *.apk $BUILD_DEST/opt/$name/$folderName/$buildfolder
                rm -rf $BUILD_DEST/opt/$name/$folderName/$buildfolder/$build_subfolder
                continue
            fi
            if [ "${build_subfolder:0:20}" == "webgl_webrtc_disable" ];then
                echo "Use --manifest to build..."
                echo "Add --xwalk-command-line option..."
                python make_apk.py --manifest=$BUILD_DEST/opt/$name/$folderName/$buildfolder/$build_subfolder/manifest.json --mode=$mode --arch=$arch --xwalk-command-line='--disable-webgl --disable-webrtc'
                rmfile $build_subfolder
                mv *.apk $BUILD_DEST/opt/$name/$folderName/$buildfolder
                rm -rf $BUILD_DEST/opt/$name/$folderName/$buildfolder/$build_subfolder
                continue
            fi
            if [ "${build_subfolder:0:6}" == "update" ];then
                echo "This app not support android..."
                continue
            fi
            if [ "${build_subfolder:0:9}" == "extension" ];then
                echo "build extension webapp..."
                python make_apk.py --package=org.xwalk.$build_subfolder --name=$build_subfolder --app-root=$BUILD_DEST/opt/$name/$folderName/$buildfolder/$build_subfolder --app-local-path=index.html --extensions=$BUILD_DEST/opt/$name/$folderName/$buildfolder/$build_subfolder/contactextension --mode=$mode --arch=$arch
                rmfile $build_subfolder
                mv *.apk $BUILD_DEST/opt/$name/$folderName/$buildfolder
                rm -rf $BUILD_DEST/opt/$name/$folderName/$buildfolder/$build_subfolder
                continue
            fi
            python make_apk.py --package=org.xwalk.$build_subfolder --name=$build_subfolder --app-root=$BUILD_DEST/opt/$name/$folderName/$buildfolder/$build_subfolder --app-local-path=index.html --mode=$mode --arch=$arch
            if [ $? -ne 0 ];then
                echo "Create $build_subfolder.apk fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
                clean_workspace
            fi
            #clean middle files
            rmfile $build_subfolder
            mv *.apk $BUILD_DEST/opt/$name/$folderName/$buildfolder
            rm -rf $BUILD_DEST/opt/$name/$folderName/$buildfolder/$build_subfolder
            cp $BUILD_ROOT/inst.sh.apk $BUILD_DEST/opt/$name/$folderName/$buildfolder/inst.sh
        fi
    done
done    
}

function rmfile(){
rm *.pyc
rm *.stam*
rm -r ${1//-/_}
}

function create_xpk(){
cd $BUILD_ROOT/$folderName
for buildfolder in `ls`
do
    cd $BUILD_ROOT/$folderName/$buildfolder
    for build_subfolder in `ls`
    do
      if [ -d $BUILD_DEST/opt/$name/$folderName/$buildfolder/$build_subfolder ];then
          mkdir $BUILD_DEST/opt/$name/$folderName/
          cd $xpkpacktooldir
          if [ "${build_subfolder:0:6}" == "update" ];then
              echo "Use same pem to build..."
              python make_xpk.py $BUILD_DEST/opt/$name/$folderName/$buildfolder/$build_subfolder update.pem
              continue
          fi
          python make_xpk.py $BUILD_DEST/opt/$name/$folderName/$buildfolder/$build_subfolder key.pem
          if [ $? -ne 0 ];then
              echo "Create $name.apk fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
              #clean_workspace
              exit 1
          fi
          #clean middle files
          rm key.pem
          sleep 2
      fi
    done
done
#clean update pem files
rm update.pem
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
cp -arf $BUILD_DEST/opt/ $BUILD_ROOT/
cp -af $BUILD_ROOT/common $BUILD_ROOT/opt/$name/
rm $BUILD_ROOT/opt/$name/Changelog $BUILD_ROOT/opt/$name/COPYING $BUILD_ROOT/opt/$name/README
cd $BUILD_ROOT/
zip -Drq $name-$version.$type.zip ./opt
}

function zip_for_xpk(){
cd $BUILD_DEST
cp -af $BUILD_ROOT/inst.sh.xpk $BUILD_DEST/opt/$name/inst.sh
cp -af $BUILD_ROOT/common $BUILD_DEST/opt/$name/
mv $xpkpacktooldir/*.xpk $BUILD_DEST/opt/$name/

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
    wgt) create_apk
         zip_for_apk;;
    apk) create_apk
         zip_for_apk;;
    xpk) create_xpk
         zip_for_xpk;;
    crx) zip_for_xpk
         zip_for_apk;;
    pure)
         create_pure
         zip_for_pure;;
esac


# copy zip file
echo "copy package from workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

cp -f $BUILD_ROOT/$name-$version.$type.zip $SRC_ROOT/$name-$version.$type.zip

#clean workspace
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
