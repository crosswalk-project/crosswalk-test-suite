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
        Zhang, Jing <jingx.zhang@intel.com>

*/


var tag = null;
var peer = null;

$(document).ready(function () {
    if(navigator.nfc.powered) {
        $("#on").button("disable");
        $("#off").button("enable");
        $("#write").button("enable");
        $("#read").button("enable");
        $("#send").button("enable");
    } else {
        $("#off").button=("disable");
        $("#on").button=("enable");
        $("#write").button("disable");
        $("#read").button("disable");
        $("#send").button("disable");
    }
});

function addMessage(obj, id) {
    document.getElementById(id).innerHTML = obj;
}

var events = [
    'poweron',
    'poweroff',
    'pollstart',
    'pollstop',
    'tagfound',
    'taglost',
    'peerfound',
    'peerlost'
];

navigator.nfc.addEventListener('tagfound', tagFound);
navigator.nfc.addEventListener('taglost', tagLost);
navigator.nfc.addEventListener('peerfound', peerFound);
navigator.nfc.addEventListener('peerlost', peerLost);

function tagFound(e) {
    tag = e.tag;
    addMessage("Tag found",'tag');
}

function tagLost(e) {
    tag = null;
    addMessage("Tag lost", 'tag');
}

function peerFound(e) {
    peer = e.peer;
    peer.addEventListener('messageread', onMessageRead);
    addMessage("Found peer device", 'peer');
}

function peerLost(e) {
    peer = null;
    addMessage("Peer device lost", 'peer');
}

function onMessageRead(e) {
    addMessage("Received message: " + JSON.stringify(e.message, 'eventLog'));
}

function readNDEF() {
    setEnvironment();
    addMessage("Waiting to read nfc tag...", 'eventLog');
    tag.readNDEF().then(function(record) {
    addMessage("Read tag succeeded: " + JSON.stringify(record), 'eventLog'); },
function(){ addMessage("Read tag failed", 'eventLog'); });
}

function writeTextNDEF() {
    setEnvironment();
    addMessage("Waiting to write nfc tag...", 'eventLog');
    var text = new NDEFRecordText("Hello World!", "en-US", "UTF-8");
    tag.writeNDEF(new NDEFMessage([text])).then(function(){addMessage("Write tag succeeded", 'eventLog'); },
function(){ addMessage("Write tag failed", 'eventLog'); });
}

function sendURINDEF() {
    setEnvironment();
    addMessage("Waiting to send URI NDEF to the peer device...", 'eventLog');
    var uri = new NDEFRecordURI("http://www.baidu.com");
    peer.sendNDEF(new NDEFMessage([uri])).then(function(){ addMessage("Send URI NDEF succeeded", 'eventLog'); },
function(){ addMessage("Send URI NDEF failed", 'eventLog'); });
}

function powerOn() {
    clearLog();
    navigator.nfc.powerOn().then(function(){
        addMessage("Power on succeeded", 'power');
        $("#on").button("disable");
        $("#off").button("enable");
        $("#write").button("enable");
        $("#read").button("enable");
        $("#send").button("enable"); },
function(){ addMessage("Power on failed", 'power'); });
}

function powerOff() {
    clearLog();
    navigator.nfc.powerOff().then(function(){
        addMessage("Power off succeeded", 'power');
        $("#on").button("enable");
        $("#off").button("disable");
        $("#write").button("disable");
        $("#read").button("disable");
        $("#send").button("disable"); },
function(){ addMessage("Power off failed", 'power'); });
}

function startPoll() {
    navigator.nfc.startPoll().then(function(){addMessage("Start poll succeeded", 'polling'); },
function(){addMessage("Start poll failed", 'polling'); });
}

function stopPoll() {
    navigator.nfc.stopPoll().then(function(){addMessage("Stop poll succeeded", 'polling'); },
function(){addMessage("Stop poll failed", 'polling'); });
}

function clearLog() {
    document.getElementById('power').innerHTML = "";
    document.getElementById('polling').innerHTML = "";
    document.getElementById('tag').innerHTML = "";
    document.getElementById('peer').innerHTML = "";
    document.getElementById('eventLog').innerHTML = "";
}

function setEnvironment() {
    clearLog();
    if(!navigator.nfc.polling) {
        startPoll();
    }
}
