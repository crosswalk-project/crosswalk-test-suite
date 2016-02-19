#!/usr/bin/env python
import ConfigParser
import sys
import os

PLATFROMS = ['android_xwalk', 'android_cordova', 'xw_deepin', 'chrome_ubuntu', 'windows']
PLATFORM = 'android_xwalk'

def read_config():
    try:
        global PLATFORM
        config = ConfigParser.ConfigParser()
        with open('data.conf', "r") as cfgfile:
            config.readfp(cfgfile)
        PLATFORM = config.get('info', 'env_platform')
    except Exception as e:
        print "Parser config data.config failed: %s" % e

def set_env_variables():
    read_config()
    if PLATFORM not in PLATFROMS:
        print 'Unsupportted platform type: %s' % PLATFORM
        sys.exit(1)

    if PLATFORM == 'android_xwalk':
        os.environ.update({'TEST_PLATFORM' : 'android',\
                           'DEVICE_ID': '',\
                           'CONNECT_TYPE': 'adb',\
                           'TIZEN_USER': '',\
                           'LAUNCHER': 'XWalkLauncher',\
                           'WEBDRIVER_VARS': '{"webdriver_url":"http://127.0.0.1:9515", "desired_capabilities": {"xwalkOptions": {"androidPackage": "TEST_PKG_NAME", "androidActivity": "TEST_ACTIVITY_NAME"}}, "test_prefix": "file:///android_asset/www/"}'})
    elif PLATFORM == 'android_cordova':
        os.environ.update({'TEST_PLATFORM' : 'android',\
                           'DEVICE_ID': '',\
                           'CONNECT_TYPE': 'adb',\
                           'TIZEN_USER': '',\
                           'LAUNCHER': 'CordovaLauncher',\
                           'WEBDRIVER_VARS': '{"webdriver_url":"http://127.0.0.1:9515", "desired_capabilities": {"xwalkOptions": {"androidPackage": "TEST_PKG_NAME", "androidActivity": "TEST_ACTIVITY_NAME"}}, "test_prefix": "file:///android_asset/www/"}'})
    elif PLATFORM == 'xw_deepin':
        os.environ.update({'TEST_PLATFORM' : 'deepin',\
                           'DEVICE_ID': '',\
                           'CONNECT_TYPE': '',\
                           'TIZEN_USER': '',\
                           'LAUNCHER': 'CordovaLauncher',\
                           'WEBDRIVER_VARS': '{"webdriver_url":"http://127.0.0.1:9515", "desired_capabilities": {"loggingPrefs":{},"xwalkOptions": {"binary": "/usr/bin/TEST_BINARY", "debugPort": "12450"}}}'})
    elif PLATFORM == 'chrome_ubuntu':
        os.environ.update({'TEST_PLATFORM' : 'chrome_ubuntu',\
                           'DEVICE_ID': '',\
                           'CONNECT_TYPE': '',\
                           'TIZEN_USER': '',\
                           'LAUNCHER': '',\
                           'WEBDRIVER_VARS': '{"webdriver_url":"http://127.0.0.1:9515", "desired_capabilities": {"chrome.binary": "/usr/bin/chromium-browser"}, "test_prefix": "file:///"}'})
    elif PLATFORM == 'windows':
        os.environ.update({'TEST_PLATFORM' : 'windows',\
                           'DEVICE_ID': '',\
                           'CONNECT_TYPE': '',\
                           'TIZEN_USER': '',\
                           'LAUNCHER': '',\
                           'WEBDRIVER_VARS': '{"webdriver_url":"http://127.0.0.1:9515", "desired_capabilities": {"loggingPrefs": {}, "xwalkOptions": { "binary": "C:\\\\Program Files\\\\TEST_BINARY"}}}'})
