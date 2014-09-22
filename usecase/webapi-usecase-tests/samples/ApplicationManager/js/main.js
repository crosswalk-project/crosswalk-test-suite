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
     $("#result").html(text);
  } else {
    apps = applications;
    var flag = true;
    text = "<tr class='tr0'><td width='50%'>App ID</td><td width='50%' colspan='2'>Operation</td></tr>";
    for (var i = 0; i < applications.length; i ++) {
      if(flag) {
        text = text + "<tr class='tr2'><td width='50%'>" + applications[i].id + "</td><td width='25%'><a href='javascript: appInfo(" + i +");'>AppInfo</a></td><td width='25%'><a href='javascript: launch(" + i +");'>Run App</a></td></tr>";     
      } else {
        text = text + "<tr class='tr1'><td width='50%'>" + applications[i].id + "</td><td width='25%'><a href='javascript: appInfo(" + i +");'>AppInfo</a></td><td width='25%'><a href='javascript: launch(" + i +");'>Run App</a></td></tr>";  
      }
      flag = !flag;
    }
    $("#result").html(text);
  }
}

function onError (error) {
    $("#result").text("error: " + error.name);
}

function appInfo (index) {
  $("#result").html("Getting info for " + apps[index].id);
  try {
    var appInfo = tizen.application.getAppInfo(apps[index].id);
  
    if (appInfo) {
      text = "<tr class='tr0'><td width='30%'>App ID</td><td width='20%'>App Name</td><td width='20%'>App Version</td><td width='30%'>App PackageId</td></tr><tr class='tr2'><td>" + appInfo.id + "</td><td>" + appInfo.name + "</td><td>" + appInfo.version + "</td><td>" + appInfo.packageId + "</td></tr>";
      $("#result").html(text);
    } else {
      $("#result").html("Get info for " + id + "faild!");
    }
  } catch (e) {
    $("#result").html("error : " + e.message);
  }
}

function launch(index) {
  $("#result").html("Running " + apps[index].id);
  try {
    tizen.application.launch(apps[index].id, runSuccess, onError);
  } catch (e) {
    $("#result").html("error : " + e.message);
  }
}

function runSuccess () {
  $("#result").html("Please checking the app launched on GUI and service process commandline");
}

function getAllApp () {
  try {
    tizen.application.getAppsInfo(onSuccess, onError);
  } catch (e) {
    $("#result").html("error : " + e.message);
  }
}

function CurrentApp () {
  try {
    app = tizen.application.getCurrentApplication();
    text = "<tr class='tr0'><td width='30%'>Current App ID</td><td width='20%'>Current App Name</td><td width='20%'>Current App Version</td><td>Current App PackageId</td></tr><tr class='tr2'><td>" + app.appInfo.id + "</td><td>" + app.appInfo.name + "</td><td>" + app.appInfo.version + "</td><td>" + app.appInfo.packageId + "</td></tr>";  
    $("#result").html(text);
  } catch (e) {
    $("#result").html("error : " + e.message);
  }
}

function contextSuccess (contexts) {
  $("#result").text("Getting success.");
  text = "";
  if (contexts.length == 0) {
    text = "<ul><li class='name'>There is no context.</li></ul>"
     $("#result").html(text);
  } else {
    conts = contexts;
    var flag = true;
    text = "<tr class='tr0'><td width='40%'>Context ID</td><td width='40%'>Context AppId</td><td width='20%'>Operation/td></tr>";
    for (var i = 0; i < contexts.length; i ++) {
      if(flag) {
        text = text + "<tr class='tr2'><td>" + contexts[i].id + "</td><td>" + contexts[i].appId +"</td><td><a href='javascript: kill(" + i +");'>Kill App</a></td></tr>";     
      } else {
        text = text + "<tr class='tr1'><td>" + contexts[i].id + "</td><td>" + contexts[i].appId +"</td><td><a href='javascript: kill(" + i +");'>Kill App</a></td></tr>";
      }
      flag = !flag;
    }
    $("#result").html(text);
  }
}

function kill (index) {
  tizen.application.kill(conts[index].id, onKillSuccess, onError);
}

function onKillSuccess () {
  $("#result").html("Application terminated successfully");
}

function allContext () {
  try {
    $("#result").text("Getting list of application contexts for applications that are currently running on device");
    tizen.application.getAppsContext(contextSuccess, onError);
  } catch (e) {
    $("#result").html("error : " + e.message);
  }
}

function currentContext () {
  try {
    $("#result").text("Getting  the application context for the specified application context ID.");
    var appContext = tizen.application.getAppContext();
    text = "<tr class='tr0'><td width='50%'>Current Context ID</td><td width='50%'>Current Context AppId</td</tr><tr class='tr2'><td>" + appContext.id + "</td><td>" + appContext.appId + "</td></tr>";
    $("#result").html(text);
  } catch (e) {
    $("#result").html("error : " + e.message);
  }
}

var init = function () {
   CurrentApp();
}

$(document).bind("pageinit", init);
