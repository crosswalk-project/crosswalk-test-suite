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
#	              tizen-apis and gallery, sysapps removed.
#               Releated: https://crosswalk-project.org/jira/browse/XWALK-4685


. /etc/profile
usage="Usage: ./sampleApp_pack.sh -v <sdk_version> -r
-v <sdk_version> use <sdk_version> to  pack apk only,
-r it will not only pack apk but also comparess and pack sourcecode for release !!!"
ROOT_DIR=$(dirname $(readlink -f $0))
PKG_TOOLS_DIR=/mnt/jiajiax_shared/pkg_tools

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

}

clean_dir(){
    echo "Clean workspace..."
    cd $ROOT_DIR
    rm -rf Sampleapp_sourcecode Sampleapp_binary crosswalk-samples crosswalk-$SDK_VERSION
    cd -
}

clean_dir

update_code $ROOT_DIR/crosswalk-samples-original
update_code $ROOT_DIR/webapps-hangonman
update_code $ROOT_DIR/webapps-hangonman/app/lib/smokesignals.js

if [ -d $ROOT_DIR/crosswalk-demos ]; then
    update_code $ROOT_DIR/crosswalk-demos
else
    git clone https://github.com/crosswalk-project/crosswalk-demos.git
    mv crosswalk-demos $ROOT_DIR
fi

rm -rf $ROOT_DIR/crosswalk-samples
cp -a $ROOT_DIR/crosswalk-samples-original $ROOT_DIR/crosswalk-samples

cp -a $ROOT_DIR/crosswalk-demos/HangOnMan $ROOT_DIR/crosswalk-samples/
cp -a $ROOT_DIR/crosswalk-demos/MemoryGame $ROOT_DIR/crosswalk-samples/
cp -a $ROOT_DIR/MemoryGame/src/* $ROOT_DIR/crosswalk-samples/MemoryGame/src/
cp -r $ROOT_DIR/webapps-hangonman/* $ROOT_DIR/crosswalk-samples/HangOnMan/src/
cp -a $ROOT_DIR/HexGL $ROOT_DIR/crosswalk-samples/

# subsitute the server IP and port in webrtc/client/main.js
sed -i "s|var SERVER_IP = '192.168.0.25'|var SERVER_IP = '106.187.98.180'|" $ROOT_DIR/crosswalk-samples/webrtc/client/main.js
sed -i "s|var SERVER_PORT = 9000|var SERVER_PORT = 9001|" $ROOT_DIR/crosswalk-samples/webrtc/client/main.js

if [ -n $SDK_VERSION ];then
    if [ -d $PKG_TOOLS_DIR/crosswalk-$SDK_VERSION ];then
        rm -rf $ROOT_DIR/crosswalk-$SDK_VERSION
        cp -r $PKG_TOOLS_DIR/crosswalk-$SDK_VERSION $ROOT_DIR/
        CROSSWALK_DIR=$ROOT_DIR/crosswalk-$SDK_VERSION
        
        sed -i "s|8.37.189.14|${SDK_VERSION}|" $ROOT_DIR/crosswalk-samples/extensions-android/xwalk-echo-extension-src/build.xml
        sed -i "s|crosswalkproject.sample|crosswalkproject.sample --mode=\$1 --arch=\$2|" $ROOT_DIR/crosswalk-samples/extensions-android/build.sh
        mkdir $ROOT_DIR/crosswalk-samples/extensions-android/xwalk-echo-extension-src/lib
        cp -fr $ROOT_DIR/crosswalk-${SDK_VERSION} $ROOT_DIR/crosswalk-samples/extensions-android/xwalk-echo-extension-src/lib/crosswalk-${SDK_VERSION}
        cd ${ROOT_DIR}
        zip crosswalk.zip crosswalk-${SDK_VERSION}/
        mv -fv crosswalk.zip $ROOT_DIR/crosswalk-samples/extensions-android/xwalk-echo-extension-src/lib/
    else
        echo "$PKG_TOOLS_DIR/crosswalk-$SDK_VERSION not exists, Please download first !!"
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
    python $CROSSWALK_DIR/make_apk.py --package=org.xwalk.hexgl --name=Hexgl --app-root=$ROOT_DIR/crosswalk-samples/HexGL/assets/www --app-local-path=index.html --mode=$1 --arch=$2 --enable-remote-debugging
    
    # Memorygame:
    python $CROSSWALK_DIR/make_apk.py --package=org.xwalk.memorygame --name=Memorygame --app-root=$ROOT_DIR/crosswalk-samples/MemoryGame/src --app-local-path=index.html --mode=$1 --arch=$2 --enable-remote-debugging
    
    #Simd:
    python $CROSSWALK_DIR/make_apk.py --package=org.xwalk.simd --manifest=$ROOT_DIR/crosswalk-samples/simd-mandelbrot/manifest.json --app-versionCode=1 --mode=$1 --arch=$2  --enable-remote-debugging
    
    #Webrtc
    python $CROSSWALK_DIR/make_apk.py --package=org.xwalk.webrtc --manifest=$ROOT_DIR/crosswalk-samples/webrtc/client/manifest.json --mode=$1 --arch=$2 --enable-remote-debugging
    
    #Hangoman
    python $CROSSWALK_DIR/make_apk.py --package=org.xwalk.hangonman --name=hangonman --app-root=$ROOT_DIR/crosswalk-samples/HangOnMan/src/app --app-local-path=index.html --mode=$1 --arch=$2 --enable-remote-debugging
    
    # hello-world
    python $CROSSWALK_DIR/make_apk.py --package=org.xwalk.helloworld --manifest=$ROOT_DIR/crosswalk-samples/hello-world/manifest.json --app-versionCode=1 --mode=$1 --arch=$2 --enable-remote-debugging
    
    # space-dodge-game
    python $CROSSWALK_DIR/make_apk.py --package=org.xwalk.spacedodgegame --manifest=$ROOT_DIR/crosswalk-samples/space-dodge-game/base/manifest.json --app-versionCode=1 --mode=$1 --arch=$2 --enable-remote-debugging

    python $CROSSWALK_DIR/make_apk.py --name='Space Dodge2' --package=org.xwalk.spacedodgegame2 --manifest=$ROOT_DIR/crosswalk-samples/space-dodge-game/manifest-orientation-resize/manifest.json --app-versionCode=1 --mode=$1 --arch=$2 --enable-remote-debugging

    python $CROSSWALK_DIR/make_apk.py --name='Space Dodge3' --package=org.xwalk.spacedodgegame3 --manifest=$ROOT_DIR/crosswalk-samples/space-dodge-game/manifest-orientation-scale/manifest.json --app-versionCode=1 --mode=$1 --arch=$2 --enable-remote-debugging

    python $CROSSWALK_DIR/make_apk.py --name='Space Dodge4' --package=org.xwalk.spacedodgegame4 --manifest=$ROOT_DIR/crosswalk-samples/space-dodge-game/screen-orientation-resize/manifest.json --app-versionCode=1 --mode=$1 --arch=$2 --enable-remote-debugging

    python $CROSSWALK_DIR/make_apk.py --name='Space Dodge5' --package=org.xwalk.spacedodgegame5 --manifest=$ROOT_DIR/crosswalk-samples/space-dodge-game/screen-orientation-scale/manifest.json --app-versionCode=1 --mode=$1 --arch=$2 --enable-remote-debugging
    
    # webgl
    python $CROSSWALK_DIR/make_apk.py --package=org.xwalk.webgl --manifest=$ROOT_DIR/crosswalk-samples/webgl/manifest.json --app-versionCode=1 --mode=$1 --arch=$2 --enable-remote-debugging
       
    # extensions-android
    cd $ROOT_DIR/crosswalk-samples/extensions-android
    ./build.sh $1 $2
    mv -fv $ROOT_DIR/crosswalk-samples/extensions-android/xwalk-echo-extension-src/lib/crosswalk-${SDK_VERSION}/*.apk $BINARY_DIR
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
rm -rf $CROSSWALK_DIR
