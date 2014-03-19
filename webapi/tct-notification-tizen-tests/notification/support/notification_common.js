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
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Authors:

 */

document.write("<script language=\"javascript\" src=\"..\/resources\/testharness.js\"><\/script>");
document.write("<script language=\"javascript\" src=\"..\/resources\/testharnessreport.js\"><\/script>");

var applicationControl, notificationDict, statusNotification, titleToSet = "Title",
    contentToSet = "This is a content notificaiton.",
    iconPathToSet = "images/webapi-tizen-notification-test_image1.jpg",
    iconPathToSet2 = "images/webapi-tizen-notification-test_image2.jpg",
    soundPathToSet = "music/webapi-tizen-notification-test_noise1.mp3",
    soundPathToSet2 = "music/webapi-tizen-notification-test_noise2.mp3",
    subIconPathToSet = "images/webapi-tizen-notification-test_subIcon1.jpg",
    subIconPathToSet2 = "images/webapi-tizen-notification-test_subIcon2.jpg",
    backgroundImagePathToSet = "images/webapi-tizen-notification-test_background1.jpg",
    backgroundImagePathToSet2 = "images/webapi-tizen-notification-test_background2.jpg",
    thumbnailToSet = "images/webapi-tizen-notification-test_thumbnail1.jpg",
    thumbnailToSet2 = "images/webapi-tizen-notification-test_thumbnail2.jpg",
    thumbnailToSet3 = "images/webapi-tizen-notification-test_thumbnail3.jpg",
    thumbnailToSet4 = "images/webapi-tizen-notification-test_thumbnail4.jpg",
    thumbnailToSet5 = "images/webapi-tizen-notification-test_thumbnail5.jpg",
    thumbnailToSet6 = "images/webapi-tizen-notification-test_thumbnail6.jpg",
    thumbnailToSet7 = "images/webapi-tizen-notification-test_thumbnail7.jpg",
    thumbnailToSet8 = "images/webapi-tizen-notification-test_thumbnail8.jpg",
    thumbnailToSet9 = "images/webapi-tizen-notification-test_thumbnail9.jpg",
    thumbnailToSet10 = "images/webapi-tizen-notification-test_thumbnail10.jpg",
    vibrationToSet = true,
    appIdToSet = tizen.application.getAppInfo().id, progressValueToSet = 77, numberToSet = 8,
    detailInfoToSet = [
        new tizen.NotificationDetailInfo("mainText1", "subText1"),
        new tizen.NotificationDetailInfo("mainText2", "subText2")
    ],
    thumbnailsToSet = [
        thumbnailToSet, thumbnailToSet2, thumbnailToSet3, thumbnailToSet4
    ];

applicationControl = new tizen.ApplicationControl("http://tizen.org/appcontrol/operation/default",
        null, "image/jpg", null);

notificationDict = {
    content : contentToSet,
    iconPath : iconPathToSet,
    soundPath : soundPathToSet,
    vibration : vibrationToSet,
    appControl : applicationControl,
    appId : appIdToSet,
    progressValue : progressValueToSet,
    number: numberToSet,
    subIconPath: subIconPathToSet,
    detailInfo: detailInfoToSet,
    backgroundImagePath: backgroundImagePathToSet,
    thumbnails: thumbnailsToSet
};

function test_func_property_exist(_object, _func_property_name, _desc) {
    var object = _object;
    var func_property_name = _func_property_name;
    var desc = _desc;
    try {
        test(function() {
            assert_true(func_property_name in object);
        }, desc);
    } catch (err) {
        test(function() {
            assert_true(false, "Exception - message: " + err.message);
        }, desc);
    }
}

function create_notification() {
    var appControl = new tizen.ApplicationControl("http://tizen.org/appcontrol/operation/create_content",
            null, "image/jpg", null);

    var notificationDict = {
        content : "This is a progress notificaiton.",
        iconPath : "images/webapi-tizen-notification-test_image1.jpg",
        soundPath : "music/webapi-tizen-notification-test_noise1.mp3",
        vibration : true,
        appControl : appControl,
        progressValue : 20
    };
    return new tizen.StatusNotification("PROGRESS", "Progress notification",
            notificationDict);
}

function testStatusNotificationConstructor(statusNotificationType, progessTypeToSet) {
    var i;
    notificationDict["progressType"] = progessTypeToSet;
    statusNotification = new tizen.StatusNotification(statusNotificationType, titleToSet, notificationDict);

    assert_true(statusNotification instanceof tizen.StatusNotification, "Created object is not of proper interface.");

    check_readonly(statusNotification, "postedTime", undefined, 'undefined', new Date());
    assert_equals(statusNotification.title, titleToSet, "title attribute.");
    assert_equals(statusNotification.content, contentToSet, "content attribute.");
    assert_equals(statusNotification.statusType, statusNotificationType, "statusType attribute.");
    assert_equals(statusNotification.iconPath, iconPathToSet, "iconPath attribute.");
    assert_equals(statusNotification.subIconPath, subIconPathToSet, "subIconPath attribute.");

    assert_equals(statusNotification.detailInfo.length, detailInfoToSet.length, "detailInfo attribute length.");
    for (i = 0; i < detailInfoToSet.length; i++) {
        assert_equals(statusNotification.detailInfo[i].mainText, detailInfoToSet[i].mainText, "detailInfo.mainText attribute for index = " + i + ".");
        assert_equals(statusNotification.detailInfo[i].subText, detailInfoToSet[i].subText, "detailInfo.subText attribute for index = " + i + ".");
    }
    assert_own_property(statusNotification, "ledColor", "statusNotification");
    assert_equals(statusNotification.ledOnPeriod, 0, "statusNotification.ledOnPeriod");
    assert_equals(statusNotification.ledOffPeriod, 0, "statusNotification.ledOffPeriod");

    assert_equals(statusNotification.backgroundImagePath, backgroundImagePathToSet, "backgroundImagePath attribute.");
    assert_equals(statusNotification.soundPath, soundPathToSet, "soundPath attribute.");
    assert_equals(statusNotification.vibration, vibrationToSet, "vibration attribute.");
    assert_equals(statusNotification.number, numberToSet, "number attribute.");

    assert_equals(statusNotification.appControl.uri, applicationControl.uri, "appControl.uri attribute.");
    assert_equals(statusNotification.appControl.mime, applicationControl.mime, "appControl.mime attribute.");
    assert_equals(statusNotification.appControl.category, applicationControl.category,
            "appControl.category attribute.");
    assert_array_equals(statusNotification.appControl.data, applicationControl.data,
            "appControl.data attribute.");
    assert_equals(statusNotification.appControl.operation, applicationControl.operation,
            "appControl.operation attribute.");

    check_readonly(statusNotification, "type", "STATUS", "string", "dummyType");
    assert_equals(statusNotification.appId, appIdToSet, "appId attribute.");
    assert_equals(statusNotification.progressType, progessTypeToSet, "progressType attribute.");
    assert_equals(statusNotification.progressValue, progressValueToSet, "progressValue attribute.");
    check_readonly(statusNotification, "id", undefined, "undefined", "dummyId");
    assert_array_equals(statusNotification.thumbnails, thumbnailsToSet, "thumbnails attribute.");
}
