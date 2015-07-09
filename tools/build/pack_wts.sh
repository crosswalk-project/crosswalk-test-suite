#!/bin/sh

home=$PWD

# We'll put the script to crosswalk-test-suite/tools/build/
# So here work variable will be modified: 
# before
# work=$home/crosswalk-test-suite/webapi/
# after
crosswalk_test_suite_dir=$home/../..
work=${crosswalk_test_suite_dir}/webapi

rm -rf *zip /tmp/tests
mkdir -p /tmp/tests/common
mkdir -p /tmp/tests/resources

#Add version.json file
export LANG="en_US"
echo "{\"tests_version\": \"`date +%c`\"}" >/tmp/tests/version.json

#move spec file
cd $work
cat $home/test_suites.list | while read suite
do
    ls $suite &>/dev/null
    if [ $? -ne 0 ];then
        echo "$suite not found"
        continue
    fi

    suiteFile=`echo $suite |awk -F "-" '{print $2}'`
    ls $suite/$suiteFile
    if [ $? -ne 0 ];then
        mkdir -p /tmp/tests/$suiteFile
        cp -rf $suite/spec.json /tmp/tests/$suiteFile
        ls -l $suite/ |grep '^d' |grep  -v 'webrunner' |awk  '{print $NF}' | xargs -I% cp -rf $work/$suite/% /tmp/tests/$suiteFile
    else
        suiteFilePy=${suiteFile}-py
        if [ $suite = "tct-webgl-nonw3c-tests" ];then
            mkdir -p /tmp/tests/$suiteFile
            cp -rf $PWD/$suite/$suiteFile/* /tmp/tests/$suiteFile
            cp -rf $PWD/$suite/$suiteFilePy/* /tmp/tests/$suiteFile
        else
            if [ -d $PWD/$suite/$suiteFilePy ];then
                cp -rf $PWD/$suite/$suiteFilePy /tmp/tests/$suiteFile
            else
                cp -rf $PWD/$suite/$suiteFile /tmp/tests/
            fi 
        fi
    fi
    test -d $suite/common && cp -rf $suite/common/* /tmp/tests/common
    test -d $suite/resources && cp -rf $suite/resources/* /tmp/tests/resources
done

#zip file
cd /tmp/tests/
rm -fr ./typedarrays/tools

## TODO: move qunit to manual

## Currently, SIMD qunit framework is supported to auto execution, so need to remove the special handling in 
## "-manual" option in WTS build script.
#mv simd/float32x4.html simd/float32x4-manual.html
#mv simd/float64x2.html simd/float64x2-manual.html
#mv simd/int32x4.html simd/int32x4-manual.html

##end

# Get version from crosswalk-test-suite/VERSION dynamically.

version=$(grep main-version ${crosswalk_test_suite_dir}/VERSION | awk -F \" '{print $4}')
zip -Drq tests-${version}.wts.zip ./*
mv tests-${version}.wts.zip $home

#clean environment
rm -rf /tmp/tests
