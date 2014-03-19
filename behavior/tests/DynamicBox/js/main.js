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
var installUrl;
var install_number = 0;
var uninstall_number = 0;
var launch_tpk = "";
var wgt_names = new Array('app-widget-mouse-event-false.wgt',
                          'app-widget-sample.wgt',
                          'app-widget-box-appwidgetready-event.wgt',
                          'app-widget-mouse-event-true.wgt',
                          'app-widget-load-event.wgt',
                          'app-widget-visibility-event.wgt',
                          'app-widget-box-size-decoration.wgt',
                          'app-widget-box-size-preview.wgt');

var package_ids = new Array('wrt6awi014',
                            'wrt6app001',
                            'wrt6awb006',
                            'wrt6awi013',
                            'wrt6aws016',
                            'wrt6aws018',
                            'wrt6awb003',
                            'wrt6awb005');

var id_maps = {'rMLtTXzQr2-2.0.0-arm.tpk':                'rMLtTXzQr2',
               'SD2nFxbyeA-2.0.0-i386.tpk':               'SD2nFxbyeA',
               'app-widget-mouse-event-false.wgt':        'wrt6awi014',
               'app-widget-sample.wgt':                   'wrt6app001',
               'app-widget-box-appwidgetready-event.wgt': 'wrt6awb006',
               'app-widget-mouse-event-true.wgt':         'wrt6awi013',
               'app-widget-load-event.wgt':               'wrt6aws016',
               'app-widget-visibility-event.wgt':         'wrt6aws018',
               'app-widget-box-size-decoration.wgt':      'wrt6awb003',
               'app-widget-box-size-preview.wgt':         'wrt6awb005'};

$(document).delegate("#main", "pageinit", function() {
    DisablePassButton();

    $("#install").bind("vclick", function() {
        install();
    });
    $("#launch").bind("vclick", function() {
        launch(launch_tpk);
        $("#uninstall").removeClass("ui-disabled");
    });
    $("#uninstall").bind("vclick", function() {
        uninstall(package_ids[uninstall_number]);
    });
    try {
        tizen.package.setPackageInfoEventListener(packageEventCallback);
    } catch (e) {
        alert("Exception: " + e.message);
    }
    gettpkInfoByPlatForm();
    packagePre(wgt_names[install_number]);

    $("#launch").addClass("ui-disabled");
    $("#uninstall").addClass("ui-disabled");
});

var packageEventCallback = {
        oninstalled: function(packageInfo) {
            $.mobile.loading('hide');
            alert("The package " + packageInfo.name + " is installed");
        },
        onupdated: function(packageInfo) {
            $.mobile.loading('hide');
            alert("The package " + packageInfo.name + " is updated");
        },
        onuninstalled: function(packageId) {
            $.mobile.loading('hide');
            alert("The package " + packageId + " is uninstalled");
        }
};

function gettpkInfoByPlatForm(){
    var deviceCapabilities = tizen.systeminfo.getCapabilities();
    if(deviceCapabilities.platformCoreCpuArch=="armv7"){
        wgt_names.unshift("rMLtTXzQr2-2.0.0-arm.tpk");
        package_ids.unshift("rMLtTXzQr2");
        launch_tpk = "rMLtTXzQr2.DBV";
    }else if(deviceCapabilities.platformCoreCpuArch=="x86"){
        wgt_names.unshift("SD2nFxbyeA-2.0.0-i386.tpk");
        package_ids.unshift("SD2nFxbyeA");
        launch_tpk = "SD2nFxbyeA.DBV";
    }
}

function fileURI(wgt_name) {
    var documentsDir;

    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            if(files[i].name == wgt_name)
            {
                var Url = files[i].toURI();
                installUrl = Url.replace("file:///", "/");
                if(install_number != 0){
                    install();
                }
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

function checkWgtName(filePath) {
    var name = "";
    wgt_names.forEach(function (wgt_name) {
        if (filePath.indexOf(wgt_name) != -1) {
            name = wgt_name;
        }
    });

    return name;
}

function install() {
    var totalBar = Math.floor(install_number / wgt_names.length * 100);
    var onInstallationSuccess = {
        onprogress: function(packageId, percentage)
        {
            console.log("On installation(" + packageId + "): progress(" + percentage + ")");
            $.mobile.loading('show', {
                text: 'Installing...' + totalBar + '%',
                textVisible: true,
                theme: 'a',
                textonly: false,
                html: ""
            });
        },
        oncomplete: function(packageId)
        {
            console.log("Installation(" + packageId + ") Complete");
            install_number++;
            if(install_number < wgt_names.length){
                setTimeout(function() {
                    packagePre(wgt_names[install_number]);
                }, 500);
            }else{
                install_number = 0;
                $.mobile.loading('hide');
                alert("All widgets is installed!");
                $("#launch").removeClass("ui-disabled");
            }
        }
    }

    var onError = function (err) {
        $.mobile.loading('hide');
        if (err.name != "UnknownError") {
            alert("Error occured on installation : " + err.name);
        }
        if (install_number < package_ids.length) {
            $("#install").removeClass("ui-disabled");
        }
    }

    $("#install").addClass("ui-disabled");
    try {
        var wgt_name = checkWgtName(installUrl);
        if (wgt_name && checkInstalledPkg(id_maps[wgt_name])) {
            install_number++;
            if(install_number < wgt_names.length){
                packagePre(wgt_names[install_number]);
            } else {
                install_number = 0;
                $.mobile.loading('hide');
                alert("All widgets is installed!");
                $("#install").addClass("ui-disabled");
                $("#launch").removeClass("ui-disabled");
            }
        } else {
            tizen.package.install(installUrl, onInstallationSuccess, onError);
        }
    } catch (e) {
        alert("Exception: " + e.name);
    }
}

function uninstall(package_id) {
    var totalBar = Math.floor(uninstall_number / package_ids.length * 100);
    var onUninstallationSuccess = {

        onprogress: function(packageId, percentage)
        {
            console.log("On uninstallation(" + packageId + "): progress(" + percentage + ")");
            $.mobile.loading('show', {
                text: 'Uninstalling...' + totalBar + '%',
                textVisible: true,
                theme: 'a',
                textonly: false,
                html: ""
            });
        },
        oncomplete: function(packageId)
        {
            console.log("Uninstallation(" + packageId + ") Complete");
            uninstall_number++;
            if(uninstall_number < package_ids.length){
                setTimeout(function() {
                    uninstall(package_ids[uninstall_number]);
                }, 1000);
            }else{
                uninstall_number = 0;
                $.mobile.loading('hide');
                alert("All widgets is uninstalled!");
                EnablePassButton();
            }
        }
    }

    var onError = function (err) {
        $.mobile.loading('hide');
        if (err.name != "UnknownError") {
            alert("Error occured on uninstallation : " + err.name);
        }
        if (uninstall_number < package_ids.length) {
            $("#uninstall").removeClass("ui-disabled");
        }
    }

    $("#launch").addClass("ui-disabled");
    $("#uninstall").addClass("ui-disabled");
    try {
        tizen.package.uninstall(package_id, onUninstallationSuccess, onError);
    } catch (e) {
        alert("Exception: " + e.name);
    }
}

function launch(launch_tpk) {
    function onSuccess() {
        console.log(id + " launched successfully!");
    }

    function onError(err) {
        $.mobile.loading('hide');
        alert("launch failed : " + err.message);
    }
    try {
        tizen.application.launch(launch_tpk, onSuccess, onError);
    } catch (exc) {
        alert("launch exc:" + exc.message);
    }
}

function packagePre(wgt_name) {
    var documentsDir;
    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            if(files[i].name == wgt_name)
            {
                documentsDir.copyTo(
                    files[i].fullPath,
                    "documents/" + wgt_name,
                    true,
                    function() {
                        console.log(wgt_name + " Precondition Success(1)!");
                    });
            }
        }
        fileURI(wgt_name);
    }

    function onerror(error) {
        alert("The error " + error.message + " occurred when listing the files in the selected folder");
    }

    tizen.filesystem.resolve(
        'wgt-package/tests/DynamicBox/res/',
        function(dir){
            documentsDir = dir;
            dir.listFiles(onsuccess, onerror);
        }, function(e) {
            alert("Error" + e.message);
        }, "r"
    );
}
