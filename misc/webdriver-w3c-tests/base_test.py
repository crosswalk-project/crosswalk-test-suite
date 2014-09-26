
import ConfigParser
import json
import os
import sys
import unittest

from webserver import Httpd
from network import get_lan_ip

class WebDriverBaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = create_driver()

        cls.webserver = Httpd(host=get_lan_ip())
        cls.webserver.__dict__['mobile'] = os.environ.get("WD_BROWSER", 'firefox')
        cls.webserver.__dict__['appId'] = appId
        cls.webserver.start()

    @classmethod
    def tearDownClass(cls):
        cls.webserver.stop()
        if cls.driver:
            cls.driver.quit()

appId = None
def create_driver():
    config = ConfigParser.ConfigParser()
    config.read('webdriver.cfg')
    section = os.environ.get("WD_BROWSER", 'firefox')
    url = 'http://127.0.0.1:4444/wd/hub'
    if config.has_option(section, 'url'):
        url = config.get(section, "url")
    capabilities = None
    if config.has_option(section, 'capabilities'):
        try:
            capabilities = json.loads(config.get(section, "capabilities"))
        except:
            pass
    mode = 'compatibility'
    if config.has_option(section, 'mode'):
        mode = config.get(section, 'mode')
    if section == "android" or section == "tizen":
        # import xwalk webdriver
        exec "from selenium import webdriver"
        # Save appId to build path of tizen app
        if section == "tizen":
            global appId
            appId = capabilities["xwalkOptions"]["tizenAppId"]
        return webdriver.Remote(url, capabilities)
    else:
        # import browser webdriver
        exec "from webdriver.driver import WebDriver"
        exec "from webdriver import exceptions, wait"
        return WebDriver(url, {}, capabilities, mode)
