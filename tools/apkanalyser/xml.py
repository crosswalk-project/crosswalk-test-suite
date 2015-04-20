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
from datetime import *
from lxml import etree as et
import comm

def insert_xml_result(pathname, apkfile, apksize, appname, packagename,
                      launchableactivity, versioncode, versionname, sdkversion, targetsdkversion,
                      mode, architecture,
                      crosswalk, webview, chromium, coreinternal, cordova, xwalkwebvieweg, isintelxdk, xwalklist, chromiumlist, cordovalist, smalilist, assetlist, note):
    print apkfile, apksize, appname, packagename, launchableactivity, versioncode, versionname, sdkversion, targetsdkversion, mode, architecture, crosswalk, coreinternal, cordova, xwalkwebvieweg, isintelxdk, webview, note

    parser = et.XMLParser(remove_blank_text=True)
    tree = et.parse(pathname, parser)
    xroot = tree.getroot()
    xapk = et.SubElement(xroot, 'apk')
    xapk.attrib['id'] = packagename
    xcrosswalk = et.SubElement(xapk, 'crosswalk')
    xcrosswalk.attrib['iscrosswalk'] = crosswalk
    xcrosswalk.attrib['mode'] = mode
    xcrosswalk.attrib['architecture'] = architecture
    xcrosswalk.attrib['webview'] = webview
    xcrosswalk.attrib['chromium'] = chromium
    xcrosswalk.attrib['coreinternal'] = coreinternal
    xcrosswalk.attrib['cordova'] = cordova
    xcrosswalk.attrib['xwalkwebvieweg'] = xwalkwebvieweg
    xcrosswalk.attrib['intelxdk'] = isintelxdk
    xcrosswalk.attrib['note'] = note

    xapp = et.SubElement(xapk, 'app')
    xapp.attrib['name'] = appname
    xapp.attrib['file'] = apkfile
    xapp.attrib['size'] = apksize
    xapp.attrib['launchableactivity'] = launchableactivity
    xapp.attrib['versioncode'] = versioncode
    xapp.attrib['versionname'] = versionname
    xapp.attrib['sdkversion'] = sdkversion
    xapp.attrib['targetsdkversion'] = targetsdkversion

    for list in xwalklist:
        if list.strip():
            xxwalk = et.SubElement(xapk, 'xwalk')
            xxwalk.text = list.strip()

    for list in chromiumlist:
        if list.strip():
            xchromium = et.SubElement(xapk, 'chromium')
            xchromium.text = list.strip()

    for list in cordovalist:
        if list.strip():
            xcordova = et.SubElement(xapk, 'cordova')
            xcordova.text = list.strip()

    for list in smalilist:
        if list.strip():
            xsmali = et.SubElement(xapk, 'smali')
            xsmali.text = list.strip()

    for list in assetlist:
        if list.strip():
            xasset = et.SubElement(xapk, 'asset')
            xasset.text = list.strip()
    tree.write(pathname, pretty_print=True, xml_declaration=True, encoding='utf-8')

def generate_xml_report(pathname):
    tmp = pathname.split('/')[-1]
    dirname = pathname.replace('/' + tmp, '')
    comm.mk_dir(dirname)
    print 'Save result into:' + pathname

    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    root = et.Element('apks')
    root.addprevious(et.PI('xml-stylesheet', 'type="text/xsl" href="apk-analyser-result.xsl"'))
    root.attrib['datetime'] = date
    file = et.ElementTree(root)
    file.write(pathname, pretty_print=True, xml_declaration=True, encoding='utf-8')

