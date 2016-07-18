#!/usr/bin/env python
import os
import commands
import sys
import json
import logging
import urllib2
import stat
import shutil
import fnmatch
import subprocess
import time
import re
from bs4 import BeautifulSoup
from optparse import OptionParser
script_path = os.path.realpath(__file__)
const_path = os.path.dirname(script_path)
tool_path = const_path + "/../tools/"
plugin_tool = const_path + "/../tools/cordova-plugin-crosswalk-webview/"

def setUp():
    global CROSSWALK_VERSION
    global CROSSWALK_BRANCH
    global LOG
    LOG = logging.getLogger("pack-tool")

    with open("../VERSION", "rt") as pkg_version_file:
        pkg_version_raw = pkg_version_file.read()
        pkg_version_file.close()
        pkg_version_json = json.loads(pkg_version_raw)
        CROSSWALK_VERSION = pkg_version_json["main-version"]
        CROSSWALK_BRANCH = pkg_version_json["crosswalk-branch"]

def getLatestCrosswalkVersion(channel=None, main_version=None):
    version = ""
    crosswalk_url_tmp = "https://download.01.org/crosswalk/releases/crosswalk-lite/android/maven2/org/xwalk/" \
                "xwalk_core_library"
    if channel == "beta":
        crosswalk_url = "%s_beta/" % crosswalk_url_tmp
    elif channel == "stable":
        crosswalk_url = "%s/" % crosswalk_url_tmp
    elif channel == "canary":
        crosswalk_url = "%s_canary/" % crosswalk_url_tmp
    else:
        LOG.error("getLatestCrosswalkVersion only support stable or beta")
        sys.exit(1)
    print crosswalk_url
    htmlDoc = urllib2.urlopen(crosswalk_url).read()
    soup = BeautifulSoup(htmlDoc)
    alist = soup.find_all('a')
    for index in range(-1, -len(alist)-1, -1):
        aEle = alist[index]
        version = aEle['href'].strip('/')
        if re.search('%s\.[0-9]*\.[0-9]*\.[0-9]*' % main_version, version):
            break
    print "version----------------------------------------------------------:" + version
    return version

def create(app_name, pkg_name, tmp_path):
    print "begin to create project:"
    project_path = os.path.join(tmp_path, app_name)
    os.chdir(tmp_path)
    if os.path.exists(project_path):
        doRemove([project_path])

    os.system("cordova create %s %s %s" % (app_name, pkg_name, app_name))
    os.chdir(project_path)
    # Set activity name as app_name
    replaceUserString(
        project_path,
        'config.xml',
        '<widget',
        '<widget android-activityName="%s"' %
        app_name)
    # Workaround for XWALK-3679
    replaceUserString(
        project_path,
        'config.xml',
        '</widget>',
        '    <allow-navigation href="*" />\n</widget>')
    os.system("cordova platform add android")

def installWebviewPlugin(xwalk_mode=None, xwalk_version=None):
    print "Install webview plugin----------------> Start"
    xwalk_mode_cmd = "--variable XWALK_MODE=\"%s\"" % xwalk_mode
    xwalk_version_cmd = ""
    if xwalk_version: 
        xwalk_version_cmd = "--variable XWALK_VERSION=\"%s\"" % xwalk_version

    crosswalk_plugin_source = plugin_tool

    install_crosswalk_cmd = "cordova plugin add %s %s %s" % (crosswalk_plugin_source, xwalk_version_cmd, xwalk_mode_cmd)
    os.system(install_crosswalk_cmd)
    print install_crosswalk_cmd
    print "Install webview plugin----------------> OK"

def removeWebviewPlugin():
    print "Remove webview plugin----------------> Start"
    cmd = "cordova plugin remove cordova-plugin-crosswalk-webview"
    print cmd
    buildstatus = commands.getstatusoutput(cmd)
    print "\nRemove webview plugin----------------> OK"

def build(appname, pkgarch="arm"):
    print "Build project %s ----------------> START" % appname
    cmd = "cordova build android -- --gradleArg=-PcdvBuildArch=%s --minSdkVersion=16" % pkgarch
    print cmd
    buildstatus = os.system(cmd)
    print "\nBuild project %s ----------------> OK\n" % appname

def checkApkExist(apk_path):
    lsstatus = commands.getstatusoutput("ls %s" % apk_path)
    if lsstatus[0] == 0:
        print "Build Package Successfully"
    else:
        print "Build Package Error"


def doCopy(src_item=None, dest_item=None):
    LOG.info("Copying %s to %s" % (src_item, dest_item))
    try:
        if os.path.isdir(src_item):
            overwriteCopy(src_item, dest_item, symlinks=True)
        else:
            if not os.path.exists(os.path.dirname(dest_item)):
                LOG.info("Create non-existent dir: %s" %
                         os.path.dirname(dest_item))
                os.makedirs(os.path.dirname(dest_item))
            shutil.copy2(src_item, dest_item)
    except Exception as e:
        LOG.error("Fail to copy file %s: %s" % (src_item, e))
        return False

    return True

def overwriteCopy(src, dest, symlinks=False, ignore=None):
    if not os.path.exists(dest):
        os.makedirs(dest)
        shutil.copystat(src, dest)
    sub_list = os.listdir(src)
    if ignore:
        excl = ignore(src, sub_list)
        sub_list = [x for x in sub_list if x not in excl]
    for i_sub in sub_list:
        s_path = os.path.join(src, i_sub)
        d_path = os.path.join(dest, i_sub)
        if symlinks and os.path.islink(s_path):
            if os.path.lexists(d_path):
                os.remove(d_path)
            os.symlink(os.readlink(s_path), d_path)
            try:
                s_path_s = os.lstat(s_path)
                s_path_mode = stat.S_IMODE(s_path_s.st_mode)
                os.lchmod(d_path, s_path_mode)
            except Exception:
                pass
        elif os.path.isdir(s_path):
            overwriteCopy(s_path, d_path, symlinks, ignore)
        else:
            shutil.copy2(s_path, d_path)

def replaceUserString(path, fnexp, old_s, new_s):
    print "Replace value ----------------> START"
    for sub_file in iterfindfiles(path, fnexp):
        try:
            with open(sub_file, 'r') as sub_read_obj:
                read_string = sub_read_obj.read()
        except IOError as err:
            #LOG.error("Read %s Error : " % sub_file + str(err))
            return False
        if read_string.find(old_s) >= 0:
            try:
                with open(sub_file, 'w') as sub_write_obj:
                    sub_write_obj.write(read_string.replace(old_s, new_s))
            except IOError as err:
                #LOG.error("Modify %s Error : " % sub_file + str(err))
                return False
    print "Replace value ----------------> OK"
    return True

def iterfindfiles(path, fnexp):
    for root, dirs, files in os.walk(path):
        for filename in fnmatch.filter(files, fnexp):
            yield os.path.join(root, filename)

def doRemove(target_file_list=None):
    print target_file_list
    for i_file in target_file_list:
        print "Removing %s" % i_file
        try:
            if os.path.isdir(i_file):
                shutil.rmtree(i_file)
            else:
                os.remove(i_file)
        except Exception as e:
            print "Fail to remove file %s: %s" % (i_file, e)
            return False
    return True

