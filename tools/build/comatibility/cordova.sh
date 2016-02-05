#!/bin/bash

#
#   This script aims to pack the test suites involved to the Cordova
#   for compatibility tests.
#   
#   Written by: Zhong Qiu(zhongx.qiu@intel.com)
#   Date:       2015-11-25
#

CWD=$(pwd)
source ${PWD}/config

update_code() {

    DIR_NAME=$1    
    if [[ ${DIR_NAME} == "NPLUS1" ]];then
        CTS_DIR=${WORKSPACE}/crosswalk-test-suite
    elif [[ ${DIR_NAME} == "N" ]]; then
        CTS_DIR=${WORKSPACE}/crosswalk-test-suite-${N}
    elif [[ ${DIR_NAME} == "N1" ]]; then
        CTS_DIR=${WORKSPACE}/crosswalk-test-suite-${N1}
    elif [[ ${DIR_NAME} == "N2" ]]; then
        CTS_DIR=${WORKSPACE}/crosswalk-test-suite-${N2}
    elif [[ ${DIR_NAME} == "N3" ]]; then
        CTS_DIR=${WORKSPACE}/crosswalk-test-suite-${N3}
    else
        echo "Params Error!"
        exit 1
    fi

    cd ${CTS_DIR}

    git reset --hard HEAD
    git pull
    
    cd -
}

update_version() {

    DIR_NAME=$1
    xwalk_version=$2
    if [[ ${DIR_NAME} == "NPLUS1" ]];then
        CTS_DIR=${WORKSPACE}/crosswalk-test-suite
    elif [[ ${DIR_NAME} == "N" ]]; then
        CTS_DIR=${WORKSPACE}/crosswalk-test-suite-${N}
    elif [[ ${DIR_NAME} == "N1" ]]; then
        CTS_DIR=${WORKSPACE}/crosswalk-test-suite-${N1}
    elif [[ ${DIR_NAME} == "N2" ]]; then
        CTS_DIR=${WORKSPACE}/crosswalk-test-suite-${N2}
    elif [[ ${DIR_NAME} == "N3" ]]; then
        CTS_DIR=${WORKSPACE}/crosswalk-test-suite-${N3}
    else
        echo "Params Error!"
        exit 1        
    fi 

    cd ${CTS_DIR}

    sed -i "s|\"main-version\": \"\([^\"]*\)\"|\"main-version\": \"${xwalk_version}\"|g" VERSION

    if [[ ${DIR_NAME} == "NPLUS1" ]]; then
        sed -i "s|beta|canary|g" VERSION
    elif [[ ${DIR_NAME} == "N1" ]]; then
        echo "beta"
    else
        sed -i "s|beta|stable|g" VERSION
    fi

    cd -
}

copy_sampleapp_code() {

    DIR_NAME=$1
    if [[ ${DIR_NAME} == "NPLUS1" ]];then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite/tools
    elif [[ ${DIR_NAME} == "N" ]]; then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite-${N}/tools
    elif [[ ${DIR_NAME} == "N1" ]]; then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite-${N1}/tools
    elif [[ ${DIR_NAME} == "N2" ]]; then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite-${N2}/tools
    elif [[ ${DIR_NAME} == "N3" ]]; then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite-${N2}/tools        
    else
        echo "Params Error!"
        exit 1
    fi

    cd ${TOOLS_DIR}

    if [[ ! -d circ ]]; then
        git clone ${CORDOVA_CIRC_URL}
    fi

    if [[ ! -d workshop-cca-eh ]]; then
        git clone ${CORDOVA_EH_URL}
    fi

    if [[ ! -d mobilespec ]]; then
        mkdir -pv mobilespec/
        cd mobilespec
        git clone ${CORDOVA_MOBILESPEC_URL}
        git clone ${CORDOVA_COHO_URL}
    fi

    cd ${WORKSPACE}
}

copy_cordova_plugin() {

    DIR_NAME=$1

    if [[ ${DIR_NAME} == "NPLUS1" ]];then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite/tools
    elif [[ ${DIR_NAME} == "N" ]]; then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite-${N}/tools
    elif [[ ${DIR_NAME} == "N1" ]]; then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite-${N1}/tools
    elif [[ ${DIR_NAME} == "N2" ]]; then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite-${N2}/tools
    elif [[ ${DIR_NAME} == "N3" ]]; then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite-${N3}/tools        
    else
        echo "Params Error!"
        exit 1
    fi

    cd ${TOOLS_DIR}

    if [[ ! -d cordova_plugins ]]; then
        if [[ -d ${PKG_TOOLS_DIR}/cordova_plugins_4.0 ]]; then
            cp -a ${PKG_TOOLS_DIR}/cordova_plugins_4.0 ./cordova_plugins
        else
            echo "${PKG_TOOLS_DIR}/crosswalk-plugins_4.0 does not exists!"
            exit 1        
        fi
    fi

    cd -
}

update_cordova_plugin() {
    DIR_NAME=$1
    CORDOVA_PLUGIN_XWALK_WEBVIEW_BRANCH=$2

    if [[ ${DIR_NAME} == "NPLUS1" ]];then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite/tools
    elif [[ ${DIR_NAME} == "N" ]]; then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite-${N}/tools
    elif [[ ${DIR_NAME} == "N1" ]]; then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite-${N1}/tools
    elif [[ ${DIR_NAME} == "N2" ]]; then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite-${N2}/tools
    elif [[ ${DIR_NAME} == "N3" ]]; then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite-${N3}/tools 
    else
        echo "Params Error!"
        exit 1
    fi

    cd ${TOOLS_DIR}
    cd cordova_plugins/cordova-plugin-crosswalk-webview
    git reset --hard HEAD
    git checkout master
    git pull

    if [[ ${CORDOVA_PLUGIN_XWALK_WEBVIEW_BRANCH} == "release-testing" ]]; then
        git checkout ${CORDOVA_PLUGIN_XWALK_WEBVIEW_BRANCH}
    else
        tag=${CORDOVA_PLUGIN_XWALK_WEBVIEW_BRANCH}
        git checkout ${tag}
    fi

    cd ${WORKSPACE}
}

modify_gradle() {

    DIR_NAME=$1
    if [[ ${DIR_NAME} == "NPLUS1" ]];then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite/tools
    elif [[ ${DIR_NAME} == "N" ]]; then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite-${N}/tools
    elif [[ ${DIR_NAME} == "N1" ]]; then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite-${N1}/tools
    elif [[ ${DIR_NAME} == "N2" ]]; then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite-${N2}/tools
    elif [[ ${DIR_NAME} == "N3" ]]; then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite-${N3}/tools 
    else
        echo "Params Error!"
        exit 1
    fi

    cd ${TOOLS_DIR}
    cd cordova_plugins/cordova-plugin-crosswalk-webview
    git checkout -- ${GRADLE}
    if [[ ${DIR_NAME} == "NPLUS1" ]]; then
        begin_line=`sed -n '/  maven {/=' ${GRADLE}`
        end_line=$[$begin_line + 2]
        sed -i "${begin_line},${end_line}d" ${GRADLE}
        sed -i "${begin_line}i\  mavenLocal()" ${GRADLE}       
    fi

    cd ${WORKSPACE}
}

modify_gradle_4cca() {

    DIR_NAME=$1
    BRANCH=$2
    CROSSWALK_VERSION=$3
    mode=$4

    if [[ ${DIR_NAME} == "NPLUS1" ]];then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite/tools
    elif [[ ${DIR_NAME} == "N" ]]; then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite-${N}/tools
    elif [[ ${DIR_NAME} == "N1" ]]; then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite-${N1}/tools
    elif [[ ${DIR_NAME} == "N2" ]]; then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite-${N2}/tools
    elif [[ ${DIR_NAME} == "N3" ]]; then
        TOOLS_DIR=${WORKSPACE}/crosswalk-test-suite-${N3}/tools 
    else
        echo "Params Error!"
        exit 1
    fi

    cd ${TOOLS_DIR}
    cd cordova_plugins/cordova-plugin-crosswalk-webview
    git checkout -- ${GRADLE}
    if [[ ${BRANCH} == "master" ]]; then
        begin_line=`sed -n '/  maven {/=' ${GRADLE}`
        end_line=$[$begin_line + 2]
        sed -i "${begin_line},${end_line}d" ${GRADLE}
        sed -i "${begin_line}i\  mavenLocal()" ${GRADLE}        
        sed -i "s|ext.xwalkVersion = getConfigPreference(\"xwalkVersion\")|ext.xwalkVersion = \"${CROSSWALK_VERSION}\"|g" ${GRADLE}
    fi

    if [[ ${BRANCH} == "beta" ]]; then
        if [[ ${mode} == "embedded" ]]; then
            sed -i "s|ext.xwalkVersion = getConfigPreference(\"xwalkVersion\")|ext.xwalkVersion = \"org.xwalk:xwalk_core_library_beta:${CROSSWALK_VERSION}\"|g" ${GRADLE}
        elif [[ ${mode} == "shared" ]]; then
            sed -i "s|ext.xwalkVersion = getConfigPreference(\"xwalkVersion\")|ext.xwalkVersion = \"org.xwalk:xwalk_shared_library_beta:${CROSSWALK_VERSION}\"|g" ${GRADLE}
        else
            echo "Wrong mode!"
            exit 1
        fi
    fi

    cd ${WORKSPACE}
}

pack_cordova_tc() {
    DIR_NAME=$1
    mode=$2
    arch=$3
    tag=$4
    branch_num=$5
    sub_mode=$6

    if [[ ${DIR_NAME} == "NPLUS1" ]];then
        CTS_DIR=${WORKSPACE}/crosswalk-test-suite
    elif [[ ${DIR_NAME} == "N" ]]; then
        CTS_DIR=${WORKSPACE}/crosswalk-test-suite-${N}
    elif [[ ${DIR_NAME} == "N1" ]]; then
        CTS_DIR=${WORKSPACE}/crosswalk-test-suite-${N1}
    elif [[ ${DIR_NAME} == "N2" ]]; then
        CTS_DIR=${WORKSPACE}/crosswalk-test-suite-${N2}
    elif [[ ${DIR_NAME} == "N3" ]]; then
        CTS_DIR=${WORKSPACE}/crosswalk-test-suite-${N3} 
    else
        echo "Params Error!"
        exit 1
    fi

    cd ${CTS_DIR}
    if [ ${mode} == "embedded" ]; then
        for tc in ${CORDOVA_SAMPLE_APPS_TC}
        do
            if [ -d $tc ]; then
                echo "rm -fv *.zip"
                echo "../../tools/build/pack.py -t cordova --sub-version 4.x -a ${arch} -m ${mode}"            
                echo "${branch_num}.${branch_num}-${tag}-embedded > ${DEST_DIR}/cordova/embedded/${branch_num}/${branch_num}/${arch}/README"
                echo "mv -fv *.zip ${DEST_DIR}/cordova/embedded/${branch_num}/${branch_num}/${arch}/"
            fi
        done

        for tc in ${USECASE_CORDOVA_TC}
        do
            if [ -d $tc ]; then
                echo "rm -fv *.zip"
                echo "../../tools/build/pack.py -t cordova --sub-version 4.x -a ${arch} -m ${mode}"
                echo "mv -fv *.zip ${DEST_DIR}/cordova/embedded/${branch_num}/${branch_num}/${arch}/"
            fi
        done
    fi
    if [ ${mode} == "shared" ]; then
        for tc in ${CORDOVA_SAMPLE_APPS_TC}
        do
            if [ -d $tc ]; then
                echo "rm -fv *.zip"
                echo "../../tools/build/pack.py -t cordova --sub-version 4.x -a ${arch} -m ${mode}"            
                echo "${branch_num}.${branch_num}-${tag}-shared > ${DEST_DIR}/cordova/embedded/${branch_num}/${branch_num}/${arch}/README"
                echo "mv -fv *.zip ${DEST_DIR}/cordova/shared/${branch_num}/${branch_num}/${arch}/"
            fi
        done

        for tc in ${USECASE_CORDOVA_TC}
        do
            if [ -d $tc ]; then
                echo "rm -fv *.zip"
                echo "../../tools/build/pack.py -t cordova --sub-version 4.x -a ${arch} -m ${mode}"
                echo "mv -fv *.zip ${DEST_DIR}/cordova/shared/${branch_num}/${branch_num}/${arch}/"
            fi
        done
    fi  
    if [ ${mode} == "matrix" ]; then
        for tc in ${CORDOVA_SAMPLE_APPS_TC}
        do
            if [ -d $tc ]; then
                echo "rm -fv *.zip"
                echo "../../tools/build/pack.py -t cordova --sub-version 4.x -a ${arch} -m ${sub_mode}"            
                echo "${branch_num}.${branch_num}-${tag} > ${DEST_DIR}/cordova/embedded/${branch_num}/${branch_num}/${arch}/README"
                echo "mv -fv *.zip ${DEST_DIR}/cordova/matrix/${branch_num}/${sub_mode}/${arch}/"
            fi
        done

        for tc in ${USECASE_CORDOVA_TC}
        do
            if [ -d $tc ]; then
                echo "rm -fv *.zip"
                echo "../../tools/build/pack.py -t cordova --sub-version 4.x -a ${arch} -m ${sub_mode}"
                echo "mv -fv *.zip ${DEST_DIR}/cordova/shared/${branch_num}/${sub_mode}/${arch}/"
            fi
        done
    fi      
}

pack_cordova_sampleapps() {
    DIR_NAME=$1
    mode=$2
    arch=$3
    tag=$4
    branch_num=$5
    sub_mode=$6

    if [[ ${DIR_NAME} == "NPLUS1" ]]; then
        BUILD_DIR=${WORKSPACE}/crosswalk-test-suite/tools/build
    elif [[ ${DIR_NAME} == "N" ]]; then
        BUILD_DIR=${WORKSPACE}/crosswalk-test-suite-${N}/tools/build
    elif [[ ${DIR_NAME} == "N1" ]]; then
        BUILD_DIR=${WORKSPACE}/crosswalk-test-suite-${N1}/tools/build
    elif [[ ${DIR_NAME} == "N2" ]]; then
        BUILD_DIR=${WORKSPACE}/crosswalk-test-suite-${N2}/tools/build
    elif [[ ${DIR_NAME} == "N3" ]]; then
        BUILD_DIR=${WORKSPACE}/crosswalk-test-suite-${N3}/tools/build
    else
        echo "Params Error!"
        exit 1
    fi

    cd ${BUILD_DIR}
    if [ ${mode} == "embedded" ]; then
        for app in ${N2_CORDOVA_SAMPLE_APPS}
        do
            # echo "rm -fv *.apk"
            # echo "rm -fv *.zip"

           echo "./pack_cordova_sample.py -n ${app} --cordova-version 4.x -a ${arch} -m ${mode}"
           echo "mv -fv ${app}.apk ${DEST_DIR}/cordova/embedded/${branch_num}/${branch_num}/${arch}"
        done

        for app in ${MOBILESPEC_APP}
        do
            # echo "rm -fv *.apk"
            # echo "rm -fv *.zip"

            echo "./pack_cordova_sample.py -n ${app} --cordova-version 4.x -a ${arch} -m ${mode} -p 000"
            echo "mv -fv ${app}.apk ${DEST_DIR}/cordova/embedded/${branch_num}/${branch_num}/${arch}"            
        done        
    fi     
    if [ ${mode} == "shared" ]; then
        if [[ ${DIR_NAME} == "N2" ]]; then
            for app in ${N2_CORDOVA_SAMPLE_APPS}
            do
                # echo "rm -fv *.apk"
                # echo "rm -fv *.zip"

                echo "./pack_cordova_sample.py -n ${app} --cordova-version 4.x -a ${arch} -m ${mode}"
                echo "mv -fv ${app}.apk ${DEST_DIR}/cordova/shared/${branch_num}/${branch_num}/${arch}"
            done
        fi

        if [[ ${DIR_NAME} == "N3" ]]; then
            for app in ${N3_CORDOVA_SAMPLE_APPS}
            do
                # echo "rm -fv *.apk"
                # echo "rm -fv *.zip"

                echo "./pack_cordova_sample.py -n ${app} --cordova-version 4.x -a ${arch} -m ${mode}"
                echo "mv -fv ${app}.apk ${DEST_DIR}/cordova/shared/${branch_num}/${branch_num}/${arch}"
            done

        fi
        for app in ${MOBILESPEC_APP}
        do
            # echo "rm -fv *.apk"
            # echo "rm -fv *.zip"

            echo "./pack_cordova_sample.py -n ${app} --cordova-version 4.x -a ${arch} -m ${mode} -p 000"
            echo "mv -fv ${app}.apk ${DEST_DIR}/cordova/shared/${branch_num}/${branch_num}/${arch}"            
        done
    fi

    if [[ ${mode} == "matrix" ]]; then 
        if [[ ${DIR_NAME} == "N1" ]]; then
            for app in ${N1_CORDOVA_SAMPLE_APPS}
            do
                # echo "rm -fv *.apk"
                # echo "rm -fv *.zip"

                echo "./pack_cordova_sample.py -n ${app} --cordova-version 4.x -a ${arch} -m ${sub_mode}"
                echo "mv -fv ${app}.apk ${DEST_DIR}/cordova/matrix/${branch_num}/${sub_mode}/${arch}"
            done
        fi        
        if [[ ${DIR_NAME} == "N2" ]]; then
            for app in ${N2_CORDOVA_SAMPLE_APPS}
            do
                # echo "rm -fv *.apk"
                # echo "rm -fv *.zip"

                echo "./pack_cordova_sample.py -n ${app} --cordova-version 4.x -a ${arch} -m ${sub_mode}"
                echo "mv -fv ${app}.apk ${DEST_DIR}/cordova/matrix/${branch_num}/${sub_mode}/${arch}"
            done
        fi

        if [[ ${DIR_NAME} == "N3" ]]; then
            for app in ${N3_CORDOVA_SAMPLE_APPS}
            do
                # echo "rm -fv *.apk"
                # echo "rm -fv *.zip"

                echo "./pack_cordova_sample.py -n ${app} --cordova-version 4.x -a ${arch} -m ${sub_mode}"
                echo "mv -fv ${app}.apk ${DEST_DIR}/cordova/matrix/${branch_num}/${sub_mode}/${arch}"
            done

        fi
        for app in ${MOBILESPEC_APP}
        do
            # echo "rm -fv *.apk"
            # echo "rm -fv *.zip"

            echo "./pack_cordova_sample.py -n ${app} --cordova-version 4.x -a ${arch} -m ${sub_mode} -p 000"
            echo "mv -fv ${app}.apk ${DEST_DIR}/cordova/matrix/${branch_num}/${sub_mode}/${arch}"            
        done
    fi
}

pack_cordova_sampleapps_cca() {
    DIR_NAME=$1
    mode=$2
    arch=$3
    tag=$4
    branch_num=$5
    sub_mode=$6

    if [[ ${DIR_NAME} == "NPLUS1" ]]; then
        BUILD_DIR=${WORKSPACE}/crosswalk-test-suite/tools/build
    elif [[ ${DIR_NAME} == "N" ]]; then
        BUILD_DIR=${WORKSPACE}/crosswalk-test-suite-${N}/tools/build
    elif [[ ${DIR_NAME} == "N1" ]]; then
        BUILD_DIR=${WORKSPACE}/crosswalk-test-suite-${N1}/tools/build
    elif [[ ${DIR_NAME} == "N2" ]]; then
        BUILD_DIR=${WORKSPACE}/crosswalk-test-suite-${N2}/tools/build
    elif [[ ${DIR_NAME} == "N3" ]]; then
        BUILD_DIR=${WORKSPACE}/crosswalk-test-suite-${N3}/tools/build
    else
        echo "Params Error!"
        exit 1
    fi

    cd ${BUILD_DIR}
    if [ ${mode} == "embedded" ]; then
        for app in ${CCA_SAMPLE_APPS}
        do
            # echo "rm -fv *.apk"
            # echo "rm -fv *.zip"

            echo "./pack_cordova_sample.py -n ${app} --cordova-version 4.x -a ${arch} -m ${mode}"
            echo "mv -fv ${app}.apk ${DEST_DIR}/cordova/embedded/${branch_num}/${branch_num}/${arch}"
        done
    fi
    if [ ${mode} == "shared" ]; then
        for app in ${CCA_SAMPLE_APPS}
        do
            # echo "rm -fv *.apk"
            # echo "rm -fv *.zip"

            echo "./pack_cordova_sample.py -n ${app} --cordova-version 4.x -a ${arch} -m ${mode}"
            echo "mv -fv ${app}.apk ${DEST_DIR}/cordova/shared/${branch_num}/${branch_num}/${arch}"
        done
    fi
    if [ ${mode} == "matrix" ]; then
        for app in ${CCA_SAMPLE_APPS}
        do
            # echo "rm -fv *.apk"
            # echo "rm -fv *.zip"

            echo "./pack_cordova_sample.py -n ${app} --cordova-version 4.x -a ${arch} -m ${sub_mode}"
            echo "mv -fv ${app}.apk ${DEST_DIR}/cordova/matrix/${branch_num}/${sub_mode}/${arch}"
        done
    fi      
}

###############################################################################
#   Building Cordova-related apks and test suites.
###############################################################################
#   N-2.N-2.alpha-1 embedded
###############################################################################

# update_code N2
# update_version N2 ${N_2_VER}
# copy_sampleapp_code N2
# copy_cordova_plugin N2
# update_cordova_plugin N2 ${ALPHA_1}

# modify_gradle N2
# pack_cordova_tc N2 embedded arm ${ALPHA_1} ${N2}
# pack_cordova_sampleapps N2 embedded arm ${ALPHA_1} ${N2}
# modify_gradle_4cca N2 beta ${N_2_VER} embedded
# pack_cordova_sampleapps_cca N2 embedded arm ${ALPHA_1} ${N2}

###############################################################################
#   N-2.N-2.alpha-1 shared
###############################################################################
# update_code N2
# update_version N2 ${N_2_VER}
# copy_sampleapp_code N2
# copy_cordova_plugin N2
# update_cordova_plugin N2 ${ALPHA_1}

# modify_gradle N2
# pack_cordova_tc N2 shared arm ${ALPHA_1} ${N2}
# pack_cordova_sampleapps N2 shared arm ${ALPHA_1} ${N2}
# modify_gradle_4cca N2 beta ${N_2_VER} shared
# pack_cordova_sampleapps_cca N2 shared arm ${ALPHA_1} ${N2}

###############################################################################
#   N-3.N-3.alpha shared
###############################################################################
# update_code N3
# update_version N3 ${N_3_VER}
# copy_sampleapp_code N3
# copy_cordova_plugin N3
# update_cordova_plugin N3 ${ALPHA}

# modify_gradle N3
# pack_cordova_tc N3 shared arm ${ALPHA} ${N3}
# pack_cordova_sampleapps N3 shared arm ${ALPHA} ${N3}
# modify_gradle_4cca N3 beta ${N_3_VER} shared
# pack_cordova_sampleapps_cca N3 shared arm ${ALPHA} ${N3}

###############################################################################
#   N-3.alpha-1 matrix embedded
###############################################################################
# update_code N3
# update_version N3 ${N_3_VER}
# copy_sampleapp_code N3
# copy_cordova_plugin N3
# update_cordova_plugin N3 ${ALPHA_1}

# modify_gradle N3
# pack_cordova_tc N3 matrix arm ${ALPHA_1} ${N3} embedded
# pack_cordova_sampleapps N3 matrix arm ${ALPHA_1} ${N3} embedded
# modify_gradle_4cca N3 beta ${N_3_VER} embedded
# pack_cordova_sampleapps_cca N3 matrix arm ${ALPHA_1} ${N3} embedded

###############################################################################
#   N-2.alpha-2 matrix embedded
###############################################################################
# update_code N2
# update_version N2 ${N_2_VER}
# copy_sampleapp_code N2
# copy_cordova_plugin N2
# update_cordova_plugin N2 ${ALPHA_2}

# modify_gradle N2
# pack_cordova_tc N2 matrix arm ${ALPHA_2} ${N2} embedded
# pack_cordova_sampleapps N2 matrix arm ${ALPHA_2} ${N2} embedded
# modify_gradle_4cca N2 beta ${N_2_VER} embedded
# pack_cordova_sampleapps_cca N2 matrix arm ${ALPHA_2} ${N2} embedded


###############################################################################
#   N-1.alpha-1 matrix embedded
###############################################################################
# update_code N1
# update_version N1 ${N_1_VER}
# copy_sampleapp_code N1
# copy_cordova_plugin N1
# update_cordova_plugin N1 ${ALPHA_1}

# modify_gradle N1
# pack_cordova_tc N1 matrix arm ${ALPHA_1} ${N1} embedded
# pack_cordova_sampleapps N1 matrix arm ${ALPHA_1} ${N1} embedded
# modify_gradle_4cca N1 beta ${N_1_VER} embedded
# pack_cordova_sampleapps_cca N1 matrix arm ${ALPHA_1} ${N1} embedded


###############################################################################
#   N-1.alpha-1 matrix shared
###############################################################################
# update_code N1
# update_version N1 ${N_1_VER}
# copy_sampleapp_code N1
# copy_cordova_plugin N1
# update_cordova_plugin N1 ${ALPHA_1}

# modify_gradle N1
# pack_cordova_tc N1 matrix arm ${ALPHA_1} ${N1} shared
# pack_cordova_sampleapps N1 matrix arm ${ALPHA_1} ${N1} shared
# modify_gradle_4cca N1 beta ${N_1_VER} shared
# pack_cordova_sampleapps_cca N1 matrix arm ${ALPHA_1} ${N1} shared


###############################################################################
#   N.alpha matrix embedded
###############################################################################
# update_code N
# update_version N ${N_VER}
# copy_sampleapp_code N
# copy_cordova_plugin N
# update_cordova_plugin N ${ALPHA}

# modify_gradle N
# pack_cordova_tc N matrix arm ${ALPHA} ${N} embedded
# pack_cordova_sampleapps N matrix arm ${ALPHA} ${N} embedded
# modify_gradle_4cca N beta ${N_VER} embedded
# pack_cordova_sampleapps_cca N matrix arm ${ALPHA} ${N} embedded


###############################################################################
#   N.alpha matrix shared
###############################################################################
# update_code N
# update_version N ${N_VER}
# copy_sampleapp_code N
# copy_cordova_plugin N
# update_cordova_plugin N ${ALPHA}

# modify_gradle N
# pack_cordova_tc N matrix arm ${ALPHA} ${N} shared
# pack_cordova_sampleapps N matrix arm ${ALPHA} ${N} shared
# modify_gradle_4cca N beta ${N_VER} shared
# pack_cordova_sampleapps_cca N matrix arm ${ALPHA} ${N} shared