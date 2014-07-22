name="wrt-integration"
main_version="2.2.1"
release="1"
version="$main_version-$release"
appname=$(echo $name|sed 's/-/_/g')

# set value "1" if this suite need to sign,otherwise set "0" #
sign="1"

# set value "1" if this suite need to keep src_file,otherwise set "0" #
src_file="1"

# specified files to be kept in whitelist #
whitelist="
inst.sh
tests.xml
LICENSE.Apache-2.0
LICENSE.BSD-3
LICENSE.CC-BY-3.0
mediasrc"
