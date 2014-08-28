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
$(document).delegate("#main", "pageinit", function() {
    $("#alarm-remove-all").bind("vclick", function() {
        removeAll();
        return false;
    });
    $("#alarm-all-list").delegate("li", "vclick", function() {
        alarmInfo($(this).data("id"));
        return false;
    });
    $("#alarm-all-list").delegate("div", "vclick", function() {
        removeAlarm($(this).parent().data("id"));
        return false;
    });
    $("#install").bind("vclick", function() {
        install_(installUrl);
        $("#absolute-alarm-save").removeClass("ui-disabled");
        return false;
    });
    $("#absolute-alarm-save").bind("vclick", function() {
        addAlarmAbsolute();
        $("#alarm-remove-all").removeClass("ui-disabled");
        return false;
    });
    $("#absolute-alarm-save").addClass("ui-disabled");
    $("#alarm-remove-all").addClass("ui-disabled");
    try {
        tizen.package.setPackageInfoEventListener(packageEventCallback);
    } catch (e) {
        alert("Exception: " + e.message);
    }
    displayAlarms();
    alarmPre();
});

function fileURI() {
    var documentsDir;
    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            if(files[i].name === "TestAlarm.wgt")
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

function displayAlarms() {
    var alarmsArray = tizen.alarm.getAll();
    var period, str = "";

    for (var i = 0; i < alarmsArray.length; i++) {
        if (alarmsArray[i].period) {
            period = alarmsArray[i].period + " sec";
        } else {
            period = "none";
        }

        if (alarmsArray[i] instanceof tizen.AlarmAbsolute) {
            var d = alarmsArray[i].date,
            m = d.getMinutes();

            str += '<li data-id="'
                + alarmsArray[i].id
                + '">'
                + (d.getMonth() + 1)
                + '/'
                + d.getDate()
                + '/'
                + d.getFullYear()
                + ' '
                + d.getHours()
                + ':'
                + ((m < 10) ? "0" + m : m)
                + ' Absolute alarm<br>(Period: '
                + period
                + ') <div data-role="button" data-inline="true">Delete</div></li>';
        } else if (alarmsArray[i] instanceof tizen.AlarmRelative) {
            str += '<li data-id="'
                + alarmsArray[i].id
                + '">'
                + alarmsArray[i].delay
                + ' sec Relative alarm<br>(Period: '
                + period
                + ') <div data-role="button" data-inline="true">Delete</div></li>';
        } else {
            alert("Wrong alarm instance");
            break;
        }
    }
    $("#alarm-all-list").html(str).trigger("create").listview("refresh");
}

function addAlarm(alarm) {
    var arg;
    arg = new tizen.ApplicationControl("http://tizen.org/appcontrol/operation/view",
            null,
            null,
            null,
            [new tizen.ApplicationControlData("id", ["bhvtcalarm.AlarmTest"])]);

    try {
        tizen.alarm.add(alarm, "bhvtcalarm.AlarmTest", arg);
    } catch (e) {
        alert("error: " + e.message);
    }
}

function addAlarmAbsolute() {
    var period = parseInt($("#absolute-alarm-period").prop("value")),
    time = $("#alarm-time").prop("value"),
    year, month, date, hours, minutes, splits, d, t;

    if (time === null || time === "" || period < 0) {
        alert("Getting alarm settings failed");
    }
    else
    {
        splits = time.split("T");
        d = splits[0].split("-");
        t = splits[1].split(":");

        year = parseInt(d[0]);
        month = parseInt(d[1]) - 1;
        date = parseInt(d[2]);
        hours = parseInt(t[0]);
        minutes = parseInt(t[1]);

        var inputDate = new Date(year, month, date, hours, minutes, 0, 0);
        var myAlarm = new tizen.AlarmAbsolute(inputDate, (period > 0 ? period : null));

        addAlarm(myAlarm);
        alert("Absolute Alarm Added");
        displayAlarms();
    }
}

function removeAll() {
    tizen.alarm.removeAll();
    alert("Alarm delete all");
    displayAlarms();
}

function removeAlarm(id) {
    try {
        tizen.alarm.remove(id);
        alert("Alarm delete");
    } catch (e) {
        alert("Alarm remove failed. The once alarm might be already removed automatically");
    }
    displayAlarms();
}

function alarmInfo(id) {
    var alarm = tizen.alarm.get(id);

    if (alarm) {
        if (alarm instanceof tizen.AlarmAbsolute) {
            alert("Next scheduled alarm is " + alarm.getNextScheduledDate());
        } else {
            alert("Remaining seconds is " + alarm.getRemainingSeconds() + " SECS");
        }
    } else {
        alert("Alarm info retrieving failed<br/>This once alarm might be already removed automatically");
        displayAlarms();
    }
}

function install_(url) {
    var onInstallationSuccess = {
            onprogress: function(packageId, percentage)
            {
                console.log("On installation(" + packageId + "): progress(" + percentage + ")");
                document.getElementById("install").innerHTML =  '<div data-role="button" id="install" style="height:40px; line-height:40px;">Installing... ' + percentage + "%" + '</div>';
            },
            oncomplete: function(packageId)
            {
                console.log("Installation(" + packageId + ") Complete");
                document.getElementById("install").innerHTML =  '<div data-role="button" id="install" style="height:40px; line-height:40px;">AlarmTest Install</div>';
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
            install_flag = true;
        },
        onupdated: function(packageInfo) {
            alert("The package " + packageInfo.name + " is updated");
        },
        onuninstalled: function(packageId) {
            alert("The package " + packageId + " is uninstalled");
            install_flag = false;
        }
};

function alarmPre() {
    var documentsDir;
    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            if(files[i].name === "TestAlarm")
            {
                documentsDir.copyTo(
                    files[i].fullPath,
                    "documents/TestAlarm.wgt",
                    false,
                    function() {
                        console.log("Alarm Precondition Success!");
                    });
            }
        }
        fileURI();
    }

    function onerror(error) {
        alert("The error " + error.message + " occurred when listing the files in the selected folder");
    }

    tizen.filesystem.resolve(
        'wgt-package/tests/Alarm/res/',
        function(dir){
            documentsDir = dir;
            dir.listFiles(onsuccess, onerror);
        }, function(e) {
            alert("Error " + e.message);
        }, "r"
    );
}
