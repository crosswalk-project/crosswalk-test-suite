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
        Wang, Hongjuan <hongjuanx.wang@intel.com>

*/

var deviceReady = false;
function init() {
  document.addEventListener("deviceready", function() {
    deviceReady = true;
  }, false);
  window.setTimeout(function() {
    if (!deviceReady) {
      alert("Error: Apache Cordova did not initialize.  Demo will not run correctly.");
    }
  },1000);
}

var beep = function(){
  navigator.notification.beep(3);
};

var vibrate = function() {
  navigator.notification.vibrate(3000);
}

var confirmDialogB = function(message, title, buttons) {
  navigator.notification.confirm(message,
    function(r) {
      if(r===0){
        console.log("Dismissed dialog without making a selection.");
        alert("Dismissed dialog without making a selection.");
      }else{
        console.log("You selected " + r);
        alert("You selected " + buttons[r-1]);
      }
    },
  title,
  buttons);
};

var promptDialog = function(message, title, buttons) {
navigator.notification.prompt(message,
  function(r) {
    if(r && r.buttonIndex===0){
      var msg = "Dismissed dialog";
      if( r.input1 ){
          msg+=" with input: " + r.input1
      }
      console.log(msg);
      alert(msg);
    }else{
      console.log("You selected " + r.buttonIndex + " and entered: " + r.input1);
      alert("You selected " + buttons[r.buttonIndex-1] + " and entered: " + r.input1);
    }
  },
  title,
  buttons);
};
