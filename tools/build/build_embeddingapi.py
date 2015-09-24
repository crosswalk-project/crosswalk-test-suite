#!/usr/bin/env python
#
# Copyright (c) 2014 Intel Corporation.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of works must retain the original copyright notice, this
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Intel Corporation nor the names of its contributors
#   may be used to endorse or promote products derived from this work without
#   specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors:
#         Fan, Yugang <yugang.fan@intel.com>
#         Hao, Yunfei <yunfeix.hao@intel.com>

import os
import shutil
import glob
import time
import sys
import stat
import random
import json
import logging
import zipfile
import signal
import fnmatch
import subprocess
import commands
import re
from optparse import OptionParser
import varshop
import utils

global LOG
LOG = utils.getLogger("build_embeddingapi")

def packEmbeddingAPI_ant(
        build_json=None, app_src=None, app_dest=None, app_name=None, app_version=None):
    BUILD_PARAMETERS = varshop.getValue("BUILD_PARAMETERS")
    BUILD_ROOT = varshop.getValue("BUILD_ROOT")
    CROSSWALK_VERSION= varshop.getValue("CROSSWALK_VERSION")
    DEFAULT_CMD_TIMEOUT= varshop.getValue("DEFAULT_CMD_TIMEOUT")
    app_name = app_name.replace("-", "_")

    library_dir_name = utils.safelyGetValue(build_json, "embeddingapi-library-name")
    if not library_dir_name:
        LOG.error("Fail to get embeddingapi-library-name ...")
        return False

    new_library_dir_name = "core_library"
    pack_tool = os.path.join(app_src, "..", new_library_dir_name)

    if os.path.exists(pack_tool):
        if not utils.doRemove([pack_tool]):
            return False

    if not utils.doCopy(
            os.path.join(BUILD_PARAMETERS.pkgpacktools, library_dir_name),
            pack_tool):
        return False

    if os.path.exists(os.path.join(pack_tool, "bin", "res", "crunch")):
        if not utils.doRemove([os.path.join(pack_tool, "bin", "res", "crunch")]):
            return False

    orig_dir = os.getcwd()
    android_project_path = os.path.join(app_src, "android-project")
    try:
        os.makedirs(android_project_path)
    except Exception as e:
        LOG.error("Fail to create tmp project dir: %s" % e)
        return False

    (return_code, output) = utils.doCMDWithOutput("android list target", DEFAULT_CMD_TIMEOUT)
    api_level = ""
    for line in output:
        if "API level:" in line:
            api_level = line.split(":")[1].strip()
    if not api_level:
        LOG.error("Fail to get Android API Level")
        os.chdir(orig_dir)
        return False

    android_project_cmd = "android create project --name %s --target " \
                          "android-%s --path %s --package com.%s " \
                          "--activity MainActivity" % (
                              app_name, api_level, android_project_path, app_name)
    if not utils.doCMD(android_project_cmd, DEFAULT_CMD_TIMEOUT):
        os.chdir(orig_dir)
        return False

    try:
        update_file = open(
            os.path.join(android_project_path, "project.properties"), "a+")
        update_file.writelines(
            "{0}\n".format(
                "android.library.reference.1=../%s" %
                new_library_dir_name))
        update_file.close()
    except Exception as e:
        LOG.error(
            "Fail to update %s: %s" %
            (os.path.join(
                android_project_path,
                "project.properties"),
                e))
        os.chdir(orig_dir)
        return False

    if not utils.doCopy(os.path.join(android_project_path, "build.xml"),
                  os.path.join(app_src, "build.xml")):
        os.chdir(orig_dir)
        return False

    if not utils.doCopy(
            os.path.join(android_project_path, "project.properties"),
            os.path.join(app_src, "project.properties")):
        os.chdir(orig_dir)
        return False

    if not utils.doCopy(
            os.path.join(android_project_path, "local.properties"),
            os.path.join(app_src, "local.properties")):
        os.chdir(orig_dir)
        return False

    if not utils.doCopy(
            os.path.join(android_project_path, "local.properties"),
            os.path.join(pack_tool, "local.properties")):
        os.chdir(orig_dir)
        return False

    release_mode_tmp = "release"
    if BUILD_PARAMETERS.bnotdebug:
        LOG.info("Package release mode pkg start ...")
        ant_cmd = ["ant", "release", '-f', os.path.join(app_src, 'build.xml')]
        key_store = os.path.join(BUILD_PARAMETERS.pkgpacktools, 'crosswalk', 'xwalk-debug.keystore')
        if not os.path.exists(key_store):
            LOG.error("Need to copy xwalk-debug.keystore file from Crosswalk-<version> to crosswalk-test-suite/tools/crosswalk")
            return False
        ant_cmd.extend(['-Dkey.store=%s' % os.path.abspath(key_store)])
        ant_cmd.extend(['-Dkey.alias=xwalkdebugkey'])
        ant_cmd.extend(['-Dkey.store.password=xwalkdebug'])
        ant_cmd.extend(['-Dkey.alias.password=xwalkdebug'])
        ant_result = subprocess.call(ant_cmd)
        if ant_result != 0:
            os.chdir(orig_dir)
            return False
    else:
        LOG.info("Package debug mode pkg start ...")
        os.chdir(app_src)
        if not utils.doCMD("ant debug", DEFAULT_CMD_TIMEOUT):
           os.chdir(orig_dir)
           return False
        release_mode_tmp = "debug"

    if not utils.doCopy(
            os.path.join(app_src, "bin", "%s-%s.apk" % (app_name, release_mode_tmp)),
            os.path.join(app_dest, "%s.apk" % app_name)):
        os.chdir(orig_dir)
        return False
    os.chdir(orig_dir)
    return True


def packEmbeddingAPI_gradle(
        build_json=None, app_src=None, app_dest=None, app_name=None, app_version=None):
    BUILD_PARAMETERS = varshop.getValue("BUILD_PARAMETERS")
    BUILD_ROOT = varshop.getValue("BUILD_ROOT")
    CROSSWALK_VERSION= varshop.getValue("CROSSWALK_VERSION")
    DEFAULT_CMD_TIMEOUT= varshop.getValue("DEFAULT_CMD_TIMEOUT")
	app_name_origin = app_name
    app_name = app_name.replace("-", "_")
    orig_dir = os.getcwd()
    LOG.info("app_src: %s" % app_src)
    LOG.info("app_dest: %s" % app_dest)

    os.chdir(BUILD_ROOT)
    utils.replaceUserString(
        app_src,
        'build.gradle',
        '{crosswalk.version}',
        CROSSWALK_VERSION)

    version_parts = CROSSWALK_VERSION.split('.')
    if len(version_parts) < 4:
        LOG.error("The crosswalk version is not configured exactly!")
        return False
    versionType = version_parts[3]
    if versionType == '0':
        utils.replaceUserString(
            app_src,
            'build.gradle',
            'xwalk_core_library_beta',
            'xwalk_core_library')
        utils.replaceUserString(
            app_src,
            'build.gradle',
            'maven {\n        url \'https://download.01.org/crosswalk/releases/crosswalk/android/maven2\'\n    }',
            '    mavenLocal()')

        username = commands.getoutput("echo $USER")
        repository_aar_path = "/home/%s/.m2/repository/org/xwalk/xwalk_core_library/%s/" \
            "xwalk_core_library-%s.aar" % \
            (username, CROSSWALK_VERSION, CROSSWALK_VERSION)
        repository_pom_path = "/home/%s/.m2/repository/org/xwalk/xwalk_core_library/%s/" \
            "xwalk_core_library-%s.pom" % \
            (username, CROSSWALK_VERSION, CROSSWALK_VERSION)

        if not os.path.exists(repository_aar_path) or not os.path.exists(repository_pom_path):
            wget_cmd = "wget https://download.01.org/crosswalk/releases/crosswalk/" \
                "android/canary/%s/crosswalk-%s.aar" % \
                (CROSSWALK_VERSION, CROSSWALK_VERSION)
            if not utils.doCMD(wget_cmd, DEFAULT_CMD_TIMEOUT * 3):
                os.chdir(orig_dir)
                return False
            install_cmd = "mvn install:install-file -DgroupId=org.xwalk " \
                "-DartifactId=xwalk_core_library -Dversion=%s -Dpackaging=aar " \
                "-Dfile=crosswalk-%s.aar -DgeneratePom=true" % \
                (CROSSWALK_VERSION, CROSSWALK_VERSION)
            if not utils.doCMD(install_cmd, DEFAULT_CMD_TIMEOUT):
                os.chdir(orig_dir)
                return False

    os.chdir(app_src)
    if not utils.doCMD("gradle build", DEFAULT_CMD_TIMEOUT):
        os.chdir("..")
        return False
    if BUILD_PARAMETERS.pkgarch and BUILD_PARAMETERS.pkgarch == "arm":
        if not utils.doCopy(
                os.path.join(
                    app_src,
                    "build",
                    "outputs",
                    "apk",
                    "%s-armv7-debug.apk" %
                    app_name_origin),
                os.path.join(app_dest, "%s.apk" % app_name)):
            return False
    else:
        if not utils.doCopy(
                os.path.join(
                    app_src,
                    "build",
                    "outputs",
                    "apk",
                    "%s-x86-debug.apk" %
                    app_name_origin),
                os.path.join(app_dest, "%s.apk" % app_name)):
            return False
    os.chdir(orig_dir)
    return True


def packEmbeddingAPI_maven(
        build_json=None, app_src=None, app_dest=None, app_name=None, app_version=None):
    BUILD_PARAMETERS = varshop.getValue("BUILD_PARAMETERS")
    BUILD_ROOT = varshop.getValue("BUILD_ROOT")
    CROSSWALK_VERSION= varshop.getValue("CROSSWALK_VERSION")
    DEFAULT_CMD_TIMEOUT= varshop.getValue("DEFAULT_CMD_TIMEOUT")
    app_name = app_name.replace("-", "_")
    orig_dir = os.getcwd()
    LOG.info("app_src: %s" % app_src)
    LOG.info("app_dest: %s" % app_dest)

    os.chdir(BUILD_ROOT)
    utils.replaceUserString(
        app_src,
        'pom.xml',
        '{crosswalk.version}',
        CROSSWALK_VERSION)

    version_parts = CROSSWALK_VERSION.split('.')
    if len(version_parts) < 4:
        LOG.error("The crosswalk version is not configured exactly!")
        return False
    versionType = version_parts[3]

    if versionType == '0':
        utils.replaceUserString(
            app_src,
            'pom.xml',
            'xwalk_core_library_beta',
            'xwalk_core_library')

        username = commands.getoutput("echo $USER")
        repository_path = "/home/%s/.m2/repository/org/xwalk/xwalk_core_library/%s" % \
            (username, CROSSWALK_VERSION)
        repository_aar_path = "/home/%s/.m2/repository/org/xwalk/xwalk_core_library/%s/" \
            "xwalk_core_library-%s.aar" % \
            (username, CROSSWALK_VERSION, CROSSWALK_VERSION)
        repository_pom_path = "/home/%s/.m2/repository/org/xwalk/xwalk_core_library/%s/" \
            "xwalk_core_library-%s.pom" % \
            (username, CROSSWALK_VERSION, CROSSWALK_VERSION)

        if not os.path.exists(repository_aar_path) or not os.path.exists(repository_pom_path):
            wget_cmd = "wget https://download.01.org/crosswalk/releases/crosswalk/android" \
                "/canary/%s/crosswalk-%s.aar" % \
                (CROSSWALK_VERSION, CROSSWALK_VERSION)
            if not utils.doCMD(wget_cmd, DEFAULT_CMD_TIMEOUT * 3):
                os.chdir(orig_dir)
                return False
            install_cmd = "mvn install:install-file -DgroupId=org.xwalk " \
                "-DartifactId=xwalk_core_library -Dversion=%s -Dpackaging=aar " \
                "-Dfile=crosswalk-%s.aar -DgeneratePom=true" % \
                (CROSSWALK_VERSION, CROSSWALK_VERSION)
            if not utils.doCMD(install_cmd, DEFAULT_CMD_TIMEOUT):
                os.chdir(orig_dir)
                return False

        if not utils.doCopy(
                repository_aar_path,
                os.path.join(repository_path, "xwalk_core_library-%s-x86.aar" % CROSSWALK_VERSION)):
            os.chdir(orig_dir)
            return False
        if not utils.doCopy(
                repository_aar_path,
                os.path.join(repository_path, "xwalk_core_library-%s-arm.aar" % CROSSWALK_VERSION)):
            os.chdir(orig_dir)
            return False

        utils.replaceUserString(
            app_src,
            'pom.xml',
            'https://download.01.org/crosswalk/releases/crosswalk/android/maven2',
            'file:///home/%s/.m2/repository' % username)

    os.chdir(app_src)
    utils.replaceUserString(
        app_src,
        'AndroidManifest.xml',
        'android:versionCode=\"1\"',
        'android:versionCode=\"${app.version.code}\"')
    utils.replaceUserString(
        app_src,
        'AndroidManifest.xml',
        'android:versionName=\"1.0\"',
        'android:versionName=\"${app.version.name}\"')
    manifest_path = os.path.join(app_src, "AndroidManifest.xml")
    if not utils.doCopy(
            manifest_path, os.path.join(app_src, "src", "main", "AndroidManifest.xml")):
        return False
    if not utils.doRemove([manifest_path]):
        return False

    res_path = os.path.join(app_src, "res")
    if os.path.exists(res_path):
        if not utils.doCopy(res_path, os.path.join(app_src, "src", "main", "res")):
            return False
        if not utils.doRemove([res_path]):
            return False

    assets_path = os.path.join(app_src, "assets")
    if os.path.exists(assets_path):
        if not utils.doCopy(
                assets_path, os.path.join(app_src, "src", "main", "assets")):
            return False
        if not utils.doRemove([assets_path]):
            return False

    src_org_path = os.path.join(app_src, "src", "org")
    if not utils.doCopy(
            src_org_path, os.path.join(app_src, "src", "main", "java", "org")):
        return False
    if not utils.doRemove([src_org_path]):
        return False

    libs_path = os.path.join(app_src, "libs")
    if os.path.exists(libs_path):
        if not utils.doCopy(
                libs_path, os.path.join(app_src, "../libs")):
            return False
        if not utils.doRemove([libs_path]):
            return False

    if BUILD_PARAMETERS.pkgarch and BUILD_PARAMETERS.pkgarch == "arm":
        if not utils.doCMD("mvn clean install -Parm", DEFAULT_CMD_TIMEOUT):
            return False
        if not utils.doCopy(
                os.path.join(
                    app_src,
                    "target",
                    "embeddingapi-tests-arm.apk"),
                os.path.join(app_dest, "%s.apk" % app_name)):
            return False
    else:
        if not utils.doCMD("mvn clean install -Px86", DEFAULT_CMD_TIMEOUT):
            return False
        if not utils.doCopy(
                os.path.join(app_src, "target", "embeddingapi-tests-x86.apk"),
                os.path.join(app_dest, "%s.apk" % app_name)):
            return False
    os.chdir(orig_dir)
    return True
