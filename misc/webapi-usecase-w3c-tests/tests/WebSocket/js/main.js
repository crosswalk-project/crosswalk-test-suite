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

$("#send").live("tap", function () {
    var flag = false;
    try {
        window.webSocket = new WebSocket('ws://127.0.0.1:8081');
        webSocket.addEventListener('open', function (evt) {
            flag = true;
            $("#chatbox").text("WebSocket - open.\n" + $("#chatbox").text());
            webSocket.send($("#socketinput").attr("value"));
            $("#chatbox").text("WebSocket - send - "  + $("#socketinput").attr("value") + "\n" + $("#chatbox").text());
            $("#socketinput").attr("value", "");
        }, true);
        webSocket.addEventListener('message', function (evt) {
            $("#chatbox").text("WebSocket - recive - "  + evt.data + "\n" + $("#chatbox").text());
        }, true);
        webSocket.addEventListener('close', function (evt) {
            if (!flag) {
                $("#chatbox").text("WebSocket - can't open.\n" + $("#chatbox").text());
            }
        }, true);
    } catch (err) {
        $("#chatbox").text(err + "\n" + $("#chatbox").text());
    }
});
