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
        Xu, Jianfeng <jianfengx.xu@intel.com>

*/


var text = "";
var calllist = "";
function start(name) {
  if (name == "event") {
    calllist.innerHTML = "The history is updated, Getting new history.";
  } else {
    calllist.innerHTML = "Getting Call History";
  }
  tizen.callhistory.find(onSuccess, onError, null, new tizen.SortMode('startTime', 'DESC'));
}

function onSuccess(results) {
  if (results.length == 0) {
    calllist.innerHTML = "No Call History."
  } else {
    text = "";
    for (var i=0; i<results.length; i++) {
      text = text + i + ". " + results[i].toString() + "<br>";
    }
    calllist.innerHTML = text;
  }
} 

function onError() {
  calllist.innerHTML = "Query failed" + error.name;
}

function onSuccessCallback() {
  start("event");
}

function end () {
  tizen.callhistory.removeAll(removeSuccess, removeError);
}

function removeSuccess () {
  calllist.innerHTML = "Remove Success";
}

function removeError () {
  calllist.innerHTML = "Remove failed" + error.name;
}

$(document).ready(function(){
    calllist = document.getElementById("calllist");
    start();
    var callHistoryListener = {
				onadded: onSuccessCallback,
				onchanged: onSuccessCallback,
				onremoved: onSuccessCallback
			};
    tizen.callhistory.addChangeListener(callHistoryListener);
});
