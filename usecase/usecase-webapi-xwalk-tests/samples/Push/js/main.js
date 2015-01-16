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

var installUrl;
var reg;

$(document).ready(function() {
    $("#launch").attr('disabled', true);
    $("#push").attr('disabled', true);
    try {
        tizen.package.setPackageInfoEventListener(packageEventCallback);
    } catch (e) {
        $("#popup_info").modal(showMessage("error", "Exception: " + e.message));
    }
    pushPre();
});

function installPush() {
  install(installUrl);
  $("#launch").attr('disabled', false);
  $("#push").attr('disabled', false);
  return false;
}

function launchPush() {
  launch();
  return false;
}

function pushClient() {
  regID();
  return false;
}

var packageEventCallback = {
        oninstalled: function(packageInfo) {
            $("#popup_info").modal(showMessage("success", "The package " + packageInfo.name + " is installed"));
        },
        onupdated: function(packageInfo) {
            $("#popup_info").modal(showMessage("success", "The package " + packageInfo.name + " is updated"));
        },
        onuninstalled: function(packageId) {
            $("#popup_info").modal(showMessage("success", "The package " + packageId + " is uninstalled"));
        }
};

function fileURI() {
    var documentsDir;
    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            if(files[i].name == "TestPush.wgt")
            {
                var Url1 = files[i].toURI();
                installUrl = Url1.replace("file:///", "/");
            }
        }
    }

    function onerror(error) {
        $("#popup_info").modal(showMessage("error", "The error " + error.message + " occurred when listing the files in the selected folder"));
    }

    tizen.filesystem.resolve(
            'documents',
            function(dir){
                documentsDir = dir;
                dir.listFiles(onsuccess, onerror);
            }, function(e) {
                $("#popup_info").modal(showMessage("error", "Error " + e.message));
            }, "r"
    );
}

function install(url) {
    var onInstallationSuccess = {
            onprogress: function(packageId, percentage)
            {
                console.log("On installation(" + packageId + "): progress(" + percentage + ")");
                document.getElementById("install").innerHTML =  '<div data-role="button" id="install" style="height:40px; line-height:40px;">Installing... ' + percentage + "%" + '</div>';
            },
            oncomplete: function(packageId)
            {
                console.log("Installation(" + packageId + ") Complete");
                document.getElementById("install").innerHTML =  '<div data-role="button" id="install" style="height:40px; line-height:40px;">PushClient Install</div>';
                $("#install").attr('disabled', true);
            }
    }

    var onError = function (err) {
        $("#popup_info").modal(showMessage("error", "Error occured on installation : " + err.message));
    }

    try {
        tizen.package.install(url, onInstallationSuccess, onError);
    } catch (e) {
        $("#popup_info").modal(showMessage("error", "Exception: " + e.name));
    }
}

function launch() {
    function onSuccess() {
        console.log("Application launched successfully");
    }

    function onError(err) {
        $("#popup_info").modal(showMessage("error", "launch failed : " + err.message));
    }

    try {
        tizen.application.launch("bhvtcpush0.PushClient", onSuccess, onError);
    } catch (exc) {
        $("#popup_info").modal(showMessage("error", "launch exc:" + exc.message));
    }
}

function regID() {
    var documentsDir;
    var flag = false;
    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            if(files[i].name == "PushRegId.txt")
            {
                flag = true;
                files[i].readAsText(
                    function(str){
                        reg = str;
                        send();
                        }, function(e){
                            $("#popup_info").modal(showMessage("error", "Error " + e.message));
                        }, "UTF-8"
                );
                break;
            }
            else
                flag = false;
        }
        if(flag == false)
            $("#popup_info").modal(showMessage("error", "Not found Registration ID.\nPlease TestPush(PushClient) app install and launch or Check network connection."));
    }

    function onerror(error) {
        $("#popup_info").modal(showMessage("error", "Error " + error.message));
    }

    tizen.filesystem.resolve(
        "documents",
            function(dir){
                documentsDir = dir;
                dir.listFiles(onsuccess, onerror);
            }, function(e) {
                $("#popup_info").modal(showMessage("error", "Error" + e.message));
            }, "r"
    );
}

function checkNum(i) {
    if (i < 10) {
        i = "0" + i;
    }
    return i;
}

function send() {
    var appId = "bhvtcpush0";
    var msg = $("#message").val();
    var sec = "27A91C190007B2E7987627A9392C6291";
    var h = new Date().getHours();
    var m = new Date().getMinutes();
    var s = new Date().getSeconds();
    h = checkNum(h);
    m = checkNum(m);
    s = checkNum(s);

    if(msg == "")
    {
        $("#popup_info").modal(showMessage("error", "Message is empty"));
    }
    else if(reg == "")
    {
        $("#popup_info").modal(showMessage("error", "Registration ID is empty"));
    }
    else
    {
        var request = new XMLHttpRequest();
        var data = {"regID":reg, "requestID":"000001", "message":"action=ALERT&alertMessage="+msg, "appData":msg+"("+h+":"+m+":"+s+")"};
        var regID = reg.substring(0, 2);
        switch(regID)
        {
        case "00":
            request.open("POST", "https://useast.push.samsungosp.com:8088/spp/pns/api/push", true);
            break;
        case "01":
            request.open("POST", "https://uswest.push.samsungosp.com:8088/spp/pns/api/push", true);
            break;
        case "02":
            request.open("POST", "https://apsoutheast.push.samsungosp.com:8088/spp/pns/api/push", true);
            break;
        case "03":
            request.open("POST", "https://euwest.push.samsungosp.com:8088/spp/pns/api/push", true);
            break;
        case "04":
            request.open("POST", "https://apnortheast.push.samsungosp.com:8088/spp/pns/api/push", true);
            break;
        case "05":
            request.open("POST", "https://apkorea.push.samsungosp.com:8088/spp/pns/api/push", true);
            break;
        case "06":
            request.open("POST", "https://apchina.push.samsungosp.com.cn:8088/spp/pns/api/push", true);
            break;
        case "7c":
            request.open("POST", "https://175.41.248.50:8088/spp/pns/api/push", true);
        }
        request.setRequestHeader("Content-Type", "application/json");
        request.setRequestHeader("appID", appId);
        request.setRequestHeader("appSecret", sec);
        request.onreadystatechange = function() {
            if (request.readyState == 4 && request.status == 200) {
                console.log(request.responseText);
                $("#popup_info").modal(showMessage("success", "Push Success"));
            }
        };
        request.send(JSON.stringify(data));
    }
}

function pushPre() {
    var documentsDir;
    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            if(files[i].name == "TestPush")
            {
                documentsDir.copyTo(
                    files[i].fullPath,
                    "documents/TestPush.wgt",
                    true,
                    function() {
                        console.log("TestPush Precondition Success!");
                    });
            }
        }
        fileURI();
    }

    function onerror(error) {
        $("#popup_info").modal(showMessage("error", "Error " + error.message));
    }

    tizen.filesystem.resolve(
        'wgt-package/tests/Push/res/',
        function(dir){
            documentsDir = dir;
            dir.listFiles(onsuccess, onerror);
        }, function(e) {
            $("#popup_info").modal(showMessage("error", "Error " + e.message));
        }, "r"
    );
}
