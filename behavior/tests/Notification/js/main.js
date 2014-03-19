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

var gCurrentNoti;
var iconPath, soundPath, thumbnailPath1, thumbnailPath2, thumbnailPath3, thumbnailPath4;

var init = function () {
    showNotifications();
    setTimeout(init, 500);
};

$(document).delegate("#main", "pageinit", function() {
    $("#noti-list").delegate("div", "vclick", function() {
        var id = $(this).parent().data("id");

        try {
            tizen.notification.remove(id);
            alert("Notification delete");
        } catch (exc) {
            alert("notification.remove failed: " + exc.message);
        }
        showNotifications();
        return false;
    });
    $("#delete-all").bind("vclick", function() {
        try {
            tizen.notification.removeAll();
            alert("Notification delete all");
        } catch (exc) {
            alert("notification.removeAll failed: " + exc.message);
        }
        showNotifications();
        return false;
    });
    $("#noti-type-simple").bind("vclick", function() {
        postNotification("SIMPLE");
        showNotifications();
        $("#delete-all").removeClass("ui-disabled");
        return false;
    });
    $("#noti-type-ongoing").bind("vclick", function() {
        postNotification("ONGOING");
        showNotifications();
        $("#delete-all").removeClass("ui-disabled");
        return false;
    });
    $("#noti-type-progress").bind("vclick", function() {
        postNotification("PROGRESS");
        showNotifications();
        $("#delete-all").removeClass("ui-disabled");
        return false;
    });
    $("#noti-type-thumbnail").bind("vclick", function() {
        postNotification("THUMBNAIL");
        showNotifications();
        $("#delete-all").removeClass("ui-disabled");
        return false;
    });
    $("#install").bind("vclick", function() {
        install(installUrl);
        $("#noti-type-simple").removeClass("ui-disabled");
        $("#noti-type-ongoing").removeClass("ui-disabled");
        $("#noti-type-progress").removeClass("ui-disabled");
        $("#noti-type-thumbnail").removeClass("ui-disabled");
        return false;
    });
    $("#noti-type-simple").addClass("ui-disabled");
    $("#noti-type-ongoing").addClass("ui-disabled");
    $("#noti-type-progress").addClass("ui-disabled");
    $("#noti-type-thumbnail").addClass("ui-disabled");
    $("#delete-all").addClass("ui-disabled");
    try {
        tizen.package.setPackageInfoEventListener(packageEventCallback);
    } catch (e) {
        alert("Exception: " + e.message);
    }
    notificationPre();
});

function showNotifications() {
    var notiArray, str = "";

    try {
        notiArray = tizen.notification.getAll();
    } catch (exc) {
        alert("notification.getAll failed");
        return;
    }

    for (var i = 0; i < notiArray.length; i++) {
        str += '<li data-id="'
            + notiArray[i].id
            + '">'
            + notiArray[i].title
            //+ ' ('
            //+ notiArray[i].statusType
            //+ ')'
            + '<div data-role="button" data-inline="true">Delete</div></li>';
    }
    $("#noti-list").html(str).trigger("create").listview("refresh");
}

function postNotification(type) {
    var title = "";
    var appControl = new tizen.ApplicationControl("http://tizen.org/appcontrol/operation/view", null, null, null);
    var notiDict = {
            iconPath : iconPath,
            soundPath : soundPath,
            vibration : true,
            ledColor : "#4B0082",
            ledOnPeriod : 1000,
            ledOffPeriod : 500
        };
    if (type == "SIMPLE") {
        notiDict.content = "A touch to the notification makes it disappeared";
        title = "SIMPLE_Notification";
        notiDict.appId = "bhvtcnotif.NotificationTest";
    }
    if (type == "PROGRESS") {
        notiDict.content = "A touch to the notification does not make it disappeared";
        title = "PROGRESS_Notification";
        notiDict.progressValue = 20;
    }
    if (type == "ONGOING") {
        notiDict.content = "A touch to the notification does not make it disappeared";
        title = "ONGOING_Notification";
    }
    if (type == "THUMBNAIL") {
        notiDict.content = "A touch to the notification makes it disappeared";
        title = "THUMBNAIL_Notification";
        notiDict.thumbnails = [thumbnailPath1, thumbnailPath2, thumbnailPath3, thumbnailPath4];
    }
    try {
        var noti = new tizen.StatusNotification(type, title, notiDict);
        tizen.notification.post(noti);
        alert(type + " Notification Add");
        setTimeout(update, 3000);
    } catch (exc) {
        alert("notification.post failed: " + exc.message);
    }

    function update() {
        noti.progressValue = 63;
        tizen.notification.update(noti);
    }
}

function fileURI() {
    var documentsDir;
    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            if(files[i].name == "TestNotification.wgt")
            {
                var Url1 = files[i].toURI();
                installUrl = Url1.replace("file:///", "/");
            }
        }
    }

    function onerror(error) {
        alert("The error " + error.message + " occurred when listing the files in the selected folder");
    }

    tizen.filesystem.resolve(
            'documents',
            function(dir){
                documentsDir = dir;
                dir.listFiles(onsuccess, onerror);
            }, function(e) {
                alert("Error " + e.message);
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
                document.getElementById("install").innerHTML =  '<div data-role="button" id="install" style="height:40px; line-height:40px;">NotificationTest Install</div>';
            }
    }

    var onError = function (err) {
        alert("Error occured on installation : " + err.message);
    }

    try {
        tizen.package.install(url, onInstallationSuccess, onError);
    } catch (e) {
        alert("Exception: " + e.name);
    }
}

var packageEventCallback = {
        oninstalled: function(packageInfo) {
            alert("The package " + packageInfo.name + " is installed");
        },
        onupdated: function(packageInfo) {
            alert("The package " + packageInfo.name + " is updated");
        },
        onuninstalled: function(packageId) {
            alert("The package " + packageId + " is uninstalled");
        }
};

function notificationPre() {
    var documentsDir;
    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            if(files[i].name == "TestNotification")
            {
                documentsDir.copyTo(
                    files[i].fullPath,
                    "documents/TestNotification.wgt",
                    true,
                    function() {
                        console.log("Notification Precondition Success(1)!");
                    });
            }
            if(files[i].name == "notification.wav")
            {
                soundPath = files[i].toURI();
                soundPath = soundPath.replace("file:///", "/");
            }
            if(files[i].name == "noti.png")
            {
                iconPath = files[i].toURI();
                iconPath = iconPath.replace("file:///", "/");
            }
            if(files[i].name == "noti1.png")
            {
                thumbnailPath1 = files[i].toURI();
                thumbnailPath1 = thumbnailPath1.replace("file:///", "/");
            }
            if(files[i].name == "noti2.png")
            {
                thumbnailPath2 = files[i].toURI();
                thumbnailPath2 = thumbnailPath2.replace("file:///", "/");
            }
            if(files[i].name == "noti3.png")
            {
                thumbnailPath3 = files[i].toURI();
                thumbnailPath3 = thumbnailPath3.replace("file:///", "/");
            }
            if(files[i].name == "noti4.png")
            {
                thumbnailPath4 = files[i].toURI();
                thumbnailPath4 = thumbnailPath4.replace("file:///", "/");
            }
        }
        fileURI();
    }

    function onerror(error) {
        alert("The error " + error.message + " occurred when listing the files in the selected folder");
    }

    tizen.filesystem.resolve(
        'wgt-package/tests/Notification/res/',
        function(dir){
            documentsDir = dir;
            dir.listFiles(onsuccess, onerror);
        }, function(e) {
            alert("Error " + e.message);
        }, "r"
    );
}
$(document).bind('pageinit', init);
