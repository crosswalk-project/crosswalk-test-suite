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
        Jiazhen, Shentu <jiazhenx.shentu@intel.com>

*/

var _appURL;
var noSupport = {};
var isLaunching = false;
var storage = window.sessionStorage;

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
    $("#tool_title").empty().append("<h1 style=\"width:75%; margin-left:auto; margin-right:auto;\">TCT Behavior Test Tool</h1><a class=\"ui-btn-right\">" + version + "</a>");
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
                                  "<a href=\"" + url + "\">" +
                                  "<h1>" + $(this).attr("purpose") + "</h1></a></li>";
                    $("#mylist").append(appLine);
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
    var len = storage.length;
    if (len > 0) {
        for(var i=0;i<len;i++){
            var key = storage.key(i)
            var str = "h1:contains("+ key +")";
            var node = $(str).parent();
            var item = storage.getItem(key);
            if (item == "PASS") {
                node.parent().attr('data-theme', 'g');
                node.append("<img src='css/images/pass.png' class='ui-li-thumb'>");
                node.append("<span class='ui-li-count' style='color:green;'>PASS</span>");
            } else if (item == "FAIL"){
                node.parent().attr('data-theme', 'r');
                node.append("<img src='css/images/fail.png' class='ui-li-thumb'>");
                node.append("<span class='ui-li-count' style='color:red;'>FAIL</span>");
            }
        }
    }
}

function exportResult() {
    //TODO: export the test result from the saved result in session storage.
}

function SaveAndExit() {
    //TODO: export the test result from the saved result in session storage, then exit the app.
}

function reset() {
    storage.clear();
    $("#home_ui").trigger("pageshow");
}

function launchMain() {
    $("#test_frame").attr("src", "");
    $.mobile.changePage("#home_ui", {
        'allowSamePageTransition' : true,
        'transition' : 'slide',
        'reverse' : true
    });
    $.mobile.changePage("#main", {
        'allowSamePageTransition' : true,
        'transition' : 'slide',
        'reverse' : true
    });
}

function launchApp() {
    $("#test_frame").attr("src", _appURL);
    $.mobile.changePage("#test_ui", {
        'allowSamePageTransition' : true,
        'transition' : 'slide',
        'changeHash' : false
    });
}

function runApp(url) {
    if (isLaunching){
        setTimeout(function(){isLaunching = false;}, 200);
        return;
    }
    isLaunching = true;
    _appURL = url;
    _timer = setTimeout(launchApp, 200);
    $("#test_frame").attr("height", $(window).height());
}

function closeWindow() {
    $("#popup_exit").popup("close");
    window.open('', '_self', '');
    window.close();
}

function closePop() {
    $("#popup_exit").popup("close");
}

function refresh() {
    $("#mylist").listview('refresh');
    updateAppDecorationStyle();
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
            updateAppDecoration();
        }
    });
}

$("#home_ui").live("pagecreate", function (evt) {
  updateToolTitle();
  loadTests();

});

$('#home_ui').live('pageshow',function(event, ui){
    updateAppDecoration();
    updateBar();
    refresh();
    $('li').live("click", function (event) {
        runApp($(this).find("a").attr("href"));
        return false;
    });
});
