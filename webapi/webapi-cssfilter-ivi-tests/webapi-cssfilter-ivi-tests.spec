name=$(basename $(pwd))
main_version="6.34.1.3"
release="1"
version="6.34.1.3"
appname=$(echo $name|sed 's/-/_/g')

# set value "1" if this suite need to sign,otherwise set "0" #
sign="0"

# set value "1" if this suite need to keep src_file,otherwise set "0" #
src_file="0"

# specified files to be kept in whitelist #
whitelist="
inst.sh
tests.xml
tests.full.xml
COPYING
LICENSE.Apache-2.0
LICENSE.CC-BY-3.0
NOTICE
mediasrc"
