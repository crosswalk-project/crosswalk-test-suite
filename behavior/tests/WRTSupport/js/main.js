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
var allId=new Array('wrt3lue021',
                    'wrt3olo022',
                    'wrt3ous027',
                    'wrt3ous125',
                    'wrt3owa028',
                    'wrt3uam046',
                    'wrt3uam047',
                    'wrt3uam048',
                    'wrt5pec002',
                    'wrt5pec120');

var installedId = new Array();
var resultXML, tests;
var MOUDLE_NAME = "WRTSupport";
var RESULT_FILE_NAME = "tct-behavior-child.wrts.result.xml";

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
            console.log("Current Package ID : " + packageInfo.id);
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

function recordResultToXML(test_name, result){
    tests.each(
        function() {
            if($(this).attr('id') == test_name){
                $(this).attr('result', result);
            }
        }
    );
}

function initTests() {
    loadTests();
    window.addEventListener('message', function(e) {
        console.log(e.data);
        var jsonData = eval("(" + e.data + ")");
        if(jsonData.length > 0){
            if(jsonData[0].testname != "" && jsonData[0].result != ""){
                recordResultToXML(jsonData[0].testname, jsonData[0].result);
                updateAppDecoration();
                exportTmpResult();
            }
        }
    }, false);
}

function exportTmpResult() {
    writeFile(RESULT_FILE_NAME, (new XMLSerializer()).serializeToString(resultXML), false);
}

function writeFile(filename, content, need_exit) {
    successCallback = function(fs) {
        fs.write(content);
        fs.close();
        if (need_exit)
            exitTest();
    };

    onsuccess = function(dir) {
        dir.deleteFile(dir.fullPath + "/" + filename);

        file = dir.createFile(filename);
        file.openStream("rw", successCallback, onerror, "UTF-8");
    };

    onerror = function(error) {
        alert("Export result fail: " + error);
    };

    try {
        tizen.filesystem.resolve('documents', onsuccess, onerror, "rw");
    } catch (err) {
        alert("Write file fail: " + err.message);
    }
}

function loadTests() {
    $.ajax({
        async : false,
        type : "GET",
        url : "../../subtestresult.xml",
        dataType : "xml",
        success : function(xml){
            resultXML = xml;
            $(xml).find("set").each(
                function(){
                    if($(this).attr("name") == MOUDLE_NAME){
                        tests = $(this).find("testcase");
                    }
                }
            );
            loadTmpResult();
        }
    });
}

function loadTmpResult(){
    successCallback = function(files) {
        for(var i = 0; i < files.length; i++){
            if (files[i].name == RESULT_FILE_NAME) {
                if (confirm("Continue last test?")) {
                    files[i].readAsText(
                        function(xml){
                            _mergeResult($(xml).find("set"));
                            updateAppDecoration();
                        }, function(err){
                            console.log("read tmp result error: " + err.message);
                        }, "UTF-8"
                    );
                    return;
                }
                else break;
            }
        }
    };

    onsuccess = function(dir) {
        dir.listFiles(successCallback, onerror);
    };

    onerror = function(error) {
        console.log(error);
        updateAppDecoration();
    };

    try {
        tizen.filesystem.resolve('documents', onsuccess, onerror, "rw");
    } catch (err) {
        console.log("Load tmp result fail: " + err.message);
        updateAppDecoration();
    }
}

function _mergeResult(tmpResult) {
    tests.each(
        function(index, item) {
            tmpResult.each(
                function(order1, tmpItem1){
                    if($(tmpItem1).attr("name") == MOUDLE_NAME){
                        $(tmpItem1).find("testcase").each(
                            function(order, tmpItem){
                                if ($(item).attr("id") === $(tmpItem).attr("id")) {
                                    $(item).attr("result", $(tmpItem).attr("result"));
                                }
                            }
                        );
                    }
                }
            );
        }
    );
}

function updateAppDecoration() {
    $(resultXML).find("set").each(
        function(){
            if($(this).attr("name") == MOUDLE_NAME){
                $(this).find("testcase").each(
                    function() {
                        if($(this).attr("result") == "PASS"){
                            $("#"+$(this).attr("id")).find("h2").css("color","green");
                        }else if($(this).attr("result") == "FAIL"){
                            $("#"+$(this).attr("id")).find("h2").css("color","red");
                        }
                    }
                );
            }
        }
    );
    $("#cspList").listview( "refresh" );
}

window.addEventListener('load', initTests, false);
