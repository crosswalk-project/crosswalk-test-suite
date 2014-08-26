/*
Copyright (c) 2013 Samsung Electronics Co., Ltd.

Licensed under the Apache License, Version 2.0 (the License);
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Authors:
        Choi, Jongheon <j-h.choi@samsung.com>

 */

var writeMessage = "", readMessage = "", newMessage = "";
var nfcFlag;

$(document).delegate("#main", "pageinit", function() {
    $("#read").bind("vclick", function() {
        nfcFlag = false;
        alert("Read NFC Tag\nPlace the NFC Tag to device");
    });
    $("#write").bind("vclick", function() {
        writeMsg();
        if(writeMessage != "") {
            nfcFlag = true;
            alert("Write NFC Tag\nPlace the NFC Tag to device");
        }
    });
    $("#communicate").bind("vclick", function() {
        writeMsg();
        if(writeMessage != "")
            alert("Peer to Peer NFC\nConnected two device which are operated NFC");
    });
    try {
        tizen.nfc.setExclusiveMode(true) ;
    } catch (err) {
        console.log (err.name + ": " + err.message);
    }
    setPower(function(){
        setTagListener();
        setPeerListener();    
    });
});

function writeMsg() {
    newMessage = new tizen.NDEFMessage();
    writeMessage = $("#wmsg").val();
    if(writeMessage == "") {
        alert("Fill in NFC Write Message");
        nfcFlag = null;
    }
    else
        newMessage.records[0] = new tizen.NDEFRecordText(writeMessage, "en-US");
}

function setPower(onpowered) {
    var gNfcAdapter;
    try {
        gNfcAdapter = tizen.nfc.getDefaultAdapter();
        if (!gNfcAdapter.powered) {
            gNfcAdapter.setPowered(
                    true,
                    function () {onpowered();console.log("Power on succeed");},
                    function () {console.log("Power on failed")});
        } else {
            onpowered();
        }
    } catch (err) {
        console.log (err.name + ": " + err.message);
    }
}

function setTagListener() {
    var adapter = tizen.nfc.getDefaultAdapter();
    var onSuccessCB = {
            onattach : function(nfcTag) {
                console.log("NFC Tag's type is " + nfcTag.type);
                if(nfcFlag == false)
                {
                    try {
                        nfcTag.readNDEF(
                                function(message){
                                    readMessage = message.records[0].text;
                                    alert("Read message : " + readMessage);
                                    document.getElementById("rmsg").innerHTML = readMessage;
                                },
                                function(e){
                                    console.log(e.message);
                                });
                    } catch (err) {
                        console.log (err.name + ": " + err.message);
                    }
                }
                if(nfcFlag == true)
                {
                    try {
                        nfcTag.writeNDEF(
                                newMessage,
                                function(){
                                    alert("Write message : " + writeMessage);
                                },
                                function(e){
                                    console.log(e.message);
                                });
                    } catch (err) {
                        console.log (err.name + ": " + err.message);
                    }
                }
            },
            ondetach : function() {
                console.log("NFC Tag is detached");
            }};
    function unsetListen() {
        adapter.unsetTagListener();
    }
    adapter.setTagListener(onSuccessCB);
}

function setPeerListener() {
    var adapter = tizen.nfc.getDefaultAdapter();
    var onSuccessCB = {
            onattach : function(nfcPeer) {
                console.log("NFC Target is detected");

                nfcPeer.setReceiveNDEFListener(
                        function(message){
                            readMessage = message.records[0].text;
                            alert("Receive message : " + readMessage);
                            document.getElementById("rmsg").innerHTML = readMessage;
                            nfcPeer.unsetReceiveNDEFListener();
                        });
                nfcPeer.sendNDEF(
                        newMessage,
                        function(){
                            console.log("Send message");
                        },
                        function(e){
                            console.log(e.message);
                        });
            },
            ondetach : function() {
                console.log("NFC Target is detached");
            }};
    function unsetListen() {
        adapter.unsetPeerListener();
    }
    adapter.setPeerListener(onSuccessCB);
}