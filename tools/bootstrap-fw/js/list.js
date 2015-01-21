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
var sid = location.search.split('=')[1];

function listTest() {
  var setarr = JSON.parse(lstorage.getItem(sid));
  var sname = setarr.name;
  document.title = sname;
  $('#setname').append(sname);
  if (lstorage.getItem("test-suite") == "DemoExpress") {
    showMessage("help", sname + " Demos");
  } else {
    showMessage("help", sname + " Usecases");
  }
  var tids = setarr.tids.split(',');
  var tbg = "color-swatches " + setarr.background;
  var ticon = "glyphicon " + setarr.icon;
  var passnum = failnum = 0;
  var totalnum = 0;
  for(var i = 0; i < tids.length; i++) {
    var tid = tids[i];
    var casearr = JSON.parse(lstorage.getItem(tid));
    var tnum = parseInt(casearr.num);
    totalnum += tnum;
    var tpass = parseInt(casearr.pass);
    var tfail = parseInt(casearr.fail);
    var tresult = casearr.result;
    var turl = "samples/" + tid + "/index.html?tid=" + tid;
    var resultline = "";
    var midstyle = 'style=\"height:26px; line-height:26px\"';
    if(tnum > 1) {
      passnum = passnum + casearr.pass;
      failnum = failnum + casearr.fail;
    } else {
      passnum = tresult == "pass" ? passnum + 1 : passnum;
      failnum = tresult == "fail" ? failnum + 1 : failnum;
   } 
   if(tresult != "" && tnum > 1) {
      resultline = '<span class=\"label label-primary\" style=\"margin-right:5px\">Total:' + tnum + '</span>\n'
                    + '<span class=\"label label-success\">' + tpass + '</span>\n'
                    + '<span class=\"label label-danger\">' + tfail + '</span>\n'
                    + '<span class=\"label label-default\">' + (tnum-tpass-tfail) + '</span>\n';
      midstyle = "";
    }
    var testline = '<div class=\"col-md-3\">\n<div class=\"media ' + tresult + '\">\n'
                  + '<a class=\"pull-left\" href=\"' + turl + '\">\n'
                  + '<div class=\"' + tbg + '\"><span class=\"' + ticon + '\"></span></div>\n</a>\n'
                  + '<div class=\"media-body\">\n'
                  + '<a href=\"' + turl +'\"><h5 class=\"media-heading\"'+ midstyle +'>' + tid + '</h5></a>\n'
                  + resultline
                  + '</div>\n</div>\n</div>\n';
    $('#mytest').append(testline);
  }
  if(passnum == 0 && failnum == 0)
    passnum = failnum = "";
  var setresarr = {totalnum:totalnum, passnum:passnum, failnum:failnum};
  lstorage.setItem(sid + "res", JSON.stringify(setresarr));
}

$(document).ready(function(){
  document.getElementById('app-version').innerHTML = lstorage.getItem("app-version");
  listTest();
});



