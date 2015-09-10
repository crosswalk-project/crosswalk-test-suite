#!/bin/bash
source $(dirname $0)/webapi-noneservice-tests.spec

usage="Usage: ./pack.sh [-t <package type: apk | cordova>] [-a <apk runtime arch: x86 | arm>] [-m <package mode: embedded | shared>] [-v <sub version: 3.6 | 4.x>] [-p <local | npm>]
[-t apk] option was set as default.
[-a x86] option was set as default.
[-m embedded] option was set as default.
[-v 3.6] option was set as default.
[-p local] option was set as default.
"

SRC_ROOT=$(cd $(dirname $0);pwd)
BUILD_ROOT=/tmp/${name}-${path_flag}_pack
BUILD_DEST=/tmp/${name}-${path_flag}

dest_dir=$SRC_ROOT
pack_type="apk"
arch="x86"
pack_mode="embedded"
sub_version="3.6"
crosswalk_version=""
crosswalk_branch=""
plugin_location="local"
while getopts a:t:m:d:v:p: o
do
    case "$o" in
    a) arch=$OPTARG;;
    t) pack_type=$OPTARG;;
    m) pack_mode=$OPTARG;;
    d) dest_dir=$OPTARG;;
    v) sub_version=$OPTARG;;
    p) plugin_location=$OPTARG;;
    *) echo "$usage"
       exit 1;;
    esac
done

main_version=$(cat ../../VERSION | awk 'NR==2')
for((i=1;i<=4;i++)) 
do
    crosswalk_version=$(echo $main_version|cut -d "\"" -f$i)
done

crosswalk_branch_tmp=$(cat ../../VERSION | awk 'NR==3')
for((i=1;i<=4;i++)) 
do
    crosswalk_branch=$(echo $crosswalk_branch_tmp|cut -d "\"" -f$i)
done

# clean
function clean_workspace(){
    echo "cleaning workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
    rm -rf $BUILD_ROOT $BUILD_DEST
}

clean_workspace
mkdir -p $BUILD_ROOT $BUILD_DEST

# copy source code
rm -rf $dest_dir/$name-$version-$sub_version.$pack_type.zip
rm -rf $SRC_ROOT/*.zip
cp -arf $SRC_ROOT/* $BUILD_ROOT/

for list in $LIST;do
    cp -ar $list $BUILD_ROOT/
done

## creat testlist.json ##
echo "[
    {\"category\": \"W3C\", \"tests\":
        [" > $BUILD_DEST/testlist.json
for suite in $LIST;do
    echo "\"`basename $suite`\"",
done | sort | sed '$s/,//' >>$BUILD_DEST/testlist.json
echo "        ]
    }
]" >>$BUILD_DEST/testlist.json


if [ $pack_type == "cordova" ]; then
    for suite in $LIST;do
        suitename=`basename $suite`
        if [ $sub_version == "4.x" ]; then
            python $SRC_ROOT/../../tools/build/pack.py -t ${pack_type}-aio -m $pack_mode -a $arch -d $BUILD_DEST --sub-version $sub_version --pack-type $plugin_location -s $SRC_ROOT/../../webapi/$suitename
        elif [ $sub_version == "3.6" ]; then
            python $SRC_ROOT/../../tools/build/pack.py -t ${pack_type}-aio -m $pack_mode -d $BUILD_DEST --sub-version $sub_version -s $SRC_ROOT/../../webapi/$suitename
        else
            echo "package sub version can only be 3.6 or 4.x, now exit.... >>>>>>>>>>>>>>>>>>>>>>>>>"
            clean_workspace
            exit 1
        fi
        if [ -d $BUILD_DEST/opt/$suitename/HOST_RESOURCES ];then
            mkdir -p $BUILD_ROOT/host_resources/opt/$suitename
            mv $BUILD_DEST/opt/$suitename/HOST_RESOURCES/* $BUILD_ROOT/host_resources/opt/$suitename
        fi
    done
else
    for suite in $LIST;do
        suitename=`basename $suite`
        python $SRC_ROOT/../../tools/build/pack.py -t ${pack_type}-aio -m $pack_mode -a $arch -d $BUILD_DEST -s $SRC_ROOT/../../webapi/$suitename
        if [ -d $BUILD_DEST/opt/$suitename/HOST_RESOURCES ];then
            mkdir -p $BUILD_ROOT/host_resources/opt/$suitename
            mv $BUILD_DEST/opt/$suitename/HOST_RESOURCES/* $BUILD_ROOT/host_resources/opt/$suitename
        fi
    done
fi


mkdir $BUILD_ROOT/apps
mv `find $BUILD_DEST -name '*apk'` $BUILD_ROOT/apps

cd $BUILD_DEST
cat > index_tmp.html << EOF
<!doctype html>
<head>
    <meta http-equiv="Refresh" content="1; url=index_real.html?testprefix=./">
</head>
EOF
cp -a $BUILD_ROOT/icon.png     $BUILD_DEST/
mkdir -p $BUILD_DEST/opt/$name

if [ $pack_type == "apk" ]; then
    find $BUILD_DEST -name '*apk' -exec cp {} $BUILD_ROOT/apps \;
    find $BUILD_DEST -name '*apk' -exec rm {} \;
    #mv `find /tmp/webapi-noneservice-tests/ -name '*apk'` $BUILD_ROOT/apps
    cp -a $BUILD_ROOT/webrunner/*     $BUILD_DEST/
    mv $BUILD_DEST/index.html $BUILD_DEST/index_real.html
    mv $BUILD_DEST/index_tmp.html $BUILD_DEST/index.html
    ## creat apk ##
    cp -ar $SRC_ROOT/../../tools/crosswalk $BUILD_ROOT/crosswalk
    cd $BUILD_ROOT/crosswalk
    python make_apk.py --package=org.xwalk.$appname --name=$appname --app-root=$BUILD_DEST --app-local-path=index.html --icon=$BUILD_DEST/icon.png --mode=$pack_mode --arch=$arch --enable-remote-debugging
    if [ $? -ne 0 ];then
        echo "Create $name.apk fail.... >>>>>>>>>>>>>>>>>>>>>>>>>"
        clean_workspace
        exit 1
    fi
    
    ## creat zip package ##
    mv $BUILD_ROOT/crosswalk/*.apk $BUILD_DEST/opt/$name/
    if [ -f $BUILD_DEST/opt/$name/WebapiNoneserviceTests_$arch.apk ] || [ -f $BUILD_DEST/opt/$name/WebapiNoneserviceTests.apk ];then
        mv $BUILD_DEST/opt/$name/WebapiNoneserviceTests*.apk $BUILD_DEST/opt/$name/$appname.apk
    fi
elif [ $pack_type == "cordova" ]; then
    if [ $sub_version == "4.x" ]; then
        cp -ar $SRC_ROOT/../../tools/cordova_plugins $BUILD_ROOT/cordova_plugins
        cd $BUILD_ROOT
        cordova create $appname org.xwalk.$appname $appname
        sed -i "s/<widget/<widget android-activityName=\"$appname\"/g" $BUILD_ROOT/$appname/config.xml
        sed -i "s/<\/widget>/    <allow-navigation href=\"*\" \/>\\n<\/widget>/g" $BUILD_ROOT/$appname/config.xml

        cp -a $BUILD_ROOT/webrunner/*  $BUILD_ROOT/$appname/www
        mv $BUILD_ROOT/$appname/www/index.html $BUILD_ROOT/$appname/www/index_real.html
        cp -a $BUILD_DEST/opt $BUILD_ROOT/$appname/www
        mv $BUILD_DEST/testlist.json $BUILD_ROOT/$appname/www
        mv $BUILD_DEST/index_tmp.html $BUILD_ROOT/$appname/www/index.html
        mv $BUILD_DEST/icon.png $BUILD_ROOT/$appname/www

        cd $BUILD_ROOT/$appname
        cordova platform add android

        for plugin in `ls $BUILD_ROOT/cordova_plugins`
        do
            if [ $plugin == "cordova-plugin-crosswalk-webview" ]; then
                version_cmd=""
                plugin_crosswalk_source=$BUILD_ROOT/cordova_plugins/$plugin
                if [ $crosswalk_branch == "beta" ]; then
                    if [ $pack_mode == "shared" ]; then
                        version_cmd="--variable XWALK_VERSION="org.xwalk:xwalk_shared_library_beta:$crosswalk_version""
                    else
                        version_cmd="--variable XWALK_VERSION="org.xwalk:xwalk_core_library_beta:$crosswalk_version""
                    fi
                else
                    version_cmd="--variable XWALK_VERSION="$crosswalk_version""
                fi
                if [ $plugin_location == 'npm' ]; then
                   plugin_crosswalk_source="cordova-plugin-crosswalk-webview"
                fi
                echo $version_cmd
                echo $plugin_crosswalk_source
                cordova plugin add $plugin_crosswalk_source $version_cmd --variable XWALK_MODE="$pack_mode" 
            else
                cordova plugin add $BUILD_ROOT/cordova_plugins/$plugin
            fi
        done
        cordova build android
        if [ $arch == 'x86' ]; then
            if [ -f $BUILD_ROOT/$appname/platforms/android/build/outputs/apk/$appname-x86-debug.apk ];then
                mv $BUILD_ROOT/$appname/platforms/android/build/outputs/apk/$appname-x86-debug.apk $BUILD_DEST/opt/$name/$appname.apk
            elif [ -f $BUILD_ROOT/$appname/platforms/android/build/outputs/apk/android-x86-debug.apk ];then
                mv $BUILD_ROOT/$appname/platforms/android/build/outputs/apk/android-x86-debug.apk $BUILD_DEST/opt/$name/$appname.apk
            else
                echo "Copy apk failed, " + $BUILD_ROOT + "/" + $appname + "/platforms/android/build/outputs/apk/android-x86-debug.apk does not exist"
                clean_workspace
                exit 1
            fi
        else
            if [ $arch != 'arm' ]; then
                echo "apk runtime arch can only be x86 or arm, now take arm as default.... >>>>>>>>>>>>>>>>>>>>>>>>>"
            fi
            if [ -f $BUILD_ROOT/$appname/platforms/android/build/outputs/apk/$appname-armv7-debug.apk ];then
                mv $BUILD_ROOT/$appname/platforms/android/build/outputs/apk/$appname-armv7-debug.apk $BUILD_DEST/opt/$name/$appname.apk
            elif [ -f $BUILD_ROOT/$appname/platforms/android/build/outputs/apk/android-armv7-debug.apk ];then
                mv $BUILD_ROOT/$appname/platforms/android/build/outputs/apk/android-armv7-debug.apk $BUILD_DEST/opt/$name/$appname.apk
            else
                echo "Copy apk failed, " + $BUILD_ROOT + "/" + $appname + "/platforms/android/build/outputs/apk/android-armv7-debug.apk does not exist"
                clean_workspace
                exit 1
            fi
        fi
    elif [ $sub_version == "3.6" ]; then
        cp -ar $SRC_ROOT/../../tools/cordova $BUILD_ROOT/cordova
        cp -ar $SRC_ROOT/../../tools/cordova_plugins $BUILD_ROOT/cordova_plugins

        cd $BUILD_ROOT/cordova

        if [ $pack_mode == "shared" ]; then
            bin/create $appname org.xwalk.$appname $appname --xwalk-shared-library
        else
            if [ $pack_mode != "embedded" ]; then
                echo "package mode can only be embedded or shared, now take embedded as default.... >>>>>>>>>>>>>>>>>>>>>>>>>"
            fi
            bin/create $appname org.xwalk.$appname $appname
        fi

        cd $BUILD_ROOT/cordova/$appname

        for plugin in `ls $BUILD_ROOT/cordova_plugins`
        do
            plugman install --platform android --project ./ --plugin $BUILD_ROOT/cordova_plugins/$plugin
        done

        cp -a $BUILD_ROOT/webrunner/*  $BUILD_ROOT/cordova/$appname/assets/www
        mv $BUILD_ROOT/cordova/$appname/assets/www/index.html $BUILD_ROOT/cordova/$appname/assets/www/index_real.html
        cp -a $BUILD_DEST/opt $BUILD_ROOT/cordova/$appname/assets/www
        mv $BUILD_DEST/testlist.json $BUILD_ROOT/cordova/$appname/assets/www
        mv $BUILD_DEST/index_tmp.html $BUILD_ROOT/cordova/$appname/assets/www/index.html
        mv $BUILD_DEST/icon.png $BUILD_ROOT/cordova/$appname/assets/www

        ./cordova/build
        ##pack sub packages

        if [ -f $BUILD_ROOT/cordova/$appname/bin/$appname-debug.apk ];then
            mv $BUILD_ROOT/cordova/$appname/bin/$appname-debug.apk $BUILD_DEST/opt/$name/$appname.apk
        fi
    else
        echo "package sub version can only be 3.6 or 4.x, now exit.... >>>>>>>>>>>>>>>>>>>>>>>>>"
        clean_workspace
        exit 1
    fi
fi

## cp tests.xml and inst.sh ##
cp $BUILD_ROOT/inst.py $BUILD_DEST/opt/$name/inst.py
cp -a $BUILD_ROOT/apps $BUILD_DEST/opt/$name
if [ -d $BUILD_ROOT/host_resources/opt ];then
    cp -r $BUILD_ROOT/host_resources/opt $BUILD_DEST/opt/$name
fi
cp -a $SRC_ROOT/../../tools/resources/bdd/bddrunner $BUILD_DEST/opt/$name
cp -a $SRC_ROOT/../../tools/resources/bdd/data.conf $BUILD_DEST/opt/$name
cp -a $SRC_ROOT/../../tools/resources/xsl/* $BUILD_DEST/opt/$name

for suite in `ls $BUILD_ROOT |grep "\-tests" |grep -v spec$`;do
    cp $BUILD_ROOT/$suite/tests.xml  $BUILD_DEST/opt/$name/$suite.tests.xml
    cp $BUILD_ROOT/$suite/tests.full.xml  $BUILD_DEST/opt/$name/$suite.tests.full.xml
    sed -i "s/<suite/<suite widget=\"$name\"/g" $BUILD_DEST/opt/$name/$suite.tests.xml
    sed -i "s/<suite/<suite widget=\"$name\"/g" $BUILD_DEST/opt/$name/$suite.tests.full.xml
    rm -rf $BUILD_DEST/opt/$suite
done

cd $BUILD_DEST

zip -Drq $BUILD_DEST/$name-$version-$sub_version.$pack_type.zip opt/
if [ $? -ne 0 ];then
    echo "Create zip package fail... >>>>>>>>>>>>>>>>>>>>>>>>>"
    clean_workspace
    exit 1
fi

# copy zip file
echo "copy package from workspace... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
cd $SRC_ROOT
mkdir -p $dest_dir
cp -f $BUILD_DEST/$name-$version-$sub_version.$pack_type.zip $dest_dir

# clean workspace
clean_workspace

# validate
echo "checking result... >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
if [ ! -f $dest_dir/$name-$version-$sub_version.$pack_type.zip ];then
    echo "------------------------------ FAILED to build $name packages --------------------------"
    exit 1
fi

echo "------------------------------ Done to build $name packages --------------------------"
cd $dest_dir
ls *.zip 2>/dev/null
