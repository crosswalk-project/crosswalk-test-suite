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
        Liu,Yun <yunx.liu@intel.com>
*/

var showId;
var pc1, pc2, dc1, dc2;
var pc1_offer;
var pc2_answer;
var datawindow = document.getElementById("datawindow");
var pc1_input = document.getElementById("pc1_input");
var pc2_input = document.getElementById("pc1_input");
var startbutton = document.getElementById("startbutton");
var stopbutton = document.getElementById("stopbutton");
var pc1_send = document.getElementById("pc1_send");
var pc2_send = document.getElementById("pc2_send");
startbutton.onclick = start;
stopbutton.onclick = stop;
pc1_send.onclick = pc1Send;
pc2_send.onclick = pc2Send;
stopbutton.disabled = true;
pc1_send.disabled = true;
pc2_send.disabled = true;

function show() {
  fancy_log("The first channel onDataChannel cannot be fired.", "black");
  clearTimeout(showId);
}

function fancy_log(msg,color) {
  clearTimeout(showId);
  var message = '<span style="color: ' + color + ';">' + msg + '</span>';
  datawindow.innerHTML = "<p>" + message + "</p>" + datawindow.innerHTML;
}

function pc1Send() {
  dc1.send(pc1_input.value);
  pc1_input.value = "";
}

function pc2Send() {
  dc2.send(pc2_input.value);
  pc2_input.value = "";
}

function requestFailed(code) {
  fancy_log("Failure callback: " + code, "black");
}

// pc1.createOffer finished, call pc1.setLocal
function requestSuccessed1(offer) {
  pc1_offer = offer;
  pc1.setLocalDescription(offer, requestSuccessed2, requestFailed);
}

// pc1.setLocal finished, call pc2.setRemote
function requestSuccessed2() {
  pc2.setRemoteDescription(pc1_offer, requestSuccessed3, requestFailed);
};

// pc2.setRemote finished, call pc2.createAnswer
function requestSuccessed3() {
  pc2.createAnswer(requestSuccessed4, requestFailed);
}

// pc2.createAnswer finished, call pc2.setLocal
function requestSuccessed4(answer) {
  pc2_answer = answer;
  pc2.setLocalDescription(answer, requestSuccessed5, requestFailed);
}

// pc2.setLocal finished, call pc1.setRemote
function requestSuccessed5() {
  pc1.setRemoteDescription(pc2_answer, function() {}, requestFailed);
}

function gotLocalCandidate(event) {
  if (event.candidate) {
    pc2.addIceCandidate(event.candidate);
  }
}

function gotRemoteIceCandidate(event) {
  if (event.candidate) {
    pc1.addIceCandidate(event.candidate);
  }
}

function handleSendChannelStateChange1() {
  var readyState = dc1.readyState;
  fancy_log("pc1 Channel state is: " + readyState, "black");
  if (readyState == "open") {
    startbutton.disabled = true;
    stopbutton.disabled = false;
    pc1_send.disabled = false;
  } else {
    startbutton.disabled = false;
    stopbutton.disabled = true;
    pc1_send.disabled = true;
  }
}

function handleSendChannelStateChange2() {
  var readyState = dc2.readyState;
  fancy_log("pc2 Channel state is: " + readyState, "black");
  if (readyState == "open") {
    startbutton.disabled = true;
    stopbutton.disabled = false;
    pc2_send.disabled = true;
  } else {
    startbutton.disabled = false;
    stopbutton.disabled = true;
    pc2_send.disabled = true;
  }
}

function start() {
  datawindow.innerHTML = "Connecting......";
  startbutton.disabled = true;
  clearTimeout(showId);
  showId = setTimeout("show()", 10000);

  pc1 = new webkitRTCPeerConnection(null, {optional: [{RtpDataChannels: true}]});
  dc1 = pc1.createDataChannel("This is pc1");
  dc1.onopen = handleSendChannelStateChange1;
  dc1.onclose = handleSendChannelStateChange1;
  pc1.onicecandidate = gotLocalCandidate;
  pc1.ondatachannel = function(event) {
    clearTimeout(showId);
    dc1 = event.channel;

    dc1.onmessage = function(evt) {
      fancy_log("pc1 received message: " + evt.data, "blue");
    };
    dc1.onopen = function() {
      fancy_log("pc2 can send message to pc1 now!", "black");
    };
    dc1.onclose = function() {
      fancy_log("The pc1 datachannel connection is closed, stop send message now!", "black");
    };
  };
  pc2 = new webkitRTCPeerConnection(null, {optional: [{RtpDataChannels: true}]});
  dc2 = pc2.createDataChannel("This is pc2");
  dc2.onopen = handleSendChannelStateChange2;
  dc2.onclose = handleSendChannelStateChange2;
  pc2.onicecandidate = gotRemoteIceCandidate;
  pc2.ondatachannel = function(event) {
    dc2 = event.channel;

    dc2.onmessage = function(evt) {
      fancy_log("pc2 received message: " + evt.data, "blue");
    };
    dc2.onopen = function() {
      fancy_log("pc1 can send message to pc2 now!", "black");
    };
    dc2.onclose = function() {
      fancy_log("The pc2 datachannel connection is closed, stop send message now!", "black");
    };
  };
  pc1.createOffer(requestSuccessed1, requestFailed);
}

function stop() {
  dc1.close();
  dc2.close();
  pc1.close();
  pc2.close();
}
