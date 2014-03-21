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
        Li, Hao <haox.li@intel.com>
        Fan, Yugang <yugang.fan@intel.com>

*/

function EnablePassButton(){
    $('#pass_button').removeClass("ui-disabled");
}

function DisablePassButton(){
    $('#pass_button').addClass("ui-disabled");
}

function getAppName() {
    var lpath = window.location.pathname;
    var from = lpath.lastIndexOf("tests/") + 6;
    var to = lpath.lastIndexOf("/");
    return lpath.substring(from, to);
}

function backAppsHome() {
    window.close();
}

function reportResult(res) {
    var jsonStr="[{\"testname\":\""+getAppName()+"\",\"result\":\""+res+"\"}]";
    window.opener.postMessage(jsonStr, '*');
    backAppsHome();
}

function testLaunching(){
    var jsonStr="[{\"testname\":\""+getAppName()+"\",\"result\":\"\"}]";
    window.opener.postMessage(jsonStr, '*');
}

function updateFooterButton(){
    var footbar = $(':jqmData(role=footer)');
    footbar.empty();
    footbar.attr("align", "center");
    footbar.append("<div data-role=\"controlgroup\" data-type=\"horizontal\">" +
        "<a href=\"javascript:reportResult('PASS');\" id=\"pass_button\" data-role=\"button\" data-icon=\"check\" style=\"color: green\">Pass</a>" +
        "<a href=\"javascript:reportResult('FAIL');\" id=\"fail_button\" data-role=\"button\" data-icon=\"delete\" style=\"color: red\">Fail</a>" +
        "<a href=\"#popup_info\" data-role=\"button\" data-icon=\"info\" data-rel=\"popup\" data-transition=\"pop\">Info</a>" +
        "<a href=\"javascript:backAppsHome();\" data-role=\"button\" data-icon=\"home\">Back</a></div>");

    footbar.trigger("create");
    footbar.find(':jqmData(role=button) > span:first-child').css('padding', '15px 10px 15px 30px');
    $("#popup_info").popup( "option", "theme", "a");
    var maxHeight = $(window).height() - 100 + "px";
    $("#popup_info").css("max-height", maxHeight);
    $("#popup_info").css("margin-bottom", "30px");
    $("#popup_info").css("overflow-y", "auto");
}

$(document).bind('pagecreate', updateFooterButton);

function Parm(data, name) {
    var p;
    ts = $(data).find(name);
    if (ts) {
        t = $(ts).get(0);
        if (t)
            p = $(t).text().trim();
    }

    if (p) {
        var rawVal = decodeURI(p);
        if (rawVal.indexOf(',') < 0)
            p = rawVal;
        else
            p = rawVal.split(',');
    }

    return p;
}

function getParms() {
    var parms = new Array();
    var str = location.search.substring(1);
    var items = str.split('&');
    for ( var i = 0; i < items.length; i++) {
        var pos = items[i].indexOf('=');
        if (pos > 0) {
            var key = items[i].substring(0, pos);
            var val = items[i].substring(pos + 1);
            if (!parms[key]) {
                var rawVal = decodeURI(val);
                if (rawVal.indexOf(',') < 0)
                    parms[key] = rawVal;
                else
                    parms[key] = rawVal.split(',');
            }
        }
    }

    return parms["test_name"];
}

$(document).ready(function(){
    testLaunching();
    var testname = getParms();
    document.title = testname
    $("#main_page_title").text(testname);
    window.history.pushState(window.location.href);
//    var qstr = location.search.substring(1);
//    if (!qstr || qstr.indexOf("reenter") < 0)
//        $("[href='#popup_info']").click();
});

function checkInstalledPkg(pkgId) {
    var packageInfo = null;
    try {
        if(pkgId && (typeof(tizen) != 'undefined')) {
            packageInfo = tizen.package.getPackageInfo(pkgId);
        }
    } catch (e) {}

    return packageInfo === null ? false : true;
}
