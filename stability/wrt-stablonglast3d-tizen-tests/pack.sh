#!/bin/bash
suiteName=$(basename $(pwd))
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

if [ $type == "xpk" ]; then
    xpkpacktooldir=$PWD/../../tools
fi
#get spec name
folderName_tmp=${suiteName#*-}
folderName=${folderName_tmp%%-*}

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
rm -rf $BUILD_ROOT $BUILD_DEST
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

#create dynamic xpk
cd $BUILD_ROOT/$folderName
for buildfolder in `ls`
do
    if [ -d $BUILD_DEST/opt/$name/$folderName/$buildfolder ];then
        cd $xpkpacktooldir
        python make_xpk.py $BUILD_DEST/opt/$name/$folderName/$buildfolder k.pem
        if [ $? -ne 0 ];then
            echo "Create $name.apk fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
            #clean_workspace
            exit 1
        fi
        #clean middle files
        rm k.pem
        rm -rf $BUILD_DEST/opt/$name/$folderName/$buildfolder
        sleep 2
    fi
done

# zip for resource
#mv $xpkpacktooldir/*.xpk $BUILD_DEST/opt/$name/$folderName
#cd $BUILD_DEST
#zip -rq $BUILD_DEST/opt/$name/$name.zip *
#if [ $? -ne 0 ];then
#   echo "Create $name.zip fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
#   clean_workspace
#   exit 1
#fi

# zip_for_xpk
mv $xpkpacktooldir/*.xpk $BUILD_DEST/opt/$name/$folderName
cp -af $BUILD_ROOT/inst.sh $BUILD_DEST/opt/$name/inst.sh
cd $BUILD_DEST
if [ $src_file -eq 0 ];then
    for file in $(ls opt/$name |grep -v zip);do
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
