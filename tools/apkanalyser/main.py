#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2015 Intel Corporation. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#   * Redistributions of source code must retain the above copyright
#     notice, this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in
#     the documentation and/or other materials provided with the
#     distribution.
#   * Neither the name of Intel Corporation nor the names of its
#     contributors may be used to endorse or promote products derived
#     from this software without specific prior written permission.
#
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

        if (r.find('lib/armeabi-v7a/libxwalkcore.so') >-1 or r.find('lib/armeabi/libxwalkcore.so') >-1) and r.find('lib/x86/libxwalkcore.so') >-1:
            architecture = 'arm + x86'
        elif r.find('lib/armeabi-v7a/libxwalkcore.so') >-1 or r.find('lib/armeabi/libxwalkcore.so') >-1:
            print 'arm'
            architecture = 'arm'
        elif r.find('lib/x86/libxwalkcore.so') >-1:
            print 'x86'
            architecture = 'x86'
        return [architecture]

    except Exception, ex:
        print ex
        return ['']


def getxwalkwebviewplugin(path):
    linen = 1
    xversion = ''
    f1 = file(path, mode='r')
    line = f1.readline()
    while line:
        if line.find('cordova-plugin-crosswalk-webview') > -1:
            xversion = line.replace('cordova-plugin-crosswalk-webview','').replace('"','').replace(':','').strip()
        line = f1.readline()
        linen += 1
    f1.close()
    return xversion

def apktoolanalyser(path):

    apkname = path.split('/')[-1]
    apkdedecompiled = os.path.join(workpath, apkname.replace('.apk',''))
    embeddedpatharm = os.path.join(apkdedecompiled, 'lib', 'armeabi-v7a', 'libxwalkcore.so')
    embeddedpatharmv5 = os.path.join(apkdedecompiled, 'lib', 'armeabi', 'libxwalkcore.so')
    embeddedpathx86 = os.path.join(apkdedecompiled, 'lib', 'x86', 'libxwalkcore.so')

    xwalkcoreviewsmali = os.path.join(apkdedecompiled, 'smali', 'org', 'xwalk', 'core', 'XWalkView.smali')
    apachecordova = os.path.join(apkdedecompiled, 'smali', 'org', 'apache', 'cordova')
    smalipath = os.path.join(apkdedecompiled, 'smali')
    xwalkcoreinternal = os.path.join(apkdedecompiled, 'smali', 'org', 'xwalk', 'core', 'internal')
    intelxdk = os.path.join(apkdedecompiled, 'smali', 'com', 'intel', 'xdk')
    intelxdkjs = os.path.join(apkdedecompiled, 'assets', 'www', 'intelxdk.js')
    xwalkwebviewengine = os.path.join(apkdedecompiled, 'smali', 'org', 'crosswalk', 'engine', 'XWalkWebViewEngine.smali')
    xwalkwebviewplugin = os.path.join(apkdedecompiled, 'assets', 'www', 'cordova_plugins.js')

    mode = ''
    crosswalk = ''
    coreinternal = ''
    cordova = ''
    isintelxdk = ''
    webview = ''
    chromium = ''
    note = ''
    xwalkwebvieweg = ''
    xwalklist = []
    cordovalist = []
    chromiumlist = []
    smalilist = []
    assetlist = []

    try:
        apktoolcmd = 'apktool d -f ' + path
        t = subprocess.check_output(apktoolcmd, shell=True)
        if comm.find_dir(apkdedecompiled):

            if comm.find_file(embeddedpatharm) > -1 or comm.find_file(embeddedpatharmv5) > -1 or comm.find_file(embeddedpathx86) > -1:
                mode = 'embedded'
            elif comm.find_file(xwalkcoreviewsmali):
                mode = 'shared'

            if comm.find_file(xwalkcoreviewsmali):
                crosswalk = 'yes'
            else:
                note = 'Not a Crosswalk based app.'

            if comm.find_dir(xwalkcoreinternal):
                coreinternal = 'yes'

            if comm.find_dir(apachecordova):
                cordova = 'yes'

            if comm.find_file(xwalkwebviewengine):
                xwalkwebvieweg = 'yes'
            if comm.find_file(xwalkwebviewplugin): 
                if getxwalkwebviewplugin(xwalkwebviewplugin):
                    xwalkwebvieweg = getxwalkwebviewplugin(xwalkwebviewplugin)

            if crosswalk != 'yes':
                for root, dir, files in os.walk(smalipath):
                    for fn in files:
                            if fn.lower().find('cordovawebview') > -1:
                                cordova = 'yes'
                                webview = 'yes'
                            elif fn.lower().find('webview') > -1:
                                webview = 'yes'

            if comm.find_dir(intelxdk) or comm.find_file(intelxdkjs):
                isintelxdk = 'yes'

            for dirname, dirnames, filenames in os.walk(smalipath):
                t = dirname.replace(smalipath + '/', '')
                if t.find('xwalk') > -1:
                    xwalklist.append(t)
                elif t.find('chromium') > -1:
                    chromium = 'yes'
                    if t.count('/') >= 2 and t.count('/') < 4:
                        chromiumlist.append(t)
                elif t.find('cordova') > -1:
                    if t.count('/') >= 2 and t.count('/') < 4:
                        cordovalist.append(t)
                elif t.find('webkit') > -1:
                        webview = 'yes webkit'
                        smalilist.append(t)
                elif t.count('/') == 2 or t.count('/') == 3:
                    smalilist.append(t)

            assetpath = os.path.join(apkdedecompiled, 'assets')

            for dirname, dirnames, filenames in os.walk(assetpath):
                for f in filenames:
                    extname = ['png', 'gif', 'jpg', 'eot', 'woff', 'woff2', 'otf', 'ttf', 'wav', 'mp3', 'mp4', 'ogg', 'ogv', 'webm', 'svg']
                    if f.split('.')[-1] not in extname:
                        assetlist.append(f)

        else:
            print 'Decompile failed: ' + apkname
        shutil.rmtree(apkdedecompiled)

        return [crosswalk, mode, webview, chromium, coreinternal, cordova, xwalkwebvieweg, isintelxdk, note, xwalklist, chromiumlist, cordovalist, smalilist, assetlist]

    except Exception, ex:
        print ex
        return ['','', '','','','','','', '',[],[],[],[],[]]

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
    webview = k[2]
    chromium = k[3]
    coreinternal = k[4]
    cordova = k[5]
    xwalkwebvieweg = k[6]
    isintelxdk = k[7]
    note = k[8]
    xwalklist = k[9]
    chromiumlist = k[10]
    cordovalist = k[11]
    smalilist = k[12]
    assetlist = k[13]

    filename = path.split('\\')[-1].split('/')[-1]

    xml.insert_xml_result(xmlpath, filename, apksize(path), appname, packagename,
                          launchableactivity, versioncode, versionname, sdkversion, targetsdkversion,
                          mode, architecture,
                          crosswalk, webview, chromium, coreinternal, cordova, xwalkwebvieweg, isintelxdk, xwalklist, chromiumlist, cordovalist, smalilist, assetlist, note)
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