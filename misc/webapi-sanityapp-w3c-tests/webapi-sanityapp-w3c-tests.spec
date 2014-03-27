name="webapi-sanityapp-w3c-tests"
main_version="6.34.1.1"
release="1"
version="6.34.1.1"
appname=$(echo $name|sed 's/-/_/g')

# set value "1" if this suite need to sign,otherwise set "0" #
sign="1"

# set value "1" if this suite need to keep src_file,otherwise set "0" #
src_file="1"

# specified files to be kept in whitelist #
whitelist="
inst.sh
tests.xml
LICENSE.BSD-3
mediasrc"
