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
        Shentu, Jiazhen <jiazhenx.shentu@intel.com>

*/
var testFlag = {
    green: false,
    red: false,
    blue: false
};
var showId;

function status() {
    if (testFlag.green && testFlag.red && testFlag.blue) {
        EnablePassButton();
    }
}

function show() {
    $("#chatbox").text("Timeout, please check if WebSocket server is enable.\n" + $("#chatbox").text());
    clearTimeout(showId);
    showButton();
}

function showButton() {
    $("#connect").attr('disabled', false);
    $("#disconnect").attr('disabled', true);
    $("#send").attr('disabled', true);
}

function connectWebSocket() {
    testFlag.green = true;
    clearTimeout(showId);
    showId = setTimeout("show()", 10000);
    try {
        $("#chatbox").text("Connecting......");
        window.webSocket = new WebSocket('ws://127.0.0.1:8081');
        webSocket.addEventListener('open', function (evt) {
            clearTimeout(showId);
            $("#connect").attr('disabled', true);
            $("#disconnect").attr('disabled', false);
            $("#send").attr('disabled', false);
            $("#chatbox").text("Successfully connect to WebSocket server.\n" + $("#chatbox").text());
        }, true);
        webSocket.addEventListener('message', function (evt) {
            $("#chatbox").text("WebSocket - receive - "  + evt.data + "\n" + $("#chatbox").text());
        }, true);
        webSocket.addEventListener('close', function (evt) {
            clearTimeout(showId);
            showButton();
            $("#chatbox").text("WebSocket connection is closed. "  +  evt.reason + "\n" + $("#chatbox").text());
        }, true);
    } catch (err) {
        showButton();
        $("#chatbox").text("Error: " + err + "\n" + $("#chatbox").text());
    }
    status();
}

function disconnectWebSocket() {
    testFlag.blue = true;
    webSocket.close();
    showButton();
    status();
}

function sendWebSocket() {
    testFlag.red = true;
    webSocket.send(document.getElementById("socketinput").value);
    $("#chatbox").text("WebSocket - send - "  + document.getElementById("socketinput").value + "\n" + $("#chatbox").text());
    $("#socketinput").val("");
    status();
}

$(document).ready(function() {
    DisablePassButton();
    showButton();
});
