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
var allId=new Array('wrt1wvt006',
                    'wrt1smt007',
                    'wrt1smt008',
                    'wrt1smt009',
                    'wrt1smt010',
                    'UZmPMhuMeO',
                    'ZkMSjQuYt8');

var installedId = new Array();
var resultXML, tests;
var MOUDLE_NAME = "PackageManagement";
var RESULT_FILE_NAME = "tct-behavior-child.pm.result.xml";

$(document).delegate("#main", "pageinit", function() {
    DisablePassButton();
    $("#wgtClean").bind("vclick", function() {
        showTotalBar();
    });
});

function showTotalBar(){
    $.each(allId,function(key,val){
        try {
            var packageInfo = tizen.package.getPackageInfo(val);
        } catch (e) {
            //alert("Exception: " + e.message);
        }
        if(packageInfo != "" && packageInfo != undefined){
            installedId.push(val);
        }
    });
    checkInstalledPackage();
}

function checkInstalledPackage(){
    if(installedId.length > 0){
        setTimeout(function() {
            uninstall(installedId[0]);
        }, 1000);
    } else {
        $.mobile.hidePageLoadingMsg();
        alert("All widgets is uninstalled!");
        if (checkIfAllPackagePass()) {
            EnablePassButton();
        }
    }
}

function checkIfAllPackagePass() {
    var result = true;

    tests.each(function() {
        if ($(this).attr('result') != "PASS") {
            result = false;
        }
    });
    return result;
}

function getPackageInfo(packageId){
    var packageInfo = tizen.package.getPackageInfo(packageId);
    console.log("Current Package ID : " + packageInfo.id);
}

function uninstall(val) {
    installedId.shift();
    var totalBar = Math.floor((allId.length - installedId.length - 1) / allId.length * 100);

    var onUninstallationSuccess = {

        onprogress: function(packageId, percentage)
        {
            console.log("On uninstallation(" + packageId + "): progress(" + percentage + ")");
            $.mobile.showPageLoadingMsg();
        },
        oncomplete: function(packageId)
        {
            console.log("Uninstallation(" + packageId + ") Complete");
            alert("The package " + packageId + " is uninstalled");
            checkInstalledPackage();
        }
    }

    var onError = function (err) {
        $.mobile.hidePageLoadingMsg();
        if (err.name != "UnknownError") {
            alert("Error occured on uninstallation : " + err.name);
        }
    }

    try {
        tizen.package.uninstall(val, onUninstallationSuccess, onError);
    } catch (e) {
        alert("Exception: " + e.name);
    }
}
