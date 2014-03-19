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
        Feng, GangX <gangx.feng@intel.com>

*/

var installUrl;
var wgt_name;
var app_id;
var package_id;
var install_wgt = new Array('test-half-memory');

$(document).ready(function(){
    updateFooterButton();
    DisablePassButton();

    wgt_name = $("#wgt_name").val();
    app_id = $("#app_id").val();
    package_id = $("#package_id").val();

    $("#install").bind("vclick", function() {
        install();
    });
    if(jQuery.inArray(wgt_name, install_wgt) != -1){
        $('#launch').hide();
        $('#launch_divider').hide();
    } else {
        $("#launch").bind("vclick", function() {
            launch(app_id);
            $('#uninstall').removeClass("ui-disabled");
        });
    }
    $("#uninstall").bind("vclick", function() {
        uninstall(package_id);
    });
    try {
        tizen.package.setPackageInfoEventListener(packageEventCallback);
    } catch (e) {
        alert("Exception: " + e.message);
    }

    packagePre(wgt_name);
    $('#uninstall').addClass("ui-disabled");
    $('#launch').addClass("ui-disabled");

    if(checkInstalledPkg(package_id)) {
        $('#install').addClass("ui-disabled");
        if(jQuery.inArray(wgt_name, install_wgt) != -1){
            $('#uninstall').removeClass("ui-disabled");
        } else {
            $('#launch').removeClass("ui-disabled");
        }
    }
});

var packageEventCallback = {
    oninstalled: function(packageInfo) {
        $.mobile.hidePageLoadingMsg();
        alert("The package " + packageInfo.name + " is installed");
    },
    onupdated: function(packageInfo) {
        $.mobile.hidePageLoadingMsg();
        alert("The package " + packageInfo.name + " is updated");
    },
    onuninstalled: function(packageId) {
        $.mobile.hidePageLoadingMsg();
        alert("The package " + packageId + " is uninstalled");
    }
}

function fileURI(wgt_name) {
    var documentsDir;
    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            if(files[i].name == wgt_name+".wgt")
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

function install() {
    var onInstallationSuccess = {
        onprogress: function(packageId, percentage)
        {
            console.log("On installation(" + packageId + "): progress(" + percentage + ")");
            $.mobile.showPageLoadingMsg();
        },
        oncomplete: function(packageId)
        {
            console.log("Installation(" + packageId + ") Complete");
            if(checkInstalledPkg(package_id)) {
                $('#install').addClass("ui-disabled");
                if(jQuery.inArray(wgt_name, install_wgt) != -1){
                    $('#uninstall').removeClass("ui-disabled");
                } else {
                    $('#launch').removeClass("ui-disabled");
                }
            }
        }
    }

    var onError = function (err) {
        alert("Error occured on installation : " + err.message);
        $.mobile.hidePageLoadingMsg();
    }

    try {
        tizen.package.install(installUrl, onInstallationSuccess, onError);
    } catch(e) {
        alert("Exception: " + e.name);
    }
}

function uninstall(package_id) {
    var onUninstallationSuccess = {

            onprogress: function(packageId, percentage)
            {
                console.log("On uninstallation(" + packageId + "): progress(" + percentage + ")");
                $.mobile.showPageLoadingMsg();
            },
            oncomplete: function(packageId)
            {
                console.log("Uninstallation(" + packageId + ") Complete");
                $('#launch').addClass("ui-disabled");
                $('#uninstall').addClass("ui-disabled");
                EnablePassButton();
            }
    }

    var onError = function (err) {
        alert("Error occured on uninstallation : " + err.name);
        $.mobile.hidePageLoadingMsg();
    }

    try {
        tizen.package.uninstall(package_id, onUninstallationSuccess, onError);
    } catch (e) {
        alert("Exception: " + e.name);
    }
}

function launch(app_id) {
    function onSuccess() {
        console.log(id + " launched successfully!");
    }

    function onError(err) {
        alert("launch failed : " + err.message);
    }

    try {
        tizen.application.launch(app_id, onSuccess, onError);
    } catch (exc) {
        alert("launch exc:" + exc.message);
    }
}

function packagePre(wgt_name) {
    var documentsDir;
    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            if(files[i].name == wgt_name+".wgt")
            {
                documentsDir.copyTo(
                    files[i].fullPath,
                    "documents/"+wgt_name+".wgt",
                    true,
                    function() {
                        console.log(wgt_name+" Precondition Success!");
                    });
            }
        }
        fileURI(wgt_name);
    }

    function onerror(error) {
        alert("The error " + error.message + " occurred when listing the files in the selected folder");
    }

    tizen.filesystem.resolve(
        'wgt-package/tests/Stability/res/',
        function(dir){
            documentsDir = dir;
            dir.listFiles(onsuccess, onerror);
        }, function(e) {
            alert("Error" + e.message);
        }, "r"
    );
}

function reportResult(res) {
    var jsonStr="[{\"testname\":\"" + wgt_name + "\",\"result\":\"" + res + "\"}]";
    window.opener.postMessage(jsonStr, '*');
    backAppsHome();
}
