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

var sstorage = window.sessionStorage;
var applist;
var subapplist;
var ifcloased = 0;

function getCurrentTime() {
  var myDate = new Date();
  var year = myDate.getFullYear();
  var month = myDate.getMonth() + 1 < 10 ? "0" + (myDate.getMonth() + 1) : myDate.getMonth() + 1;
  var date = myDate.getDate() < 10 ? "0" + myDate.getDate() : myDate.getDate();
  var hours = myDate.getHours() < 10 ? "0" + myDate.getHours() : myDate.getHours();
  var minutes = myDate.getMinutes() < 10 ? "0" + myDate.getMinutes() : myDate.getMinutes();
  var seconds = myDate.getSeconds() < 10 ? "0" + myDate.getSeconds() : myDate.getSeconds();
  return (year + "" + month + "" + date + "" + hours + "" + minutes + "" + seconds);
}

function exportResult(flag) {
  ifcloased = flag;
  try{
    tizen.filesystem.resolve(
      'downloads',
      function(dir) {
        documentsDir = dir; 
        dir.listFiles(resolveSuccess, onerror);
      }, function(e) {
        $("#exportlog").html("Error: " + e.message);
        $('#popup_export').popup('open');
        if (ifcloased == 1) {
          var app = tizen.application.getCurrentApplication();
          app.exit();
        }
      }, "rw");
  } catch(error) {
    $("#exportlog").html("Error" + error.message);
    $('#popup_export').popup('open');
    if (ifcloased == 1) {
      exitTest();
    }
  }
}

function resolveSuccess(files) {
  var time = getCurrentTime();
  var testSuiteName = sstorage.getItem("test-suite");
  var fileName = testSuiteName + "_" + time + ".report.csv";
  var fsTestDir;
  if (files.length > 0) {
    for(var i = 0; i < files.length; i++) {
      if (files[i].isDirectory) {
        documentsDir.deleteDirectory(
          files[i].fullPath,
          true,
          function(){
          }, function(e) {
            $("#exportlog").html("Error" + e.message);
            $('#popup_export').popup('open');
            if (ifcloased == 1) {
              var app = tizen.application.getCurrentApplication();
              app.exit();
            }
          });
      }
    }
  }
  fsTestDir = documentsDir.createDirectory(testSuiteName);
  var testFile = fsTestDir.createFile(fileName);
  if (testFile != null) {
    testFile.openStream(
      "w",
      function(fs) {
        var snum = parseInt(sstorage.getItem("setnum"));
        var resultReport = "Feature, Case Id, Test Case, Pass, Fail, N/A, Measured, Comment, Measurement Name, Value, Unit, Target, Failure\n";
        for(var i = 0; i < snum; i++) {
          var sid = "set" + (i + 1);
          var setarr = JSON.parse(sstorage.getItem(sid));
          var tids = setarr.tids.split(',');
          for(var j = 0; j < tids.length; j++) {
            var tid = tids[j];
            var casearr = JSON.parse(sstorage.getItem(tid));
            var resultarr = JSON.parse(sstorage.getItem(casearr.purpose));
            var tresult = "";
            if (resultarr != null) {
              tresult = resultarr.result;
            }
            resultReport += setarr.name + "," + tid + "," + casearr.purpose;
            var pass0, fail0, notrun0;
            if (casearr.issubcase) {
              var resultnum = tresult;
              if (resultnum[3] == "PASS" || resultnum[3] == "FAIL") {
                pass0 = resultnum[0];
                fail0 = resultnum[1];
                notrun0 = resultnum[2];
              } else {
                pass0 = 0;
                fail0 = 0;
                notrun0 = (JSON.parse(sstorage.getItem("sub_" + tid))).subcasenum;
              }
            } else {
              pass0 = tresult == "PASS" ? 1 : 0;
              fail0 = tresult == "FAIL" ? 1 : 0;
              notrun0 = tresult != "" ? 0 : 1;
            }
            resultReport += "," + pass0 + "," + fail0 + "," + notrun0 + "\n";
          } 
        }
        fs.write(resultReport);
        fs.close();
        $("#exportlog").html("Download 'report.csv' successfully! You can get it from 'TESTER-HOME-DIR/content/Downloads/" + testSuiteName + "/'.");
        $('#popup_export').popup('open');
        if (ifcloased == 1) {
          var app = tizen.application.getCurrentApplication();
          app.exit();
        }
      }, function(e) {
        $("#exportlog").html("CreateFile error: " + e.message);
        $('#popup_export').popup('open');
        if (ifcloased == 1) {
          var app = tizen.application.getCurrentApplication();
          app.exit();
        }
      }, "UTF-8");
  }
}

function onerror(error) {
  $("#exportlog").html("The error " + error.message + " occurred when listing the files in the selected folder");
  $('#popup_export').popup('open');
}

function getVersion() {
  var version = "";
  $.ajax({
    async : false,
    type : "GET",
    url : "config.xml",
    dataType : "xml",
    success : function(xml){
      $(xml).find("widget").each(function(){version = $(this).attr("version");});
    }
  });
  return version;
}

function getApps() {
  var tests = "";
  $.ajax({
    async : false,
    type : "GET",
    url : "tests.xml",
    dataType : "xml",
    success : function(xml){tests = xml;}
  });
  return tests;
}

function getSubApps() {
  var tests = "";
  $.ajax({
    async : false,
    type : "GET",
    url : "subtestresult.xml",
    dataType : "xml",
    success : function(xml){tests = xml;}
  });
  return tests;
}

function updateList() {
  $("#mylist").empty();
  var i = 0;
  var sname, tid, purpose, testsuite, subcaselist, subcasename;
  subcaselist = []; 
  $(subapplist).find("set").each(function(){
    subcasename = $(this).attr("name");
    subcaselist.push(subcasename);
    var subcasenum = 0;
    $(this).find("testcase").each(function(){
      subcasenum++;
    });
    var subcasearr = {subcasenum: subcasenum};
    sstorage.setItem("sub_" + subcasename, JSON.stringify(subcasearr));
  });
  $(applist).find("suite").each(function() {
    testsuite = $(this).attr("name");
  })
  sstorage.setItem("test-suite", testsuite);
  $(applist).find("set").each(function(){
    i++;
    var tids = "";
    sname = $(this).attr("name");
    $("#mylist").append("<li data-role=\"list-divider\">"+$(this).attr("name")+"</li>");
    $(this).find("testcase").each(function(){
      tid = $(this).attr("id");
      purpose = $(this).attr("purpose");
      tids += tid + ",";
      var url = "tests/" + tid + "/index.html?test_name="+tid;
      var appLine = "<li class=\"app\" id=\"" + tid + "\">"
                  + "<a href=\"" + url + "\">" + "<h2>" + purpose + "</h2></a></li>";
      $("#mylist").append(appLine);
      var issubcase = 0;
      if (subcaselist.indexOf(tid) != -1) {
        issubcase = 1;
      }
      casearr = {purpose:purpose, sid:"set" + i, issubcase: issubcase};
      sstorage.setItem(tid, JSON.stringify(casearr));
    });
    setarr = {name:sname, tids:tids.substring(0, tids.length-1)};
    sstorage.setItem("set" + i, JSON.stringify(setarr));
  });
  sstorage.setItem("setnum", i);
  for(var j = 0; j < i; j++) {
    sid = "set" + (j + 1);
    setarr = JSON.parse(sstorage.getItem(sid));
    tids = setarr.tids.split(',');
    for(var k = 0; k < tids.length; k++) {
      tid = tids[k];
      casearr = JSON.parse(sstorage.getItem(tid));
      resultarr = JSON.parse(sstorage.getItem(casearr.purpose));
      var name = casearr.purpose;
      var item = "";
      if (resultarr != null) {
        item = resultarr.result;
      }
      var node = $("h2:contains('"+ name + "')").parent().parent();
      if (item == "PASS") {
        node.attr("data-theme", "g");
        node.append("<img src='css/images/pass.png' class='ui-li-thumb'>");
        node.append("<span class='ui-li-count' style='color:green;'>PASS</span>");
        node.find("a h2").css("padding-left", "20px");
      } else if (item == "FAIL"){
        node.attr("data-theme", "r");
        node.append("<img src='css/images/fail.png' class='ui-li-thumb'>");
        node.append("<span class='ui-li-count' style='color:red;'>FAIL</span>");
        node.find("a h2").css("padding-left", "20px");
      } else if (item != "") {
        resultnum = item;
        if (resultnum[3] == "PASS") {
          node.attr("data-theme", "g");
          node.append("<img src='css/images/pass.png' class='ui-li-thumb'>");
          node.append("<span class='ui-li-count' style='color:green;'>"  + resultnum[0] + "</span>");
          node.append("<span class='ui-li-count' style='color:red;'>"  + resultnum[1] + "</span>");
          node.append("<span class='ui-li-count' style='color:gray;'>"  + resultnum[2] + "</span>");
          node.find("a h2").css("padding-left", "20px");
        } else if (resultnum[3] == "FAIL"){
          node.attr("data-theme", "r");
          node.append("<img src='css/images/fail.png' class='ui-li-thumb'>");
          node.append("<span class='ui-li-count' style='color:green;'>"  + resultnum[0] + "</span>");
          node.append("<span class='ui-li-count' style='color:red;'>"  + resultnum[1] + "</span>");
          node.append("<span class='ui-li-count' style='color:gray;'>"  + resultnum[2] + "</span>");
          node.find("a h2").css("padding-left", "20px");
        }
      }
    }
  }
  $("#mylist").listview("refresh");
  $(".ui-li-has-count").each(function() {
    var childs = $(this).find(".ui-li-count");
    if (childs.length == 3) {
      $(childs[0]).css("min-width","10px");
      $(childs[1]).css("min-width","10px");
      $(childs[2]).css("min-width","10px");
      var shiftSecond = ($(childs[2]).position().left - $(childs[1]).outerWidth());
      var shiftFirst = (shiftSecond - 23);
      $(childs[0]).css("left", shiftFirst).css("right","auto");
      $(childs[1]).css("left", shiftSecond).css("right","auto");
    }
  });
}

function updateFooter() {
  $(':jqmData(role=footer)').find(':jqmData(role=button) > span:first-child').css('padding', '15px 10px 15px 30px');
}

function launchMain(node) {
  if ($("#home_ui").find("div").length > 0) {
    updateList();
    $.mobile.changePage("#home_ui", {
      'allowSamePageTransition' : true,
      'transition' : 'slide',
      'reverse' : true
    });
    if (node != "") {
      $("html,body").animate({
        scrollTop:$("h2:contains(" + node +")").offset().top - 25
      }, 500);
    }
  } else {
    $.mobile.changePage("#main", {
      'allowSamePageTransition' : true,
      'transition' : 'slide',
      'reverse' : true
    });
  }
  $("#test_frame").attr("src", "");
}

function runApp(url) {
  $.mobile.changePage("#test_ui", {
    'allowSamePageTransition' : true,
    'transition' : 'slide',
    'changeHash' : false
  });
  $("#test_frame").attr("height", $(window).height());
  $("#test_frame").attr("src", url);
}

$("#home_ui").live("pagebeforecreate", function () {
  $("#version").text(getVersion());
});

$("#home_ui").live("pageshow", function () {
  applist = getApps();
  subapplist = getSubApps();
  updateList();
  updateFooter();
});

function exitTest(){
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

$("#reset").live("click", function (event) {
  sstorage.clear();
  updateList();
  return false;
});

$(".app").live("click", function () {
  runApp($(this).find("div div a").attr("href"));
  return false;
});

$('#main').live('pageshow',function(){  
  for(var i=0;i<$("#cspList").find("h2").length;i++){
    var str = "h2:contains("+ $("#cspList").find("h2")[i].innerHTML +")";
    var node = $(str);
    var item = JSON.parse(sstorage.getItem($("#cspList").find("h2")[i].innerHTML));
    if (item != null) {
      if (item.result == "PASS") {
        node.attr('style', 'color:green;');
      } else if (item.result == "FAIL"){
        node.attr('style', 'color:red;');
      }
    }
  }
  updateFooter();
});
