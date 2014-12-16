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


 */

(function () {
   var head_src = document.head.innerHTML;
   if (head_src.search(/\/testharness.js\W/) === -1) {
       document.write('<script language="javascript" src="../resources/testharness.js"></script>\n');
   }
   if (head_src.search(/\/testharnessreport.js\W/) === -1) {
       document.write('<script language="javascript" src="../resources/testharnessreport.js"></script>\n');
   }
})();

var attribute = "";
var status_value = "";
var isRoaming = false;

var SYSTEM_INFO_NETWORK_TYPE = ["NONE", "2G", "2.5G", "3G", "4G", "WIFI", "ETHERNET", "UNKNOWN"];
var SystemInfoDeviceCapability = ["bluetooth", "nfc", "nfcReservedPush", "multiTouchCount", "inputKeyboard", "inputKeyboardLayout", "wifi", "wifiDirect", "opengles", "openglestextureFormat", "openglesVersion1_1", "openglesVersion2_0", "fmRadio", "platformVersion", "webApiVersion", "nativeApiVersion", "platformName", "camera", "cameraFront", "cameraFrontFlash", "cameraBack", "cameraBackFlash", "location", "locationGps", "locationWps", "microphone", "usbHost", "usbAccessory", "screenOutputRca", "screenOutputHdmi", "platformCoreCpuArch", "platformCoreFpuArch", "sipVoip", "duid", "speechRecognition", "speechSynthesis", "accelerometer", "accelerometerWakeup", "barometer", "barometerWakeup", "gyroscope", "gyroscopeWakeup", "magnetometer", "magnetometerWakeup", "photometer", "photometerWakeup", "proximity", "proximityWakeup", "tiltmeter", "tiltmeterWakeup", "dataEncryption", "graphicsAcceleration", "push", "telephony", "telephonyMms", "telephonySms", "screenSizeNormal", "screenSize480_800", "screenSize720_1280", "autoRotation", "shellAppWidget", "visionImageRecognition", "visionQrcodeGeneration", "visionQrcodeRecognition", "visionFaceRecognition", "secureElement", "nativeOspCompatible", "profile"];
var SystemInfoStorageUnit = ["type", "capacity", "availableCapacity", "isRemovable"];
var systemInfoPropertyId = ["BATTERY", "CPU", "STORAGE", "DISPLAY", "DEVICE_ORIENTATION", "LOCALE", "NETWORK", "WIFI_NETWORK", "CELLULAR_NETWORK", "SIM", "PERIPHERAL"];
var SYSTEM_INFO_DEVICE_ORIENTATION_STATUS = ["PORTRAIT_PRIMARY", "PORTRAIT_SECONDARY", "LANDSCAPE_PRIMARY", "LANDSCAPE_SECONDARY"];
var SYSTEM_INFO_SIM_STATE = ["ABSENT", "INITIALIZING", "READY", "PIN_REQUIRED", "PUK_REQUIRED", "NETWORK_LOCKED", "SIM_LOCKED", "UNKNOWN"];
var PLATFROM_CORE_CPU_ARCH = ["armv6", "armv7", "x86", "llvm"];
var PLATFROM_CORE_FPU_ARCH = ["vfpv3", "sse2", "sse3", "ssse3"];
var SYSTEM_INFO_PROFILE = ["MOBILE_FULL", "MOBILE_WEB"];

var INVALID_VALUES_ERR = {
    name: "InvalidValuesError"
};
var TYPE_MISMATCH_ERR = {
    name: "TypeMismatchError"
};

function assert_value_in_range(minValue, maxValue, attributeValue, description) {
    var expected, epsilon;

    assert_type(attributeValue, "number", "attributeValue is not a number.");

    epsilon = Math.abs((Number(maxValue) - Number(minValue)) / 2);
    expected = Number(maxValue) - epsilon;
    assert_approx_equals(attributeValue, expected, epsilon, description)
}
