import os
import sys
import json
from atip import environment as atipenv
try:
    from urllib2 import URLError
except ImportError:
    from urllib.error import URLError

webdriver_json_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "webdriver.json")


def clean_context(context):
    for app in context.apps.values():
        try:
            app.quit()
        except URLError:
            pass

    context.app = None
    context.apps = {}


def load_default_config():
    webdriver_json = None
    try:
        platform_name = os.environ['TEST_PLATFORM']
        device = os.environ['DEVICE_ID']
        comm_mode = os.environ['CONNECT_TYPE']
        webdriver_envs = json.loads(os.environ['WEBDRIVER_VARS'])
        webdriver_json = {}
        platform = {}
        platform.update({"name": platform_name})
        platform.update({"comm-mode": comm_mode})
        platform.update({"device": device})
        webdriver_json.update({"platform": platform})
        webdriver_json.update(
            {"desired-capabilities": webdriver_envs["desired_capabilities"]})
        webdriver_json.update({"driver-url": webdriver_envs["webdriver_url"]})
        if webdriver_envs.has_key("test_prefix"):
            webdriver_json.update(
                {"url-prefix": webdriver_envs["test_prefix"]})
        else:
            webdriver_json.update({"url-prefix": ""})
    except Exception, e:
        print "Failed to get test envs: %s, switch to webdriver.json" % e
        try:
            with open(webdriver_json_path, "rt") as webdriver_json_file:
                webdriver_json_raw = webdriver_json_file.read()
                webdriver_json_file.close()
                webdriver_json = json.loads(webdriver_json_raw)
        except Exception, e:
            print "Failed to read webdriver json: %s" % e
            return None

    return webdriver_json


def before_all(context):
    atipenv.before_all(context)
    context.app = None
    context.apps = {}
    context.web_config = load_default_config()
    if not context.web_config:
        sys.exit(1)


def after_all(context):
    atipenv.after_all(context)
    clean_context(context)


def before_feature(context, feature):
    atipenv.before_feature(context, feature)


def after_feature(context, feature):
    atipenv.after_feature(context, feature)
    clean_context(context)


def before_scenario(context, scenario):
    atipenv.before_scenario(context, scenario)


def after_scenario(context, scenario):
    atipenv.after_scenario(context, scenario)
    clean_context(context)
