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
$(document).ready(function() {
    installUrl = "TESTER-HOME-DIR/apps_rw/xwalk/applications/usecaseweb.WebAPIWEBUseCaseTests/samples/Package/res/TestPackage1.wgt";
    updateUrl = "TESTER-HOME-DIR/apps_rw/xwalk/applications/usecaseweb.WebAPIWEBUseCaseTests/samples/Package/res/TestPackage2.wgt";
    try {
        tizen.package.setPackageInfoEventListener(packageEventCallback);
    } catch (e) {
        $("#popup_info").modal(showMessage("error", "Exception: " + e.message));
    }
    //packagePre();
    $("#launch1").attr('disabled', true);
    $("#launch2").attr('disabled', true);
    $("#launch3").attr('disabled', true);
    $("#uninstall").attr('disabled', true);
    $("#update").attr('disabled', true);
});

function installPackage() {
  install(installUrl, "install");
  $("#launch1").attr('disabled', false);
}

function uninstallPackage() {
  uninstall();
  $("#launch3").attr('disabled', false);
  $("#launch2").attr('disabled', true);
}

function updatePackage() {
  install(updateUrl, "update");
  $("#launch2").attr('disabled', false);
  $("#launch1").attr('disabled', true);
}

function launch1Package() {
  launch();
  $("#update").attr('disabled', false);
}

function launch2Package() {
  launch();
  $("#uninstall").attr('disabled', false);
}

function launch3Package() {
  launch();
}

var packageEventCallback = {
        oninstalled: function(packageInfo) {
            $("#popup_info").modal(showMessage("success", "The package " + packageInfo.name + " is installed"));
            flag = true;
        },
        onupdated: function(packageInfo) {
            $("#popup_info").modal(showMessage("success", "The package " + packageInfo.name + " is updated"));
            flag = true;
        },
        onuninstalled: function(packageId) {
            $("#popup_info").modal(showMessage("success", "The package " + packageId + " is uninstalled"));
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

function install(url, type) {
    var onInstallationSuccess = {
            onprogress: function(packageId, percentage)
            {
                console.log("On installation(" + packageId + "): progress(" + percentage + ")");
                if(type == "install")
                    document.getElementById("install").innerHTML =  '<div type="button" class="btn btn-default btn-lg btn-block" id="install">Installing... ' + percentage + "%" + '</div>';
                if(type == "update")
                    document.getElementById("update").innerHTML =  '<div type="button" class="btn btn-default btn-lg btn-block" id="update">Updating... ' + percentage + "%" + '</div>';
            },
            oncomplete: function(packageId)
            {
                console.log("Installation(" + packageId + ") Complete");
                if(type == "install"){
                    document.getElementById("install").innerHTML =  '<div type="button" class="btn btn-default btn-lg btn-block" id="install">TestPackage1 Install</div>';
                    $("#install").attr('disabled', true);
                }
                if(type == "update") {
                    document.getElementById("update").innerHTML =  '<div type="button" class="btn btn-default btn-lg btn-block" id="update">TestPackage2 Update</div>';
                    $("#update").attr('disabled', true);
                }
            }
    }

    var onError = function (err) {
        $("#popup_info").modal(showMessage("error", "Error occured on installation : " + err.name));
    }

    try {
        tizen.package.install(url, onInstallationSuccess, onError);
    } catch (e) {
        $("#popup_info").modal(showMessage("error", "Exception: " + e.name));
    }
}

function uninstall() {
    var onUninstallationSuccess = {
            onprogress: function(packageId, percentage)
            {
                console.log("On uninstallation(" + packageId + "): progress(" + percentage + ")");
                document.getElementById("uninstall").innerHTML =  '<div type="button" class="btn btn-default btn-lg btn-block" id="uninstall">UnInstalling... ' + percentage + "%" + '</div>';
            },
            oncomplete: function(packageId)
            {
                console.log("Uninstallation(" + packageId + ") Complete");
                document.getElementById("uninstall").innerHTML =  '<div type="button" class="btn btn-default btn-lg btn-block" id="uninstall">TestPackage UnInstall</div>';
            }
    }

    var onError = function (err) {
        $("#popup_info").modal(showMessage("error", "Error occured on installation : " + err.name));
    }

    try {
        if(flag == false)
            $("#popup_info").modal(showMessage("error", "TestPackage is already Uninstalled or not Installed"));
        else
            tizen.package.uninstall("bhvtcpacka", onUninstallationSuccess, onError);
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
        tizen.application.launch("bhvtcpacka.TestPackage", onSuccess, onError);
    } catch (exc) {
        $("#popup_info").modal(showMessage("error", "launch exc:" + exc.message));
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
        $("#popup_info").modal(showMessage("error", "The error " + error.message + " occurred when listing the files in the selected folder"));
    }
    // FIXME(babu): https://crosswalk-project.org/jira/browse/XWALK-2564
    /*tizen.filesystem.resolve(
        'wgt-package/samples/Package/res/',
        function(dir){
            documentsDir = dir;
            dir.listFiles(onsuccess, onerror);
        }, function(e) {
            alert("Error " + e.message);
        }, "r"
    );*/
}
