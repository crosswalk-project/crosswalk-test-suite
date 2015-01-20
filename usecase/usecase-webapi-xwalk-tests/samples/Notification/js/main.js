/*
Copyright (c) 2014 Intel Corporation.

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
        Liu, Xin <xinx.liu@intel.com>

*/
var notification;

$(document).ready(function() {
  gInfo =  makeDividerListItem("Notifcations messages");
  $("#info-list1").html(gInfo);
  var titleInput = document.getElementById('title-input');
  var contentInput = document.getElementById('content-input');
  var typeSelect = document.getElementById('type-select');
  var notificationsContainer = document.getElementById('notifications-container');
});

function showNotification() {
  try {
    var notificationDict = {
              content : "This is a simple notification.",
              iconPath : "",
              soundPath : "", 
              vibration : true};

    notification = new tizen.StatusNotification("SIMPLE", 
              "Simple notification", notificationDict);
                     
    tizen.notification.post(notification);
  } catch (err) {
    $("#popup_info").modal(showMessage("error", "Failed to add notification: " + err.message));
  }
}

function updateNotification() {
  try {
    // Uses a variable for the previously posted notification.
    notification.content = "My notification";
    tizen.notification.update(notification); 
  } catch (err) {
    $("#popup_info").modal(showMessage("error", "Failed to update notification: " + err.message));
  }
}

function send() {
  var titleValue = titleInput.value;
  if (!titleValue)
    titleValue = titleInput.placeholder;

  var contentValue = contentInput.value;
  if (!contentValue)
     contentValue = contentInput.placeholder;

  var options = {
     content: contentValue
  };
  try {
    tizen.notification.post(new tizen.StatusNotification(typeSelect.value, titleValue, options));
    refreshNotifications(tizen.notification.getAll());
  } catch (e) {
    $("#popup_info").modal(showMessage("error", "Failed to send notification: " + e));
  }
}

function clear() {
  try {
    tizen.notification.removeAll()
    refreshNotifications(tizen.notification.getAll());
  } catch (e) {
    $("#popup_info").modal(showMessage("error", "Failed to clear notifications: " + e));
  }
}

function refreshNotifications(notifications) {
  gInfo = makeDividerListItem("Notifcations messages");
  for (var i = 0; i < notifications.length; i++) {
    gInfo += make1lineListItem("notification id:" + notifications[i].id)
          + make1lineListItem("notification title:" + notifications[i].title)
          + make1lineListItem("notification content:" + notifications[i].content);
  }
  $("#info-list1").html(gInfo);
}

function make1lineListItem(value) {
  return '<div class="panel-body">' + value + '</div>';
}

function makeDividerListItem(value) {
  return '<div class="panel-heading">' + value + '</div>';
}
