#!/bin/bash

# This script mainly do the following jobs:
# 1. Update the sample apps source code
# 2. Copy all the sample app source directories to crosswalk-samples
# 3. Packing all the apk packages for the sample apps, both embedded and shared mode, arm and x86 architecture
# 4. Compress 4 kinds of apk packages: embedded-arm, embedded-x86, shared-arm, shared-x86
# 5. Compress the crosswalk-samples directory.
# 6. Copy the zip files to /mnt/otcqa/Sampleapp_SourceCode_And_Binary
#
# Attention:
#   At present this script can only be executed on orange host(10.239.52.64 by the time the script is modfied)
#   Path /home/orange/00_jiajia/workspace/sampleApp@orange
#   This is because it copys the zip files to the directory 
#   /mnt/otcqa/Sampleapp_SourceCode_And_Binary/ which is exposed to public URL
#   https://otcqa.sh.intel.com/qa-auto/live/Xwalk-testsuites/Sampleapp_SourceCode_And_Binary/
#   And only orange machine can map  /mnt/otcqa/Sampleapp_SourceCode_And_Binary/ to a valid path
#
# Modified:
#   2015-07-08: Add 6 sample apps from repository https://github.com/crosswalk-project/crosswalk-samples
#               Related: https://crosswalk-project.org/jira/browse/XWALK-4555
#   2015-07-23:  Modified the server IP and port for test team before packing the webrtc sample app.
#               Releated: https://crosswalk-project.org/jira/browse/XWALK-4663
#   2015-09-07: Add the building of crosswalk-samples/extensions-android
#   2015-09-23: Change the samples reference from crosswalk-samples.
#               tizen-apis and gallery, sysapps removed.
#               Releated: https://crosswalk-project.org/jira/browse/XWALK-4685
#   2015-12-03: Replace make_apk.py by app tools
#               Releated: https://crosswalk-project.org/jira/browse/XWALK-5737


. /etc/profile
usage="Usage: ./sampleApp_pack.sh -v <sdk_version> -r
-v <sdk_version> use <sdk_version> to  pack apk only,
-r it will not only pack apk but also comparess and pack sourcecode for release !!!"
ROOT_DIR=$PWD
PKG_TOOLS_DIR=$CROSSWALK_APP_TOOLS_CACHE_DIR
CROSSWALK_PKG=$PKG_TOOLS_DIR/crosswalk-app-tools/src/crosswalk-pkg

SDK_VERSION=""
RELEASE_FLAG=0
MODE="embedded"
ARCH="x86"

while getopts v:m:a:r opt
do
    case "$opt" in 
    v)  SDK_VERSION=$OPTARG;;
    m)  MODE=$OPTARG;;
    a)  ARCH=$OPTARG;;
    r)  RELEASE_FLAG=1;;
    *)  echo "$usage"
        exit 1;;
    esac
done

if [ -z $SDK_VERSION ];then
    echo $usage
    exit 1
fi


update_code(){

    cd $1
    git reset --hard HEAD
    git checkout master
    git pull
    git submodule update --init --recursive
}

clean_dir(){
    echo "Clean workspace..."
    cd $ROOT_DIR
    rm -rf Sampleapp_sourcecode Sampleapp_binary crosswalk-samples
    cd -
}

clean_dir

if [ ! -d $ROOT_DIR/crosswalk-demos ]; then
   git clone https://github.com/crosswalk-project/crosswalk-demos.git $ROOT_DIR/crosswalk-demos
fi

update_code $ROOT_DIR/crosswalk-demos
update_code $ROOT_DIR/crosswalk-samples-original

rm -rf $ROOT_DIR/crosswalk-samples
cp -a $ROOT_DIR/crosswalk-samples-original $ROOT_DIR/crosswalk-samples

cp -a $ROOT_DIR/crosswalk-demos/HangOnMan $ROOT_DIR/crosswalk-samples/
cp -a $ROOT_DIR/crosswalk-demos/HangOnMan/manifest.json $ROOT_DIR/crosswalk-samples/HangOnMan/src
cp -a $ROOT_DIR/crosswalk-demos/MemoryGame $ROOT_DIR/crosswalk-samples/
cp -a $ROOT_DIR/crosswalk-demos/MemoryGame/manifest.json $ROOT_DIR/crosswalk-samples/MemoryGame/src
cp -a $ROOT_DIR/HexGL $ROOT_DIR/crosswalk-samples/


# subsitute the server IP and port in webrtc/client/main.js
sed -i "s|var SERVER_IP = '192.168.0.25'|var SERVER_IP = '106.187.98.180'|" $ROOT_DIR/crosswalk-samples/webrtc/client/main.js
sed -i "s|var SERVER_PORT = 9000|var SERVER_PORT = 9001|" $ROOT_DIR/crosswalk-samples/webrtc/client/main.js

if [ -n $SDK_VERSION ];then
    if [ -f $PKG_TOOLS_DIR/crosswalk-$SDK_VERSION.zip ];then
        CROSSWALK_ZIP=$PKG_TOOLS_DIR/crosswalk-$SDK_VERSION.zip

        sed -i "s|8.37.189.14|${SDK_VERSION}|" $ROOT_DIR/crosswalk-samples/extensions-android/xwalk-echo-extension-src/build.xml
        sed -i "s|crosswalkproject.sample|crosswalkproject.sample --mode=\$1 --arch=\$2|" $ROOT_DIR/crosswalk-samples/extensions-android/build.sh
        mkdir $ROOT_DIR/crosswalk-samples/extensions-android/xwalk-echo-extension-src/lib
        cp -a $CROSSWALK_ZIP $ROOT_DIR/crosswalk-samples/extensions-android/xwalk-echo-extension-src/lib/crosswalk.zip
    else
        echo "$PKG_TOOLS_DIR/crosswalk-$SDK_VERSION.zip not exists, Please download first !!"
        exit 1
    fi
fi

build_apk(){

    BINARY_DIR=$ROOT_DIR/Sampleapp_binary
    rm -rf $BINARY_DIR
    mkdir -p $BINARY_DIR
    cd $BINARY_DIR
    
    set -e
    
    cp $ROOT_DIR/inst.py $BINARY_DIR/
    
    # Hexgl:
    $CROSSWALK_PKG --crosswalk=$CROSSWALK_ZIP --platforms=android --android=$1 --targets=$2 --enable-remote-debugging $ROOT_DIR/crosswalk-samples/HexGL/assets/www
    
    # Memorygame:
    $CROSSWALK_PKG --crosswalk=$CROSSWALK_ZIP --platforms=android --android=$1 --targets=$2 --enable-remote-debugging $ROOT_DIR/crosswalk-samples/MemoryGame/src
    
    #Simd:
    $CROSSWALK_PKG --crosswalk=$CROSSWALK_ZIP --platforms=android --android=$1 --targets=$2 --enable-remote-debugging $ROOT_DIR/crosswalk-samples/simd-mandelbrot
    
    #Webrtc
    $CROSSWALK_PKG --crosswalk=$CROSSWALK_ZIP --platforms=android --android=$1 --targets=$2 --enable-remote-debugging $ROOT_DIR/crosswalk-samples/webrtc/client
    
    #Hangoman
    $CROSSWALK_PKG --crosswalk=$CROSSWALK_ZIP --platforms=android --android=$1 --targets=$2 --enable-remote-debugging $ROOT_DIR/crosswalk-samples/HangOnMan/src
    
    # hello-world
    $CROSSWALK_PKG --crosswalk=$CROSSWALK_ZIP --platforms=android --android=$1 --targets=$2 --enable-remote-debugging $ROOT_DIR/crosswalk-samples/hello-world
    
    # space-dodge-game
    $CROSSWALK_PKG --crosswalk=$CROSSWALK_ZIP --platforms=android --android=$1 --targets=$2 --enable-remote-debugging $ROOT_DIR/crosswalk-samples/space-dodge-game/base

    # Change package id of other version space-dodge-game, to void same apk name.
    sed -i "s/Space Dodge/Space Dodge2/g" $ROOT_DIR/crosswalk-samples/space-dodge-game/manifest-orientation-resize/manifest.json
    sed -i "s/org.xwalk.spacedodgegame/org.xwalk.spacedodgegame2/g" $ROOT_DIR/crosswalk-samples/space-dodge-game/manifest-orientation-resize/manifest.json
    $CROSSWALK_PKG --crosswalk=$CROSSWALK_ZIP --platforms=android --android=$1 --targets=$2 --enable-remote-debugging  $ROOT_DIR/crosswalk-samples/space-dodge-game/manifest-orientation-resize

    sed -i "s/Space Dodge/Space Dodge3/g" $ROOT_DIR/crosswalk-samples/space-dodge-game/manifest-orientation-scale/manifest.json
    sed -i "s/org.xwalk.spacedodgegame/org.xwalk.spacedodgegame3/g" $ROOT_DIR/crosswalk-samples/space-dodge-game/manifest-orientation-scale/manifest.json
    $CROSSWALK_PKG --crosswalk=$CROSSWALK_ZIP --platforms=android --android=$1 --targets=$2 --enable-remote-debugging  $ROOT_DIR/crosswalk-samples/space-dodge-game/manifest-orientation-scale

    sed -i "s/Space Dodge/Space Dodge4/g" $ROOT_DIR/crosswalk-samples/space-dodge-game/screen-orientation-resize/manifest.json
    sed -i "s/org.xwalk.spacedodgegame/org.xwalk.spacedodgegame4/g" $ROOT_DIR/crosswalk-samples/space-dodge-game/screen-orientation-resize/manifest.json
    $CROSSWALK_PKG --crosswalk=$CROSSWALK_ZIP --platforms=android --android=$1 --targets=$2 --enable-remote-debugging  $ROOT_DIR/crosswalk-samples/space-dodge-game/screen-orientation-resize

    sed -i "s/Space Dodge/Space Dodge5/g" $ROOT_DIR/crosswalk-samples/space-dodge-game/screen-orientation-scale/manifest.json
    sed -i "s/org.xwalk.spacedodgegame/org.xwalk.spacedodgegame5/g" $ROOT_DIR/crosswalk-samples/space-dodge-game/screen-orientation-scale/manifest.json
    $CROSSWALK_PKG --crosswalk=$CROSSWALK_ZIP --platforms=android --android=$1 --targets=$2 --enable-remote-debugging  $ROOT_DIR/crosswalk-samples/space-dodge-game/screen-orientation-scale
    
    # webgl
    $CROSSWALK_PKG --crosswalk=$CROSSWALK_ZIP --platforms=android --android=$1 --targets=$2 --enable-remote-debugging $ROOT_DIR/crosswalk-samples/webgl
       
    # extensions-android
    cd $ROOT_DIR/crosswalk-samples/extensions-android
    ./build.sh $1 $2
    mv -fv *.apk $BINARY_DIR
    cd $BINARY_DIR
    
    set +e
    
    cd $ROOT_DIR
    rm -rf Sampleapp_binary.zip
    rm -rf Sampleapp_binary-${SDK_VERSION}-${1}-${2}.zip
    zip -r Sampleapp_binary-${SDK_VERSION}-${1}-${2}.zip Sampleapp_binary
}

if [ $RELEASE_FLAG -eq 0 ];then
    build_apk $MODE $ARCH
    wweek=$(date +"%W" -d "+1 weeks") 
    wtoday=$[$(date +%w)] 
    wdir="WW"$wweek 
    now_time=`date +%m-%d-%H%M`
 
    otcqa_dir=/mnt/otcqa/$wdir/master/"ww"$wweek"."$wtoday/sampleApp-$SDK_VERSION-$MODE-$ARCH/
    mkdir -p $otcqa_dir
    cp Sampleapp_binary-${SDK_VERSION}-${MODE}-${ARCH}.zip $otcqa_dir/

    echo "SampleApp apks have been packed done !!!"
    echo "You can check it here : http://otcqa.sh.intel.com/qa-auto/live/Xwalk-testsuites/$wdir/master/"ww"$wweek"."$wtoday/sampleApp-$SDK_VERSION-$MODE-$ARCH/"

elif [ $RELEASE_FLAG -eq 1 ];then
    build_apk embedded x86
    build_apk embedded arm
    build_apk shared x86
    build_apk shared arm
    rm -rf Sampleapp_sourcecode.zip
    
    # Remove the crosswalk-${VERSION} and crosswalk.zip file.
    rm -fr ${ROOT_DIR}/crosswalk-samples/extensions-android/xwalk-echo-extension-src/lib
    rm -fr ${ROOT_DIR}/crosswalk-samples/extensions-android/xwalk-echo-extension-src/build
    
    # Modify the crosswalk version back to make sure the source code is original.
    sed -i "s|${SDK_VERSION}|8.37.189.14|" $ROOT_DIR/crosswalk-samples/extensions-android/xwalk-echo-extension-src/build.xml
    zip -r Sampleapp_sourcecode.zip crosswalk-samples

    cp -fv Sampleapp_binary-${SDK_VERSION}-*.zip /mnt/otcqa/Sampleapp_SourceCode_And_Binary/
    cp -fv Sampleapp_sourcecode.zip /mnt/otcqa/Sampleapp_SourceCode_And_Binary/
    echo "SampleApp sourcecode and binary for release has been updated !!!"
    echo "You can check it here : http://otcqa.sh.intel.com/qa-auto/live/Xwalk-testsuites/Sampleapp_SourceCode_And_Binary/"
    #START# Put sampleapps on jiajiax [Yunfei] 2015.08.26
    data_folder=`find /data/TestSuites_Storage/live/android/ -type d -name ${SDK_VERSION}`
    if test -z ${data_folder};then
        echo "No ${data_folder} folder in /data/TestSuites_Storage/live/android/"
    else
        cp Sampleapp_binary-${SDK_VERSION}-shared-x86.zip ${data_folder}/testsuites-shared/x86/
        cp Sampleapp_binary-${SDK_VERSION}-shared-arm.zip ${data_folder}/testsuites-shared/arm/
        cp Sampleapp_binary-${SDK_VERSION}-embedded-x86.zip ${data_folder}/testsuites-embedded/x86/
        cp Sampleapp_binary-${SDK_VERSION}-embedded-arm.zip ${data_folder}/testsuites-embedded/arm/
    fi
    #END# Put sampleapps on jiajiax [Yunfei] 2015.08.26

fi


clean_dir
