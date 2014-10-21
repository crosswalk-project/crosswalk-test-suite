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

var installUrl, updateUrl;
var flag = false;
$(document).delegate("#main", "pageinit", function() {
    $("#install").bind("vclick", function() {
        install(installUrl, "install");
        $("#launch1").removeClass("ui-disabled");
    });
    $("#uninstall").bind("vclick", function() {
        uninstall();
        $("#launch3").removeClass("ui-disabled");
        $("#launch2").addClass("ui-disabled");
    });
    $("#update").bind("vclick", function() {
        install(updateUrl, "update");
        $("#launch2").removeClass("ui-disabled");
        $("#launch1").addClass("ui-disabled");
    });
    $("#launch1").bind("vclick", function() {
        launch();
        $("#update").removeClass("ui-disabled");
    });
    $("#launch2").bind("vclick", function() {
        launch();
        $("#uninstall").removeClass("ui-disabled");
    });
    $("#launch3").bind("vclick", function() {
        launch();
    });
    try {
        tizen.package.setPackageInfoEventListener(packageEventCallback);
    } catch (e) {
        alert("Exception: " + e.message);
    }
    packagePre();
    $("#launch1").addClass("ui-disabled");
    $("#launch2").addClass("ui-disabled");
    $("#launch3").addClass("ui-disabled");
    $("#uninstall").addClass("ui-disabled");
    $("#update").addClass("ui-disabled");
});

var packageEventCallback = {
        oninstalled: function(packageInfo) {
            alert("The package " + packageInfo.name + " is installed");
            flag = true;
        },
        onupdated: function(packageInfo) {
            alert("The package " + packageInfo.name + " is updated");
            flag = true;
        },
        onuninstalled: function(packageId) {
            alert("The package " + packageId + " is uninstalled");
            flag = false;
        }
};

function fileURI() {
    var documentsDir;
    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            if(files[i].name == "TestPackage1.wgt")
            {
                var Url1 = files[i].toURI();
                installUrl = Url1.replace("file:///", "/");
            }
            if(files[i].name == "TestPackage2.wgt")
            {
                var Url2 = files[i].toURI();
                updateUrl = Url2.replace("file:///", "/");
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

function install(url, type) {
    var onInstallationSuccess = {
            onprogress: function(packageId, percentage)
            {
                console.log("On installation(" + packageId + "): progress(" + percentage + ")");
                if(type == "install")
                    document.getElementById("install").innerHTML =  '<div data-role="button" id="install" style="height:40px; line-height:40px;">Installing... ' + percentage + "%" + '</div>';
                if(type == "update")
                    document.getElementById("update").innerHTML =  '<div data-role="button" id="update" style="height:40px; line-height:40px;">Updating... ' + percentage + "%" + '</div>';
            },
            oncomplete: function(packageId)
            {
                console.log("Installation(" + packageId + ") Complete");
                if(type == "install"){
                    document.getElementById("install").innerHTML =  '<div data-role="button" id="install" style="height:40px; line-height:40px;">TestPackage1 Install</div>';
                    $("#install").addClass("ui-disabled");
                }
                if(type == "update") {
                    document.getElementById("update").innerHTML =  '<div data-role="button" id="update" style="height:40px; line-height:40px;">TestPackage2 Update</div>';
                    $("#update").addClass("ui-disabled");
                }
            }
    }

    var onError = function (err) {
        alert("Error occured on installation : " + err.name);
    }

    try {
        tizen.package.install(url, onInstallationSuccess, onError);
    } catch (e) {
        alert("Exception: " + e.name);
    }
}

function uninstall() {
    var onUninstallationSuccess = {
            onprogress: function(packageId, percentage)
            {
                console.log("On uninstallation(" + packageId + "): progress(" + percentage + ")");
                document.getElementById("uninstall").innerHTML =  '<div data-role="button" id="uninstall" style="height:40px; line-height:40px;">UnInstalling... ' + percentage + "%" + '</div>';
            },
            oncomplete: function(packageId)
            {
                console.log("Uninstallation(" + packageId + ") Complete");
                document.getElementById("uninstall").innerHTML =  '<div data-role="button" id="uninstall" style="height:40px; line-height:40px;">TestPackage UnInstall</div>';
            }
    }

    var onError = function (err) {
        alert("Error occured on installation : " + err.name);
    }

    try {
        if(flag == false)
            alert("TestPackage is already Uninstalled or not Installed");
        else
            tizen.package.uninstall("bhvtcpacka", onUninstallationSuccess, onError);
    } catch (e) {
        alert("Exception: " + e.name);
    }
}

function launch() {
    function onSuccess() {
        console.log("Application launched successfully");
    }

    function onError(err) {
        alert("launch failed : " + err.message);
    }

    try {
        tizen.application.launch("bhvtcpacka.TestPackage", onSuccess, onError);
    } catch (exc) {
        alert("launch exc:" + exc.message);
    }
}

function packagePre() {
    var documentsDir;
    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            if(files[i].name == "TestPackage2")
            {
                documentsDir.copyTo(
                    files[i].fullPath,
                    "documents/TestPackage2.wgt",
                    true,
                    function() {
                        console.log("Package Precondition Success(1)!");
                    });
            }
            if(files[i].name == "TestPackage1")
            {
                documentsDir.copyTo(
                    files[i].fullPath,
                    "documents/TestPackage1.wgt",
                    true,
                    function() {
                        console.log("Package Precondition Success(2)!");
                    });
            }
        }
        fileURI();
    }

    function onerror(error) {
        alert("The error " + error.message + " occurred when listing the files in the selected folder");
    }

    tizen.filesystem.resolve(
        'wgt-package/samples/Package/res/',
        function(dir){
            documentsDir = dir;
            dir.listFiles(onsuccess, onerror);
        }, function(e) {
            alert("Error " + e.message);
        }, "r"
    );
}
