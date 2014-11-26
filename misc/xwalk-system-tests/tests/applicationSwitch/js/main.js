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
       Xu, Jianfeng <jianfengx.xu@intel.com>

 */

var app, text;
function CurrentApp () {
  try {
    app = tizen.application.getCurrentApplication();
    text = "<tr class='tr0'><td width='30%'>Current App ID</td><td width='20%'>Current App Name</td><td width='20%'>Current App Version</td><td>Current App PackageId</td></tr><tr class='tr2'><td>" + app.appInfo.id + "</td><td>" + app.appInfo.name + "</td><td>" + app.appInfo.version + "</td><td>" + app.appInfo.packageId + "</td></tr>";
    $("#result").html(text);
  } catch (e) {
    $("#result").html("error : " + e.message);
  }
}

function hideApp () {
  app.hide();
  setTimeout(function(){
    app.show();
  }, 5000);
}

var init = function () {
  CurrentApp();
}

$(document).bind("pageinit", init);
