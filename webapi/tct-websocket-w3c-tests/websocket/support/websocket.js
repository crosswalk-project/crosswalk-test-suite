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
        Li, HaoX <haox.li@intel.com>

*/

var SERVER_NAME = "127.0.0.1";
var _PORT = 8081;
var _URL = "ws://" + SERVER_NAME + ":" + _PORT;

var WSS_SERVER_NAME = "127.0.0.1";
var WSS_PORT = 8443;
var WSS_PATH = "echo";
var WSS_URL = "wss://" + WSS_SERVER_NAME + ":" + WSS_PORT + "/" + WSS_PATH;

var wsocket;

var browser = (function getBrowser() {
    if (navigator.userAgent.indexOf("WebKit") > 0) {
        return "webkit";
    }
    if (navigator.userAgent.indexOf("Firefox") > 0) {
        return "moz";
    }
    if (navigator.userAgent.indexOf("MSIE") > 0) {
        return "msie";
    }
    if (navigator.userAgent.indexOf("Safari") > 0) {
        return "safari";
    }
    if (navigator.userAgent.indexOf("Camino") > 0) {
        return "camino";
    }
    if (navigator.userAgent.indexOf("Gecko/") > 0) {
        return "gecko";
    }
})();

function CreateWebSocket() {
    if (window["WebSocket"]) {
        wsocket = new WebSocket(_URL, 'fragmentation-test');
    }
    else if (window["MozWebSocket"]) {
        wsocket = new MozWebSocket(_URL);
    }
    return wsocket;
}
function CreateWebSocket_url(url) {
    if (window["WebSocket"]) {
        wsocket = new WebSocket(url);
    }
    else if (window["MozWebSocket"]) {
        wsocket = new MozWebSocket(url);
    }
    return wsocket;
}

function showmsg(msg) {
    document.getElementById("test").innerHTML += msg + "<br/>";
}

function binaryToBlob(data) {
    var arr = new Uint8Array(data.length);
    for (var i = 0, l = data.length; i < l; i++) {
        arr[i] = data.charCodeAt(i);
    }
    return new Blob([arr.buffer]);
}
