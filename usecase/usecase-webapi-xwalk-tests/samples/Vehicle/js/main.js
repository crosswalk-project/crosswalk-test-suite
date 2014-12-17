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
        Liu, Xin <xinx.liu@intel.com>

*/

window.onload = DisablePassButton;

function getVehicle() {
  try {
    EnablePassButton();
    // Verify vehicleSpeed:
    jQuery("#vehicleSpeed").text("vehicle vehicleSpeed: " + tizen.vehicle.vehicleSpeed);
    // Verify zones
    jQuery("#zones").text("vehicleSpeed zones: " + tizen.vehicle.vehicleSpeed.zones);

    // Verify Availability, check speed is availabled for get():
    var speedFlag = vehicle.vehicleSpeed.availableForRetrieval("speed") === "available";
    
    if(speedFlag) {
      // Verify get:
      tizen.vehicle.vehicleSpeed.get().then(function(vehicleSpeed) {
        jQuery("#speed").text("vehicleSpeed speed: " + vehicleSpeed.speed);
      },
      function(error) {
        window.alert("Error callback: " + error.message);
      });
    }
    
    // Verify subscribe and unsubscribe:
    var vehicleSpeedSub = tizen.vehicle.vehicleSpeed.subscribe(function(vehicleSpeed) {
      jQuery("#speedChange").text("vehicle speed changed to: " + vehicleSpeed.speed);
      tizen.vehicle.vehicleSpeed.unsubscribe(vehicleSpeedSub);
    });

    if(vehicle.vehicleSpeed.isLogged)
    {
      // Verify getHistory:
      tizen.vehicle.vehicleSpeed.getHistory(tizen.vehicle.vehicleSpeed.from, tizen.vehicle.vehicleSpeed.to).then(function(data) {
        jQuery("#historyData").text("history data: " + data.length);
      });
    }

  } catch (err) {
    window.alert("Thrown an error: " + err.message);
  }
}

function setVehicleDoor() {
  // Check door supported:
  var doorFlag = tizen.vehicle.door.supported();
  if(doorFlag) {
    var zone = Zone;
    // Verify set:
    tizen.vehicle.door.set({"lock" : true}, zone.driver).then(function() {
      window.alert("Set door lock success");
    }, function(error) {
      window.alert("Error callback: " + error.message);
    });
  }else {
    window.alert("vehicle door is not supported");
  }
}

