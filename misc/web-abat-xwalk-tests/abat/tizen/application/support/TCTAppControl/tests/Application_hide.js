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

*/

test(function () {
    var retVal, currentApplication = tizen.application.getCurrentApplication();

    retVal = currentApplication.hide();
    assert_equals(retVal, undefined, "wrong returned value");

}, "Application_hide");
