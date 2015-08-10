#!/usr/bin/env python
import os
import commands
import sys
import json
import logging
import urllib2
import stat
import shutil
import subprocess
import time
import re
from bs4 import BeautifulSoup
from optparse import OptionParser

def setUp():
    global CROSSWALK_VERSION
    global CROSSWALK_BRANCH
    global LOG
    LOG = logging.getLogger("pack-tool")
    with open("../../tools/VERSION", "rt") as pkg_version_file:
        pkg_version_raw = pkg_version_file.read()
        pkg_version_file.close()
        pkg_version_json = json.loads(pkg_version_raw)
        CROSSWALK_VERSION = pkg_version_json["main-version"]
        CROSSWALK_BRANCH = pkg_version_json["crosswalk-branch"]


def installCrosswalk(pkgmode):
    version_parts = CROSSWALK_VERSION.split('.')
    if len(version_parts) < 4:
        print "The crosswalk version is not configured exactly!"
        sys.exit(1)
    versionType = version_parts[3]
    if versionType == '0':
        username = commands.getoutput("echo $USER")
        if pkgmode == "shared":
            repository_aar_path = "/home/%s/.m2/repository/org/xwalk/xwalk_shared_library/%s/" \
                "xwalk_shared_library-%s.aar" % \
                (username, CROSSWALK_VERSION, CROSSWALK_VERSION)
            repository_pom_path = "/home/%s/.m2/repository/org/xwalk/xwalk_shared_library/%s/" \
                "xwalk_shared_library-%s.pom" % \
                (username, CROSSWALK_VERSION, CROSSWALK_VERSION)
        else:
            repository_aar_path = "/home/%s/.m2/repository/org/xwalk/xwalk_core_library/%s/" \
                "xwalk_core_library-%s.aar" % \
            (username, CROSSWALK_VERSION, CROSSWALK_VERSION)
        repository_pom_path = "/home/%s/.m2/repository/org/xwalk/xwalk_core_library/%s/" \
            "xwalk_core_library-%s.pom" % \
            (username, CROSSWALK_VERSION, CROSSWALK_VERSION)

    if not os.path.exists(repository_aar_path) or not os.path.exists(repository_pom_path):
        if pkgmode == "shared":
            wget_cmd = "wget https://download.01.org/crosswalk/releases/crosswalk/" \
                "android/canary/%s/crosswalk-shared-%s.aar" % \
                (CROSSWALK_VERSION, CROSSWALK_VERSION)
            install_cmd = "mvn install:install-file -DgroupId=org.xwalk " \
                "-DartifactId=xwalk_shared_library -Dversion=%s -Dpackaging=aar " \
                "-Dfile=crosswalk-shared-%s.aar -DgeneratePom=true" % \
                (CROSSWALK_VERSION, CROSSWALK_VERSION)
        else:
            wget_cmd = "wget https://download.01.org/crosswalk/releases/crosswalk/" \
                "android/canary/%s/crosswalk-%s.aar" % \
                (CROSSWALK_VERSION, CROSSWALK_VERSION)
            install_cmd = "mvn install:install-file -DgroupId=org.xwalk " \
                "-DartifactId=xwalk_core_library -Dversion=%s -Dpackaging=aar " \
                "-Dfile=crosswalk-%s.aar -DgeneratePom=true" % \
                (CROSSWALK_VERSION, CROSSWALK_VERSION)

        os.system(wget_cmd)
        os.system(install_cmd)

def getLatestCrosswalkVersion(channel=None):
    version = ''
    crosswalk_url = ""
    if channel == "beta":
        crosswalk_url = 'https://download.01.org/crosswalk/releases/crosswalk/android/maven2/org/xwalk/' \
                'xwalk_core_library_beta/'
    elif channel == "stable":
        crosswalk_url = 'https://download.01.org/crosswalk/releases/crosswalk/android/maven2/org/xwalk/' \
                'xwalk_core_library/'
    else:
        LOG.error("getLatestCrosswalkVersion only support stable or beta")
        sys.exit(1)
    htmlDoc = urllib2.urlopen(crosswalk_url).read()
    soup = BeautifulSoup(htmlDoc)
    alist = soup.find_all('a')
    for index in range(-1, -len(alist)-1, -1):
        aEle = alist[index]
        version = aEle['href'].strip('/')
        if re.search('[0-9]*\.[0-9]*\.[0-9]*\.[0-9]*', version):
            break
    return version

