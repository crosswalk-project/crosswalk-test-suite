#!/bin/bash
source $(dirname $0)/webapi-service-tests.spec
SRC_ROOT=$(cd $(dirname $0);pwd)
BUILD_ROOT=/tmp/$name

usage="Usage: ./pack.sh [-t <package type: apk | cordova>] [-a <apk runtime arch: x86 | arm>]
[-t apk] option was set as default.
[-a x86] option was set as default.
"

pack_type="apk"
arch="x86"
while getopts a:t: o
do
    case "$o" in
    a) arch=$OPTARG;;
    t) pack_type=$OPTARG;;
    *) echo "$usage"
       exit 1;;
    esac
done

rm -rf $SRC_ROOT/*.zip

# clean
function clean_workspace(){
    echo "cleaning workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    rm -rf $BUILD_ROOT
}

echo "cleaning workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
clean_workspace
mkdir -p $BUILD_ROOT

## creat apk ##
cp -a $SRC_ROOT/icon.png     $BUILD_ROOT/

if [ $pack_type == "apk" ];then
    cp -ar $SRC_ROOT/../../tools/crosswalk $BUILD_ROOT/crosswalk
 
    cd $BUILD_ROOT/crosswalk
    python make_apk.py --package=org.xwalk.$appname --name=$appname --app-url=http://127.0.0.1:8080/index.html --icon=$BUILD_ROOT/icon.png --mode=embedded --arch=$arch --enable-remote-debugging
elif [ $pack_type == "cordova" ];then
    cp -ar $SRC_ROOT/../../tools/cordova $BUILD_ROOT/cordova
    cp -ar $SRC_ROOT/../../tools/cordova_plugins $BUILD_ROOT/cordova_plugins
    
    cd $BUILD_ROOT/cordova
    bin/create $appname org.xwalk.$appname $appname
    
    cd $BUILD_ROOT/cordova/$appname
    
    for plugin in `ls $BUILD_ROOT/cordova_plugins`
    do
        plugman install --platform android --project ./ --plugin $BUILD_ROOT/cordova_plugins/$plugin
    done
    
    cd $BUILD_ROOT/cordova/$appname/assets/www
    
    cat > index.html << EOF
<!doctype html>
<head>
    <meta http-equiv="Refresh" content="1; url=http://127.0.0.1:8080/index.html">
</head>
EOF

    cd $BUILD_ROOT/cordova/$appname

    ./cordova/build
fi

if [ $? -ne 0 ];then
    echo "Create $name.apk fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi

## cp tests.xml and inst.sh ##
mkdir -p $BUILD_ROOT/opt/$name
cp $SRC_ROOT/inst.py $BUILD_ROOT/opt/$name/inst.py

for list in $LIST;do
    suite=`basename $list`
    cp $SRC_ROOT/../../../crosswalk-test-suite/webapi/$list/tests.xml  $BUILD_ROOT/opt/$name/$suite.tests.xml
    sed -i "s/<suite/<suite widget=\"$name\"/g" $BUILD_ROOT/opt/$name/$suite.tests.xml
    cp $SRC_ROOT/../../../crosswalk-test-suite/webapi/$list/tests.full.xml  $BUILD_ROOT/opt/$name/$suite.tests.full.xml
    sed -i "s/<suite/<suite widget=\"$name\"/g" $BUILD_ROOT/opt/$name/$suite.tests.full.xml
done

## creat zip package ##
if [ $pack_type == "apk" ];then
    mv $BUILD_ROOT/crosswalk/*.apk $BUILD_ROOT/opt/$name/

    if [ -f $BUILD_ROOT/opt/$name/WebapiServiceTests_$arch.apk ];then
        mv $BUILD_ROOT/opt/$name/WebapiServiceTests_$arch.apk $BUILD_ROOT/opt/$name/$appname.apk
    fi
elif [ $pack_type == "cordova" ];then
    if [ -f $BUILD_ROOT/cordova/$appname/bin/$appname-debug.apk ];then
        mv $BUILD_ROOT/cordova/$appname/bin/$appname-debug.apk $BUILD_ROOT/opt/$name/$appname.apk
    fi
fi

cd $BUILD_ROOT
zip -Drq $BUILD_ROOT/$name-$version-$sub_version.$pack_type.zip opt/
if [ $? -ne 0 ];then
    echo "Create zip package fail... >>>>>>>>>>>>#>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi

# copy zip file
echo "copy package from workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
cp -f $BUILD_ROOT/$name-$version-$sub_version.$pack_type.zip $SRC_ROOT/

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
