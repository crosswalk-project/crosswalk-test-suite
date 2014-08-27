#!/bin/bash
source $(dirname $0)/webapi-embeddingapi-xwalk-tests.spec

#parse params
usage="Usage: ./pack.sh"

if [[ $1 == "-h" || $1 == "--help" ]]; then
    echo "$usage"
    exit 1
fi

type="apk"

SRC_ROOT=$PWD

# init
function init_workspace(){
    echo "init workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    rm -rf opt/
    cp libs/chromium/*.jar libs/
    cp libs/testkit/*.jar libs/
}


# clean
function clean_workspace(){
    echo "cleaning workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    rm -rf bin/ gen/
    rm local.properties build.xml project.properties
    rm -rf opt/
    rm libs/*.jar
}

## function for create apk ##
function create_apk(){
    targetID=$(android list |grep "API level:" |awk -F ":" '{print $NF}' |sed 's/^[ \t]*//g')
    mkdir embeddingapi
    cd embeddingapi
    android create project --name embeddingapi --target android-$targetID --path . --package com.embeddingapi --activity MainActivity
    echo "targetID:" $targetID
    scp build.xml local.properties project.properties ../
    cd ..
    rm -rf embeddingapi

    echo "android.library.reference.1=../crosswalk-webview" >> project.properties
    scp local.properties ../crosswalk-webview
    rm -rf ../crosswalk-webview/bin/res/crunch
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
    cp -af $SRC_ROOT/tests.xml opt/$name/tests.xml
    cp -af $SRC_ROOT/bin/embeddingapi-debug.apk opt/$name/

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

## init workspace ##
init_workspace

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
