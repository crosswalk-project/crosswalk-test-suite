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
        JungHyuk, Park <junghyuk.park@samsung.com>

*/

var TEST_SMS_RECIPIENT = ""; // this variable MUST be set before executing tests
var TEST_SMS_RECIPIENT_2 = ""; // this variable MUST be set before executing tests

var TYPE_MISMATCH_ERR  = 'TypeMismatchError';
var INVALID_VALUES_ERR = 'InvalidValuesError';
var NOT_FOUND_ERR      = 'NotFoundError';
var NOT_SUPPORTED_ERR  = 'NotSupportedError';
var IO_ERR             = 'IOError';
var UNKNOWN_ERR        = 'UnknownError';
var EXCEPTION_TYPE = "name";

var SMS_RESEND_LIMIT = 10;

var generatePlainBody = function () {
    var datetime = new Date().getTime();
    var count = 0;
    var plainBody = function(datetime, count) {
        return "sample plainBody: "+datetime+"-"+count;
    }

    generatePlainBody = function () {
        count++;
        return plainBody(datetime, count);
    }
    return plainBody(datetime, count);
};

function addDraft(t, service, initDict, onSuccess) {
    var msg, addSuccess, addError, serviceListSuccess, serviceListError;

    addError = t.step_func(function (error) {
        assert_unreached("failed to add draft: " + error.message);
    });

    addSuccess = t.step_func(function () {
        onSuccess(msg);
    });

    msg = new tizen.Message(service.type, initDict);
    service.messageStorage.addDraftMessage(msg, addSuccess, addError);
}


function addSMSDraft(t, service, initDict, onSuccess) {
    addDraft(t, service, initDict, onSuccess);
}


function removeAllMessages(t, service, onSuccess) {
    var msg, findSuccess, findError, removeSuccess, removeError, msgs, typeFilter;

    removeError = t.step_func(function (error) {
        assert_unreached("failed to remove messages: " + error.message);
    });

    removeSuccess = t.step_func(function () {
        onSuccess();
    });

    findError = t.step_func(function (error) {
        assert_unreached("failed to find messages: " + error.message);
    });

    findSuccess = t.step_func(function (msgs) {
        if (msgs.length > 0) {
            service.messageStorage.removeMessages(msgs, removeSuccess, removeError);
        } else {
            onSuccess();
        }
    });

    t.step(function () {
        assert_equals(service.type, "messaging.sms",
            "Fix your test: unknown service type: " + service.type);

        typeFilter = new tizen.AttributeFilter("type", "EXACTLY", "messaging.sms");
        service.messageStorage.findMessages(typeFilter, findSuccess, findError);
    });
}


function sendMessage(t, service, msg, onSuccess, onError) {
    var sendError, requestSending, resend=0;

    sendError = t.step_func(function (error) {
        if (resend <= SMS_RESEND_LIMIT) {
            setTimeout(requestSending, 5000);
        } else {
            onError(error);
        }
    });

    requestSending = t.step_func(function () {
        resend++;
        service.sendMessage(msg, onSuccess, sendError);
    });

    requestSending();
}

// change TEST_SMS_RECIPIENT and TEST_SMS_RECIPIENT_2
document.write('<script src="../webrunner/jquery-1.10.2.min.js"></script>');
document.write('<script src="support/getJsonConf.js"></script>');
