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

var serverConnected = false;
var clientConnected = false;
var globalSocket = null;
var adapter = null;
var type = null;

$(document).delegate("#main", "pageinit", function() {
    $("#server").bind("vclick", function() {
        setListener();
        startServer();
        $("#client").addClass("ui-disabled");
        $("#disconnect").removeClass("ui-disabled");
        type = "server";
    });
    $("#client").bind("vclick", function() {
        setListener();
        connectToServer();
        $("#server").addClass("ui-disabled");
        $("#disconnect").removeClass("ui-disabled");
        type = "client";
    });
    $("#send").bind("vclick", function() {
        if(type == "server")
            sendMsgS();
        if(type == "client")
            sendMsgC();
    });
    $("#disconnect").bind("vclick", function() {
        adapter.unsetChangeListener();
        disconnect();
        serverConnected = false;
        clientConnected = false;
        type = null;
        $("#server").removeClass("ui-disabled");
        $("#client").removeClass("ui-disabled");
        $("#disconnect").addClass("ui-disabled");
        $("#send").addClass("ui-disabled");
    });
    $("#send").addClass("ui-disabled");
    $("#disconnect").addClass("ui-disabled");
});

function setListener() {
    var changeListener = {
        onstatechanged: function(powered) {
            console.log ("Power state is changed into: " + powered);
        },
        onnamechanged: function(name) {
            console.log("Name is changed to: " + name);
        },
        onvisibilitychanged: function(visible) {
            console.log("Visibility is changed into: " + visible);
        }
    };
    adapter = tizen.bluetooth.getDefaultAdapter();
    adapter.setChangeListener(changeListener);
}

function startServer() {
    if (clientConnected) {
        alert("Already connected");
        return;
    }
    adapter = tizen.bluetooth.getDefaultAdapter();
    console.log("StartServer Name : " + "BehaviorBT");
    function registerSuccessCallback(handler) {
        chatServiceHandler = handler;
        alert("Wait for client...");
        console.log("Chat service register success");
        chatServiceHandler.onconnect = function(socket) {
            globalSocket = socket;
            var peerDevice = socket.peer;
            alert("Socket state:" + socket.state + " [" + peerDevice.name + "(" + peerDevice.address + ")]");
            console.log("Server connented address(" + socket.peer.address + ")" + " connected service uuid: " + socket.uuid);
            clientConnected = true;
            $("#send").removeClass("ui-disabled");
            socket.onmessage = function() {
                var data = socket.readData();
                var recvmsg = "";
                for (var i = 0; i < data.length;i++) {
                    recvmsg += String.fromCharCode(data[i]);
                }
                recvmsg = decodeURIComponent(recvmsg);
                document.getElementById("rmsg").innerHTML = "Client : " + recvmsg;
                alert("Client : " + recvmsg);
            };
            socket.onerror = function(e) {
                console.log("Socket error");
                clientConnected = false;
                socket.close();
            };
            socket.onclose = function() {
                clientConnected = false;
                console.log("Socket disconnected");
            };
        };
    };
    function onError(e) {
        console.log("Operation error");
        clientConnected = false;
    }
    function setVisibleAndRegister() {
        adapter.setVisible(true, function() {
            adapter.registerRFCOMMServiceByUUID(
                    "5BCE9431-6C75-32AB-AFE0-2EC108A30860",
                    "My service",
                    registerSuccessCallback,
                    onError
            );
        });
    }
    function setNameWithTimer() {
        adapter.setName("BehaviorBT", function() {
            console.log("Set name ok");
            setVisibleAndRegister();
        }, onError);
    }
    function onSuccess() {
        console.log("Turn on success");
        setTimeout(setNameWithTimer, 3000);
    }
    adapter.setPowered(true, onSuccess, function() {
        console.log("Device is busy");
        onError();
    });
}

function connectToServer() {
    if (serverConnected) {
        alert("Already connected");
        return;
    }
    console.log("Connect to Server " + "BehaviorBT");
    adapter = tizen.bluetooth.getDefaultAdapter();
    function onSocketConnected(socket) {
        globalSocket = socket;
        var peerDevice = socket.peer;
        alert("Socket state:" + socket.state + " [" + peerDevice.name + "(" + peerDevice.address + ")]");
        console.log("Server connented address(" + socket.peer.address + ")" + " connected service uuid: " + socket.uuid);
        serverConnected = true;
        $("#send").removeClass("ui-disabled");
        socket.onmessage = function() {
            var data = socket.readData();
            var recvmsg = "";
            for (var i = 0; i < data.length;i++) {
                recvmsg += String.fromCharCode(data[i]);
            }
            recvmsg = decodeURIComponent(recvmsg);
            document.getElementById("rmsg").innerHTML = "Server : " + recvmsg;
            alert("Server : " + recvmsg);
        };
        socket.onerror = function(e) {
            console.log("Socket error");
            serverConnected = false;
            socket.close();
        };
        socket.onclose = function() {
            serverConnected = false;
            console.log("Socket disconnected");
        };
    }
    function onSocketError(e) {
        console.log("Socket error: " + e.message);
        serverConnected = false;
    }
    function onError(e) {
        console.log("Operation error");
        serverConnected = false;
    }
    function getDeviceSuccessCB(device) {
        if (device != null) {
            console.log("Get device and then try to connect: " + "5BCE9431-6C75-32AB-AFE0-2EC108A30860");
            device.connectToServiceByUUID("5BCE9431-6C75-32AB-AFE0-2EC108A30860", onSocketConnected, onSocketError);
        }
        else
            console.log("Get device infomration error");
    }
    function bondSuccess(device) {
        console.log("Bond success!");
        adapter.getDevice(device.address, getDeviceSuccessCB, onError);
    }
    var discoverDevicesSuccessCallback = {
            onstarted : function() {
                alert("Device discovery start!");
            },
            ondevicefound: function (device) {
                var msg = device.name + "("+ device.address + ")";
                if (device.name == "BehaviorBT") {
                    adapter.stopDiscovery(function() {});
                    console.log("Try to connect");
                    if (device.isBonded == true) {
                        console.log("Try to get device information");
                        adapter.getDevice(device.address, getDeviceSuccessCB, onError);
                    }
                    else {
                        console.log("Try to bond");
                        adapter.createBonding(device.address, bondSuccess, onError);
                    }
                }
                else
                    console.log(msg + " found");
            },
            ondevicedisappeared: function(device) {},
            onfinished : function (devices) {
                alert("Discovery finished");
            }
    };
    function onSuccess() {
        console.log("Turn on success");
        adapter.discoverDevices(discoverDevicesSuccessCallback, onError);
    }
    console.log("Try to turn on");
    adapter.setPowered(true, onSuccess, onError);
}

function sendMsgS() {
    var inputText = document.getElementById("wmsg");
    var textmsg = inputText.value;
    if(textmsg.length != 0){
        var sendtextmsg = new Array();
        textmsg = encodeURIComponent(textmsg);
        for (var i = 0; i < textmsg.length; i++)
            sendtextmsg[i] = textmsg.charCodeAt(i);
        if (globalSocket != null && clientConnected == true) {
            var length = globalSocket.writeData(sendtextmsg);
            if (length != 0)
                console.log("writeData");
            else
                console.log("writeData fail");
        }
        else
            console.log("socket is not set");
    }
    else
        alert("Fill in Send Message");
}

function sendMsgC() {
    var inputText = document.getElementById("wmsg");
    var textmsg = inputText.value;
    if(textmsg.length != 0){
        var sendtextmsg = new Array();
        textmsg = encodeURIComponent(textmsg);
        for (var i = 0; i < textmsg.length; i++)
            sendtextmsg[i] = textmsg.charCodeAt(i);
        if (globalSocket != null && serverConnected == true) {
            var length = globalSocket.writeData(sendtextmsg);
            if (length != 0)
                console.log("writeData");
            else
                console.log("writeData fail");
        }
        else
            console.log("socket is not set");
    }
    else
        alert("Fill in Send Message");
}

function disconnect() {
    if (serverConnected == true && globalSocket != null) {
        try {
            globalSocket.close();
            alert("Disconnected");
        }
        catch(e) {
            console.log(e.message);
        }
    }
    try {
        if (adapter != null)
            adapter.setPowered(
                    false,
                    function() {
                        alert("Bluetooth Power Off");
                        globalSocket = null;
                        serverConnected = false;
                        clientConnected = false;
                        adapter = null;
                        type = null;
                    }, function(e) {
                        console.log(e.message);
                    }
            );
    }
    catch(e) {
        console.log(e.message);
    }
}
