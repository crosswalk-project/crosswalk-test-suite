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

*/

test(function () {
    var reqAppControl = tizen.application.getCurrentApplication().getRequestedAppControl(),
        appControl;

    assert_true("appControl" in reqAppControl, "RequestedApplicationControl should have appControl attribute");

    appControl = reqAppControl.appControl;
    assert_type(appControl, "object", "incorrect type of appControl");
    assert_true("operation" in appControl, "ApplicationControl should have operation attribute");
    assert_true("uri" in appControl, "ApplicationControl should have uri attribute");
    assert_true("mime" in appControl, "ApplicationControl should have mime attribute");
    assert_true("category" in appControl, "ApplicationControl should have category attribute");
    assert_true("data" in appControl, "ApplicationControl should have data attribute");

    reqAppControl.appControl = {
        operation: "dummy",
        uri: "dummy",
        mime: "dummy",
        category: "dummy",
        data: []
    };

    assert_equals(reqAppControl.appControl.operation, appControl.operation, "appControl is not readonly");
    assert_equals(reqAppControl.appControl.uri, appControl.uri, "appControl is not readonly");
    assert_equals(reqAppControl.appControl.mime, appControl.mime, "appControl is not readonly");
    assert_equals(reqAppControl.appControl.category, appControl.category, "appControl is not readonly");
    if(appControl.data) {
        assert_equals(reqAppControl.appControl.data.length, appControl.data.length, "appControl is not readonly");
    } else {
        assert_equals(reqAppControl.appControl.data, appControl.data, "appControl is not readonly");
    }

}, "RequestedApplicationControl_appControl_attribute");
