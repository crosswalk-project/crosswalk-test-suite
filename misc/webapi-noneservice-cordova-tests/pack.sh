#!/bin/bash
source $(dirname $0)/webapi-noneservice-cordova-tests.spec

usage="Usage: ./pack.sh [-a <apk runtime arch: x86 | arm>]"

arch="x86"
while getopts a: o
do
    case "$o" in
    a) arch=$OPTARG;;
    *) echo "$usage"
       exit 1;;
    esac
done

SRC_ROOT=$(cd $(dirname $0);pwd)
BUILD_ROOT=/tmp/${name}_pack
BUILD_DEST=/tmp/${name}

# clean
function clean_workspace(){
    echo "cleaning workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    rm -rf $BUILD_ROOT $BUILD_DEST
}
function install_plugins() 
{ 
  plugman install --platform android --project ./ --plugin $SRC_ROOT/../../tools/cordova_plugins/cordova-plugin-battery-status 
  plugman install --platform android --project ./ --plugin $SRC_ROOT/../../tools/cordova_plugins/cordova-plugin-camera 
  plugman install --platform android --project ./ --plugin $SRC_ROOT/../../tools/cordova_plugins/cordova-plugin-contacts 
  plugman install --platform android --project ./ --plugin $SRC_ROOT/../../tools/cordova_plugins/cordova-plugin-device 
  plugman install --platform android --project ./ --plugin $SRC_ROOT/../../tools/cordova_plugins/cordova-plugin-device-motion 
  plugman install --platform android --project ./ --plugin $SRC_ROOT/../../tools/cordova_plugins/cordova-plugin-device-orientation  
  plugman install --platform android --project ./ --plugin $SRC_ROOT/../../tools/cordova_plugins/cordova-plugin-dialogs
  plugman install --platform android --project ./ --plugin $SRC_ROOT/../../tools/cordova_plugins/cordova-plugin-file 
  plugman install --platform android --project ./ --plugin $SRC_ROOT/../../tools/cordova_plugins/cordova-plugin-file-transfer
  plugman install --platform android --project ./ --plugin $SRC_ROOT/../../tools/cordova_plugins/cordova-plugin-geolocation 
  plugman install --platform android --project ./ --plugin $SRC_ROOT/../../tools/cordova_plugins/cordova-plugin-globalization 
  plugman install --platform android --project ./ --plugin $SRC_ROOT/../../tools/cordova_plugins/cordova-plugin-inappbrowser 
  plugman install --platform android --project ./ --plugin $SRC_ROOT/../../tools/cordova_plugins/cordova-plugin-media 
  plugman install --platform android --project ./ --plugin $SRC_ROOT/../../tools/cordova_plugins/cordova-plugin-media-capture
  plugman install --platform android --project ./ --plugin $SRC_ROOT/../../tools/cordova_plugins/cordova-plugin-network-information
  plugman install --platform android --project ./ --plugin $SRC_ROOT/../../tools/cordova_plugins/cordova-plugin-splashscreen
  plugman install --platform android --project ./ --plugin $SRC_ROOT/../../tools/cordova_plugins/cordova-plugin-vibration 
}

clean_workspace
mkdir -p $BUILD_ROOT $BUILD_DEST

# copy source code
rm -rf $SRC_ROOT/*.zip
cp -arf $SRC_ROOT/* $BUILD_ROOT/

for list in $LIST;do
    cp -ar $list $BUILD_ROOT/
done

## creat testlist.json ##
echo "[
    {\"category\": \"W3C\", \"tests\":
        [" > $BUILD_DEST/testlist.json
for suite in $LIST;do
    echo "\"`basename $suite`\"",
done | sort | sed '$s/,//' >>$BUILD_DEST/testlist.json
echo "        ]
    }
]" >>$BUILD_DEST/testlist.json


for suite in $LIST;do
    #python $SRC_ROOT/../../tools/build/pack.py -t apk-aio -m embedded -a $arch -d $BUILD_DEST -s $SRC_ROOT/$suite
    python $SRC_ROOT/../../tools/build/pack.py -t cordova-aio -d $BUILD_DEST -s $SRC_ROOT/$suite
done

mkdir $BUILD_ROOT/apps
mv `find /tmp/webapi-noneservice-cordova-tests/ -name '*apk'` $BUILD_ROOT/apps

## creat apk ##
cd $BUILD_DEST
cp -a $BUILD_ROOT/icon.png     $BUILD_DEST/
cp -a $BUILD_ROOT/webrunner/*     $BUILD_DEST/
mv $BUILD_DEST/index.html $BUILD_DEST/wr-index.html
cat > index.html << EOF
<!doctype html>
<head>
    <meta http-equiv="Refresh" content="1; url=wr-index.html?testprefix=./">
</head>
EOF
#cp -a $BUILD_ROOT/testlist.json     $BUILD_DEST/

cp -ar $SRC_ROOT/../../tools/cordova $BUILD_ROOT/
#cd $BUILD_ROOT/crosswalk
#python make_apk.py --package=org.xwalk.$appname --name=$appname --app-root=$BUILD_DEST --app-local-path=entry.html --icon=$BUILD_DEST/icon.png --mode=embedded --arch=$arch --enable-remote-debugging
cd $BUILD_ROOT/cordova/
bin/create $appname org.xwalk.$appname $appname
cd $BUILD_ROOT/cordova/$appname
install_plugins
cp -ar $BUILD_DEST/* $BUILD_ROOT/cordova/$appname/assets/www/
cd $BUILD_ROOT/cordova/$appname/
sed -i '/<uses-permission android:name="android.permission.INTERNET"/a <uses-permission android:name="android.permission.CAMERA" />' AndroidManifest.xml
./cordova/build
if [ $? -ne 0 ];then
    echo "Create $name.apk fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi

## cp tests.xml and inst.sh ##
mkdir -p $BUILD_DEST/opt/$name
cp $BUILD_ROOT/inst.py $BUILD_DEST/opt/$name/inst.py
cp -a $BUILD_ROOT/apps $BUILD_DEST/opt/$name

for suite in `ls $BUILD_ROOT |grep "\-tests" |grep -v spec$`;do
    cp $BUILD_ROOT/$suite/tests.xml  $BUILD_DEST/opt/$name/$suite.tests.xml
    cp $BUILD_ROOT/$suite/tests.full.xml  $BUILD_DEST/opt/$name/$suite.tests.full.xml
    if [ -f $BUILD_ROOT/$suite/tests.full.xml ];then
        cp $BUILD_ROOT/$suite/tests.android.xml  $BUILD_DEST/opt/$name/$suite.tests.xml
    fi
    sed -i "s/<suite/<suite widget=\"$name\"/g" $BUILD_DEST/opt/$name/$suite.tests.xml
    sed -i "s/<suite/<suite widget=\"$name\"/g" $BUILD_DEST/opt/$name/$suite.tests.full.xml
    rm -rf $BUILD_DEST/opt/$suite
done

## creat zip package ##
mv $BUILD_ROOT/cordova/*.apk $BUILD_DEST/opt/$name/
mv $BUILD_ROOT/cordova/$appname/bin/$appname-debug.apk $BUILD_DEST/opt/$name/$appname.apk
if [ -f $BUILD_DEST/opt/$name/WebapiNoneserviceTests_$arch.apk ];then
    mv $BUILD_DEST/opt/$name/WebapiNoneserviceTests_$arch.apk $BUILD_DEST/opt/$name/webapi_noneservice_cordova_tests.apk
fi
cd $BUILD_DEST

zip -Drq $BUILD_DEST/$name-$version-$sub_version.apk.zip opt/
if [ $? -ne 0 ];then
    echo "Create zip package fail... >>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi

# copy zip file
echo "copy package from workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
cp -f $BUILD_DEST/$name-$version-$sub_version.apk.zip $SRC_ROOT/

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
