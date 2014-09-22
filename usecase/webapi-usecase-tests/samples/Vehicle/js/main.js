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

