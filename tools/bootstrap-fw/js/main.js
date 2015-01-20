/*
Copyright (c) 2014 Intel Corporation.

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
        Lin, Wanming <wanmingx.lin@intel.com>
*/

var popup_info;
var fileName;

if(!window.localStorage) {
  showMessage("error", "This platform does not support localStorage!");
}
if(!window.sessionStorage) {
  showMessage("error", "This platform does not support sessionStorage!");
}
var lstorage = window.localStorage;
var sstorage = window.sessionStorage;

function testStorage() {
  lstorage.clear();
  var tests = getApps("tests.xml", "xml");
  var i = 0;
  var sname, sbg, sicon, tid, tnum, tids, tpass, tfail, setarr, setresarr, casearr, testsuite;
  /** get&set app-version **/
  var version = "";
  $(getApps("VERSION", "json")).each(function() {
    version = $(this).attr("app-version");
  });
  lstorage.setItem("app-version", version);
  /** get&set test suite **/
  $(tests).find("suite").each(function() {
    testsuite = $(this).attr("name");
  })
  lstorage.setItem("test-suite", testsuite);
  /** set loop **/
  $(tests).find("set").each(function() {
    sname = $(this).attr("name");
    sbg = $(this).attr("background");
    sicon = $(this).attr("icon");
    if(!sbg) {
      showMessage("error", "Invalid tests.xml! Miss background attribute in set node.");
    }
    if(!sicon) {
      showMessage("error", "Invalid tests.xml! Miss icon attribute in set node.");
    }
    i++;
    var j = 0;
    /** test case loop **/
    tids = "";
    $(this).find("testcase").each(function() {
      tid = $(this).attr("id");
      purpose = $(this).attr("purpose");
      tids += tid + ",";
      tnum = 1;
      if($(this).attr("subcase")) {
        tnum = parseInt($(this).attr("subcase"));
      }
      casearr = {purpose:purpose, num:tnum, pass:"0", fail:"0", result:"", sid:"set" + i}; //result: "", "pass", "fail"
      j += tnum;
      lstorage.setItem(tid, JSON.stringify(casearr)); //store case info
    });
    setarr = {name:sname, background:sbg, icon:sicon, tids:tids.substring(0, tids.length-1)};
    lstorage.setItem("set" + i, JSON.stringify(setarr)); //store set info
    setresarr = {totalnum:j, passnum:"", failnum:""};
    lstorage.setItem("set" + i + "res", JSON.stringify(setresarr)); //store set result
  });
  lstorage.setItem("setnum", i);  //store set total num
}

function listSet() {
  $('#main_title').append(lstorage.getItem("test-suite"));
  if (lstorage.getItem("test-suite") != "DemoExpress") {
    $("#btn-group").html('<button type="button" id="showTestResult" class="btn btn-default" onclick="document.location.href=\'report.html\'"><span class="glyphicon glyphicon-leaf"></span><span class="nbsp">Report</span></button>' + $("#btn-group").html());
  }
  $("#help").click(help);
  $("#exit").click(exit);
  document.getElementById('app-version').innerHTML = lstorage.getItem("app-version");
  var snum = parseInt(lstorage.getItem("setnum"));
  for(var i = 0; i < snum; i++) {
    var sid = "set" + (i + 1);
    var setarr = JSON.parse(lstorage.getItem(sid));
    var sname = setarr.name;
    var sbg = "color-swatches " + setarr.background;
    var sicon = "glyphicon " + setarr.icon;
    var surl = "tests_list.html?sid=" + sid;
    var setresarr = JSON.parse(lstorage.getItem(sid + "res"));
    var totalnum = parseInt(setresarr.totalnum);
    var passnum = setresarr.passnum;
    var failnum = setresarr.failnum;
    var setresline = "";
    if(passnum != "" || failnum != "") {
      setresline = '<span class=\"label label-primary\" style=\"margin-right:5px\">Total:' + totalnum +'</span>\n'
                    + '<span class=\"label label-success\">' + passnum + '</span>\n'
                    + '<span class=\"label label-danger\">' + failnum + '</span>\n'
                    + '<span class=\"label label-default\">' + (totalnum-parseInt(passnum)-parseInt(failnum)) + '</span>\n';
    }
    var setline = '<div class=\"col-md-4\">\n<div class=\"media\">\n'
                  + '<a class=\"pull-left\" href=\"' + surl + '\">\n'
                  + '<div class=\"' + sbg + '\"><span class=\"' + sicon + '\"></span></div>\n</a>\n'
                  + '<div class=\"media-body\">\n'
                  + '<a href=\"' + surl +'\"><h4 class=\"media-heading\">' + sname + '</h4></a>\n'
                  + setresline
                  + '</div>\n</div>\n</div>\n';
    $('#myset').append(setline);
  }
}

function help() {
  showMessage("help", popup_info);
}

function exit() {
  showMessage("exit", "Are you sure to exit?");
  $("#ifConfirm").click(confirmExit);
}

function confirmExit() {
  try {
    var app = tizen.application.getCurrentApplication();
    app.exit();
  } catch(error) {
    closeWindow();
  } finally {
    closeWindow();
  }
}

function closeWindow() {
  window.open('', '_self');
  window.close();
}

function uselstorage() {
  window.location.reload();
  testStorage();
}

$(document).ready(function(){
  popup_info = $("#popup_info").html();
  if (lstorage.getItem("test-suite") == null || lstorage.getItem("test-suite") == "DemoExpress") {
    testStorage();
  } else {
    if(sstorage.getItem("lsflag") == null) {
      $("#popup_info").modal(showMessage("lstorage", "Do you want to continue the last test?"));//ask if need use old lstorage
      $("#ifCancel").click(uselstorage);
    }
  }
  sstorage.setItem("lsflag", "1"); //flag for once testing without exiting app
  listSet();
});



