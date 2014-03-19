/*
Copyright (c) 2013 Samsung Electronics Co., Ltd.

Licensed under the Apache License, Version 2.0 (the License);
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Authors:
        Krzysztof Lachacz <k.lachacz@samsung.com>
        Mariusz Polasinski <m.polasinski@samsung.com>
        Junghyuk Park <junghyuk.park@samsung.com>

*/


var METADATA_KEY = "testKey";
var METADATA_VALUE = "testValue";
var TCT_APPCONTROL_APPID_METADATA = {
    testKey1: "testValue1",
    testKey2: "testValue2"
}

var THIS_APP_ID = "api1appli0.WebAPITizenApplicationTests";
var INVALID_APP_ID = "api1appli0.WebAPITizenApplicationTestsInvalid";
var APP_INFO_TEST_APP_ID = "api1appli3.TCTAppInfoEventTest";

var TCT_APPCONTROL_APPID = "api1appli1.TCTAppControl";
var TCT_APPCONTROL_MOCK_APPID = "api1appli2.TCTAppControlMock";

var TCT_APPCONTROL_LAUNCH_APPCONTROL_OPERATION = "http://tizen.org/appcontrol/operation/tct/launch";
var TCT_APPCONTROL_LAUNCH_APPCONTROL_URI = "tct://launch_appcontrol.html";
var TCT_APPCONTROL_LAUNCH_APPCONTROL_MIME = "text/html";
var TCT_APPCONTROL_LAUNCH_APPCONTROL_MIME_INVALID = "invalid/invalid";

var TCT_APPCONTROL_LAUNCH_APPCONTROL_EXPLICIT_OPERATION = "http://tizen.org/appcontrol/operation/tct/launch/explicit";
var TCT_APPCONTROL_LAUNCH_APPCONTROL_EXPLICIT_URI = "tct://launch_appcontrol.html";
var TCT_APPCONTROL_LAUNCH_APPCONTROL_EXPLICIT_MIME = "text/html";

var TCT_APPCONTROL_REPLY_RESULT_OPERATION = "http://tizen.org/appcontrol/operation/tct/reply_result";
var TCT_APPCONTROL_REPLY_RESULT_WITH_DATA_OPERATION = "http://tizen.org/appcontrol/operation/tct/reply_result/data";
var TCT_APPCONTROL_REPLY_FAILURE_OPERATION = "http://tizen.org/appcontrol/operation/tct/reply_failure";

var TCT_APPCONTROL_RUN_TEST_OPERATION = "http://tizen.org/appcontrol/operation/tct/run_test";
var TCT_APPCONTROL_RUN_TEST_URI_PREFIX = "tct://";
var TCT_APPCONTROL_RUN_TEST_MIME = "application/javascript";

var TCT_APPCONTROL_EXIT_OPERATION = "http://tizen.org/appcontrol/operation/tct/exit";

var TYPE_MISMATCH_ERR = {name: 'TypeMismatchError'};

var TIMEOUT_AUTO_TEST = 30000;
setup({timeout: TIMEOUT_AUTO_TEST});

/**
 * Function runs test in other application (TCTAppControl) and receives
 * the results.
 *
 * @param testName name of the test
 */
function runTestAtTCTAppControl(testName) {
    var t = async_test(testName, { timeout: TIMEOUT_AUTO_TEST }),
    appControl, onreply, onerror, data;

    setup_launch(t, TCT_APPCONTROL_APPID, function () {
        appControl = new tizen.ApplicationControl(
                        TCT_APPCONTROL_RUN_TEST_OPERATION,
                        TCT_APPCONTROL_RUN_TEST_URI_PREFIX+testName,
                        TCT_APPCONTROL_RUN_TEST_MIME);

        onreply = {
            onsuccess: t.step_func(function (dataArray) {
                assert_true(dataArray.length == 2, "Unexpected dataArray");

                for (data in dataArray) {
                    if (dataArray[data].key === "status") {
                        t.status = parseInt(dataArray[data].value[0]);
                    } else if (dataArray[data].key === "message") {
                        t.message = dataArray[data].value[0];
                    } else {
                        assert_unreached("Unexpected key in data");
                        return;
                    }
                }

                t.done();
            }),
            onfailure: t.step_func(function () {
                assert_unreached("Unexpected onfailure");
            })
        };

        onerror = t.step_func(function (error) {
            assert_unreached("launchAppControl failure: " + error.message);
        });

        tizen.application.launchAppControl(appControl, null, null, onerror, onreply);
    });
}

function setup_launch(t, appId, onready) {
    t.step(function() {
        onready = t.step_func(onready);
      
        tizen.application.getAppsContext(
            t.step_func(function (contexts) {
                for (var i in contexts) {
                    if (contexts[i].appId === appId) {
                        tizen.application.kill(contexts[i].id, onready, onready);
                        return;
                    }
                }
                onready();
            }),
            t.step_func(function (error) {
                assert_unreached("setup_launch fails: " + error.name + " with message: " + error.message);
            })
        );  
    });
}

function assert_launch(t, appId, onsuccess) {
    var intervalId = setInterval(t.step_func(function() {
        tizen.application.getAppsContext(
            t.step_func(function (contexts) {
                for (var i in contexts) {
                    if (contexts[i].appId === appId) {
                        clearInterval(intervalId);
                        t.step_func(onsuccess)(contexts[i]);
                        return;
                    }
                }
            }),
            t.step_func(function (error) {
                assert_unreached("assert_launch fails: " + error.name + " with message: " + error.message);
            })
        );
    }), 1000);
}

function assert_not_launch(t, appId, onsuccess) {
    tizen.application.getAppsContext(
        t.step_func(function (contexts) {
            for (var i in contexts) {
                if (contexts[i].appId === appId) {
                    assert_unreached("assert_not_launch fails: "+appId+" has launched");
                    return;
                }
            }
            t.step_func(onsuccess)();
        }),
        t.step_func(function (error) {
            assert_unreached("assert_not_launch fails: " + error.name + " with message: " + error.message);
        })
    );
}

function assert_kill(t, appId, onsuccess) {
    var intervalId = setInterval(t.step_func(function() {
        tizen.application.getAppsContext(
            t.step_func(function (contexts) {
                for (var i in contexts) {
                    if (contexts[i].appId === appId) {
                        return;
                    }
                }
                clearInterval(intervalId);
                t.step_func(onsuccess)();
            }),
            t.step_func(function (error) {
                assert_unreached("assert_kill fails: " + error.name + " with message: " + error.message);
            })
        );
    }), 1000);
}

function assert_not_kill(t, appId, onsuccess) {
    tizen.application.getAppsContext(
        t.step_func(function (contexts) {
            for (var i in contexts) {
                if (contexts[i].appId === appId) {
                    t.step_func(onsuccess)();
                    return;
                }
            }
            assert_unreached("assert_not_kill fails: " + appId + " is not found");
        }),
        t.step_func(function (error) {
            assert_unreached("assert_not_kill fails: " + error.name + " with message: " + error.message);
        })
    );
}

function assert_exit(t, appId, onsuccess) {
    assert_kill(t, appId, onsuccess);
}
