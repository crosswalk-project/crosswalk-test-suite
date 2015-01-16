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
        Choi, Jongheon <j-h.choi@samsung.com>

*/

var h, m, s, day, year, month, date;
var deviceCapabilities;

$(document).ready(function() {
    deviceCapabilities = tizen.systeminfo.getCapabilities();
    if(!deviceCapabilities.telephonyMms) {
        $("#mms").attr('disabled', true);
    }
});

function sms() {
    tizen.messaging.getMessageServices("messaging.sms", smsSuccessCallback, errorCallback);
}

function mms() {
    tizen.messaging.getMessageServices("messaging.mms", mmsSuccessCallback, errorCallback);
}

function checkTime(i) {
    if (i < 10) {
        i = "0" + i;
    }
    return i;
}

function checkDay(i) {
    switch(i)
    {
    case 0:
        i = "Sunday";
        break;
    case 1:
        i = "Monday";
        break;
    case 2:
        i = "Tuesday";
        break;
    case 3:
        i = "Wednesday";
        break;
    case 4:
        i = "Thursday";
        break;
    case 5:
        i = "Friday";
        break;
    case 6:
        i = "Saturday";
        break;
    }
    return i;
}

function checkMonth(i) {
    switch(i)
    {
    case 0:
        i = "January";
        break;
    case 1:
        i = "February";
        break;
    case 2:
        i = "March";
        break;
    case 3:
        i = "April";
        break;
    case 4:
        i = "May";
        break;
    case 5:
        i = "June";
        break;
    case 6:
        i = "July";
        break;
    case 7:
        i = "August";
        break;
    case 8:
        i = "September";
        break;
    case 9:
        i = "October";
        break;
    case 10:
        i = "November";
        break;
    case 11:
        i = "December";
        break;
    }
    return i;
}

function currentTime() {
    h = new Date().getHours();
    m = new Date().getMinutes();
    s = new Date().getSeconds();
    day = new Date().getDay();
    month = new Date().getMonth();
    date = new Date().getDate();
    year = new Date().getFullYear();
    h = checkTime(h);
    m = checkTime(m);
    s = checkTime(s);
    day = checkDay(day);
    month = checkMonth(month);
}

function smsSuccessCallback(services) {
    currentTime();
    if (services.length > 0) {
        var sms = new tizen.Message("messaging.sms");
        sms.body.plainBody = "BehaviorTC SMS Messaging Test\n" + h + ":" + m + ":" + s;
        sms.to = [$("#tel").val()];
        services[0].sendMessage(sms, messageSent, messageFailed);
    }
}

function mmsSuccessCallback(services) {
    currentTime();
    if (services.length > 0) {
        var mms = new tizen.Message("messaging.mms");
        mms.body.plainBody = "BehaviorTC MMS Messaging Test\n" + day + ", " + month + " " + date + ", " + year + ". " + h + ":" + m + ":" + s;
        mms.to = [$("#tel").val()];
        mms.subject = "BehaviorTC Messaging Test";
        mms.attachments = [new tizen.MessageAttachment("wgt-package/tests/MessagingSMSMMS/res/image.png", "image/png")];
        services[0].sendMessage(mms, messageSent, messageFailed);
    }
}

function messageSent(recipients) {
    $("#popup_info").modal(showMessage("success", "Message sent successfully to " + recipients.length + " recipients."));
}

function messageFailed(error) {
    $("#popup_info").modal(showMessage("error", 'Error occured while sending the message! ' + error.message));
}

function errorCallback(error) {
    $("#popup_info").modal(showMessage("error", "Cannot get messaging service " + error.message));
}
