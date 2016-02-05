#!/bin/bash

# Authors: Li, Jiajia <jiajiax.li@intel.com>
# Modified by: Qiu, Zhong <zhongx.qiu@intel.com>              
#   2015-07-03: Add maven/gradle/ant build way for embeddingapi packages.
#   2015-07-08: tools/mobilespec directory tree changed: now tools/mobilespec contains the following subdirectories
#               tools/mobilespec/mobilespec_3.6
#               tools/mobilespec/mobilespec_4.0
#               Releated pull request: https://github.com/crosswalk-project/crosswalk-test-suites/pull/2453 
#   2015-07-09: Substitute the crosswalk version in pom.xml for every embeddingapi test suite.  
#   2015-07-29: Cordova-plugin-crosswalk-webview/platforms/android/xwalk.gradle doesn't config the crosswalk
#               version any more. And crosswalk version is specified in crosswalk-test-suite/VERSION


PATH=/usr/java/sdk/tools:/usr/java/sdk/platform-tools:/usr/java/jdk1.7.0_67/bin:/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/share/apache-maven/bin:/usr/java/gradle-2.4/bin

ROOT_DIR=$(dirname $(readlink -f $0))
SHARED_SPACE_DIR=/mnt/jiajiax_shared/release
CTS_DIR=$ROOT_DIR/../work_space/release/crosswalk-test-suite-x64
DEMOEX_DIR=$CTS_DIR/../demo-express
LOG_DIR=$ROOT_DIR/logs
RELEASE_COMMIT_FILE=$LOG_DIR/$(date +%Y-%m-%d-%T)_release
VERSION_FLAG=$ROOT_DIR/version_flag/Canary_New_Number
VERSION_NO=$(cat $VERSION_FLAG)
BUILD_LOG=$LOG_DIR/canary_error_${VERSION_NO}.log
PKG_TOOLS=$CTS_DIR/../pkg_tools_64/
SAMPLE_LIST=""
wweek=$(date +"%W" -d "+1 weeks")
WW_DIR=/data/TestSuites_Storage/live
. $SHARED_SPACE_DIR/list_suites/release_list
PACK_TYPES="maven
gradle
ant
"
PATCH_DIR="/home/orange/01_qiuzhong/04-work/patch/aio/64"
echo "Begin flag:" > $BUILD_LOG
echo "---------------- `date` ---------------" >> $BUILD_LOG 

CORDOVA3_SAMPLEAPP_LIST="mobilespec
helloworld
remotedebugging
spacedodge
statusbar
renamePkg
xwalkCommandLine
setBackgroundColor
privateNotes
loadExtension"

# Update to change config path[yunfei 2015.07.23] 
##### START #####
#CORDOVA4_CONFIG=$CTS_DIR/tools/cordova_plugins/cordova-plugin-crosswalk-webview/src/android/xwalk.gradle
CORDOVA4_CONFIG=$CTS_DIR/tools/cordova_plugins/cordova-plugin-crosswalk-webview/platforms/android/xwalk.gradle
##### END #####

CORDOVA_SAMPLEAPP_LIST=""


NEW_VERSION_FLAG=0
SUITE_DIR=""
declare -A tests_path_arr
declare -A cordova3_path_arr
declare -A cordova4_path_arr
EMBEDDED_TESTS_DIR=""
SHARED_TESTS_DIR=""
TIZEN_TESTS_DIR=""
ANDROID_IN_PROCESS_FLAG=""
ANDROID_IN_PROCESS_FLAG64=""
TIZEN_IN_PROCESS_FLAG=""
RELEASE_COMMIT_ID=""
CORDOVA3_EMBEDDED_DIR=""
CORDOVA3_SHARED_DIR=""
CORDOVA4_EMBEDDED_DIR=""
CORDOVA4_SHARED_DIR=""
BRANCH_TYPE="master"
BRANCH_NAME="master"

ARCH_BITS="64bit"

init_ww(){
    
    [ -d $1/android/$BRANCH_TYPE/${VERSION_NO}-${ARCH_BITS} ] && rm -rf $1/android/$BRANCH_TYPE/${VERSION_NO}-${ARCH_BITS}
    if [ $(date +%w) -eq 4 ];then
        mkdir -p $1/android/{$BRANCH_TYPE/${VERSION_NO}-${ARCH_BITS}/{testsuites-embedded/{x86_64,arm64},testsuites-shared/{x86_64,arm64},cordova4.x-embedded/{x86_64,arm64},cordova4.x-shared/{x86_64,arm64}},beta}
    else
        mkdir -p $1/android/{$BRANCH_TYPE/${VERSION_NO}-${ARCH_BITS}/{testsuites-embedded/{x86_64,arm64},testsuites-shared/{x86_64,arm64},cordova4.x-embedded/{x86_64,arm64},cordova4.x-shared/{x86_64,arm64}},beta}
    fi
    
    EMBEDDED_TESTS_DIR=$1/android/$BRANCH_TYPE/${VERSION_NO}-${ARCH_BITS}/testsuites-embedded/
    SHARED_TESTS_DIR=$1/android/$BRANCH_TYPE/${VERSION_NO}-${ARCH_BITS}/testsuites-shared/
    CORDOVA3_EMBEDDED_DIR=$1/android/$BRANCH_TYPE/${VERSION_NO}-${ARCH_BITS}/cordova3.6-embedded/
    CORDOVA3_SHARED_DIR=$1/android/$BRANCH_TYPE/${VERSION_NO}-${ARCH_BITS}/cordova3.6-shared/
    CORDOVA4_EMBEDDED_DIR=$1/android/$BRANCH_TYPE/${VERSION_NO}-${ARCH_BITS}/cordova4.x-embedded/
    CORDOVA4_SHARED_DIR=$1/android/$BRANCH_TYPE/${VERSION_NO}-${ARCH_BITS}/cordova4.x-shared/
    ANDROID_IN_PROCESS_FLAG=$1/android/$BRANCH_TYPE/${VERSION_NO}-${ARCH_BITS}/BUILD-INPROCESS

    [ ! -f $ANDROID_IN_PROCESS_FLAG ] && touch $ANDROID_IN_PROCESS_FLAG
    tests_path_arr=([embedded]=$EMBEDDED_TESTS_DIR [shared]=$SHARED_TESTS_DIR)
    cordova3_path_arr=([embedded]=$CORDOVA3_EMBEDDED_DIR [shared]=$CORDOVA3_SHARED_DIR)
    cordova4_path_arr=([embedded]=$CORDOVA4_EMBEDDED_DIR [shared]=$CORDOVA4_SHARED_DIR)

    # special 64-bit building flag for arm64 and x86_64
    ANDROID_IN_PROCESS_FLAG64=$1/android/$BRANCH_TYPE/${VERSION_NO}/BUILD-INPROCESS-64 
}


prepare_tools(){
    cd $CTS_DIR/tools
    # START ----Update to add XWalkCoreShell.apk in tools/ yunfei 2015.08.21
    if [ -f $PKG_TOOLS/crosswalk-test-apks-$VERSION_NO-$1/XWalkCoreShell.apk ];then
        rm -rf XWalkCoreShell.apk
        cp $PKG_TOOLS/crosswalk-test-apks-$VERSION_NO-$1/XWalkCoreShell.apk . 
    else
        echo "[tools] crosswalk-test-apks-$VERSION_NO-$1/XWalkCoreShell.apk not exist !!!" >> $BUILD_LOG
    fi
    # END ----Update to add XWalkCoreShell.apk in tools/ yunfei 2015.08.21
    # Update the number of arguments for prepare_tools as cordova supports 4.x supports shared mode now / Qiu Zhong 2015.9.2
    if [ $# -ge 2 ];then
        if [[ $2 == "apk" ]];then
            if [ -f $PKG_TOOLS/crosswalk-apks-$VERSION_NO-$1/XWalkRuntimeLib.apk ];then
                rm -rf XWalkRuntimeLib.apk
                cp $PKG_TOOLS/crosswalk-apks-$VERSION_NO-$1/XWalkRuntimeLib.apk . 
            else
                echo "[tools] crosswalk-apks-$VERSION_NO-$1/XWalkRuntimeLib.apk not exist !!!" >> $BUILD_LOG
                return 1
            fi

            if [ -d $PKG_TOOLS/crosswalk-${VERSION_NO}-${ARCH_BITS} ];then
                rm -rf crosswalk
                cp -a $PKG_TOOLS/crosswalk-${VERSION_NO}-${ARCH_BITS} crosswalk
            else
                echo "[tools] crosswalk-$VERSION_NO not exist !!!" >> $BUILD_LOG
                return 1

            fi
            # tempoary patch for aio
            cp -fv ${PATCH_DIR}/misc/webapi-service-tests/pack.sh ${CTS_DIR}/misc/webapi-service-tests/pack.sh
            cp -fv ${PATCH_DIR}/misc/webapi-noneservice-tests/pack.sh ${CTS_DIR}/misc/webapi-noneservice-tests/pack.sh            
        fi

        if [[ $2 == "cordova3.6" ]];then
            if [ -d $PKG_TOOLS/crosswalk-cordova-$VERSION_NO-$1 ];then
                rm -rf cordova
                rm -rf cordova_plugins
                cp -a $PKG_TOOLS/crosswalk-cordova-$VERSION_NO-$1 cordova
                cp -a $PKG_TOOLS/cordova_plugins_3.6 cordova_plugins
            else
                echo "[tools] crosswalk-cordova-$VERSION_NO-$1 not exist !!!" >> $BUILD_LOG
                return 1

            fi
        fi

        if [[ $2 == "cordova4.x" ]];then
                rm -rf cordova
                rm -rf cordova_plugins
                cp -a $PKG_TOOLS/cordova_plugins_4.0 cordova_plugins

                cd $CTS_DIR/tools/cordova_plugins/cordova-plugin-crosswalk-webview;git reset --hard HEAD;git checkout master;git pull
                begin_line=`sed -n '/  maven {/=' $CORDOVA4_CONFIG`
                end_line=$[$begin_line + 2]
                sed -i "${begin_line},${end_line}d" $CORDOVA4_CONFIG
                sed -i "${begin_line}i\  mavenLocal()" $CORDOVA4_CONFIG

                if [[ $3 == "shared" ]]; then
                    echo "Use 32bit crosswalk-shared-${VERSION_NO}.aar!"
                else
                    mvn install:install-file -DgroupId=org.xwalk -DartifactId=xwalk_core_library -Dversion=${VERSION_NO} -Dpackaging=aar  -Dfile=${PKG_TOOLS}/crosswalk-${VERSION_NO}-${ARCH_BITS}.aar -DgeneratePom=true -Dclassifier=64bit
                fi
        fi

        if [[ $2 == "embeddingapi" ]];then
            if [ -d $PKG_TOOLS/crosswalk-webview-$VERSION_NO-$1 ];then
                rm -rf crosswalk-webview
                cp -a $PKG_TOOLS/crosswalk-webview-$VERSION_NO-$1 crosswalk-webview
            else
                echo "[tools] $PKG_TOOLS/crosswalk-webview-$VERSION_NO-$1 not exist !!!" >> $BUILD_LOG
                return 1

            fi
        fi

    else
        echo "arguments error !!!"
    fi

}

update_usecase_cordova_extra_plugins() {
    cd $1
    git pull
    cd -
}

sync_Code(){
    # Get latest code from github
    cd $DEMOEX_DIR ; git reset --hard HEAD ;git checkout master ;git pull ;cd -
    #cd $CTS_DIR ; git reset --hard HEAD; git checkout master; cd -
    if [ $(date +%w) -eq 4 ];then
        cd $CTS_DIR
        git reset --hard HEAD
        git checkout $BRANCH_NAME
        git pull
        echo "---------- Release Commit -------">>$RELEASE_COMMIT_FILE
        git log -1 --name-status >>$RELEASE_COMMIT_FILE
        echo "---------------------------------">>$RELEASE_COMMIT_FILE
        RELEASE_COMMIT_ID=$(git log -1 --pretty=oneline | awk '{print $1}')
        echo $RELEASE_COMMIT_ID > $SHARED_SPACE_DIR/Release_ID
        cd -
        cat $RELEASE_COMMIT_FILE | mutt -s "$wweek Week Release Commit" yunfeix.hao@intel.com
    else
        RELEASE_COMMIT_ID=`cat $SHARED_SPACE_DIR/Release_ID`
        cd $CTS_DIR ; git reset --hard HEAD;git checkout $BRANCH_NAME;git pull ;git reset --hard $RELEASE_COMMIT_ID;cd -
    fi

    chmod u+x ${CTS_DIR}/tools/build/pack.py
    # Create the commit id file when the code is sync.
    touch $EMBEDDED_TESTS_DIR/../$RELEASE_COMMIT_ID 
    # End
    
    # Start update all the plugins in usecase/usecase-cordova-android-tests
    update_usecase_cordova_extra_plugins ${CTS_DIR}/usecase/usecase-cordova-android-tests/extra_plugins/cordova-admob-4.x
    update_usecase_cordova_extra_plugins ${CTS_DIR}/usecase/usecase-cordova-android-tests/extra_plugins/cordova-screenshot-4.x
    # End

}


updateVersionNum(){

    sed -i "s|\"main-version\": \"\([^\"]*\)\"|\"main-version\": \"$VERSION_NO\"|g" $CTS_DIR/VERSION
    # VERSION file contains branch information, so change it to canary. / Qiu Zhong 2015.9.2
    sed -i "s/beta/canary/" $CTS_DIR/VERSION
}



merge_Tests(){
    if [ $1 = "usecase-webapi-xwalk-tests" ];then

        echo "process usecase-webapi-xwalk-tests start..."
        cp -dpRv $DEMOEX_DIR/samples/* $2/samples/
        cp -dpRv $DEMOEX_DIR/res/* $2/res/

    elif [ $1 = "usecase-wrt-android-tests" ];then

        echo "process usecase-wrt-android-tests start..."
        cp -dpRv $DEMOEX_DIR/samples-wrt/* $2/samples/
    elif [ $1 = "usecase-cordova-android-tests" ];then
        echo "process usecase-cordova-android-tests..."
        cp -dpRv $DEMOEX_DIR/samples-cordova/* $2/samples/
    fi

}

recover_Tests(){

    if [ $1 = "usecase-webapi-xwalk-tests" ];then
        SAMPLE_LIST=`ls $DEMOEX_DIR/samples/`
        cd $2/samples/
        rm -rf $SAMPLE_LIST
        git checkout .
        cd -

        cd $2/res/
        git clean -dfx .
        git checkout .
        cd -
    elif [ $1 = "usecase-wrt-android-tests" ];then
        SAMPLE_LIST=`ls $DEMOEX_DIR/samples-wrt/`
        cd $2/samples/
        rm -rf $SAMPLE_LIST
        git checkout .
        cd -
    elif [ $1 = "usecase-cordova-android-tests" ];then
        SAMPLE_LIST=`ls $DEMOEX_DIR/samples-cordova/`
        cd $2/samples/
        rm -rf $SAMPLE_LIST
        git checkout .
        cd -
    fi
}

multi_thread_pack(){
    trap "exec 100>&-;exec 100<&-;exit 0" 2

    mkfifo $CTS_DIR/operator_tmp
    exec 100<>$CTS_DIR/operator_tmp
    
    for ((i=1;i<=$1;i++));do
        echo -ne "\n" 1>&100
    done

}

clean_operator(){

    
    rm -f $CTS_DIR/operator_tmp
    exec 100>$-
    exec 100<$-

}

pack_Wgt(){

    for wgt in $WGTLIST;do
        read -u 100
        {
            wgt_num=`find $CTS_DIR -name $wgt -type d | wc -l`
            if [ $wgt_num -eq 1 ];then
                wgt_dir=`find $CTS_DIR -name $wgt -type d`
                $CTS_DIR/tools/build/pack.py -t wgt -s $wgt_dir -d $TIZEN_TESTS_DIR --tools=$CTS_DIR/tools
                [ $? -ne 0 ] && echo "[wgt] <$wgt>" >> $BUILD_LOG
            elif [ $wgt_num -gt 1 ];then
                echo "$1 not unique !!!" >> $BUILD_LOG
            else
                echo "$1 not exists !!!" >> $BUILD_LOG
            fi
             echo -ne "\n" 1>&100
        }&
    done
    wait

}

pack_Xpk(){
    for xpk in $XPKLIST;do
        xpk_num=`find $CTS_DIR -name $xpk -type d | wc -l`
        if [ $xpk_num -eq 1 ];then
            xpk_dir=`find $CTS_DIR -name $xpk -type d`
            $CTS_DIR/tools/build/pack.py -t xpk -s $xpk_dir -d $TIZEN_TESTS_DIR --tools=$CTS_DIR/tools
            [ $? -ne 0 ] && echo "[xpk] <$xpk>" >> $BUILD_LOG
        elif [ $xpk_num -gt 1 ];then
            echo "$xpk not unique !!!" >> $BUILD_LOG
        else
            echo "$xpk not exists !!!" >> $BUILD_LOG
        fi
    done
}

pack_Apk(){

        for apk in $APKLIST;do
            read -u 100
            {
                apk_num=`find $CTS_DIR -name $apk -type d | wc -l`
                if [ $apk_num -eq 1 ];then
                    apk_dir=`find $CTS_DIR -name $apk -type d`
                    $CTS_DIR/tools/build/pack.py -t apk -m $2 -a $1 -s $apk_dir -d ${tests_path_arr[$2]}/$1 --tools=$CTS_DIR/tools
                    [ $? -ne 0 ] && echo "[apk] [$1] [$2] <$apk>" >> $BUILD_LOG
                elif [ $apk_num -gt 1 ];then
                    echo "$apk not unique !!!" >> $BUILD_LOG
                else
                    echo "$apk not exists !!!" >> $BUILD_LOG
                fi

                echo -ne "\n" 1>&100
            }&
        done

        wait
}


pack_Cordova(){

        for cordova in $CORDOVALIST;do
            read -u 100
            {
                cordova_num=`find $CTS_DIR -name $cordova -type d | wc -l`
                if [ $cordova_num -eq 1 ];then
                    cordova_dir=`find $CTS_DIR -name $cordova -type d`
                    if [ $3 = "3.6" ];then
                        $CTS_DIR/tools/build/pack.py -t cordova --sub-version $3 -m $2 -s $cordova_dir -d ${cordova3_path_arr[$2]}/$1 --tools=$CTS_DIR/tools
                    elif [ $3 = "4.x" ];then
                        $CTS_DIR/tools/build/pack.py -t cordova --sub-version $3 -a $1 -m $2 -s $cordova_dir -d ${cordova4_path_arr[$2]}/$1 --tools=$CTS_DIR/tools
                    fi
                    [ $? -ne 0 ] && echo "[cordova] [$1] [$2] [$3]<$cordova>" >> $BUILD_LOG
                elif [ $cordova_num -gt 1 ];then
                    echo "$cordova not unique !!!" >> $BUILD_LOG
                else
                    echo "$cordova not exists !!!" >> $BUILD_LOG
                fi
                echo -ne "\n" 1>&100
            }&
        done

        wait

}

pack_Cordova_SampleApp(){

        cd $CTS_DIR/tools/build
        rm -fv *.apk
        rm -fv cordova${3}_sampleapp_${1}.zip
        CORDOVA_SAMPLEAPP_LIST=$CORDOVA3_SAMPLEAPP_LIST
        for cordova_sampleapp in $CORDOVA_SAMPLEAPP_LIST;do
            read -u 100
            {
                if [ $3 = "3.6" ];then
                    sed -i "s|https://github.com/Telerik-Verified-Plugins/NativePageTransitions.git#r0.4.1|/home/orange/02_yunfei/NativePageTransitions|g" ./pack_cordova_sample.py 
                    sed -i "s|DEFAULT_CMD_TIMEOUT * 5|DEFAULT_CMD_TIMEOUT * 10|g" ../pack_cordova_sample.py 
                    ./pack_cordova_sample.py -n $cordova_sampleapp --cordova-version $3 -m $2 --tools=$CTS_DIR/tools
                elif [ $3 = "4.x" ];then
                    sed -i "s|https://github.com/Telerik-Verified-Plugins/NativePageTransitions.git#r0.4.1|/home/orange/02_yunfei/NativePageTransitions|g" ./pack_cordova_sample.py 
                    sed -i "s|DEFAULT_CMD_TIMEOUT * 5|DEFAULT_CMD_TIMEOUT * 10|g" ../pack_cordova_sample.py 
                    ./pack_cordova_sample.py -n $cordova_sampleapp --cordova-version $3 -a $1 -m $2 -p 000 --tools=$CTS_DIR/tools
                fi
                [ $? -ne 0 ] && echo "[cordova_sampleapp] [$1] [$2] [$3] $cordova_sampleapp" >> $BUILD_LOG
                echo -ne "\n" 1>&100
            }&
        done

        wait
        if [ $3 = "3.6" ];then
            zip cordova${3}_sampleapp_${1}.zip *.apk && cp cordova${3}_sampleapp_${1}.zip ${cordova3_path_arr[$2]}/$1
        elif [ $3 = "4.x" ];then
            zip cordova${3}_sampleapp_${1}.zip *.apk && cp cordova${3}_sampleapp_${1}.zip ${cordova4_path_arr[$2]}/$1
        fi

}

pack_Embeddingapi(){

        for emb_suite in $EMBEDDINGLIST;do
            for pack_type in ${PACK_TYPES};do
            read -u 100
            {
                emb_num=`find $CTS_DIR -name $emb_suite -type d | wc -l`
                if [ $emb_num -eq 1 ];then
                    emb_dir=`find $CTS_DIR -name $emb_suite -type d`
                    if [ $2 = "shared" ];then
                        find $CTS_DIR/tools/crosswalk-webview/ -name "libxwalkcore.so" -exec rm -f {} \;
                        find $CTS_DIR/tools/crosswalk-webview/ -name "xwalk_core_library_java_library_part.jar" -exec rm -f {} \;
                         #$CTS_DIR/tools/build/pack.py -t embeddingapi -s $emb_dir -d $SHARED_TESTS_DIR/$1 --tools=$CTS_DIR/tools           
                         $CTS_DIR/tools/build/pack.py -t embeddingapi --pack-type ${pack_type} -s $emb_dir -d $SHARED_TESTS_DIR/$1 --tools=$CTS_DIR/tools
                    elif [ $2 = "embedded" ];then
                        #$CTS_DIR/tools/build/pack.py -t embeddingapi -s $emb_dir -d $EMBEDDED_TESTS_DIR/$1 --tools=$CTS_DIR/tools
                        $CTS_DIR/tools/build/pack.py -t embeddingapi --pack-type ${pack_type} -s $emb_dir -d $EMBEDDED_TESTS_DIR/$1 --tools=$CTS_DIR/tools
                    fi
                    [ $? -ne 0 ] && echo "[embeddingapi] [$1] [$2] <$emb_suite>" >> $BUILD_LOG
                elif [ $emb_num -gt 1 ];then
                    echo "$emb_suite not unique !!!" >> $BUILD_LOG
                else
                    echo "$emb_suite not exists !!!" >> $BUILD_LOG
                fi
                echo -ne "\n" 1>&100
            }&
            done
        done
        
        wait

}

pack_Aio(){

        for aio in $AIOLIST;do
            read -u 100
            {
                aio_num=`find $CTS_DIR -name $aio -type d | wc -l`
                if [ $aio_num -eq 1 ];then
                    aio_dir=`find $CTS_DIR -name $aio -type d`
                    cd $aio_dir
                    ##### START add workaround for new webrunner [2015.08.14]###
                    mkdir -p webrunner
                    cp $CTS_DIR/tools/resources/webrunner/* webrunner -a
                    ##### END add workaround for new webrunner [2015.08.14]###
                    rm -f *.zip
                    if [ $1 = "apk" ];then
                        ./pack.sh -a $2 -m $3 -d ${tests_path_arr[$3]}/$2
                        [ $? -ne 0 ] && echo "[aio] [$1] [$2] [$3] <$aio>" >> $BUILD_LOG
                        #mv ${aio}-${VERSION_NO}-1.apk.zip ${tests_path_arr[$3]}/$2
                    elif [ $1 = "cordova3.6" ];then
                        ./pack.sh -t cordova -m $3 -d ${cordova3_path_arr[$3]}/$2
                        [ $? -ne 0 ] && echo "[aio] [$1] [$2] [$3] <$aio>" >> $BUILD_LOG
                        #mv ${aio}-${VERSION_NO}-1.cordova.zip $CORDOVA_TESTS_DIR/$2
                    elif [ $1 = "cordova4.x" ];then
                        ./pack.sh -t cordova -a $2 -v 4.x -d ${cordova4_path_arr[$3]}/$2
                        [ $? -ne 0 ] && echo "[aio] [$1] [$2] [$3] <$aio>" >> $BUILD_LOG
                    fi
                elif [ $aio_num -gt 1 ];then
                    echo "$aio not unique !!!" >> $BUILD_LOG
                else
                    echo "$aio not exists !!!" >> $BUILD_LOG
                fi
                echo -ne "\n" 1>&100
            }&
        done

        wait
}

copy_SDK(){

    SDK_dir=$ROOT_DIR/../images/linux-ftp.sh.intel.com/pub/mirrors/01org/crosswalk/releases/crosswalk/android/canary/$VERSION_NO
    WW_SDK_dir=$EMBEDDED_TESTS_DIR/../crosswalk-tools
    [ -d $SDK_dir ] && cp -a $SDK_dir $WW_SDK_dir
    touch $EMBEDDED_TESTS_DIR/../$RELEASE_COMMIT_ID 

}

save_Package(){
    wtoday=$[$(date +%w)]
    wdir="WW"$wweek

    mail_pkg_address=android/$BRANCH_TYPE/$VERSION_NO-${ARCH_BITS}
    python $ROOT_DIR/smail.py $VERSION_NO $mail_pkg_address $RELEASE_COMMIT_ID $BRANCH_NAME nightly
    mkdir -p /mnt/otcqa/$wdir/{$BRANCH_TYPE/"ww"$wweek"."$wtoday,stable,webtestingservice}
    if [ $wtoday -eq 5 ];then
        fulltest_dir=/mnt/otcqa/$wdir/$BRANCH_TYPE/"ww"$wweek"."$wtoday/FullTest
        mkdir -p $fulltest_dir
        cp -r $EMBEDDED_TESTS_DIR $fulltest_dir/
        cp -r $CORDOVA3_EMBEDDED_DIR/../cordova* $fulltest_dir/
        chmod -R 777 $fulltest_dir
        mail_pkg_address=$wdir/$BRANCH_TYPE/"ww"$wweek"."$wtoday/FullTest
        python $ROOT_DIR/smail.py $VERSION_NO $mail_pkg_address $RELEASE_COMMIT_ID $BRANCH_NAME DL
    fi    
    
}


# Move all the arm64 and x86_64 to $VERSION_NO and remove the while $VERSION_NO-64bit directory
mv_64() {
    MASTER_DIR=$(dirname $(dirname ${EMBEDDED_TESTS_DIR}))
    mv -fv ${EMBEDDED_TESTS_DIR}/arm64 ${MASTER_DIR}/${VERSION_NO}/testsuites-embedded/
    mv -fv {EMBEDDED_TESTS_DIR}/x86_64 ${MASTER_DIR}/${VERSION_NO}/testsuites-embedded/

    mv -fv ${SHARED_TESTS_DIR}/arm64 ${MASTER_DIR}/${VERSION_NO}/testsuites-shared
    mv -fv ${SHARED_TESTS_DIR}/x86_64 ${MASTER_DIR}/${VERSION_NO}/testsuites-shared

    rm -fr ${MASTER_DIR}/${VERSION_NO}-${ARCH_BITS}

    rm -fv ${ANDROID_IN_PROCESS_FLAG64}
}


init_ww $WW_DIR
sync_Code
updateVersionNum

recover_Tests usecase-webapi-xwalk-tests $CTS_DIR/usecase/usecase-webapi-xwalk-tests
recover_Tests usecase-wrt-android-tests $CTS_DIR/usecase/usecase-wrt-android-tests
recover_Tests usecase-cordova-android-tests $CTS_DIR/usecase/usecase-cordova-android-tests

merge_Tests usecase-webapi-xwalk-tests $CTS_DIR/usecase/usecase-webapi-xwalk-tests
merge_Tests usecase-wrt-android-tests $CTS_DIR/usecase/usecase-wrt-android-tests
merge_Tests usecase-cordova-android-tests $CTS_DIR/usecase/usecase-cordova-android-tests


clean_operator
multi_thread_pack 8


prepare_tools x86_64 embeddingapi
prepare_tools x86_64 apk

pack_Apk x86_64 embedded &
pack_Apk x86_64 shared &
pack_Aio apk x86_64 embedded &
pack_Aio apk x86_64 shared &
pack_Embeddingapi x86_64 embedded &
wait

pack_Embeddingapi x86_64 shared &
wait

prepare_tools arm64 embeddingapi
prepare_tools arm64 apk

pack_Apk arm64 embedded &
pack_Apk arm64 shared &
pack_Aio apk arm64 shared &
pack_Aio apk arm64 embedded &
pack_Embeddingapi arm64 embedded &
wait

pack_Embeddingapi arm64 shared &
wait

rm -f $ANDROID_IN_PROCESS_FLAG
mv_64
echo "Delete the file 'BUILD-INPROCESS':" >> $BUILD_LOG
echo " ---------------- `date`------------------" >> $BUILD_LOG

# prepare_tools x86_64 cordova3.6

# pack_Cordova x86_64 embedded 3.6 &
# pack_Cordova x86_64 shared 3.6 &
# pack_Cordova_SampleApp x86_64 embedded 3.6 &
# pack_Cordova_SampleApp x86_64 shared 3.6 &
# pack_Aio cordova3.6 x86_64 embedded &
# pack_Aio cordova3.6 x86_64 shared &
# wait


# prepare_tools arm64 cordova3.6

# pack_Cordova arm64 embedded 3.6 &
# pack_Cordova arm64 shared 3.6 &
# pack_Cordova_SampleApp arm64 embedded 3.6 &
# pack_Cordova_SampleApp arm64 shared 3.6 &
# pack_Aio cordova3.6 arm64 embedded &
# pack_Aio cordova3.6 arm64 shared &
# wait




prepare_tools x86_64 cordova4.x embedded

# pack_Cordova x86_64 embedded 4.x &
# pack_Cordova_SampleApp x86_64 embedded 4.x &
# pack_Aio cordova4.x x86_64 embedded &
# wait

pack_Cordova arm64 embedded 4.x &
pack_Cordova_SampleApp arm64 embedded 4.x &
pack_Aio cordova4.x arm64 embedded &
wait

# #START# add cordova4.x share mode [yunfei] 2015.08.26
# prepare_tools x86_64 cordova4.x shared

# pack_Cordova x86_64 shared 4.x &
# pack_Cordova_SampleApp x86_64 shared 4.x &
# pack_Aio cordova4.x x86_64 shared &
# wait

# pack_Cordova arm64 shared 4.x &
# pack_Cordova_SampleApp arm64 shared 4.x &
# pack_Aio cordova4.x arm64 shared &
# wait
#END# add cordova4.x share mode [yunfei] 2015.08.26

clean_operator

# copy_SDK
echo "End flag:" >> $BUILD_LOG
echo "---------------- `date`------------------" >> $BUILD_LOG

# save_Package
# Pack CIRC and Eh cordova sample app particularly
/home/orange/01_qiuzhong/04-work/scripts/circ_eh_master_x64.sh ${VERSION_NO}

recover_Tests usecase-webapi-xwalk-tests $CTS_DIR/usecase/usecase-webapi-xwalk-tests
recover_Tests usecase-wrt-android-tests $CTS_DIR/usecase/usecase-wrt-android-tests
recover_Tests usecase-cordova-android-tests $CTS_DIR/usecase/usecase-cordova-android-tests

echo "SampleApp code and source Start flag:" >> $BUILD_LOG
cd /home/orange/01_qiuzhong/git/03-lihao/crosswalk-test-suite/misc/sampleapp-android-tests
./sampleApp_pack_64bit.sh -v $VERSION_NO -r
cd -
echo "SampleApp code and source End flag:" >> $BUILD_LOG
echo "---------------- `date`------------------" >> $BUILD_LOG
