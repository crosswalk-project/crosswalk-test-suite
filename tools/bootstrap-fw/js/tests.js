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
        Liu, Yun <yunx.liu@intel.com>
*/

var popup_info, tid, subid, sid, title;
var lstorage = window.localStorage;
var addr = window.location.href;
var id = location.search.split('=')[1];
var isSubcase = false;
var keyarr = JSON.parse(lstorage.getItem(id));
var purpose = keyarr.purpose;

if(location.search.indexOf('subkey=') > 0) {
  isSubcase = true;
  subid = keyarr.id;
  tid = keyarr.tid;
  title = tid + " - " + subid;
} else {
  sid = keyarr.sid;
  tid = id;
  title = tid;
}

function EnablePassButton() {
  $('#pass_button').attr('disabled', false);
}

function DisablePassButton() {
  $('#pass_button').attr('disabled', true);
}

function back() {
  var url;
  if(isSubcase) {
    url = addr.substring(0, addr.indexOf("/" + tid + "/") + tid.length + 2) + "index.html?tid=" + tid;
  } else {
    url = addr.substring(0, addr.indexOf("/samples/")) + "/tests_list.html?sid=" + sid;
  }
  window.location.href = url;
}

function reportResult(res) {
  var storearr;
  if (isSubcase) {
    storearr = {id: subid, result: res, tid: tid};
  } else {
    storearr = {purpose: purpose, num: 1, pass: "0", fail: "0", result: res, sid: sid};
  }
  lstorage.setItem(id, JSON.stringify(storearr));
  back();
}

function initStep(testname) {
  var script = document.createElement("script");
  script.type = "text/javascript";
  var str = addr.substring(0, addr.indexOf("/index.html"));
  script.src = str.replace("/samples/", "/steps/") + "/step.js";
  document.body.appendChild(script);
  script.onload = script.onreadystatechange = null;
  script.onload = script.onreadystatechange = function() {
    if (!this.readyState || this.readyState == "loaded" || this.readyState == "complete") {
      if(typeof step != "undefined") {
        addPassFailButton();
        showMessage("help", step);       
      } else {
        showMessage("help", popup_info);
      }
    }
  }
}

function addPassFailButton() {
  var casearr = JSON.parse(lstorage.getItem(id));
  if ((isSubcase == false && parseInt(casearr.num) == 1) || isSubcase) {
    $("#btn-group").html("<button id='pass_button' type='button' class='btn btn-default' onclick='javascript: reportResult(\"pass\");'><span class='glyphicon glyphicon-ok-sign'></span><span class='nbsp'>Pass</span></button><button type='button' class='btn btn-default' onclick='javascript: reportResult(\"fail\");'><span class='glyphicon glyphicon-remove-sign'></span><span class='nbsp'>Fail</span></button>" + $("#footer").html());
  }
}

function help() {
  if(typeof step != "undefined") {
    showMessage("help", step);
  } else {
    showMessage("help", popup_info);
  }
}

$(document).ready(function(){
  document.title = title;
  $("#main_page_title").text(title);
  $("#main_page_title").css({"font-weight":"bold", "font-size":"140%"});
  $("#header").addClass("navbar navbar-default navbar-fixed-top text-center");
  $("#footer").html("<div id='btn-group' class='btn-group'></div>");
  $("#btn-group").html("<button type='button' id='help' onclick='help()' class='btn btn-default' data-toggle='modal' data-target='#popup_info'><span class='glyphicon glyphicon-info-sign'></span><span class='nbsp'>Help</span></button><button type='button' class='btn btn-default' onclick='javascript: back();'><span class='glyphicon glyphicon-circle-arrow-left'></span><span class='nbsp'>Back</span></button>");
  $("#footer").addClass("container text-center");
  initStep(tid);
  popup_info = $("#popup_info").html();
});
