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
        Wang, Jing J <jing.j.wang@intel.com>
        Fan, Yugang <yugang.fan@intel.com>

*/

var _appURL;
var _resultXML;
var Tests;
var caps;
//var accMarks = {}; //Re-enter popup
var noSupport = {};
var resultFile = "webapi-sanityapp-tizen-tests_" + getCurrentTime() + ".result.xml";
var tmpResultFile = "webapi-sanityapp-tizen-tests.tmpresult.xml";
var isLaunching = false;

function checkTizen(){
    if (typeof(tizen) == 'undefined')
        return false;
    else
        return true;
}

function updateToolTitle() {
    var version = '';
    $.ajax({
        async : false,
        type : "GET",
        url : "config.xml",
        dataType : "xml",
        success : function(xml){
            $(xml).find("widget").each(
                function(){
                    if ($(this).attr('version'))
                        version = $(this).attr('version');
                }
            );
        }
    });

    $("#tool_title").empty().append("<h1 style=\"width:75%; margin-left:auto; margin-right:auto;\">WebAPI Sanity Test Tool</h1><a class=\"ui-btn-right\">" + version + "</a>");
}

function launchApp() {
    window.open(_appURL);
    $.mobile.hidePageLoadingMsg();
    $('#overlay').remove();
}

function runApp(url) {
    if (isLaunching){
        setTimeout(function(){isLaunching = false;}, 200);
        return;
    }
/*  Re-enter popup
    if (accMarks[url] == 1)
        url += "?reenter";
    else
        accMarks[url] = 1;
*/
    isLaunching = true;
    _appURL = url;
    $.mobile.showPageLoadingMsg();
    $('<div></div>').prependTo('body').attr('id', 'overlay');
    _timer = setTimeout(launchApp, 200);
}

function updateAppDecorationStyle() {
    $(".ui-content").css("padding", '6px');
    $("a.ui-link-inherit").css("padding", '0px 85px 0px 10px');
    $(".ui-li-has-thumb a.ui-link-inherit").css("padding-left", '40px');
    $(".ui-li-heading").css("font-size", '14px');
}

function updateAppDecoration() {
    $("#mylist").empty();
    $(_resultXML).find("set").each(
        function(){
            $("#mylist").append("<li data-role=\"list-divider\" role=\"heading\">"+$(this).attr("name")+"</li>");
            $(this).find("testcase").each(
                function(){
                     var url = "tests/" + $(this).attr("id") + "/index.html?test_name="+$(this).attr("purpose");
                     var appLine = "<li id=\"" + $(this).attr("id") + "\" class=\"test_app\">" +
                           "<a href=\"javascript:runApp('" + url + "')\">" +
                           "<h1>" + $(this).attr("purpose") + "</h1></a></li>";
                     $("#mylist").append(appLine);
                     if($(this).attr("result") == "PASS"){
                         $("#mylist > li :last").find("a").append("<img src='css/images/pass.png' class='ui-li-thumb'>");
                         $("#mylist > li :last").find("a").append("<span class='ui-li-count' style='color:green;'>" +
                             "PASS" + "</span>");
                         $("#mylist > li :last").attr('data-theme', 'g');
                     } else if($(this).attr("result") == "FAIL"){
                         $("#mylist > li :last").find("a").append("<img src='css/images/fail.png' class='ui-li-thumb'>");
                         $("#mylist > li :last").find("a").append("<span class='ui-li-count' style='color:red;'>" +
                             "FAIL" + "</span>");
                         $("#mylist > li :last").attr('data-theme', 'r');
                     }
                     if (noSupport[$(this).attr("id")]) {
                        $("#mylist > li :last").find("a").attr('href', '');
                        $("#mylist > li :last").attr('data-theme', 'a');
                        $("#mylist > li :last").find("a").append("<span class='ui-li-count' style='color:black;'>" +
                             "UNSUPPORTED" + "</span>");
                     }
                }
            );
        }
    );
    $("#mylist").listview( "refresh" );
    updateAppDecorationStyle();
}

function exportResult() {
    writeFile(resultFile, (new XMLSerializer()).serializeToString(_resultXML), false);
}

function exportTmpResult() {
    writeFile(tmpResultFile, (new XMLSerializer()).serializeToString(_resultXML), false);
}

function resetResult() {
    _resetResult();
    updateAppDecoration();
    isLaunching = false;
}

function _resetResult() {
    Tests.each(
        function() {
            var testAppname = $(this).attr("id");
            var isCappresent = true;
            $(this).find("capability").each(function(){
                isCappresent = isCapPresent($(this).attr("name"));
                if (isCappresent === false)
                    return false;
            });
            if (isCappresent === false) {
                noSupport[testAppname] = true;
                $(this).attr("result", "UNSUPPORTED");
            } else {
                $(this).attr("result", "N/A");
            }

        }
    );
}

function exitTest(){
    try {
        var app = tizen.application.getCurrentApplication();
        app.exit();
    } catch(err) {
        closeWindow();
    }
}

function closeWindow() {
    window.open('', '_self', '');
    window.close();
}

function getCurrentTime() {
    var d = new Date();
    return d.toISOString();
}

function removeUnsupportedFeature(content) {
    var xml = content;
    var pos, before, after, posBefore, posAfter;

    pos = xml.indexOf('result="UNSUPPORTED"');
    while (pos != -1)
    {
        before = xml.substring(0, pos);
        after = xml.substring(pos);
        posBefore = before.lastIndexOf("<testcase");
        posAfter = after.indexOf("<testcase");
        if (posAfter == -1) {
            posAfter = after.indexOf("</set>");
        }
        xml = before.substring(0, posBefore) + after.substring(posAfter);
        pos = xml.indexOf('result="UNSUPPORTED"');
    }

    return xml;
}

function writeFile(filename, content, need_exit) {
    successCallback = function(fs) {
        fs.write(removeUnsupportedFeature(content.replace("testcase.xsl", "testresult.xsl")));
        fs.close();

        if (filename == resultFile)
            alert("Export result to " + resultFile + " successfully.");

        if (need_exit)
            exitTest();
    };


    onsuccess = function(dir) {
        dir.deleteFile(dir.fullPath + "/webapi-sanityapp-tizen-tests/" + filename);

        file = dir.createFile("webapi-sanityapp-tizen-tests/" + filename);
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

function SaveAndExit() {
    writeFile(resultFile, (new XMLSerializer()).serializeToString(_resultXML), true);
}

function updateBar() {
    $(':jqmData(role=header)').removeClass("slidedown");
    $(':jqmData(role=footer)').removeClass("slideup");
    $(':jqmData(role=footer)').attr("align", "center");
    $(':jqmData(role=footer)').find(':jqmData(role=button) > span:first-child').css('padding', '15px 20px 15px 40px');
}

function loadTests() {
    $.ajax({
        async : false,
        type : "GET",
        url : "./tests.xml",
        dataType : "xml",
        success : function(xml){
            _resultXML = xml;
            Tests = $(xml).find("testcase");
            getSummary();
            getCapPresent();
            loadTmpResult();
        }
    });
}

function loadTmpResult(){
    successCallback = function(files) {
        for(var i = 0; i < files.length; i++)
            if (files[i].name == tmpResultFile) {
                if (confirm("Continue last test?")) {
                    files[i].readAsText(
                        function(xml){
                            _mergeResult($(xml).find("testcase"));
                            updateAppDecoration();
                        }, function(err){
                            console.log("read tmp result error: " + err.message);
                        }, "UTF-8"
                    );
                    return;
                }
                else break;
            }
        _resetResult();
        updateAppDecoration();
    };

    onsuccess = function(dir) {
        dir.listFiles(successCallback, onerror);
    };

    onerror = function(error) {
        console.log(error);
        updateAppDecoration();
    };

    try {
        tizen.filesystem.resolve('documents/webapi-sanityapp-tizen-tests', onsuccess, onerror, "rw");
    } catch (err) {
        console.log("Load tmp result fail: " + err.message);
        updateAppDecoration();
    }
}

function _mergeResult(tmpResult) {
    Tests.each(
        function(index, item) {
            tmpResult.each(
                function(order, tmpItem) {
                    if ($(item).attr("id") === $(tmpItem).attr("id")) {
                        $(item).attr("result", $(tmpItem).attr("result"));
                        return false;
                    }
                }
            );
            var testAppname = $(this).attr("id");
            var isCappresent = true;
            $(this).find("capability").each(function(){
                isCappresent = isCapPresent($(this).attr("name"));
                if (isCappresent === false)
                    return false;
            });
            if(isCappresent === false){
                noSupport[testAppname] = true;
            }
        }
    );
}

function recordResultToXML(test_name, result){
    Tests.each(
        function() {
            if($(this).attr('id') == test_name){
                $(this).attr('result', result)
            }
        }
    );
}

function initTests() {
    updateBar();
    loadTests();
    window.addEventListener('message', function(e) {
        console.log(e.data);
        var jsonData = eval("(" + e.data + ")");
        if(jsonData.length > 0){
            if(jsonData[0].testname != "" && jsonData[0].result == ""){
                isLaunching = false;
            } else {
                recordResultToXML(jsonData[0].testname, jsonData[0].result);
                updateAppDecoration();
                exportTmpResult();
            }
        }
    }, false);
}

function getSummary() {

    if (!checkTizen())
        return;

    var summaryXML = "";

    if (tizen.systeminfo == 'undefined') {
        return;
    } else {
        summaryXML += "<capabilities>";
        var caps = tizen.systeminfo.getCapabilities();
        for (x in caps) {
            if (typeof(caps[x]) == "boolean")
                summaryXML += "    <capability name=\"" + x + "\" support=\"" + caps[x] + "\" type=\"boolean\"/>\r\n";
            else {
                if (typeof(caps[x]) == "number")
                    summaryXML += "    <capability name=\"" + x + "\" support=\"true\" type=\"Integer\">\r\n";
                else if (typeof(caps[x]) == "string")
                    summaryXML += "    <capability name=\"" + x + "\" support=\"true\" type=\"String\">\r\n";
                else
                    summaryXML += "    <capability name=\"" + x + "\" support=\"true\" type=\"" + typeof(caps[x]) + "\">\r\n";
                summaryXML += "        <value>" + caps[x] + "</value>\r\n";
                summaryXML += "    </capability>\r\n";
            }
        }
        summaryXML += "</capabilities>";
    }
    var summaryDoc = $.parseXML(summaryXML);
    var testDef = $(_resultXML).find("test_definition");
    $(testDef[0]).prepend(summaryDoc.documentElement);
}

function getCapPresent() {
    try {
        caps = tizen.systeminfo.getCapabilities();
    } catch (err){
        alert("Exception: " + err.message);
    }
}

function isCapPresent(name) {
    if ((caps != undefined) && (caps[name] != undefined)) {
        if (typeof(caps[name]) == "boolean")
            return caps[name];
        else
            return true;
    }
    else
        return false;
}

window.addEventListener('load', initTests, false);
