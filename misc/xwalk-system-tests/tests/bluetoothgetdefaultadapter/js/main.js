/**
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
 Chen, Yanbo <yanbox.a.chen@intel.com>
 */
$(document).bind("pagecreate", "#main", function() {
  var adapter = tizen.bluetooth.getDefaultAdapter();
  adapter.powered == true ? $("#bluetooth").val("on").flipswitch("refresh") : $("#bluetooth").val("off").flipswitch("refresh");
  $("#bluetooth").live("change", bluetoothChanged);
  function bluetoothChanged(e) {
    var id = this.id, value = this.value;
    if (value == "on") {
      powerOn();
    } else {
      powerOff();
    }
  };
  function powerOn() {
    // If adapter is not powered on
    if (!adapter.powered) {
      // Initiates power on
      adapter.setPowered(true, function() {
        alert("Bluetooth powered on success.");
      }, function(e) {
        alert("Failed to power on Bluetooth: " + e.message);
      });
    }
  };
  function powerOff() {
    // If powered on
    if (adapter.powered) {
      // Initiates power off
      adapter.setPowered(false, function() {
        alert("Bluetooth powered off successfully.");
      }, function(e) {
        alert("Failed to power off Bluetooth: " + e.message);
      });
    }
  };
  function onsuccess() {
    console.log("The application has launched successfully");
  };
  function onerror() {
    console.log("The application has launched fail");
  };
  function startapp(appid) {
    tizen.application.launch(appid, onsuccess, onerror);
  };
  $("#launchMediaPlayer").live("click", function() {
    startapp("Modello007.Multimediaplayer");
  });
  $("#launchPhone").live("click", function() {
    startapp("Modello009.Phone");
  });
  $("#launchPhone").live("click", function() {
    startapp("Modello006.Hvac");
  });
});
