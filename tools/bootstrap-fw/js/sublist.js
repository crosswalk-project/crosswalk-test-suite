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

var lstorage = window.localStorage;
var tid = location.search.split('=')[1];
var casearr = JSON.parse(lstorage.getItem(tid));
var sid = casearr.sid;
var purpose = casearr.purpose;

function back() {
  window.location.href = "../../tests_list.html?sid=" + sid;
}

function help() {
  showMessage("help", popup_info);
}

function listSubcase() {
  var setarr = JSON.parse(lstorage.getItem(sid));
  var tbg = "color-swatches " + setarr.background;
  var ticon = "glyphicon " + setarr.icon;
  var tnum = parseInt(casearr.num);
  var passnum = failnum = 0;
  var tresult = subresult = "";
  var subtests = getApps("subcase.json", "json");
  var i = 0;
  $(subtests).each(function() {
      i++;
      var subkey = tid + i;
      if(lstorage.getItem(subkey) != null) {
        subresult = JSON.parse(lstorage.getItem(subkey)).result;
      }
      var subid = $(this).attr("id");
      var suburl = $(this).attr("entry") + "?subkey=" + subkey;
      passnum = subresult == "pass" ? passnum + 1 : passnum;
      failnum = subresult == "fail" ? failnum + 1 : failnum;
      var midstyle = 'style=\"height:26px; line-height:26px\"';
      var testline = '<div class=\"col-md-3\">\n<div class=\"media ' + subresult + '\">\n'
                    + '<a class=\"pull-left\" href=\"' + suburl + '\">\n'
                    + '<div class=\"' + tbg + '\"><span class=\"' + ticon + '\"></span></div>\n</a>\n'
                    + '<div class=\"media-body\">\n'
                    + '<a href=\"' + suburl +'\"><h5 class=\"media-heading\"' + midstyle + '>' + subid + '</h5></a>\n'
                    + '</div>\n</div>\n</div>\n';
      $('#mytest').append(testline);
      if(lstorage.getItem(subkey) == null) {
        var subcasearr = {id: subid, result:"", tid: tid}; //result: "pass", "fail", ""
        lstorage.setItem(subkey, JSON.stringify(subcasearr)); //store subcase info
      }
  });
  if(tnum != i) {
    showMessage("error", "The number of subcase in tests.xml does not match that in subsuite.json!");
  }
  if(passnum == 0 && failnum == 0)
    tresult = "";
  else if(tnum == passnum)
    tresult = "pass";
  else
    tresult = "fail";
  var newcasearr = {purpose:purpose, num:tnum, pass:passnum, fail:failnum, result:tresult, sid:sid};
  lstorage.setItem(tid, JSON.stringify(newcasearr)); //update case result
}

$(document).ready(function(){
  popup_info = $("#popup_info").html();
  $("#subhelp").click(help);
  $("#subback").click(back);
  //document.getElementById('app-version').innerHTML = lstorage.getItem("app-version");
  $('#casename').append(tid);
  document.title = tid;
  listSubcase();
});
