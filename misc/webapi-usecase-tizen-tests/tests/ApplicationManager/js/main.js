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
        Xu, Jianfeng <jianfengx.xu@intel.com>

*/

var app, text, apps, conts;

function onSuccess (applications) {
  text = "";
  if (applications.length == 0) {
    text = "<ul><li class='name'>There is no app.</li></ul>"
     $("#app").html(text);
  } else {
    apps = applications;
    for (var i = 0; i < applications.length; i ++) {
      text = text + "<ul>ID : " + applications[i].id + "&nbsp;&nbsp;&nbsp;<a href='javascript: appInfo(" + i +");'>AppInfo</a>&nbsp;&nbsp;&nbsp;<a href='javascript: launch(" + i +");'>Run App</a></ul>"
    }
    $("#app").html(text);
  }
}

function onError (error) {
    $("#app").text("error: " + error.name);
}

function appInfo (index) {
  $("#app").html("Getting info for " + apps[index].id);
  try {
    var appInfo = tizen.application.getAppInfo(apps[index].id);
  
    if (appInfo) {
      text = "<ul><li class='name'>ID : " + appInfo.id + "</li><li>Name : " + appInfo.name  + "</li><li>Version :" + appInfo.version  + "</li><li>Packageid : " + appInfo.packageId  + "</li></ul>"
      $("#app").html(text);
    } else {
      $("#app").html("Get info for " + id + "faild!");
    }
  } catch (e) {
    $("#app").html("error : " + e.message);
  }
}

function launch(index) {
  $("#app").html("Running " + apps[index].id);
  try {
    tizen.application.launch(apps[index].id, runSuccess, onError);
  } catch (e) {
    $("#app").html("error : " + e.message);
  }

}

function runSuccess () {
  $("#app").html("The application has launched successfully");
}

function getAllApp () {
  try {
    tizen.application.getAppsInfo(onSuccess, onError);
  } catch (e) {
    $("#app").html("error : " + e.message);
  }
}

function CurrentApp () {
  try {
    app = tizen.application.getCurrentApplication();
    text = "<ul><li class='name'>ID : " + app.appInfo.id + "</li><li>Name : " + app.appInfo.name  + "</li><li>Version :" + app.appInfo.version  + "</li><li>Packageid : " + app.appInfo.packageId  + "</li></ul>"
    $("#app").html(text);
  } catch (e) {
    $("#app").html("error : " + e.message);
  }
}

function contextSuccess (contexts) {
  $("#app").text("Getting success.");
  text = "";
  if (contexts.length == 0) {
    text = "<ul><li class='name'>There is no context.</li></ul>"
     $("#app").html(text);
  } else {
    conts = contexts;
    for (var i = 0; i < contexts.length; i ++) {
      text = text + "<ul><li class='name'>ID : " + contexts[i].id + "</li><li>AppId : " + contexts[i].appId  + "</li><li><a href='javascript: kill(" + i +");'>Kill APP</a></li></ul>"
    }
    $("#app").html(text);
  }
}

function kill (index) {
  tizen.application.kill(conts[index].id, onKillSuccess, onError);
}

function onKillSuccess () {
  $("#app").html("Application terminated successfully");
}

function allContext () {
  try {
    $("#app").text("Getting list of application contexts for applications that are currently running on device");
    tizen.application.getAppsContext(contextSuccess, onError);
  } catch (e) {
    $("#app").html("error : " + e.message);
  }
}

function currentContext () {
  try {
    $("#app").text("Getting  the application context for the specified application context ID.");
    var appContext = tizen.application.getAppContext();
    text = "<ul><li class='name'>ID : " + appContext.id + "</li><li>AppId : " + appContext.appId  + "</li></ul>"
    $("#app").html(text);
  } catch (e) {
    $("#app").html("error : " + e.message);
  }
}

var init = function () {
   tizen.application.getAppsInfo(onSuccess, onError);
}

$(document).bind("pageinit", init);
