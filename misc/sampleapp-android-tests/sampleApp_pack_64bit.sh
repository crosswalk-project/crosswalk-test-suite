#!/bin/bash

#Copyright (c) 2015 Intel Corporation.
#
#Redistribution and use in source and binary forms, with or without modification,
#are permitted provided that the following conditions are met:
#
#* Redistributions of works must retain the original copyright notice, this list
#  of conditions and the following disclaimer.
#* Redistributions in binary form must reproduce the original copyright notice,
#  this list of conditions and the following disclaimer in the documentation
#  and/or other materials provided with the distribution.
#* Neither the name of Intel Corporation nor the names of its contributors
#  may be used to endorse or promote products derived from this work without
#  specific prior written permission.
#
#THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
#AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
#INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
#BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
#OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
#EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#Authors:
#       Qiu, Zhong<zhongx.qiu@intel.com>
#       Li, Hao<haox.li@intel.com>

################################################################################
#
#  This script aims to pack 64bit Crosswalk sample apks.
#  Pre-condition:
#    1. Set CROSSWALK_APP_TOOLS_CACHE_DIR
#       $ export CROSSWALK_APP_TOOLS_CACHE_DIR=[local-path]
#    2. Clone crosswalk-app-tools to CROSSWALK_APP_TOOLS_CACHE_DIRs
#       $ git clone https://github.com/crosswalk-project/crosswalk-app-tools
#       $ cd crosswalk-app-tools
#       $ sudo npm install
#    3. Download the crosswalk zip you want to test to CROSSWALK_APP_TOOLS_CACHE_DIR
#
#  Usage:
#    ./sampleApp_pack.sh -v <crosswalk-version> -a <arch> -m <mode> -r
#
################################################################################ 

source /etc/profile

ROOT_DIR=$(cd $(dirname $0); pwd)
CROSSWALK=""
CROSSWALK_VERSION=""
MODE="embedded"
ARCH="x86_64"
PKG_TOOLS="crosswalk-pkg"

OFFICIAL_RELEASE_FLAG=false
SAMPLEAPP_DIR="/work/webapi/ww/ww03/sampleapp_code"
DEST_BINARY_DIR=""
TEST_DEST_BINARY_DIR="${ROOT_DIR}/xwalk_sampleapp"
OFFICIAL_DEST_BINARY_DIR="${ROOT_DIR}/release_sampleapp"


echo_help() {
    echo "Usage: ./sampleApp_pack.sh -v <crosswalk-version> -a <arch> -m <mode> -r"
    echo "       -v <crosswalk-version>:  crosswalk version to build apk"
    echo "       -a <arch>: build apk arch"
    echo "       -v <mode>: build apk mode"
    echo "       -r : OFFICIAL_RELEASE_FLAG it will not only pack apk but also comparess and pack sourcecode for release !!!"
}


echo_opts() {
    echo "################################################################################"
    echo "Workspace directory: ${SAMPLEAPP_DIR}"
    echo "Samples apps binary directory: ${DEST_BINARY_DIR}"
    echo "Crosswalk Version: ${CROSSWALK_VERSION}"
    echo "Crosswalk: ${CROSSWALK}"
    echo "Build mode: ${MODE}"
    echo "Build arch: ${ARCH}"
    echo "Release: ${OFFICIAL_RELEASE_FLAG}"
    echo "################################################################################"
}


while getopts v:m:a:r opt
do
    case "$opt" in 
    v)  CROSSWALK_VERSION=$OPTARG;;
    m)  MODE=$OPTARG;;
    a)  ARCH=$OPTARG;;
    r)  OFFICIAL_RELEASE_FLAG=true;;
    *)  echo_help
        exit 1;;
    esac
done


init_opts() {
    # init CROSSWALK_VERSION
    if [ -z $CROSSWALK_VERSION ];then
        echo ">>>> Fail to get crosswalk version "
        exit 1
    fi
    if [ -f ${CROSSWALK_APP_TOOLS_CACHE_DIR}/crosswalk-${CROSSWALK_VERSION}-64bit.zip ]; then
        CROSSWALK=${CROSSWALK_APP_TOOLS_CACHE_DIR}/crosswalk-${CROSSWALK_VERSION}-64bit.zip
    else
        CROSSWALK=$CROSSWALK_VERSION
    fi

    #int PKG_TOOLS
    which $PKG_TOOLS
    if [ $? -ne 0 ]; then
        PKG_TOOLS=${CROSSWALK_APP_TOOLS_CACHE_DIR}/crosswalk-app-tools/src/crosswalk-pkg
    fi

    #init DEST_BINARY_DIR
    if $OFFICIAL_RELEASE_FLAG; then
        DEST_BINARY_DIR=${OFFICIAL_DEST_BINARY_DIR}
    else
        DEST_BINARY_DIR=${TEST_DEST_BINARY_DIR}
    fi
    if [ ! -d $DEST_BINARY_DIR ]; then
        mkdir -p $DEST_BINARY_DIR
    fi
}


clean_dir() {
    if [ -d $1 ]; then
        rm -rf $1
    fi
}


clean_workspace() {
    echo ">>>> Clean workspace..."
    clean_dir ${ROOT_DIR}/Sampleapp_binary
    clean_dir ${ROOT_DIR}/crosswalk-samples
}


update_code() {
    cd $1
    git reset --hard HEAD
    git checkout master
    git pull
    git submodule update --init --recursive
    cd -
}


init_sampleapp_code() {

    # HexGL: https://github.com/BKcore/HexGL
    if [ ! -d ${SAMPLEAPP_DIR}/HexGL ]; then
        git clone https://github.com/BKcore/HexGL.git ${SAMPLEAPP_DIR}/HexGL
    fi
    update_code ${SAMPLEAPP_DIR}/HexGL

    # sample-my-private-photos: https://github.com/gomobile/sample-my-private-photos
    if [ ! -d ${SAMPLEAPP_DIR}/sample-my-private-photos ]; then
        git clone https://github.com/gomobile/sample-my-private-photos.git ${SAMPLEAPP_DIR}/sample-my-private-photos
    fi
    update_code ${SAMPLEAPP_DIR}/sample-my-private-photos

    # crosswalk-demos: https://github.com/crosswalk-project/crosswalk-demos
    if [ ! -d ${SAMPLEAPP_DIR}/crosswalk-demos ]; then
        git clone https://github.com/crosswalk-project/crosswalk-demos.git ${SAMPLEAPP_DIR}/crosswalk-demos
    fi
    update_code ${SAMPLEAPP_DIR}/crosswalk-demos

    # crosswalk-samples: https://github.com/crosswalk-project/crosswalk-samples
    if [ ! -d ${SAMPLEAPP_DIR}/crosswalk-samples ]; then
        git clone https://github.com/crosswalk-project/crosswalk-samples.git ${SAMPLEAPP_DIR}/crosswalk-samples-master
    fi
    update_code ${SAMPLEAPP_DIR}/crosswalk-samples-master


    # combine sample apps to crosswalk-samples
    if [ -d ${ROOT_DIR}/crosswalk-samples ]; then
        rm -rf ${ROOT_DIR}/crosswalk-samples
    fi
    cp -a ${SAMPLEAPP_DIR}/crosswalk-samples-master ${ROOT_DIR}/crosswalk-samples
    cp -a ${SAMPLEAPP_DIR}/crosswalk-demos/HangOnMan ${ROOT_DIR}/crosswalk-samples/
    cp -a ${SAMPLEAPP_DIR}/crosswalk-demos/HangOnMan/manifest.json ${ROOT_DIR}/crosswalk-samples/HangOnMan/src
    cp -a ${SAMPLEAPP_DIR}/crosswalk-demos/MemoryGame ${ROOT_DIR}/crosswalk-samples/
    cp -a ${SAMPLEAPP_DIR}/crosswalk-demos/MemoryGame/manifest.json ${ROOT_DIR}/crosswalk-samples/MemoryGame/src
    cp -a ${SAMPLEAPP_DIR}/HexGL ${ROOT_DIR}/crosswalk-samples/
    cp -a ${SAMPLEAPP_DIR}/sample-my-private-photos ${ROOT_DIR}/crosswalk-samples/
}

pack_sampleapp_sourcecode() {
    if [ -d ${ROOT_DIR}/crosswalk-samples ]; then
        cd ${ROOT_DIR}
        zip -qr ${DEST_BINARY_DIR}/Sampleapp_sourcecode.zip crosswalk-samples
    else
        echo ">>>>> Fail to pack sampleapp source code!!!"
        exit 1
    fi
}


update_sampeapp_config() {
    # webrtc: subsitute the server IP and port in webrtc/client/main.js
    sed -i "s|var SERVER_IP = '192.168.0.25'|var SERVER_IP = '106.187.98.180'|" ${ROOT_DIR}/crosswalk-samples/webrtc/client/main.js
    sed -i "s|var SERVER_PORT = 9000|var SERVER_PORT = 9001|" ${ROOT_DIR}/crosswalk-samples/webrtc/client/main.js

    # extensions-android: update crosswalk version for ant
    echo $CROSSWALK |grep ".zip" > /dev/null 2>&1
    if [ $? -eq 0 ]; then
        if [ ! -d ${ROOT_DIR}/crosswalk-samples/extensions-android/xwalk-echo-extension-src/lib ]; then
            mkdir -pv ${ROOT_DIR}/crosswalk-samples/extensions-android/xwalk-echo-extension-src/lib
        fi
        cp -fv $CROSSWALK ${ROOT_DIR}/crosswalk-samples/extensions-android/xwalk-echo-extension-src/lib/crosswalk.zip
        unzip -q ${ROOT_DIR}/crosswalk-samples/extensions-android/xwalk-echo-extension-src/lib/crosswalk.zip -d ${ROOT_DIR}/crosswalk-samples/extensions-android/xwalk-echo-extension-src/lib/
    fi
    sed -i "s|15.44.384.13|${CROSSWALK_VERSION}-64bit|" ${ROOT_DIR}/crosswalk-samples/extensions-android/xwalk-echo-extension-src/build.xml

    # space-dodge-game: change package id of other version space-dodge-game, to void same apk name.
    sed -i "s/Space Dodge/Space Dodge2/g" ${ROOT_DIR}/crosswalk-samples/space-dodge-game/manifest-orientation-resize/manifest.json
    sed -i "s/org.xwalk.spacedodgegame/org.xwalk.spacedodgegame2/g" ${ROOT_DIR}/crosswalk-samples/space-dodge-game/manifest-orientation-resize/manifest.json

    sed -i "s/Space Dodge/Space Dodge3/g" ${ROOT_DIR}/crosswalk-samples/space-dodge-game/manifest-orientation-scale/manifest.json
    sed -i "s/org.xwalk.spacedodgegame/org.xwalk.spacedodgegame3/g" ${ROOT_DIR}/crosswalk-samples/space-dodge-game/manifest-orientation-scale/manifest.json

    sed -i "s/Space Dodge/Space Dodge4/g" ${ROOT_DIR}/crosswalk-samples/space-dodge-game/screen-orientation-resize/manifest.json
    sed -i "s/org.xwalk.spacedodgegame/org.xwalk.spacedodgegame4/g" ${ROOT_DIR}/crosswalk-samples/space-dodge-game/screen-orientation-resize/manifest.json

    sed -i "s/Space Dodge/Space Dodge5/g" ${ROOT_DIR}/crosswalk-samples/space-dodge-game/screen-orientation-scale/manifest.json
    sed -i "s/org.xwalk.spacedodgegame/org.xwalk.spacedodgegame5/g" ${ROOT_DIR}/crosswalk-samples/space-dodge-game/screen-orientation-scale/manifest.json
}


build_apk() {
    mode=$1
    arch=$2

    BINARY_DIR=${ROOT_DIR}/Sampleapp_binary
    clean_dir $BINARY_DIR
    mkdir -pv $BINARY_DIR
    cd $BINARY_DIR

    set -e

    cp -fv ${SAMPLEAPP_DIR}/inst.py ${BINARY_DIR}

    # 1. extensions-android
    cd ${ROOT_DIR}/crosswalk-samples/extensions-android
    ./build.sh -v ${CROSSWALK_VERSION} -a ${arch} -m ${mode}
    mv -fv *.apk ${BINARY_DIR}
    cd ${BINARY_DIR}

    # 2. HangOnMan    
    $PKG_TOOLS --crosswalk=$CROSSWALK --platforms=android --android=${mode} --targets=${arch} --enable-remote-debugging ${ROOT_DIR}/crosswalk-samples/HangOnMan/src

    # 3. hello-world
    $PKG_TOOLS --crosswalk=$CROSSWALK --platforms=android --android=${mode} --targets=${arch} --enable-remote-debugging ${ROOT_DIR}/crosswalk-samples/hello-world

    # 4. HexGL
    if [ -f ${ROOT_DIR}/crosswalk-samples/HexGL/manifest.json ]; then
        $PKG_TOOLS --crosswalk=$CROSSWALK --platforms=android --android=${mode} --targets=${arch} --enable-remote-debugging ${ROOT_DIR}/crosswalk-samples/HexGL
    else
        $PKG_TOOLS --crosswalk=$CROSSWALK --manifest='{ "name": "HexGL", 
                                                        "start_url": "index.html",
                                                        "xwalk_app_version": "0.0.1",
                                                        "xwalk_package_id": "org.xwalk.hexgl",
                                                        "icons": [
                                                            {"src":"icon_32.png","sizes":"32x32"},
                                                            {"src":"icon_64.png","sizes":"64x64"},
                                                            {"src":"icon_128.png","sizes":"128x128"},
                                                            {"src":"icon_256.png","sizes":"256x256"}
                                                        ]    
                                                      }' --platforms=android --android=${mode} --targets=${arch} --enable-remote-debugging ${ROOT_DIR}/crosswalk-samples/HexGL
    fi

    # 5. MemoryGame
    $PKG_TOOLS --crosswalk=$CROSSWALK --platforms=android --android=${mode} --targets=${arch} --enable-remote-debugging ${ROOT_DIR}/crosswalk-samples/MemoryGame/src

    # 6. simd-mandelbrot
    $PKG_TOOLS --crosswalk=$CROSSWALK --platforms=android --android=${mode} --targets=${arch} --enable-remote-debugging ${ROOT_DIR}/crosswalk-samples/simd-mandelbrot

    # 7. space-dodge-game
    $PKG_TOOLS --crosswalk=$CROSSWALK --platforms=android --android=${mode} --targets=${arch} --enable-remote-debugging ${ROOT_DIR}/crosswalk-samples/space-dodge-game/base

    # 7.1 
    $PKG_TOOLS --crosswalk=$CROSSWALK --platforms=android --android=${mode} --targets=${arch} --enable-remote-debugging  ${ROOT_DIR}/crosswalk-samples/space-dodge-game/manifest-orientation-resize

    # 7.2
    $PKG_TOOLS --crosswalk=$CROSSWALK --platforms=android --android=${mode} --targets=${arch} --enable-remote-debugging  ${ROOT_DIR}/crosswalk-samples/space-dodge-game/manifest-orientation-scale

    # 7.3
    $PKG_TOOLS --crosswalk=$CROSSWALK --platforms=android --android=${mode} --targets=${arch} --enable-remote-debugging  ${ROOT_DIR}/crosswalk-samples/space-dodge-game/screen-orientation-resize

    # 7.4
    $PKG_TOOLS --crosswalk=$CROSSWALK --platforms=android --android=${mode} --targets=${arch} --enable-remote-debugging  ${ROOT_DIR}/crosswalk-samples/space-dodge-game/screen-orientation-scale

    # 8. webgl
    $PKG_TOOLS --crosswalk=$CROSSWALK --platforms=android --android=${mode} --targets=${arch} --enable-remote-debugging ${ROOT_DIR}/crosswalk-samples/webgl

    # 9. webrtc
    $PKG_TOOLS --crosswalk=$CROSSWALK --platforms=android --android=${mode} --targets=${arch} --enable-remote-debugging ${ROOT_DIR}/crosswalk-samples/webrtc/client

    set +e

    cd ${ROOT_DIR}
    if [ ${arch} == "arm64-v8a" ]; then
        friendly_arch="arm64"
    else
        friendly_arch=${arch}
    fi
    rm -rf ${DEST_BINARY_DIR}/Sampleapp_binary-${CROSSWALK_VERSION}-${mode}-${friendly_arch}.zip
    zip -qr ${DEST_BINARY_DIR}/Sampleapp_binary-${CROSSWALK_VERSION}-${mode}-${friendly_arch}.zip Sampleapp_binary
}


build_release_package() {
    build_apk embedded x86_64
    build_apk embedded arm64-v8a
    # the arch does not effect shared mode.
    build_apk shared x86_64


    echo "SampleApp sourcecode and binary for release has been updated !!!"
    echo "You can check it here : http://otcqa.sh.intel.com/qa-auto/live/Xwalk-testsuites/Sampleapp_SourceCode_And_Binary/"
}


################################################################################
# Main
################################################################################

clean_workspace

init_opts
echo_opts

init_sampleapp_code
pack_sampleapp_sourcecode
update_sampeapp_config


if $OFFICIAL_RELEASE_FLAG; then
    build_release_package
else
    build_apk $MODE $ARCH
fi

clean_workspace

