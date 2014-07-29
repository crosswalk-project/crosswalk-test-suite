name=$(basename $(pwd))
version="6.35.1.2"
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
mediasrc"
