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

$(document).delegate("#main", "pageinit", function() {
  gInfo =  makeDividerListItem("Notifcations messages");
  $("#info-list1").html(gInfo).trigger("create").listview("refresh");
  var titleInput = document.getElementById('title-input');
  var contentInput = document.getElementById('content-input');
  var typeSelect = document.getElementById('type-select');
  var notificationsContainer = document.getElementById('notifications-container');

  $("#showNotification").bind("vclick", function() {
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
      window.alert("Failed to add notification: " + err.message);
    }
  });

  $("#updateNotification").bind("vclick", function() {
    try {
      // Uses a variable for the previously posted notification.
      notification.content = "My notification";
      tizen.notification.update(notification); 
    } catch (err) {
      window.alert("Failed to update notification: " + err.message);
    }
  });


  $("#send-button").bind("vclick", function() {
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
      window.alert("Failed to send notification: " + e);
    }
  });
  
  $("#clear-button").bind("vclick", function() {
    try {
      tizen.notification.removeAll()
      refreshNotifications(tizen.notification.getAll());
    } catch (e) {
      window.alert("Failed to clear notifications: " + e);
    }
  });

});

function refreshNotifications(notifications) {
  gInfo = makeDividerListItem("Notifcations messages");
  for (var i = 0; i < notifications.length; i++) {
    gInfo += make1lineListItem("notification id:" + notifications[i].id)
          + make1lineListItem("notification title:" + notifications[i].title)
          + make1lineListItem("notification content:" + notifications[i].content);
  }
  $("#info-list1").html(gInfo).trigger("create").listview("refresh");
}

function make1lineListItem(value) {
  return '<li>' + value + '</li>';
}

function makeDividerListItem(value) {
  return '<li data-role="list-divider">' + value + '</li>';
}
