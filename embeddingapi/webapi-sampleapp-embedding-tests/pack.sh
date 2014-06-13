#!/bin/bash
source $(dirname $0)/webapi-sampleapp-embedding-tests.spec

#parse params
usage="Usage: ./pack.sh"

if [[ $1 == "-h" || $1 == "--help" ]]; then
    echo "$usage"
    exit 1
fi

type="apk"

SRC_ROOT=$PWD

# clean
function clean_workspace(){
    echo "cleaning workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    rm -rf bin/ gen/ libs/
    rm local.properties build.xml project.properties
    rm -rf opt/
}

## function for create apk ##

function create_apk(){
    targetID=$(android list |grep "API level" |awk -F ":" '{print $NF}' |sed 's/^[ \t]*//g')
    mkdir EmbeddedAPI
    cd EmbeddedAPI
    android create project --name EmbeddedAPI --target android-$targetID --path . --package com.embeddedapi --activity MainActivity

    scp build.xml local.properties project.properties ../
    cd ..
    rm -rf EmbeddedAPI

    echo "android.library.reference.1=../xwalk_core_library" >> project.properties
    scp local.properties ../xwalk_core_library
    rm -rf ../xwalk_core_library/bin/res/crunch
    ant debug
    if [ $? -ne 0 ];then
        echo "Create $name.apk fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
        clean_workspace
        exit 1
    fi
}
## zip function ##

function zip_for_apk(){
    mkdir opt
    cd opt
    mkdir $name
    cd ..
    cp -af $SRC_ROOT/inst.sh.apk opt/$name/inst.sh
    cp -af $SRC_ROOT/bin/EmbeddedAPI-debug.apk opt/$name/

    if [ $src_file -eq 0 ];then
        for file in $(ls opt/$name |grep -v apk);do
            if [[ "${whitelist[@]}" =~ $file ]];then
                echo "$file in whitelist,keep it..."
            else
                echo "Remove unnessary file:$file..."
                rm -rf opt/$name/$file
            fi
        done
    fi
    zip -Drq $SRC_ROOT/$name-$version.$type.zip opt/
    if [ $? -ne 0 ];then
        echo "Create zip package fail... >>>>>>>>>>>>>>>>>>>>>>>>>"
        clean_workspace
        exit 1
    fi
}

## create apk package ##
case $type in
    apk) create_apk
         zip_for_apk;;
esac

# clean workspace
clean_workspace

# validate
echo "checking result... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
if [ -z "`ls $SRC_ROOT | grep "\.zip"`" ];then
    echo "------------------------------ FAILED to build $name packages --------------------------"
    exit 1
fi

echo "------------------------------ Done to build $name packages --------------------------"
cd $SRC_ROOT
ls *.zip 2>/dev/null
