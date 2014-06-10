
import ConfigParser
import json
import os
import unittest

from webserver import Httpd
from network import get_lan_ip

from selenium import webdriver

class WebDriverBaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = create_driver()

        cls.webserver = Httpd(host=get_lan_ip())
        cls.webserver.start()

    @classmethod
    def tearDownClass(cls):
        cls.webserver.stop()
        if cls.driver:
            cls.driver.quit()


def create_driver():
    capabilities = {
        'xwalkOptions': {
            'androidPackage': 'org.xwalk.xwalkdrivertest',
            'androidActivity': '.XwalkDriverTestActivity',
        }
    }
    return webdriver.Remote('http://localhost:9515', capabilities)
