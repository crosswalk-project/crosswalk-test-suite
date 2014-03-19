/*
Copyright (c) 2013 Intel Corporation.

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
        Tan, Shiyou <shiyoux.tan@intel.com>
*/

var installUrl;
$(document).delegate("#main", "pageinit", function() {
    DisablePassButton();

    $("#install").bind("vclick", function() {
        install(installUrl, "install");
    });
    $("#launch1").bind("vclick", function() {
        launch();
       $("#uninstall").removeClass("ui-disabled");
    });
    $("#uninstall").bind("vclick", function() {
        uninstall();
    });
    try {
        tizen.package.setPackageInfoEventListener(packageEventCallback);
    } catch (e) {
        alert("Exception: " + e.message);
    }

    packagePre();
    $("#launch1").addClass("ui-disabled");
    $("#uninstall").addClass("ui-disabled");

    if(checkInstalledPkg("bhdragdrop")) {
        $("#install").addClass("ui-disabled");
        $("#launch1").removeClass("ui-disabled");
    }
});

var packageEventCallback = {
        oninstalled: function(packageInfo) {
            hideProcess();
            alert("The application " + packageInfo.name + " is installed");
        },
        onuninstalled: function(packageId) {
            hideProcess();
            alert("The application DragandDrop is uninstalled");
        }
};

function fileURI() {
    var documentsDir;
    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            if(files[i].name == "DragandDrop.wgt")
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
                alert("Error" + e.message);
            }, "r"
    );
}

function install(url, type) {
    var onInstallationSuccess = {
            onprogress: function(packageId, percentage)
            {
                console.log("On installation(" + packageId + "): progress(" + percentage + ")");
                showProcess();
            },
            oncomplete: function(packageId)
            {
                console.log("Installation(" + packageId + ") Complete");
                if(checkInstalledPkg("bhdragdrop")) {
                    $("#install").addClass("ui-disabled");
                    $("#launch1").removeClass("ui-disabled");
                }
            }
    }

    var onError = function (err) {
        alert("Error occured on installation : " + err.message);
        $.mobile.hidePageLoadingMsg();
    }

    try {
        tizen.package.install(url, onInstallationSuccess, onError);
    } catch(e) {
        alert("Exception: " + e.name);
    }
}

function uninstall() {

    var onUninstallationSuccess = {

            onprogress: function(packageId, percentage)
            {
                showProcess();
                console.log("On uninstallation(" + packageId + "): progress(" + percentage + ")");
            },
            oncomplete: function(packageId)
            {
                console.log("Uninstallation(" + packageId + ") Complete");
                $("#launch1").addClass("ui-disabled");
                $("#uninstall").addClass("ui-disabled");
                EnablePassButton();
            }
    }

    var onError = function (err) {
        alert("Error occured on uninstallation : " + err.name);
        $.mobile.hidePageLoadingMsg();
    }

    try {
        tizen.package.uninstall("bhdragdrop", onUninstallationSuccess, onError);
    } catch (e) {
        alert("Exception: " + e.name);
    }
}

function launch() {
    function onSuccess() {
        console.log(id + " launched successfully!");
    }

    function onError(err) {
        alert("launch failed : DragandDrop application is already uninstalled or not installed");
    }
    try {
        tizen.application.launch("bhdragdrop.DragandDrop", onSuccess, onError);
    } catch (exc) {
        alert("launch exc:" + exc.message);
    }
}

function packagePre() {
    var documentsDir;
    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            if(files[i].name == "DragandDrop")
            {
                documentsDir.copyTo(
                    files[i].fullPath,
                    "documents/DragandDrop.wgt",
                    true,
                    function() {
                        console.log("DragandDrop Precondition Success(2)!");
                    });
            }
        }
        fileURI();
    }

    function onerror(error) {
        alert("The error " + error.message + " occurred when listing the files in the selected folder");
    }

    tizen.filesystem.resolve(
        'wgt-package/tests/DragandDrop/res/',
        function(dir){
            documentsDir = dir;
            dir.listFiles(onsuccess, onerror);
        }, function(e) {
            alert("Error" + e.message);
        }, "r"
    );
}

function hideProcess() {
    $.mobile.hidePageLoadingMsg();
    $("#popup_info-screen").addClass("ui-screen-hidden");
    $("#popup_info-screen").removeClass("in");
}

function showProcess() {
    $.mobile.showPageLoadingMsg();
    $("#popup_info-screen").removeClass("ui-screen-hidden");
    $("#popup_info-screen").addClass("in");
}
