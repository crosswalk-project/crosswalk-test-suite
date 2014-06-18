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
function showNotification() {
  try {
    var notificationDict = {
                content : "This is a simple notification.",
                vibration : true};

    notification = new tizen.StatusNotification("SIMPLE", 
                "Simple notification", notificationDict);
                       
    tizen.notification.post(notification);
  } catch (err) {
      console.log (err.name + ": " + err.message);
  }
}

function updateNotification() {
  try {
    // Uses a variable for the previously posted notification.
    notification.content = "My notification";
    tizen.notification.update(notification); 
  } catch (err) {
    console.log (err.name + ": " + err.message);
  }
}

function removeNotification() {
  try {
    tizen.notification.removeAll();
  } catch (err) {
    console.log (err.name + ": " + err.message);
  }
}


