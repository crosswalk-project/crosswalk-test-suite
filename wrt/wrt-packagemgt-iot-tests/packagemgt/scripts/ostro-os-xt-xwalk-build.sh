#!/bin/bash

# This script tries to build ostro-os-xt image on a Ubuntu Linux host.
# Prerequirements:
#   HW:
#       RAM: > 8GB
#   SW:
#       Ubuntu Linux x86_64
#       GCC: 4.9+
#       Yocto environment ready for building Ostro images.

use_docker=$1

export WORKSPACE=$HOME/work/ostro-os-xt2
export all_proxy="socks://proxy-shz.intel.com:1080"
export no_proxy="intel.com,.intel.com,localhost,127.0.0.1"
export GIT_PROXY_COMMAND="oe-git-proxy"

if [ ! -d $WORKSPACE ]; then
    mkdir -pv $WORKSPACE
    cd $WORKSPACE
    git clone --recursive https://github.com/ostroproject/ostro-os-xt .
else
    cd $WORKSPACE
    git pull
    git submodule update
fi

if [ ! -d $WORKSPACE/meta-crosswalk ]; then
    cd $WORKSPACE
    git clone https://github.com/crosswalk-project/meta-crosswalk.git
else
    cd $WORKSPACE/meta-crosswalk
    git pull
fi

cd $WORKSPACE/meta-crosswalk
META_XWALK_PATH=$(pwd)

cd $WORKSPACE
rm -fr build
source ostro-init-build-env

echo "OSTRO_XT_LAYERS += \"$META_XWALK_PATH\"" >> $WORKSPACE/build/conf/bblayers.conf
sed -i "s|#require conf/distro/include/ostro-os-development.inc|require conf/distro/include/ostro-os-development.inc|" $WORKSPACE/build/conf/local.conf
echo "require $META_XWALK_PATH/include/ostro-xt-security-flags.inc" >> $WORKSPACE/build/conf/local.conf
echo "SUPPORTED_RECIPES_append = \"$META_XWALK_PATH/include/ostro-xt-supported-recipes.txt\"" >> $WORKSPACE/build/conf/local.conf
echo "OSTRO_XT_IMAGE_EXTRA_INSTALL_append = \" crosswalk\"" >> $WORKSPACE/build/conf/local.conf

bitbake ostro-xt-image-noswupd