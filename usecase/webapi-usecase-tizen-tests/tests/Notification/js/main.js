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
