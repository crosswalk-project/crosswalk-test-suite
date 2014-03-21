#!/bin/bash
source $(dirname $0)/test_suites.list
version=0.0.1
current_dir=$PWD
test_suites_dir=$current_dir/../../webapi
utilities_dir=$current_dir/utilities
temp_dir=/tmp/wts/temp
dst_dir=/tmp/wts/suites

len=${#whitelist[@]}

if [ "$len" -eq 0 ]; then
  echo "Error: Fail to pack wts package for there being none test suite in whitelist of test_suites.list"
  exit 1
fi

rm -f $current_dir/wts-*.zip

if [ -d /tmp/wts ]; then
  rm -r /tmp/wts
fi

cp -r $current_dir /tmp/wts
mkdir $temp_dir $dst_dir

websocket_suite='tct-websocket-w3c-tests'

if [[ "${whitelist[@]}" =~ "$websocket_suite" ]]; then
  if [ -d $test_suites_dir/$websocket_suite ]; then
    rm -r $test_suites_dir/$websocket_suite/websocket
    unzip $current_dir/websocket.zip -d $test_suites_dir/$websocket_suite
  fi
fi

for test_suite in ${whitelist[@]}
do
  cd $test_suites_dir/$test_suite
  ./pack.sh -t wgt
  x=`find $test_suites_dir/$test_suite/ -name '*.zip' | wc -l`
  if [ $x -eq 0 ]; then
    echo "Warning:Faii to generate the zip package from $test_suite"
  else
    package_name=`find $test_suites_dir/$test_suite/ -name '*.zip'`
    unzip $package_name -d $temp_dir
    wgt_name=$temp_dir/opt/$test_suite/$test_suite.wgt

    if [ ! -f "$wgt_name" ]; then
      echo "Warning:Faii to generate the wgt package from $test_suite"
    else
      unzip $wgt_name -d $dst_dir

      for item in `ls $dst_dir | grep -v 'opt'`
      do
        rm -rf $dst_dir/$item
      done
    fi
  fi
done

for file in `grep -rn "127.0.0.1:8081" $dst_dir/opt/* | cut -d ':' -f1 | uniq`
do
  sed -i 's/127.0.0.1:8081/MACRO_IPADDR:80/g' $file
done

for item in `cat $current_dir/utilities/ipFile`
do
  sed -i 's/127.0.0.1/MACRO_IPADDR/g' $dst_dir/$item
done

csp_suite='tct-csp-w3c-tests'

if [[ "${whitelist[@]}" =~ "$csp_suite" ]]; then
  for file in `grep -rn "127.0.0.1" $dst_dir/opt/tct-csp-w3c-tests/csp/* | cut -d ':' -f1 | uniq`
  do
    sed -i 's/127.0.0.1/MACRO_IPADDR/g' $file
  done
fi

cp -r $dst_dir/opt/"${whitelist[0]}"/testkit $dst_dir/opt

cd /tmp/wts
mkdir suites/w3c

homepage_dir=$current_dir/../homepage
harness_dir=$current_dir/../harness
cp -r $homepage_dir $harness_dir /tmp/wts

#Generate config.json into /tmp/wts/harness
bash $utilities_dir/generate_config_json.sh

csswg_test_repo=$current_dir/../../csswg-test
platform_tests_repo=$current_dir/../../web-platform-tests
cp -r $csswg_test_repo $platform_tests_repo suites/w3c

#remove .git from above two repoes
for x in `find suites/w3c/csswg-test -name '.git'`
do
  rm -rf $x
done

for x in `find suites/w3c/web-platform-tests -name '.git'`
do
  rm -rf $x
done

#chmod cgi file
for cgi_file in `find suites/opt -name '*.cgi'`
do
    chmod +x $cgi_file
done

zip -r wts_tests.zip harness homepage suites
rm -rf websocket.zip harness homepage suites pack.sh utilities test_suites.list web-platform-tests.patch temp
cd /tmp
zip -r wts-$version.zip wts
rm -rf wts
mv /tmp/wts-$version.zip $current_dir
