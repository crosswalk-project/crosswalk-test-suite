/*
Copyright (c) 2012 Intel Corporation.

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
        Fan, Yugang <yugang.fan@intel.com>
*/

var defTime = 2000;
var Tests;
var xmldoc;
var startTime;
var timeout;
var current_page_uri = "";
var activetest = true;
var iTest = 0;
var ttestsuite;
var tpriority;
var tstatus;
var ttype;
var tcategory;
var texecutiontype;
var tset;
var manualcaseslist;
var last_test_page = "";
var current_page_uri = "";
var activetest = true;
var statusNode;
var testFrame;
var statusFrame;
var messageFrame;
var controlArea;
var testArea;
var caseListArea;
var manageArea;
var loadingArea;
var iSuite = "";
var iSet = "";
var iEXEType = "";
var pageIndex = 1;
var caseListNum = 20;
var casePageNum;

var manualcases = function() {
  this.casesid = "";
  this.index = 0;
  this.result = "";
};

function getTestPageParam(uri, param) {
  var querys = uri.split("?")
  if (querys.length <= 1)
    return "";
  uri = querys[1];
  var start = uri.indexOf(param);
  if (start == -1)
    return "";
  start += param.length + 1;
  var end = uri.indexOf("&", start);
  if (end == -1)
    return uri.substring(start);
  return uri.substring(start, end);
}

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
  for (var i = 0; i < items.length; i++) {
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

  ttestsuite = parms["testsuite"];
  tpriority = parms["priority"];
  tstatus = parms["status"];
  ttype = parms["type"];
  tcategory = parms["category"];
  texecutiontype = parms["execution_type"];
  tset = parms["set"];
}

function updateXMLByParms(xml) {
  $(xml).find("set").each(
    function() {
      var v = $(this).attr('name');
      if (tset && v != tset) {
        $(this).remove();
      }
    });
  $(xml).find("testcase").each(
    function() {
      var v, vType;
      v = $(this).attr('execution_type');
      if (texecutiontype && texecutiontype == "manual")
        vType = "manual";
      else if (texecutiontype && texecutiontype == "auto")
        vType = "auto";
      else if (!texecutiontype)
        vType = ["auto", "manual"];
      else
        vType = "auto";
      if (v != vType && $.inArray(v, vType) < 0)
        $(this).remove();
      v = $(this).attr('priority');
      if (tpriority && v != tpriority && $.inArray(v, tpriority) < 0)
        $(this).remove();
      v = $(this).attr('status');
      if (tstatus && v != tstatus && $.inArray(v, tstatus) < 0)
        $(this).remove();
      v = $(this).attr('type');
      if (ttype && v != ttype && $.inArray(v, ttype) < 0)
        $(this).remove();
      var categories = $(this).find("categories > category");
      if (categories.length > 0 && tcategory) {
        var i;
        var found = false;
        for (i = 0; i < categories.length; i++) {
          var category = $(categories).get(i);
          if ($(category).text().trim() != tcategory && $.inArray($(category).text().trim(),
            tcategory) < 0) {
            found = true;
            break;
          }
        }
        if (!found)
          $(this).remove();
      }

      $(this).attr('result', "N/A");
    });
  return xml;
}

function runTestSuite(xml) {
  $("#versionrow").hide();
  document.getElementById("suitelist").options.length = 0;
  var i = 0;
  $(xml).find("suite").each(
    function() {
      var suitename = $(this).attr('name');
      document.getElementById("suitelist").options.add(new Option(suitename, i));
      i++;
    });
  xml = updateXMLByParms(xml);
  initSets(xml);
  loadingArea.hide();
  controlArea.show();
}

function getSelectedText(selectDiv) {
  var selectList = selectDiv.getElementsByClassName("checkbox");
  var selectedText = new Array();
  for (var i = 0; i < selectList.length; i++) {
    if (selectList[i].checked) {
      selectedText.push(selectList[i].value);
    }
  }
  return selectedText;
}

function getExeSelectedText() {
  var selectedText = new Array();

  if (document.getElementById("exemanualradio").checked) {
    selectedText.push(document.getElementById("exemanualradio").value);
  };

  if (document.getElementById("exeautoradio").checked) {
    selectedText.push(document.getElementById("exeautoradio").value);
  };

  return selectedText;
}

function initCases(xml) {
  $(xml).find("set").each(
    function() {
      if ($.inArray($(this).attr('name'), iSet) < 0)
        $(this).remove();
    }
  );

  $(xml).find("testcase").each(
    function() {
      if ($.inArray($(this).attr('execution_type'), iEXEType) < 0)
        $(this).remove();
    }
  );

  Tests = $(xml).find("testcase");
  xmldoc = xml;
  casePageNum = Math.ceil(Tests.length / caseListNum);
}

function showCase(iCase) {
  var ts = $(Tests[iCase]).find('test_script_entry');
  var it = $(ts).get(0);
  if (document.getElementById('iframeradio').checked) {
    testArea.show();
    if ($(Tests[iCase]).attr('execution_type') == "manual") {
      $("#statusframe").show();
      statusFrameContent = document.getElementById('statusframe').contentWindow;
      statusFrameContent.document.body.innerHTML = "";
      caseslistinfo = "Descriptions: " + $(Tests[iCase]).attr('purpose') + "<br>";

      var preC = $(Tests[iCase]).find('pre_condition');
      if (preC && preC.length > 0) {
        var preCText = $(preC).get(0);
        caseslistinfo += "PreCondition: " + $(preCText).text().trim() + "<br>";
      }

      var posC = $(Tests[iCase]).find('post_condition');
      if (posC && posC.length > 0) {
        var posCText = $(posC).get(0);
        caseslistinfo += "PostCondition: " + $(posCText).text().trim() + "<br>";
      }
      var stepInfo = $(Tests[iCase]).find('step_desc');
      var stepExp = $(Tests[iCase]).find('expected');
      for (var j = 0; j < stepInfo.length; j++) {
        var stepsnum = j + 1;
        if (stepInfo) {
          var stepInfoText = $(stepInfo[j]).get(0);
          caseslistinfo += "Step-" + stepsnum + ": " + $(stepInfoText).text().trim() + "<br>";
        }
        if (stepExp) {
          var stepExpText = $(stepExp[j]).get(0);
          caseslistinfo += "Expected" + ": " + $(stepExpText).text().trim() + "<br>";
        }
      }

      statusFrameContent.document.writeln(caseslistinfo);
    } else {
      $("#statusframe").hide();
    }

    if ($(it).text().length > 0) {
      $("#testframe").show();
      testFrame.src = $(it).text();
      caseListArea.hide();
    } else {
      $("#testframe").hide();
    }
  } else {
    testArea.hide();
    if ($(it).text().length > 0) {
      window.open($(it).text());
      //window.location.href($(it).text());
    }
  }
}

function initParmsCases(xml) {
  xml = updateXMLByParms(xml);
  initCases(xml);
}

function updateTestXML() {
  iSuiteIndex = document.getElementById("suitelist").selectedIndex;
  if (iSuite != "" && iSet != "" && iEXEType != "") {
    if (iSuite.toString() == document.getElementById("suitelist").options[iSuiteIndex].text &&
      iSet.sort().toString() == getSelectedText(document.getElementById("setlist")).sort().toString() &&
      iEXEType.sort().toString() == getExeSelectedText().sort().toString()) {
      return;
    }
  }

  pageIndex = 1;
  iSuite = document.getElementById("suitelist").options[iSuiteIndex].text;
  iSet = getSelectedText(document.getElementById("setlist"));
  iEXEType = getExeSelectedText();
  if (iSet.length <= 0 || iEXEType.length <= 0) {
    Tests = "";
    xmldoc = null;
    casePageNum = 0;
  } else {
    $.ajax({
      async: false,
      type: "GET",
      url: "/opt/" + iSuite + "/tests.xml",
      dataType: "xml",
      success: initCases,
    });
  }
}

function showCaseListIndex() {
  caseLists = document.getElementById("caselists");
  pageSwitch01 = document.getElementById("pageswitch01");
  pageSwitch02 = document.getElementById("pageswitch02");
  pageSwitch01.innerHTML = '';
  pageSwitch02.innerHTML = '';
  pageSwitch01.innerHTML += "<a href=\"javascript:gotoCaseListsPage('-1');\">Prev</a>&nbsp&nbsp;"
  pageSwitch02.innerHTML += "<a href=\"javascript:gotoCaseListsPage('-1');\">Prev</a>&nbsp&nbsp;"
  pageSwitch01.innerHTML += "<a href=\"javascript:showCaseListsPage('1');\">|\<\<</a>&nbsp&nbsp;";
  pageSwitch02.innerHTML += "<a href=\"javascript:showCaseListsPage('1');\">|\<\<</a>&nbsp&nbsp;";
  var startPage;
  if (pageIndex - 4 < 1) {
    startPage = 1;
  } else if (pageIndex + 4 > casePageNum) {
    startPage = casePageNum - 8;
    if (startPage < 1)
      startPage = 1;
  } else {
    startPage = pageIndex - 4;
  }
  for (var i = startPage; i <= casePageNum && i <= startPage + 8; i++) {
    if (i == pageIndex) {
      pageSwitch01.innerHTML += "<a style=\"color:black\" href=\"javascript:showCaseListsPage('" + i + "');\"> " + i + " </a>&nbsp;";
      pageSwitch02.innerHTML += "<a style=\"color:black\" href=\"javascript:showCaseListsPage('" + i + "');\"> " + i + " </a>&nbsp;";
    } else {
      pageSwitch01.innerHTML += "<a href=\"javascript:showCaseListsPage('" + i + "');\"> " + i + " </a>&nbsp;";
      pageSwitch02.innerHTML += "<a href=\"javascript:showCaseListsPage('" + i + "');\"> " + i + " </a>&nbsp;";
    }
  }
  pageSwitch01.innerHTML += "<a href=\"javascript:showCaseListsPage('" + casePageNum + "');\">\>\>|</a>&nbsp&nbsp;";
  pageSwitch02.innerHTML += "<a href=\"javascript:showCaseListsPage('" + casePageNum + "');\">\>\>|</a>&nbsp&nbsp;";
  pageSwitch01.innerHTML += "<a href=\"javascript:gotoCaseListsPage('1');\">Next</a>&nbsp&nbsp;"
  pageSwitch02.innerHTML += "<a href=\"javascript:gotoCaseListsPage('1');\">Next</a>&nbsp&nbsp;"
}

function showCaseList() {
  caseLists = document.getElementById("caselists");
  caseLists.innerHTML = '';
  if (casePageNum > 0) {
    var caselistsinfo = "<table id=\"caselisttb\" class=\"listtable\">";
    var iCase = 0;
    while (iCase < caseListNum) {
      var iiCase = (pageIndex - 1) * caseListNum + iCase;
      if (iiCase > Tests.length - 1)
        break;
      caselistsinfo += "<tr><th>" + [iiCase + 1] + "</th><td id=\"" + iiCase + "\" class=\"caseinfotd\"><a id=\"caseidtext\">" + $(Tests[iiCase]).attr('id') + "</a><br><a id=\"casedesctext\">" + $(Tests[iiCase]).attr('purpose') + "</a></td></tr>";
      iCase++;
    }
    caselistsinfo += "</table>";
    caseLists.innerHTML = caselistsinfo;
    var lists = document.getElementById("caselisttb").getElementsByClassName("caseinfotd");
    for (var k = 0; k < lists.length; k++) {
      lists[k].onclick = function() {
        showCase(this.id);
      }
    }
  }
}

function showCaseListsPage(index) {
  index = parseInt(index);

  if (index < 1) {
    index = 1;
  } else if (index > casePageNum) {
    index = casePageNum;
  }
  pageIndex = index;
  showCaseListIndex();
  showCaseList();
}

function gotoCaseListsPage(point) {
  caseLists = document.getElementById("caselists");
  point == "-1" ? showCaseListsPage(pageIndex - 1) : showCaseListsPage(pageIndex + 1);
}

function showCases() {
  testFrame.src = '';
  testArea.hide();
  updateTestXML();
  showCaseList();
  showCaseListIndex();
  caseListArea.show();
}

function highLightChecked(parentDiv) {
  var selectList = parentDiv.getElementsByClassName("checkbox");
  for (var i = 0; i < selectList.length; i++) {
    if (selectList[i].checked) {
      parentDiv.getElementsByClassName("selectlabel")[i].style.color = "black";
    } else {
      parentDiv.getElementsByClassName("selectlabel")[i].style.color = "#808080";
    }
  }
}

function initSets(xml) {
  var setList = document.getElementById("setlist");
  setList.innerHTML = '';
  var i = 0;
  $(xml).find("set").each(
    function() {
      if (i > 0) {
        setList.innerHTML += "<br>";
      }
      setList.innerHTML += "<label class=\"selectlabel\"><input type=\"checkbox\" class=\"checkbox\" value=\"" + $(this).attr('name') + "\">" + $(this).attr('name') + "</label>";
      i++;
    });
  var selectList = setList.getElementsByClassName("checkbox");
  for (var k = 0; k < selectList.length; k++) {
    selectList[k].onclick = function() {
      highLightChecked(setList);
    }
  }
  setList.getElementsByClassName("checkbox")[0].checked = true;
  highLightChecked(setList);
  if ($(xml).find("set").length <= 1)
    $("#setlist").hide()
  else
    $("#setlist").show()
  document.getElementById("exemanualradio").tag = 1;
  document.getElementById("exeautoradio").tag = 1;
}

function suiteUpdate() {
  iSuiteIndex = document.getElementById("suitelist").selectedIndex;
  $.ajax({
    async: false,
    type: "GET",
    url: "/opt/" + document.getElementById("suitelist").options[iSuiteIndex].text + "/tests.xml",
    dataType: "xml",
    success: initSets,
  });
}

function suiteUpdateButtonDown() {
  var i = document.getElementById("suitelist").selectedIndex;
  if (i + 1 >= document.getElementById("suitelist").options.length)
    i = 0;
  else
    i++;
  document.getElementById("suitelist").selectedIndex = i;
  suiteUpdate();
}

function suiteUpdateButtonUp() {
  var i = document.getElementById("suitelist").selectedIndex;
  if (i <= 0)
    i = document.getElementById("suitelist").options.length - 1;
  else
    i--;
  document.getElementById("suitelist").selectedIndex = i;
  suiteUpdate();
}

function exeManualRadio() {
  var radio = document.getElementById("exemanualradio");
  if (radio.tag == 1) {
    radio.checked = false;
    radio.tag = 0;
    document.getElementById("exemanuallabel").style.color = "#808080";
  } else {
    radio.checked = true;
    radio.tag = 1;
    document.getElementById("exemanuallabel").style.color = "black";
  }
}

function exeAutoRadio() {
  var radio = document.getElementById("exeautoradio");
  if (radio.tag == 1) {
    radio.checked = false;
    radio.tag = 0;
    document.getElementById("exeautolabel").style.color = "#808080";
  } else {
    radio.checked = true;
    radio.tag = 1;
    document.getElementById("exeautolabel").style.color = "black";
  }
}

function iFrameRadio() {
  var radio = document.getElementById("iframeradio");
  radio.checked = true;
  document.getElementById("iframelabel").style.color = "black";
  document.getElementById("newwinradio").checked = false;
  document.getElementById("newwinlabel").style.color = "#808080";
}

function newWinRadio() {
  var radio = document.getElementById("newwinradio");
  radio.checked = true;
  document.getElementById("newwinlabel").style.color = "black";
  document.getElementById("iframeradio").checked = false;
  document.getElementById("iframelabel").style.color = "#808080";
}

function runTestSuiteSer() {
  $("#versionrow").hide();
  document.getElementById("iframelabel").style.color = "black";
  document.getElementById("newwinlabel").style.color = "#808080";
  document.getElementById("suitelist").options.length = 0;
  $(document).ready(function() {
    $.ajax({
      type: "GET",
      url: "config.json",
      dataType: "json",
      success: function(data) {
        $.each(data, function(i, item) {
          if (item.suite) {
            document.getElementById("suitelist").options.add(new Option(item.suite, i));
          } else if (item.version) {
            $("#versiontext").text(item.version);
            $("#versionrow").show();
          }
        })
        suiteUpdate();
      }
    })
  });
  loadingArea.hide();
  controlArea.show();
}

function startTest() {
  iTest = 0;
  updateTestXML();
  controlArea.hide();
  caseListArea.hide();
  testArea.show();
  $("#testframe").show();
  $("#statusframe").show();
  statusFrame.contentWindow.document.body.innerHTML = "";
  statusNode = init_status_frame();
  doTest();
  iSuite = '';
}

function initSelectionPage() {
  $("#statusframe").show();
  statusFrame.height = "10%";
  $("#testframe").show();
  testFrame.height = "70%";
  testFrame.src = '';
  manageArea.hide();
  testArea.hide();
  controlArea.show();
}

function preCheck() {
  testArea = $("#testarea");
  caseListArea = $("#caselistarea");
  manageArea = $("#managearea");
  controlArea = $("#controlarea");
  loadingArea = $("#loadingarea");
  testArea.hide();
  caseListArea.hide();
  manageArea.hide();
  controlArea.hide();
  loadingArea.show();
  getParms();

  testFrame = document.getElementById('testframe');
  statusFrame = document.getElementById('statusframe');
  messageFrame = document.getElementById('messageframe');
  $("#messageframe").hide();

  if (!xmldoc) {
    $.ajax({
      async: false,
      type: "GET",
      url: ttestsuite,
      dataType: "xml",
      success: runTestSuite,
      error: function(x, t, e) {
        runTestSuiteSer();
      }
    });
  }
}

function escape_html(s) {
  s = String(s);
  return s.replace(/\&/g, "&amp;").replace(/</g, "&lt;").replace(/"/g,
    "&quot;").replace(/'/g, "&#39;");
}

function check_timeout(time) {
  if (time >= 11) {
    last_test_page = "";
    report('BLOCK', "Time is out");
    return;
  }
  sleep_time = time * 50;
  setTimeout("CheckResult('yes', " + time + ")", sleep_time);
}

function CheckResult(need_check_block, sleep_time) {
  var message = "";
  var total_num = "";
  var locator_key = "";
  var value = "";
  var case_uri = current_page_uri;

  try {
    var oTestWin = testFrame.contentWindow;
    var oTestDoc = oTestWin.document;

    if (oTestWin.document.readyState == "complete") {
      total_num = getTestPageParam(case_uri, "total_num");
      locator_key = getTestPageParam(case_uri, "locator_key");
      value = getTestPageParam(case_uri, "value");
      oPass = $(oTestDoc).find(".pass");
      oFail = $(oTestDoc).find(".fail");

      // Test page has parameters
      if (total_num != "" && locator_key != "" && value != "") {
        if (locator_key == "id") {
          var results;
          var passes;
          var fails;

          if (oPass.length == 0 && oFail.length == 0) {
            next_sleep_time = sleep_time + 1;
            check_timeout(next_sleep_time);
            return;
          }
          var oRes = $(oTestDoc).find("table#results");
          if (oRes) {
            results = $(oRes).find('tr');
            passes = $(oRes).find('tr.pass');
            fails = $(oRes).find('tr.fail');
          }

          var total_actual = passes.length + fails.length;
          var index = Number(value);
          if (index <= total_actual) {
            var rest = results[index].childNodes[0].innerText;
            var desc = results[index].childNodes[1].innerText;
            var msg = results[index].childNodes[2].innerText;
            if (rest && rest.toUpperCase() == "PASS")
              report('PASS', msg);
            else
              report('FAIL', msg);
          } else {
            report('BLOCK', "Found none test case");
          }
        } else if (locator_key == "test_name") {
          // Place holder
        } else if (locator_key == "msg") {
          // Place holder
        } else {
          alert("Unknown locator key");
        }
      } else if (oPass.length > 0 && oFail.length == 0) {
        if (oTestWin.resultdiv)
          message = oTestWin.resultdiv.innerHTML;
        report('PASS', message);
      } else if (oFail.length > 0) {
        var oRes = $($(oTestDoc).find("table#results")).get(0);
        // Get error log
        if (oRes) {
          var fails = $(oRes).find('tr.fail');
          var i;
          for (i = 0; i < fails.length; i++) {
            var desccell = fails[i].childNodes[1];
            if (desccell)
              message += "###Test Start###" + desccell.innerText + "###Test End###";
            var msgcell = fails[i].childNodes[2];
            if (msgcell)
              message += "###Error2 Start###" + msgcell.innerText + "###Error2 End###";
          }
        }
        report('FAIL', message);
      } else // oFail.length==0 && oPass.length==0
      if (need_check_block == 'yes') {
        next_sleep_time = sleep_time + 1;
        check_timeout(next_sleep_time);
        return;
      }
    } else // not complete
    if (need_check_block == 'yes') {
      next_sleep_time = sleep_time + 1;
      check_timeout(next_sleep_time);
      return;
    }
  } catch (e) {
    report('BLOCK', e);
  }
}

function report(result, log) {

  if (iTest >= Tests.length)
    return;
  $(Tests[iTest]).attr('result', result);
  var doc = $.parseXML("<result_info>" + "<actual_result>" + result + "</actual_result>" + "<start>" + startTime + "</start>" + "<end>" + new Date() + "</end>" + "<stdout>" + escape_html(log) + "</stdout>" + "</result_info>");
  $(Tests[iTest]).append(doc.documentElement);

  statusNode.innerHTML = "Test #" + (iTest + 1) + "/" + Tests.length + "(" + result + ") " + current_page_uri;

  try {
    var starts = log.indexOf('value:');
    var stops = log.lastIndexOf(',');
    var resultinfo = log.substring(starts + 6, stops);
    $(Tests[iTest]).find("measurement").attr('value', resultinfo);
  } catch (e) {}

  iTest++;

  if (activetest) {
    doTest();
  } else {
    activetest = true;
  }
}

function doTest() {
  while (iTest < Tests.length) {
    if ($(Tests[iTest]).attr('execution_type') != 'auto') {
      iTest++;
      continue;
    }
    var ts = $(Tests[iTest]).find('test_script_entry');
    if (ts.length == 0) {
      iTest++;
      continue;
    }
    var it = $(ts).get(0);
    var tstr = $(it).attr('timeout');
    if (!tstr)
      timeout = 8 * defTime;
    else {
      var t;
      try {
        t = parseInt(tstr) * 1000;
      } catch (e) {
        t = 8 * defTime;
      }
      timeout = t;
    }

    pset = $(Tests[iTest]).parent().attr('name');
    psuite = $(Tests[iTest]).parent().parent().attr('name');

    startTime = new Date();

    current_page_uri = $(it).text();
    var index = current_page_uri.indexOf("?");
    var test_page = "";
    if (index >= 0)
      test_page = current_page_uri.substring(0, index);
    else
      test_page = current_page_uri;

    // Don't load the same test page again
    if (test_page == last_test_page) {
      print_error_log("test page url is the same as the last one",
        test_page);
      activetest = false;
      CheckResult('yes', 0);
      continue;
    }

    if ((current_page_uri.indexOf("2DTransforms") != -1) || (current_page_uri.indexOf("3DTransforms") != -1)) {
      testFrame.height = 500000 + "px";
    } else {
      testFrame.height = 2500 + "px";
    }
    testFrame.src = current_page_uri;
    last_test_page = test_page;
    if (testFrame.attachEvent) {
      testFrame.attachEvent("onload", function() {
        CheckResult('yes', 0);
      });
    } else {
      testFrame.onload = function() {
        CheckResult('yes', 0);
      };
    }
    return;
  }

  doManualTest();
}

function doManualTest() {
  if (testFrame.attachEvent) {
    testFrame.attachEvent("onload", '');
  } else {
    testFrame.onload = '';
  }
  manualcaseslist = new Array();
  var iTemp1 = 0,
    iTemp2 = 0;
  while (iTemp1 < Tests.length) {
    if ($(Tests[iTemp1]).attr('execution_type') == 'manual') {
      manualcaseslist[iTemp2] = new manualcases();
      manualcaseslist[iTemp2].casesid = $(Tests[iTemp1]).attr('id');
      manualcaseslist[iTemp2].index = iTemp1;
      manualcaseslist[iTemp2].result = $(Tests[iTemp1])
        .attr('result');
      iTemp2++;
    }
    iTemp1++;
  }
  if (iTemp2 > 0) {
    statusFrame.src = "manualharness.html";
  } else if (iTest == Tests.length) {
    setTimeout("PublishResult()", 2000);
  }
  testFrame.src = '';
}

function PublishResult() {
  $("#statusframe").hide();
  manageArea.show();
  testFrame.height = "95%";
  if (testFrame.attachEvent) {
    testFrame.attachEvent("onload", '');
  } else {
    testFrame.onload = '';
  }
  var resultXML;
  resultXML = "<title>HTML5 Test Result XML</title>";
  resultXML += "<head><style type='text/css'>\
html {font-family:DejaVu Sans, Bitstream Vera Sans, Arial, Sans;}\
section#summary {margin-bottom:1em;}\
table#results {\
    border-collapse:collapse;\
    table-layout:fixed;\
    width:100%;\
}\
table#results th:first-child,\
table#results td:first-child {\
    width:30%;\
}\
table#results th:last-child,\
table#results td:last-child {\
    width:30%;\
}\
table#results th {\
    padding:0;\
    padding-bottom:0.5em;\
    text-align:left;\
    border-bottom:medium solid black;\
}\
table#results td {\
    padding:1em;\
    padding-bottom:0.5em;\
    border-bottom:thin solid black;\
}\
</style><head>";

  resultXML += "<section id='summary'>";
  resultXML += "<h2>Summary</h2>";
  var ipass = $(xmldoc).find("testcase[result='PASS']").length;
  var failList = $(xmldoc).find("testcase[result='FAIL']");
  var ifail = failList.length;
  resultXML += "<h3>Total:" + Tests.length + " Pass:<span style='color:green;'>" + ipass + "</span> Fail:<span style='color:red;'>" + ifail + "</span></h3>";
  resultXML += "</section>";
  resultXML += "<p><table id='results'> <tr> <th> TestSet </th> <th> Pass </th> <th> Fail </th></tr>";
  var Sets = $(xmldoc).find("set");
  var i = 0;
  for (i = 0; i < Sets.length; i++) {
    ipass = $(Sets[i]).find("testcase[result='PASS']").length;
    ifail = $(Sets[i]).find("testcase[result='FAIL']").length;
    resultXML += "<tr>";
    resultXML += "<td>" + $(Sets[i]).attr('name') + "</td>";
    resultXML += "<td style='color:green;'>" + ipass + "</td><td style='color:red;'>" + ifail + "</td>";
    resultXML += "</tr>";
  }
  resultXML += "</table>";
  if (ifail > 0) {
    resultXML += "<section id='failedlist'>";
    resultXML += "<h2>Fails</h2>";
    resultXML += "<ul>";
    for (i = 0; i < failList.length; i++) {
      var ts = $(failList[i]).find("test_script_entry");
      if (ts.length > 0) {
        var t = ts.get(0);
        resultXML += "<li style='color:red;'>" + $(t).text() + "</li>";
      }
    }
    resultXML += "</ul>";
    resultXML += "</section>";
  }
  resultXML += "<h2>Test Result XML</h2>";
  resultXML += "<textarea id='results' style='width: 100%; height: 70%;' name='filecontent' disabled='disabled'>" + (new XMLSerializer()).serializeToString(xmldoc) + "</textarea>";
  try {
    testFrame.contentWindow.document.open();
    testFrame.contentWindow.document.writeln(resultXML);
    testFrame.contentWindow.document.close();
  } catch (e) {
    if (testFrame.attachEvent) {
      testFrame.attachEvent("onload", function() {
        testFrame.contentWindow.document.open();
        testFrame.contentWindow.document.writeln(resultXML);
        testFrame.contentWindow.document.close();
        testFrame.onload = '';
      });
    } else {
      testFrame.onload = function() {
        testFrame.contentWindow.document.open();
        testFrame.contentWindow.document.writeln(resultXML);
        testFrame.contentWindow.document.close();
        testFrame.onload = '';
      };
    }
    testFrame.src = '';
  }
}

function init_message_frame() {
  messageFrame = document.getElementById('messageframe');
  messageWin = messageFrame.contentWindow;
  messageNode = messageWin.document.getElementById('message_div');
  if (null == messageNode) {
    messageNode = messageWin.document.createElement("div");
    messageNode.id = "message_div";
    messageWin.document.body.appendChild(messageNode);
    messageNode.innerHTML = "Message Area";
  }
  return messageNode;
}

function print_error_log(command, message) {
  messageFrame = document.getElementById('messageframe');
  messageFrame.height = 160 + "px";
  messageNode = init_message_frame();
  messageNode.innerHTML = "Message Area<div id=\"log_title\"></div><br/>Command: <div id=\"log_command\">" + command + "</div><br/>Message: <div id=\"log_message\">" + message + "</div>";
}

function save_session_id(session_id) {
  statusFrame = document.getElementById('statusframe');
  statusFrame.height = 270 + "px";
  statusWin = statusFrame.contentWindow;
  sessionIdNode = statusWin.document.getElementById('session_id_div');
  if (null == sessionIdNode) {
    sessionIdNode = statusWin.document.createElement("div");
    sessionIdNode.id = "session_id_div";
    statusWin.document.body.appendChild(sessionIdNode);
    sessionIdNode.innerHTML = "Session ID: <div id=\"session_id\">" + session_id + "</div><br/><div id=\"execution_progress\"></div><br/>";
  }
}

function init_status_frame() {
  statusFrame = document.getElementById('statusframe');
  statusWin = statusFrame.contentWindow;
  statusNode = statusWin.document.getElementById('status_div');
  if (null == statusNode) {
    statusNode = statusWin.document.createElement("div");
    statusNode.id = "status_div";
    statusWin.document.body.appendChild(statusNode);
  }
  return statusNode;
}

$(document).ready(function() {
  $("#backbutton").bind("click", initSelectionPage);
  $("#closewindowbutton").click(function() {
    window.open('', '_self', '');
    window.close()
  });
  $("#suitelist").bind("change", suiteUpdate);
  $("#navbuttonup").bind("click", suiteUpdateButtonUp);
  $("#navbuttondown").bind("click", suiteUpdateButtonDown);
  $("#exemanualradio").bind("click", exeManualRadio);
  $("#exeautoradio").bind("click", exeAutoRadio);
  $("#iframeradio").bind("click", iFrameRadio);
  $("#newwinradio").bind("click", newWinRadio);
  $("#viewbutton").bind("click", showCases);
  $("#runbutton").bind("click", startTest);
  preCheck();
});
