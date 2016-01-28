name="webapi-noneservice-tests"
version=$(grep main-version $(dirname $0)/../../VERSION |awk -F \" '{print $4}')
sub_version=$(grep release-version $(dirname $0)/../../VERSION |awk -F \" '{print $4}')
appname=$(echo $name|sed 's/-/_/g')

source ../../tools/build/released_suites/Android-Platform
LIST=${AIONONSERVICELIST}

path_flag=`date +%s%N | md5sum | head -c 15`
