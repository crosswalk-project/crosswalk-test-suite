import os
import ConfigParser
from behaving import environment as benv
from selenium.webdriver import Remote
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from splinter.driver.webdriver import BaseWebDriver, WebDriverElement as BaseWebDriverElement
from splinter.driver.webdriver.remote import WebDriverElement
from splinter.cookie_manager import CookieManagerAPI

TEST_APP_NAME = 'web_demo_tests'
webdriver_config = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "webdriver.cfg")

class WebDriver(BaseWebDriver):

    driver_name = "Remote webdriver"
    DEFAULT_URL = 'http://127.0.0.1:9515'

    def __init__(self, browser=driver_name, url=DEFAULT_URL, wait_time=2, desired_capabilities=None):
        self.driver = Remote(url, desired_capabilities)

        self.element_class = WebDriverElement

        self._cookie_manager = CookieManagerAPI()

        super(WebDriver, self).__init__(wait_time)

def getWebDriverParameters():
    try:
        config_file = os.environ['BDD_ATIP_CONFIG']
        print 'Using env config file: %s' % config_file
    except Exception, e:
        if os.path.exists(webdriver_config):
            config_file = webdriver_config
            print 'Using default config file: %s' % config_file
        else:
            print 'No config file found, exit ...'
            return ''

    try:
        cfg = ConfigParser.ConfigParser()
        cfg.read(config_file)
    except Exception, e:
        print 'Parser config failed: %s, exit ...' % e
        return ''

    config_parameters = {}
    try:
        config_parameters['target_platform'] = cfg.get(
            'WEBDRIVER', 'target_platform')
    except Exception, e:
        print 'Get target_platform from config failed:%s' % e
        config_parameters['target_platform'] = ''

    try:
        config_parameters['driver_url'] = cfg.get('WEBDRIVER', 'driver_url')
    except Exception, e:
        print 'Get driver_url from config failed:%s' % e
        config_parameters['driver_url'] = ''

    try:
        config_parameters['desired_capabilities'] = cfg.get(
            'WEBDRIVER', 'desired_capabilities')
    except Exception, e:
        print 'Get desired_capabilities from config failed:%s' % e
        config_parameters['desired_capabilities'] = ''

    try:
        config_parameters['test_prefix'] = cfg.get('WEBDRIVER', 'test_prefix')
    except Exception, e:
        print 'Get test_prefix from config failed:%s' % e
        config_parameters['test_prefix'] = ''

    try:
        config_parameters['sys_envs'] = cfg.get('WEBDRIVER', 'sys_envs')
    except Exception, e:
        print 'Get sys_envs  from config failed:%s' % e
        config_parameters['sys_envs'] = ''

    return config_parameters


def before_all(context):
    webdriver_parameters = getWebDriverParameters()
    if webdriver_parameters != '':
        envs = eval(webdriver_parameters['sys_envs'])
        for key in envs:
            os.environ[key] = envs[key]
        context.browser = WebDriver(browser="remote", url=eval(webdriver_parameters['driver_url']), desired_capabilities=eval(webdriver_parameters['desired_capabilities']))
        benv.before_all(context)
    else:
        return False


def after_all(context):
    benv.after_all(context)


def before_feature(context, feature):
    benv.before_feature(context, feature)


def after_feature(context, feature):
    benv.after_feature(context, feature)


def before_scenario(context, scenario):
    benv.before_scenario(context, scenario)


def after_scenario(context, scenario):
    #benv.after_scenario(context, scenario)
    pass
