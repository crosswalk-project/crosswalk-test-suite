#!/bin/sh

#
# Modified by: Qiu Zhong <zhongx.qiu@intel.com>
# 2015-07-16: Add a commit id option to make it more fexible to call this script.
# 2015-07-17: Move the error message of nofound test suite list to /tmp directory.
#
usage="Usage: ./pack_wts.sh [-a <commit id>]
-a <commit id> The 40-bit SHA-1 commit ID in git when commit
               It's optional, if this option is null, use the default Release_ID of latest commit id.
"

home=$PWD

# We'll put the script to crosswalk-test-suite/tools/build/
# So here work variable will be modified: 
# before
# work=$home/crosswalk-test-suite/webapi/
# after
crosswalk_test_suite_dir=$home/../..
work=${crosswalk_test_suite_dir}/webapi
usecase_dir=$crosswalk_test_suite_dir/usecase
demoex_dir=$crosswalk_test_suite_dir/../release/demo-express

# default release ID
release_ID=`git log --pretty=oneline -1|awk '{print $1}'`

while getopts a:h opt
do
    case "$opt" in
    a) release_ID=$OPTARG;;
    *) echo "$usage"
    	exit 1;;
    esac    
done

cd $demoex_dir;git reset --hard HEAD;git checkout master;git pull
cd $work/../;git reset --hard HEAD;git clean -dfx;git checkout master;git fetch upstream;git rebase upstream/master;git reset --hard $release_ID

cp -dpRv $demoex_dir/samples/* $usecase_dir/usecase-webapi-xwalk-tests/samples/
cp -dpRv $demoex_dir/res/* $usecase_dir/usecase-webapi-xwalk-tests/res/
#cp -dpRv $demoex_dir/samples-wrt/* $usecase_dir/usecase-wrt-android-tests/samples/
rm -rf *zip /tmp/tests
mkdir -p /tmp/tests/common
mkdir -p /tmp/tests/resources
python $work/../tools/build/copy.py

#Add version.json file
export LANG="en_US"
echo "{\"tests_version\": \"`date +%c`\"}" >/tmp/tests/version.json

#move spec file
cd $work
cat $home/released_suites/WTS | while read suite
do
    ls $suite &>/dev/null
    if [ $? -ne 0 ];then
        echo "$suite not found" >> /tmp/nofound.txt
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
        if [ $suite = "webapi-webgl-khronos-tests" ];then
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

mkdir /tmp/tests/usecase
#mkdir /tmp/tests/usecase-wrt

cp -dpRv $usecase_dir/usecase-webapi-xwalk-tests/icon.png /tmp/tests/usecase/
cp -dpRv $usecase_dir/usecase-webapi-xwalk-tests/res /tmp/tests/usecase/
cp -dpRv $usecase_dir/usecase-webapi-xwalk-tests/steps /tmp/tests/usecase/
cp -dpRv $usecase_dir/usecase-webapi-xwalk-tests/samples /tmp/tests/usecase/
cp -dpRv $usecase_dir/usecase-webapi-xwalk-tests/manifest.json /tmp/tests/usecase/
cp -dpRv $usecase_dir/usecase-webapi-xwalk-tests/tests.android.xml /tmp/tests/usecase/tests.xml
cp -dpRv $work/../tools/bootstrap-fw/* /tmp/tests/usecase/

#cp -dpRv $usecase_dir/usecase-wrt-android-tests/tests.android.xml /tmp/tests/usecase-wrt/tests.xml
#cp -dpRv $usecase_dir/usecase-wrt-android-tests/steps /tmp/tests/usecase-wrt/
#cp -dpRv $work/../tools/bootstrap-fw/* /tmp/tests/usecase-wrt



#rm Makefile
find /tmp/tests -name "Makefile*" |xargs -I% rm -rf %

#zip file
cd /tmp/tests/
rm -fr ./typedarrays/tools
## TODO: this will remove after the redirect.py has been fixed
#grep redirect.py -rl *|xargs -I% rm %
#find . -name "redirect.py" -delete
## end

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

cd $work/../
git reset --hard HEAD
git clean -dfx
