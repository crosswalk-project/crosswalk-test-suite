#!/bin/bash

USAGE="Usage: ./pack.sh"
NAME="XwalkDriverTest"
SRC_ROOT=$PWD
BUILD_ROOT=/tmp/webdriver_pack
BUILD_DEST=/tmp/webdriver

# Check params
if [[ $1 == "-h" || $1 == "--help" ]]; then
  echo "$USAGE"
  exit 1
fi

# Check precondition
function check_precondition() {
  which "$1" > /dev/null 2>&1
  if [ "$?" -ne 0 ]; then
    echo "Please install $1 first."
    exit 1
  fi
}

check_precondition autoreconf
check_precondition gcc
check_precondition make

# Clean workspace
function clean_workspace() {
  echo "Cleaning workspace ..."
  rm -rf $BUILD_ROOT $BUILD_DEST
}

clean_workspace
mkdir -p $BUILD_ROOT $BUILD_DEST

# Copy source code
rm -f ./*.apk ./*.tar.bz2 ./*.tar.gz ./*.zip
cp -arf ${SRC_ROOT}/* ${BUILD_ROOT}/
if [ "$?" -ne 0 ]; then
  echo "Unable to copy ${SRC_ROOT}/* to ${BUILD_ROOT}/"
  exit 1
fi

# Create APK package
function create_apk() {
  echo "Creating ${NAME}.apk ..."
  cd "$BUILD_ROOT"

  # Copy .html to APK subdirectory
  find -name "*.html" | grep -v support | xargs -I% cp --parents % "${BUILD_ROOT}/support/${NAME}"

  cp -ar ${SRC_ROOT}/../../tools/crosswalk ${BUILD_ROOT}/crosswalk
  if [ "$?" -ne 0 ]; then
    echo "Please get proper version of crosswalk package first."
    clean_workspace
    exit 1
  fi

  # Enable remote debugging
  temp="${BUILD_ROOT}/crosswalk/app_src/src/org/xwalk/app/template/AppTemplateActivity.java"
  line=$(sed -n '/super.onCreate/=' "$temp" | tail -n1)
  sed -i "${line}s/.*/setRemoteDebugging(true);\n&/" "$temp"

  cd "${BUILD_ROOT}/crosswalk"
  python make_apk.py --manifest="${BUILD_ROOT}/support/${NAME}/manifest.json"
  if [ "$?" -ne 0 ]; then
    echo "Failed to create ${NAME}.apk!"
    clean_workspace
    exit 1
  fi
}

create_apk
echo "Getting ${NAME}.apk package from workspace ..."
mv ${BUILD_ROOT}/crosswalk/*.apk $SRC_ROOT/

clean_workspace

# Validate the package generated
echo "Checking result ..."
cd "$SRC_ROOT"
APK=$(find -name "*.apk" | sort 2>/dev/null)
if [ -z "$APK" ]; then
  echo "FAILED to build ${NAME}.apk package!"
  exit 1
else
  echo "Done the ${NAME}.apk package build! Results:"
  echo "$APK"
  exit 0
fi

