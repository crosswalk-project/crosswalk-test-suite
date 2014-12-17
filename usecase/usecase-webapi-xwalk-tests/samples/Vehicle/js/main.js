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

vehicle = tizen.vehicle || navigator.vehicle;

function getVehicle() {
  try {
    EnablePassButton();
    // Verify vehicleSpeed:
    jQuery("#vehicleSpeed").text("vehicle vehicleSpeed: " + vehicle.vehicleSpeed);
    // Verify zones
    jQuery("#zones").text("vehicleSpeed zones: " + vehicle.vehicleSpeed.zones);

    // Verify get:
    vehicle.vehicleSpeed.get().then(function(vehicleSpeed) {
      jQuery("#speed").text("vehicleSpeed speed: " + vehicleSpeed.speed);
    },
    function(error) {
      window.alert("Error callback: " + error.message);
    });
    
    // Verify subscribe and unsubscribe:
    var vehicleSpeedSub = vehicle.vehicleSpeed.subscribe(function(vehicleSpeed) {
      jQuery("#speedChange").text("vehicle speed changed to: " + vehicleSpeed.speed);
      vehicle.vehicleSpeed.unsubscribe(vehicleSpeedSub);
    });

    // Verify getHistory:
    vehicle.vehicleSpeed.getHistory(vehicle.vehicleSpeed.from, vehicle.vehicleSpeed.to).then(function(data) {
      jQuery("#historyData").text("history data: " + data.length);
    });

  } catch (err) {
    window.alert("Thrown an error: " + err.message);
  }
}
