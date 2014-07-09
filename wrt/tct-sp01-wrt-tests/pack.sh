#!/bin/bash
source $(dirname $0)/$(basename $(pwd)).spec

#parse params
usage="Usage: ./pack.sh [-t <package type: wgt | apk | crx | xpk>]
[-t wgt] option was set as default."

if [[ $1 == "-h" || $1 == "--help" ]]; then
    echo "$usage"
    exit 1
fi

type="wgt"
while getopts t: o
do
    case "$o" in
    t) type=$OPTARG;;
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
    echo "Package name or version not specified in spec"
    exit 1
fi

SRC_ROOT=${PWD}
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

# copy signing tool
echo "copy signing tool... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
cp -arf $SRC_ROOT/../../tools/signing $BUILD_ROOT/signing
if [ $? -ne 0 ];then
    echo "No signing tool found in $SRC_ROOT/../../tools.... >>>>>>>>>>>>>>>>>>>>>>>>>"
fi

## function for create wgt apk xpk ##

function create_wgt(){
# create wgt
cd $BUILD_ROOT
pack_fail='FALSE'
suite_dir=${PWD}
all_dirs=`ls -l --time-style="long-iso" $suite_dir | grep '^d' | awk '{print $8}'|grep -v signing`
black_dirs=''
signing_white_dirs=''

#black list reserved for some non-suite folders.
if [ -f "$suite_dir/blackdirs" ]; then
    black_dirs=`cat $suite_dir/blackdirs`
    echo "Got black dirs: $black_dirs"
fi

#signning white list reserved for some signing folders.
if [ -f "$suite_dir/signing_whitedirs" ]; then
    signing_white_dirs=`cat $suite_dir/signing_whitedirs`
    echo "Got signing white dirs: $signing_white_dirs"
fi

function check_blackdir()
{
  for bdir in ${black_dirs[@]}; do
    if [ $1 == $bdir ]; then
      return 1;
    fi
  done
  return 0
}

function check_signing_whitedir()
{
  for signing_wdir in ${signing_white_dirs[@]}; do
    if [ $1 == $signing_wdir ]; then
      return 1;
    fi
  done
  return 0
}

echo "-->> Creating widgets >>--"
for app in $all_dirs; do
    check_blackdir $app
    if [ $? == 1 ]; then
        echo "Got a black dir: $app"
        continue
    elif [ $(find $app|wc -l) -eq 1 ]; then
        echo "No files found in $app, skip it ..."
        continue
    else
        if [ -f $app.wgt ]; then
            echo "Delete old packaged file"
            rm -rf $app.wgt
        fi
        cd $app
        echo "Start pack $app ..."
        zip -rq ../$app.wgt *
        if [ $? -ne 0 ]; then
            pack_fail='TRUE'
            echo "Create $app.wgt fail, continue to pack others"
        else
            check_signing_whitedir $app
            if [ $? == 0 ];then
               echo "$app is not in signing white dir, not sign for it."
               cd $suite_dir
               continue
            fi
	    if [ -d "$BUILD_ROOT/signing" ]; then
                echo "Start sign wgt ..."
                $BUILD_ROOT/signing/sign-widget.sh --dist platform $BUILD_ROOT/$app.wgt
            else
                echo "Not found signing folder."
            fi
            echo -e "Done\n"
        fi
        cd $suite_dir
    fi
done
echo "-- Create widgets done --"

if [ $pack_fail != 'FALSE' ]; then
    echo "Fail to pack some packages ..."
    exit 1
fi

# build
echo "build from workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
cd  $BUILD_ROOT
./autogen && ./configure --prefix=/ && make && make install DESTDIR=$BUILD_DEST
if [ $? -ne 0 ];then
    echo "build fail,please check Makefile.am and cofigure.ac... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi
find $BUILD_DEST -name "Makefile*" -delete
}

function create_apk(){
echo "Sorry,apk is not support yet... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
clean_workspace
exit 1
}

function create_xpk(){
echo "Sorry,xpk is not support yet... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
clean_workspace
exit 1
}

function create_crx(){
echo "Sorry,crx is not support yet... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
clean_workspace
exit 1
}

## zip function ##
function zip_for_wgt(){
cd $BUILD_DEST
# cp inst.sh script #
rm -rf $BUILD_DEST/opt/$name/inst.sh.wgt
cp -af $BUILD_ROOT/inst.sh.wgt $BUILD_DEST/opt/$name/inst.sh

zip -Drq $BUILD_DEST/$name-$version.xwalk.$type.zip opt/
if [ $? -ne 0 ];then
    echo "Create zip package fail... >>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi
}

function zip_for_apk(){
echo "Sorry,apk is not support yet... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
clean_workspace
exit 1
}

function zip_for_xpk(){
echo "Sorry,xpk is not support yet... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
clean_workspace
exit 1
}

function zip_for_crx(){
echo "Sorry,crx is not support yet... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
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
cp -f $BUILD_DEST/$name-$version.xwalk.$type.zip $SRC_ROOT/$name-$version.xwalk.$type.zip

# clean workspace
clean_workspace

# validate
echo "checking result... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
cd $SRC_ROOT
if [ -z "`ls | grep "\.zip"`" ];then
    echo "------------------------------ FAILED to build $name packages --------------------------"
    exit 1
fi

echo "------------------------------ Done to build $name packages --------------------------"
ls *.zip 2>/dev/null
