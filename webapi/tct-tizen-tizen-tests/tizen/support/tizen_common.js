/*
Copyright (c) 2012 Intel Corporation.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of works must retain the original copyright notice, this list
  of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the original copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
* Neither the name of Intel Corporation nor the names of its contributors
  may be used to endorse or promote products derived from this work without
  specific prior written permission.

THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Authors:
        Huajun Li <huajun.li@intel.com>
        Wang, ChaoX <chaox.wang@intel.com>
        Lukasz Bardeli <l.bardeli@samsung.com>

*/

var apiTest = {
    wac : {
        orgName : "WAC2.0"
    },

    w3c : {
        orgName : "W3C"
    },

    tizen : {
        orgName : "TIZEN"
    }
};

var TYPE_MISMATCH_ERR = "TypeMismatchError";
var INVALID_VALUES_ERR = "InvalidValuesError";
var NOT_FOUND_ERR = "NotFoundError";
var UNKNOWN_ERR = "UnknownError";
var NOT_SUPPORTED_ERR = "NotSupportedError";
var PERMISSION_DENIED_ERR = "SecurityError";

var DOM_CODE_NOT_FOUND_ERR = 8;

function tizen_CompositeFilter_create(type, desc) {
    // Create an attribute filter based on first name: "First name should contain 'Chris' (case insensitive)
    var firstNameFilter = new tizen.AttributeFilter("name.firstName", "CONTAINS", "Chris");
    // Create an attribute filter based on last name: "Last name should be exactly 'Smith' (case insensitive)
    var lastNameFilter = new tizen.AttributeFilter("name.lastName", "EXACTLY", "Smith");
    // Create a filter based on the intersection of these two filter:
    // "First name should contain 'Chris' AND last name should be 'Smith'".
    var filter;

    try {
        return new tizen.CompositeFilter(type, [firstNameFilter, lastNameFilter]);
    } catch (e) {
        assert_false(true, "Fail to " + desc);
    }
}

function getWebAPIException(kind) {
    try {
        if (kind === "NotFoundError") {
            tizen.application.getAppInfo("111AppID88.WhichWillNotBeFound");
        } else {

            //tizen.application.findAppControl();
            // AppControl is not supported in Crosswalk at now.
            // Use launch() instead to throw WebAPIException
            tizen.application.launch();
        }
    } catch(error) {
        return error;
    }
    assert_unreached("Expected exception was not thrown. Can\'t continue.");
}

function getWebAPIError(test_obj, callback, kind) {
    var killSuccess, killError, currentApplication;
    assert_not_equals(callback, undefined, "callback is required argument of getWebAPIException()");
    onSuccess = test_obj.step_func(function () {
        assert_unreached("successCallback should not be called");
    });
    onError = test_obj.step_func(function (error) {
        callback(error);
    });

    currentApplication = tizen.application.getCurrentApplication();
    if (kind === "NotFoundError") {
        //tizen.application.launchAppControl(
        //    new tizen.ApplicationControl("WRONG_NOT_IMPLEMENTED_OPERATION"),
        //    "111AppID88.WhichWillNotBeFound",
        //    onSuccess, onError
        //);
        // AppControl is not supported in Crosswalk at now.
        // Use launch() instead to throw WebAPIError
        tizen.application.launch("111AppID88.WhichWillNotBeFound", onSuccess, onError);
    } else {
        assert_equals(kind, undefined, "Fix the test. Requested kind of error is not available");
        tizen.application.kill(currentApplication.contextId, onSuccess, onError);
    }
}
