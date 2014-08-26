/*
Copyright (c) 2013 Intel Corporation.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of works must retain the original copyright notice, this list
  of conditions and the following disclaimer.sandbox
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
        Hao, Yunfei <yunfeix.hao@intel.com>

*/
var installUrl1;
var installUrl2;

$(document).delegate("#main", "pageinit", function() {
    DisablePassButton();

    $("#install1").bind("vclick", function() {
        install(installUrl1, "install1");
    });
    $("#install2").bind("vclick", function() {
        install(installUrl2, "install2");
    });
    $("#launch1").bind("vclick", function() {
        launch("app-control1");
        if(checkInstalledPkg("apcontrol2")) {
            $("#install2").addClass("ui-disabled");
            $("#launch2").removeClass("ui-disabled");
        } else {
            $("#install2").removeClass("ui-disabled");
        }
    });
    $("#launch2").bind("vclick", function() {
        launch("app-control2");
        $("#uninstall").removeClass("ui-disabled");
    });
    $("#uninstall").bind("vclick", function() {
        ["apcontrol1", "apcontrol2"].forEach(function(package_id) {
            if(checkInstalledPkg(package_id)) {
                setTimeout(function() {
                    uninstall(package_id);
                }, 1000);
            }
        });
    });
    try {
        tizen.package.setPackageInfoEventListener(packageEventCallback);
    } catch (e) {
        alert("Exception: " + e.message);
    }
    packagePre();
    $("#launch1").addClass("ui-disabled");
    $("#launch2").addClass("ui-disabled");
    $("#install2").addClass("ui-disabled");
    $("#uninstall").addClass("ui-disabled");

    if(checkInstalledPkg("apcontrol1")) {
        $("#install1").addClass("ui-disabled");
        $("#launch1").removeClass("ui-disabled");
    }
});

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

function fileURI() {
    var documentsDir;
    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            if(files[i].name == "app_control_custom_wgt.wgt")
            {
                var Url1 = files[i].toURI();
                installUrl1 = Url1.replace("file:///", "/");
            }
            if(files[i].name == "app_control_regular_wgt.wgt")
            {
                var Url2 = files[i].toURI();
                installUrl2 = Url2.replace("file:///", "/");
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
            alert("Error" + e.message);
        }, "r"
    );
}

function install(url, type) {

    var onInstallationSuccess = {
        onprogress: function(packageId, percentage)
        {
            console.log("On installation(" + packageId + "): progress(" + percentage + ")");
            if(type == "install1") {
                $("#install1").html('<div data-role="button" id="install1" style="height:40px; line-height:40px;">Installing... ' + percentage + "%" + '</div>');
            }
            if(type == "install2") {
                $("#install2").html('<div data-role="button" id="install2" style="height:40px; line-height:40px;">Installing... ' + percentage + "%" + '</div>');
            }
        },
        oncomplete: function(packageId)
        {
            console.log("Installation(" + packageId + ") Complete");
            if(type == "install1") {
                $("#install1").addClass("ui-disabled");
                $("#launch1").removeClass("ui-disabled");
                $("#install1").html('<div data-role="button" id="install1" style="height:40px; line-height:40px;">Install</div>');
            }
            if(type == "install2") {
                $("#install2").addClass("ui-disabled");
                $("#launch2").removeClass("ui-disabled");
                $("#install2").html('<div data-role="button" id="install2" style="height:40px; line-height:40px;">Install</div>');
            }
        }
    }

    var onError = function (err) {
        if (err.name != "UnknownError") {
            alert("Error occured on installation : " + err.name);
        }
    }

    try {
        tizen.package.install(url, onInstallationSuccess, onError);
    } catch(e) {
        alert("Exception: " + e.name);
    }
}

function uninstall(package_id) {

    var onUninstallationSuccess = {
        onprogress: function(packageId, percentage)
        {
            console.log("On uninstallation(" + packageId + "): progress(" + percentage + ")");
        },
        oncomplete: function(packageId)
        {
            console.log("Uninstallation(" + packageId + ") Complete");
            if(packageId == "apcontrol1") {
                $("#launch1").addClass("ui-disabled");
            }
            if(packageId == "apcontrol2") {
                $("#launch2").addClass("ui-disabled");
                $("#uninstall").addClass("ui-disabled");
                EnablePassButton();
            }
        }
    }

    var onError = function (err) {
        if (err.name != "UnknownError") {
            alert("Error occured on uninstallation : " + err.name);
        }
    }

    try {
        tizen.package.uninstall(package_id, onUninstallationSuccess, onError);
    } catch (e) {
        alert("Exception: " + e.name);
    }
}

function launch(option) {
    function onSuccess() {
        console.log(id + " launched successfully!");
    }

    function onError(err) {
        alert("launch failed : " + err.message);
    }

    try {
        if (option == "app-control1"){
            var control;
            var APP_CONTROL_OPERATION="http://tizen.org/appcontrol/operation/appControl1_c";
            control = new tizen.ApplicationControl(APP_CONTROL_OPERATION, null, null, null, null);
            tizen.application.launchAppControl(control, null, onSuccess, onError, null);
        }else if (option == "app-control2"){
            var control;
            var APP_CONTROL_OPERATION="http://tizen.org/appcontrol/operation/appControl2_c";
            control = new tizen.ApplicationControl(APP_CONTROL_OPERATION, null, null, null, null);
            tizen.application.launchAppControl(control, "apcontrol2.AppcontrolRegularWgt", onSuccess, onError, null);
        }
    } catch (exc) {
        alert("launch exc:" + exc.message);
    }
}

function packagePre() {
    var documentsDir;
    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            if(files[i].name == "app_control_custom_wgt")
            {
                documentsDir.copyTo(
                    files[i].fullPath,
                    "documents/app_control_custom_wgt.wgt",
                    true,
                    function() {
                        console.log("app_control_custom_wgt Precondition Success(1)!");
                    });
            }
            if(files[i].name == "app_control_regular_wgt")
            {
                documentsDir.copyTo(
                    files[i].fullPath,
                    "documents/app_control_regular_wgt.wgt",
                    true,
                    function() {
                        console.log("app_control_regular_wgt Precondition Success(2)!");
                    });
            }
        }
        fileURI();
    }

    function onerror(error) {
        alert("The error " + error.message + " occurred when listing the files in the selected folder");
    }

    tizen.filesystem.resolve(
        'wgt-package/tests/AppControlExtending/res/',
        function(dir){
            documentsDir = dir;
            dir.listFiles(onsuccess, onerror);
        }, function(e) {
            alert("Error" + e.message);
        }, "r"
    );
}
