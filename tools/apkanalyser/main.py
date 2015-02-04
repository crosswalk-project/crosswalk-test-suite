#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2014 Intel Corporation. All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:

#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.
#   * Neither the name of Intel Corporation nor the names of its
#     contributors may be used to endorse or promote products derived
#     from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Author: belem.zhang@intel.com

# https://bitbucket.org/iBotPeaches/apktool/downloads
# Install and set apktool: https://code.google.com/p/android-apktool/wiki/Install

import os, sys
import shutil
import subprocess
from optparse import OptionParser
from datetime import *
import comm, xml

workpath = os.getcwd()
apkpath = os.path.join(workpath, 'apks')
reportpath = os.path.join(workpath, 'result')
xmlpath = reportpath + '/apk-analyser-result_' + datetime.now().strftime('%Y-%m-%d_%H-%M-%S') + '.xml'

def aaptdump(path):

    try:
        aaptdump = 'aapt d badging ' + path + ' AndroidManifest.xml'
        content = subprocess.check_output(aaptdump, shell=True)

        appname = ''
        packagename = ''
        launchableactivity = ''
        versioncode = ''
        versionname = ''
        sdkversion = ''
        targetsdkversion = ''

        if content.find('ERROR') == -1:
            lines = content.splitlines()
            for index, line in enumerate(lines):
                #print line
                if line.startswith('package:'):
                    info = line.split("'")
                    packagename = info[1]
                    versioncode = info[3]
                    versionname = info[5]

                if line.startswith('application-label:'):
                    appname = line.replace('\'','').replace('application-label:','').decode('utf-8')

                if line.startswith('launchable-activity'):
                    launchableactivity = line.split("'")[1]

                if line.startswith('sdkVersion'):
                    sdkversion = line.replace('\'','').replace('sdkVersion:','')

                if line.startswith('targetSdkVersion'):
                    targetsdkversion = line.replace('\'','').replace('targetSdkVersion:','')
        return [appname, packagename, launchableactivity, versioncode, versionname, sdkversion, targetsdkversion]

    except Exception, ex:
        print ex
        return ['','','','','','','']

def aaptanalyser(path):

    architecture = ''
    try:
        aaptlist = 'aapt list -a ' + path
        r = subprocess.check_output(aaptlist, shell=True)

        if r.find('lib/armeabi-v7a/libxwalkcore.so') >-1 and r.find('lib/x86/libxwalkcore.so') >-1:
            architecture = 'arm + x86'
        elif r.find('lib/armeabi-v7a/libxwalkcore.so') >-1:
            print 'arm'
            architecture = 'arm'
        elif r.find('lib/x86/libxwalkcore.so') >-1:
            print 'x86'
            architecture = 'x86'
        return [architecture]

    except Exception, ex:
        print ex
        return ['']

def apktoolanalyser(path):

    apkname = path.split('/')[-1]
    apkdedecompiled = os.path.join(workpath, apkname.replace('.apk',''))
    embeddedpatharm = os.path.join(apkdedecompiled, 'lib', 'armeabi-v7a', 'libxwalkcore.so')
    embeddedpathx86 = os.path.join(apkdedecompiled, 'lib', 'x86', 'libxwalkcore.so')

    xwalkcoreviewsmali = os.path.join(apkdedecompiled, 'smali', 'org', 'xwalk', 'core', 'XWalkView.smali')
    apachecordova = os.path.join(apkdedecompiled, 'smali', 'org', 'apache', 'cordova')
    xwalkappruntime = os.path.join(apkdedecompiled, 'smali', 'org', 'xwalk', 'app', 'runtime')
    xwalkcoreinternal = os.path.join(apkdedecompiled, 'smali', 'org', 'xwalk', 'core', 'internal')
    intelxdk = os.path.join(apkdedecompiled, 'smali', 'com', 'intel', 'xdk')
    intelxdkjs = os.path.join(apkdedecompiled, 'assets', 'www', 'intelxdk.js')

    mode = ''
    crosswalk = ''
    appruntime = ''
    coreinternal = ''
    cordova = ''
    isintelxdk = ''
    note = ''
    smalilist = []
    assetlist = []

    try:
        apktoolcmd = 'apktool d -f ' + path
        t = subprocess.check_output(apktoolcmd, shell=True)
        if comm.find_dir(apkdedecompiled):

            if comm.find_file(embeddedpatharm) > -1 or comm.find_file(embeddedpathx86) > -1:
                mode = 'embedded'
            elif comm.find_file(xwalkcoreviewsmali):
                mode = 'shared'

            if comm.find_file(xwalkcoreviewsmali):
                #print 'xwalk/core'
                crosswalk = 'yes'
                if comm.find_dir(xwalkappruntime):
                    #print 'xwalk/app/runtime'
                    appruntime = 'yes'
                if comm.find_dir(xwalkcoreinternal):
                    #print 'xwalk/core/internal'
                    coreinternal = 'yes'
            elif comm.find_dir(xwalkcoreinternal):
                note = 'Namespace org.xwalk.core.internal included.'
            else:
                note = 'Not a crosswalk based app.'

            if comm.find_dir(apachecordova):
                cordova = 'yes'

            if comm.find_dir(intelxdk) or comm.find_file(intelxdkjs):
                isintelxdk = 'yes'

            smalipath = os.path.join(apkdedecompiled, 'smali')

            for dirname, dirnames, filenames in os.walk(smalipath):

                if dirname.replace(smalipath + '/', '').count('/') == 2:
                    smalilist.append(dirname.replace(smalipath + '/', ''))

            assetpath = os.path.join(apkdedecompiled, 'assets')

            for dirname, dirnames, filenames in os.walk(assetpath):
                for f in filenames:
                    if not f.endswith('.png') and not f.endswith('.gif') and not f.endswith('.jpg') \
                            and not f.endswith('.eot') and not f.endswith('.woff') \
                            and not f.endswith('.otf') and not f.endswith('.wav') \
                            and not f.endswith('.svg') and not f.endswith('.ttf'):
                        assetlist.append(f)

        else:
            print 'Decompile failed: ' + apkname
        shutil.rmtree(apkdedecompiled)

        return [crosswalk, mode, appruntime, coreinternal, cordova, isintelxdk, note, smalilist, assetlist]

    except Exception, ex:
        print ex
        return ['','', '','','','','',[],[]]

def apksize(path):
    asize = '{0:.1f}{1}'.format(os.path.getsize(path)/1000.0/1000.0, 'MB')
    return asize

def analyser(path):

    g = aaptdump(path)
    t = aaptanalyser(path)
    k = apktoolanalyser(path)
    appname = g[0]
    packagename = g[1]
    launchableactivity = g[2]
    versioncode = g[3]
    versionname = g[4]
    sdkversion = g[5]
    targetsdkversion = g[6]

    architecture = t[0]

    crosswalk = k[0]
    mode = k[1]
    appruntime = k[2]
    coreinternal = k[3]
    cordova = k[4]
    isintelxdk = k[5]
    note = k[6]
    smalilist = k[7]
    assetlist = k[8]

    filename = path.split('\\')[-1].split('/')[-1]

    xml.insert_xml_result(xmlpath, filename, apksize(path), appname, packagename,
                          launchableactivity, versioncode, versionname, sdkversion, targetsdkversion,
                          mode, architecture,
                          crosswalk, appruntime, coreinternal, cordova, isintelxdk, smalilist, assetlist, note)
    print 'Completed: ' + path
    print '__________________________________________'

def run(path):
    if path.lower().endswith('.apk'):
        analyser(path)
    else:
        for root, dirs, files in os.walk(path):
            for name in files:
                if name.endswith('apk'):
                    analyser(os.path.join(path, name))

def option_check(path):
    xml.generate_xml_report(xmlpath)
    if path:
        run(path)
    else:
        print 'Path option is not defined, use default value: ' + apkpath
        run(apkpath)

def main():
    parser = OptionParser()
    parser.add_option('-p', '--path', dest='path',
                  help = '(mandatory) The path of apk or apks.')
    (options, args) = parser.parse_args()
    option_check(options.path)

if __name__ == '__main__':
    sys.exit(main())
    #python main.py
    #python main.py -p <apk file or folder>
    #python main.py -p /home/belem/github/apk-checker/apks/Test_0.0.1_arm_embedded.apk