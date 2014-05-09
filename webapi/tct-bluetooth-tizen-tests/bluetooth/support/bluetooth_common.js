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

var globalBluetoothAdapter;

var UNKNOWN_ERR         = "UnknownError";
var TYPE_MISMATCH_ERR   = "TypeMismatchError";
var IO_ERR              = "IOError";
var INVALID_VALUES_ERR  = "InvalidValuesError";
var SECURITY_ERR        = "SecurityError";
var NOT_FOUND_ERR       = "NotFoundError";
var NOT_SUPPORT_ERR     = "NotSupportedError";

var BLUETOOTH_PROFILE_TYPE = ["HEALTH"];

var bluetooth = null;
var btdevice = null;
var ret = false;
var REMOTE_DEVICE_ADDRESS = "00:02:60:00:05:63";
var REMOTE_DEVICE_NAME = "Tcthelper";
var TEST_WRONG_UUID = "00001101-0000-0000-0000-111111111111";
var CHAT_SERVICE_UUID = "5BCE9431-6C75-32AB-AFE0-2EC108A30860";
var btAdapter = null;
var REMOTE_HEALTH_DEVICE_TYPE = 4100;


function setUnpowered (t, adapter, powerOfSuccess) {
    var powerOfError = t.step_func(function (e) {
        assert_unreached("powerOfError exception:" + e.message);
    });

    adapter.setPowered(false, powerOfSuccess, powerOfError);
}

function setPowered (t, adapter, powerOnSuccess) {
    var powerOnError = t.step_func(function (e) {
        assert_unreached("powerOnError exception:" + e.message);
    });

    adapter.setPowered(true, powerOnSuccess, powerOnError);
}

function stopDiscovery (t, adapter, stopDiscoverySuccess) {
    var stopDiscoveryError = t.step_func(function (e) {
         assert_unreached("stopDiscoveryError exception:" + e.message);
    });

    var powerOnSuccess = t.step_func(function () {
        adapter.stopDiscovery(stopDiscoverySuccess, stopDiscoveryError);
    });
    setPowered(t, adapter, powerOnSuccess);
}

function setBluetoothCleanup(obj, method) {
     add_result_callback(function (res) {
        if(obj && obj[method] && typeof obj[method] == "function") {
            try {
                obj[method](done,done);
            } catch(e) {
                done();
            }
        } else {
            done();
        }
    });
}

function setBluetoothHandlerCleanup(handler) {
    setBluetoothCleanup(handler, "unregister");
}

function setBluetoothDiscoveryCleanup(adapter) {
    setBluetoothCleanup(adapter, "stopDiscovery");
}

function check_bluetooth_device(device) {
    check_readonly(device, "name", device.name, "string", "new_name");
    check_readonly(device, "address", device.address, "string", "new_address");

    assert_true("deviceClass" in device, "No deviceClass in device");
    assert_type(device.deviceClass, "object", "type of deviceClass is not an object");

    device.deviceClass = undefined;
    assert_not_equals(device.deviceClass, undefined, "deviceClass should be readonly");

    check_readonly(device.deviceClass, "major", device.deviceClass.major, "number", (device.deviceClass.major + 1)%8);
    check_readonly(device.deviceClass, "minor", device.deviceClass.minor, "number", (device.deviceClass.minor + 1)%8);

    assert_true("services" in device.deviceClass, "No services in deviceClass");
    assert_type(device.deviceClass.services, "array", "type of services is not an array");

    device.deviceClass.services = undefined;
    assert_not_equals(device.deviceClass.services, undefined, "services should be readonly");

    assert_type(device.deviceClass.hasService, "function", "Device deviceClass.hasService type check:");
    assert_type(device.deviceClass.hasService(0), "boolean", "Device deviceClass.hasService return type check:");

    check_readonly(device, "isBonded", device.isBonded, "boolean", !(device.isBonded));
    check_readonly(device, "isTrusted", device.isTrusted, "boolean", !(device.isTrusted));
    check_readonly(device, "isConnected", device.isConnected, "boolean", !(device.isConnected));

    assert_true("uuids" in device, "No uuids in device");
    assert_type(device.uuids, "array", "type of uuids is not an array");
    device.uuids = undefined;
    assert_not_equals(device.uuids, undefined, "uuids should be readonly");

    assert_type(device.connectToServiceByUUID, "function", "Method connectToServiceByUUID does not exist.");
}

function check_bluetooth_device_array(devices) {
    assert_type(devices, "array", "Devices has wrong type.");
    assert_greater_than(devices.length, 0, "Bluetooth devices not found.");
}

function onloaded() {
    try {
        //var manager = document.getElementById('bt_plugin');
        //bluetooth = manager.createAPIObjectByFeature("http://tizen.org/apis/bluetooth");
        if(bluetooth == null) {
            bluetooth = tizen.bluetooth;
        }
        if(btAdapter == null) {
        //    btAdapter = bluetooth.adapter;
            btAdapter = bluetooth.getDefaultAdapter();
            console.log("Hello web bluetooth.adapter..." + btAdapter.address);
        }
    } catch(e) {
        //alert ("Exception : " + e.message);
        console.log("tizen.bluetooth.adapter Exception. reason : " + e.message + "(" + e.code + ")");
    }
}

/**********************************************
* tizen.bluetooth.device.connectToServiceByUUID
***********************************************/
var clientSocket = null;

function sendMessage(msg) {
    //Validate socket state, if everything is ok.
    if(clientSocket != null && clientSocket.state == "OPEN") {
        //Send
        clientSocket.writeData(msg);
    }
}

var socketConnectListener = {
    onMessage: function(socket) {
        var data = socket.readData();
        var recvmsg = "";
        for(var i = 0; i < data.length; i ++) {
            recvmsg += String.fromCharCode(data[i]);
        }
        console.log("server msg >> " + recvmsg);
    },

    onError: function(e, socket) {
        console.log("Socket Error: " + e.message);
    },

    onClose: function(socket) {
        console.log("socket disconnected.");
    }
};

function onSocketConnected(socket) {
    //Method to be invoked when socket is open.
    clientSocket = socket;
    socket.setSocketNotifyListener(socketConnectListener);
    console.log("Opening socket success.");
}

function onDeviceReady(device) {
    //Validate device and service uuid
    if(device != null && device.uuids.indexOf(CHAT_SERVICE_UUID) != -1) {
        device.connectToServiceByUUID(CHAT_SERVICE_UUID, onSocketConnected, function(e) {
            console.log("Error connecting to service. Reason: " + e.message);
        });
    } else {
        console.log("Char service is not supported by this device.");
    }
}

function onSetPowered() {
    tizen.bluetooth.adapter.getDevice(REMOTE_DEVICE_ADDRESS, onDeviceReady, function(e) {
        console.log("Error: " + e.message);
    });
}

/****************************************************
* tizen.bluetooth.adapter.registerRFCOMMServiceBYUUID
* tizen.bluetooth.adapter.unregisterRFCOMMService
*****************************************************/
var chatServiceHandler = null;

 var socketRegListener = {
   onMessage: function(socket) {
       var data = socket.readData();
       // handle message code goes here
       //....
   },
   // Something went wrong
   onError: function(e, socket) {
       console.log('Error : ' + e.message);
   },
   // Expected close
   onClose: function(socket) {
       console.log('Socket colosed.');
   }
 };

 var chatServiceSuccessCb = {
    // Registration success handler
    onSuccess: function() {
       console.log("Chat service registration success!");
    },

    onConnect: function(socket) {
        console.log("Client connected : " + socket.peer.name + "," + socket.peer.address);
        // Message received from remote device
        socket.setSocketNotifyListener(socketRegListener);
    }
};

function publishChatService() {
    var CHAT_SERVICE_UUID = "5bce9431-6c75-32ab-afe0-2ec108a30860";
    chatServiceHandler = tizen.bluetooth.adapter.registerRFCOMMServiceByUUID(CHAT_SERVICE_UUID, "Chat service", chatServiceSuccessCb,
      // Error handler
      function(e) {
           console.log( "Could not register service record, Error : " + e.message);
      });
}

function unRegisterChatService() {
    if(chatServiceHandler != null) {
        tizen.bluetooth.adapter.unregisterRFCOMMService(chatServiceHandler, function() {
            chatServiceHandler = null;
            console.log("Chat service unregistered.");
        }, function(e) {
            console.log("Error : " + e.message);
        });
    }
}

/***************************************
* tizen.bluetooth.adapter.discoverDevice
****************************************/

function startDiscovery() {

  var discoverDevicesSuccessCallback = {
//      onSuccess: function() {
      onStarted: function() {
          callback_flag = true;
          console.log("Device discovery started...");
      },

//      onFound: function(device) {
      onDeviceFound: function(device) {
          onfound_flag = true;
          console.log("Found device - Name: " + device.name + ", Address: " + device.address);
          if(device.name != null)
            foundname_flag = true;
          if(device.address != null)
            foundaddress_flag = true;
      },

//      onDisappear: function(address) {
      onDeviceDisappeared: function(address) {
          ondisappear_flag = true;
          console.log("Device disappeared: " + address);
      },

//      onFinish: function(devices) {
      onFinished: function(devices) {
          onfinish_flag = true;
          console.log("Device discovery finished...");

          var msg = new String("Found Devices: \n");
          if(devices.length == 0) {
              msg += "Total: " + devices.length;
              console.log(msg);
              return;
          }


          for (i=0 ;i < devices.length; i++) {
              msg += " Name: " + devices[i].name + ", Address: " + devices[i].address + "\n";
          }
          msg += "Total: " + devices.length;
          console.log(msg);
      }
  };
 // start searching for nearby devices, for 12 sec.
  bluetooth.adapter.discoverDevices(discoverDevicesSuccessCallback, function(e){
      onfound_flag = false;
      console.log("Failed to search devices: " + e.message + "(" + e.code + ")");
  });
}

function onSetPoweredError(e) {
    console.log("Could not turn on device, reason: " + e.message + "(" + e.code + ")");
}

function cancelDiscovery() {
    btAdapter.stopDiscovery(function() {
        console.log("Stop discovery success.");
    },
    function(e) {
        console.log("Error while stopDiscovery : " + e.message);
    })
}

// change REMOTE_DEVICE_ADDRESS and REMOTE_DEVICE_NAME
document.write('<script src="../webrunner/jquery-1.10.2.min.js"></script>');
document.write('<script src="support/getJsonConf.js"></script>');
