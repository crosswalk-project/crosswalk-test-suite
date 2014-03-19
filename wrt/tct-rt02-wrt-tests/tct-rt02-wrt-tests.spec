name=$(basename $(pwd))
main_version="2.2.1"
release="1"
version="$main_version-$release"
appname=$(echo $name|sed 's/-/_/g')
