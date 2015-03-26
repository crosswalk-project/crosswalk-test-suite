#!/bin/bash
source $(dirname $0)/webapi-noneservice-tests.spec

usage="Usage: ./pack.sh [-t <package type: apk | cordova>] [-a <apk runtime arch: x86 | arm>] [-m <package mode: embedded | shared>]
[-t apk] option was set as default.
[-a x86] option was set as default.
[-m embedded] option was set as default.
"

SRC_ROOT=$(cd $(dirname $0);pwd)
BUILD_ROOT=/tmp/${name}-${path_flag}_pack
BUILD_DEST=/tmp/${name}-${path_flag}

dest_dir=$SRC_ROOT
pack_type="apk"
arch="x86"
pack_mode="embedded"
while getopts a:t:m:d: o
do
    case "$o" in
    a) arch=$OPTARG;;
    t) pack_type=$OPTARG;;
    m) pack_mode=$OPTARG;;
    d) dest_dir=$OPTARG;;
    *) echo "$usage"
       exit 1;;
    esac
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


for suite in $LIST;do
    python $SRC_ROOT/../../tools/build/pack.py -t ${pack_type}-aio -m $pack_mode -a $arch -d $BUILD_DEST -s $SRC_ROOT/../../webapi/`basename $suite`
done

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
    cp -ar $SRC_ROOT/../../tools/cordova $BUILD_ROOT/cordova
    cp -ar $SRC_ROOT/../../tools/cordova_plugins $BUILD_ROOT/cordova_plugins

    cd $BUILD_ROOT/cordova
    bin/create $appname org.xwalk.$appname $appname

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
fi

## cp tests.xml and inst.sh ##
cp $BUILD_ROOT/inst.py $BUILD_DEST/opt/$name/inst.py
cp -a $BUILD_ROOT/apps $BUILD_DEST/opt/$name

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
