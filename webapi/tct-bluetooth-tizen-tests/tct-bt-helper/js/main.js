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



*/

var serviceHandler = null;

function discoverDevicesError() {
    alert("Error discoverDevices");
}

function setPoweredError() {
    alert("Error setPowered");
}

function startDiscoveryDevice() {
    var length, k;
    alert("searching - it's gona take about 10 seconds");
    var discoverDevicesSuccessCallback = {
            onstarted: function() {
            },
            ondevicefound: function(device) {
            },
            ondevicedisappeared: function(address) {
            },
            onfinished: function(devices) {
                length = devices.length;
                document.getElementById("devicesList").options.length = 0;
                for (k = 0; k < length; k++) {
                    document.getElementById("devicesList").options[k] = new Option(devices[k].address + " - " + devices[k].name, devices[k].address);
                }
                alert("search completed");
            }
        };
    adapter.discoverDevices(discoverDevicesSuccessCallback, discoverDevicesError);
}

function registerServiceSuccessCallback(handler) {
    serviceHandler = handler;
    handler.onconnect = function(socket) {
        var textmsg = "Test", sendtextmsg = [], length, i;
        length = textmsg.length;
        for (i = 0; i < length; i++) {
            sendtextmsg[i] = textmsg.charCodeAt(i);
        }
        socket.writeData(sendtextmsg);
    }
    alert("service registered");
}

function registerServiceError() {
    alert("Error registerService");
}

function startRegisterService() {
    adapter.registerRFCOMMServiceByUUID(document.getElementById("serviceTxt").value,"Chat service",registerServiceSuccessCallback,registerServiceError);
}

function discover() {
    adapter = tizen.bluetooth.getDefaultAdapter();
    adapter.setPowered(true, startDiscoveryDevice, setPoweredError)
}

function registerService() {
    adapter = tizen.bluetooth.getDefaultAdapter();
    adapter.setPowered(true,startRegisterService,setPoweredError);
}

function unregisterServiceSuccessCallback() {
    chatServiceHandler = null;
    alert("Service is unregistered.");
}

function unregisterServiceError() {
    alert("Error unregisterService");
}

function unregisterService() {
    if (serviceHandler != null) {
         serviceHandler.unregister(unregisterServiceSuccessCallback,unregisterServiceError);
    }
}

function createBondingError() {
    alert("Error createBonding");
}

function getDeviceError() {
    alert("Error getDevice");
}

function connectError() {
    alert("Error connectToServiceByUUID");
}

function connectCallback(device) {
    if (device != null && device.uuids.indexOf(document.getElementById("serviceTxt").value) !== -1) {
        // open socket
            device.connectToServiceByUUID(document.getElementById("serviceTxt").value, function() {
                alert("connected");
            },connectError);
    } else {
        alert("device UUID is null");
    }
}

function getDeviceCallback() {
    adapter.getDevice(document.getElementById("devicesList").value, connectCallback, getDeviceError);
}

function createBondingCallback() {
    adapter.createBonding(document.getElementById("devicesList").value, getDeviceCallback, createBondingError);
}

function connectService() {
    adapter = tizen.bluetooth.getDefaultAdapter();
    adapter.setPowered(true, createBondingCallback, setPoweredError);
}
