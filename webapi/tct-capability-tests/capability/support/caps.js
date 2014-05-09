/*
Copyright (c) 2012 Intel Corporation.

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
        Zhang, Ge <gex.zhang@intel.com>

 */

(function () {
    document.write('<link rel="stylesheet" href="../resources/testharness.css"></link>\n');
    document.write('<script src="../webrunner/jquery-1.10.2.min.js"></script>\n');
    document.write('<script src="../resources/testharness.js"></script>\n');
    document.write('<script src="../resources/testharnessreport.js"></script>\n');
})();

var mandatoryItems = ["usbHost", "screenSizeNormal", "multiTouchCount"];

/**
 * Method to check device capability by tizen.systeminfo.getCapabilities().
 * Example usage:
 *   isBTSupported = is_caps_supported_by_system_info("bluetooth");
 * @param cap device capability attribute
 * @returns true if a device capability is supported
 *
 */
function is_caps_supported_by_system_info(cap) {
    var deviceCapabilities;
    var supported = false;
    try {
        deviceCapabilities = tizen.systeminfo.getCapabilities();
    } catch(e) {
        assert_false(true, "tizen.systeminfo.getCapabilities() threw exception " + e.message);
        return supported;
    }
    switch (cap) {
        case "bluetooth":
            supported = deviceCapabilities.bluetooth;
        break;
        case "nfc":
            supported = deviceCapabilities.nfc;
        break;
        case "nfcReservedPush":
            supported = deviceCapabilities.nfcReservedPush;
        break;
        case "multiTouchCount":
            // This needs to be revised
            supported = deviceCapabilities.multiTouchCount > 0 ? true : false;
            console.log("The multiTouchCount value is " + deviceCapabilities.multiTouchCount);
        break;
        case "inputKeyboard":
            supported = deviceCapabilities.inputKeyboard;
        break;
        case "inputKeyboardLayout":
            supported = deviceCapabilities.inputKeyboardLayout;
        break;
        case "wifi":
            supported = deviceCapabilities.wifi;
        break;
        case "wifiDirect":
            supported = deviceCapabilities.wifiDirect;
        break;
        case "opengles":
            supported = deviceCapabilities.opengles;
        break;
        case "openglestextureFormat":
            supported = deviceCapabilities.openglestextureFormat != "" ? true : false;
            console.log("The openglestextureFormat value is " + deviceCapabilities.openglestextureFormat);
        break;
        case "openglesVersion1_1":
            supported = deviceCapabilities.openglesVersion1_1;
        break;
        case "openglesVersion2_0":
            supported = deviceCapabilities.openglesVersion2_0;
        break;
        case "fmRadio":
            supported = deviceCapabilities.fmRadio;
        break;
        case "platformVersion":
            // This needs to be revised
            supported = deviceCapabilities.platformVersion != "" ? true : false;
            console.log("The platformVersion value is " + deviceCapabilities.platformVersion);
        break;
        case "webApiVersion":
            // This needs to be revised
            supported = deviceCapabilities.webApiVersion != "" ? true : false;
            console.log("The webApiVersion value is " + deviceCapabilities.webApiVersion);
        break;
        case "nativeApiVersion":
            // This needs to be revised
            supported = deviceCapabilities.nativeApiVersion != "" ? true : false;
            console.log("The nativeApiVersion value is " + deviceCapabilities.nativeApiVersion);
        break;
        case "platformName":
            supported = deviceCapabilities.platformName != "" ? true : false;
            console.log("The platformName value is " + deviceCapabilities.platformName);
        break;
        case "camera":
            supported = deviceCapabilities.camera;
        break;
        case "cameraFront":
            supported = deviceCapabilities.cameraFront;
        break;
        case "cameraFrontFlash":
            supported = deviceCapabilities.cameraFrontFlash;
        break;
        case "cameraBack":
            supported = deviceCapabilities.cameraBack;
        break;
        case "cameraBackFlash":
            supported = deviceCapabilities.cameraBackFlash;
        break;
        case "location":
            supported = deviceCapabilities.location;
        break;
        case "locationGps":
            supported = deviceCapabilities.locationGps;
        break;
        case "locationWps":
            supported = deviceCapabilities.locationWps;
        break;
        case "microphone":
            supported = deviceCapabilities.microphone;
        break;
        case "usbHost":
            supported = deviceCapabilities.usbHost;
        break;
        case "usbAccessory":
            supported = deviceCapabilities.usbAccessory;
        break;
        case "screenOutputRca":
            supported = deviceCapabilities.screenOutputRca;
        break;
        case "screenOutputHdmi":
            supported = deviceCapabilities.screenOutputHdmi;
        break;
        case "platformCoreCpuArch":
            // This needs to be revised
            supported = deviceCapabilities.platformCoreCpuArch != "" ? true : false;
            console.log("The platformCoreCpuArch value is " + deviceCapabilities.platformCoreCpuArch);
        break;
        case "platformCoreFpuArch":
            // This needs to be revised
            supported = deviceCapabilities.platformCoreFpuArch != "" ? true : false;
            console.log("The platformCoreFpuArch value is " + deviceCapabilities.platformCoreFpuArch);
        break;
        case "sipVoip":
            supported = deviceCapabilities.sipVoip;
        break;
        case "duid":
            // This needs to be revised
            supported = deviceCapabilities.duid != "" ? true : false;
            console.log("The duid value is " + deviceCapabilities.duid);
        break;
        case "speechRecognition":
            supported = deviceCapabilities.speechRecognition;
        break;
        case "speechSynthesis":
            supported = deviceCapabilities.speechSynthesis;
        break;
        case "accelerometer":
            supported = deviceCapabilities.accelerometer;
        break;
        case "accelerometerWakeup":
            supported = deviceCapabilities.accelerometerWakeup;
        break;
        case "barometer":
            supported = deviceCapabilities.barometer;
        break;
        case "barometerWakeup":
            supported = deviceCapabilities.barometerWakeup;
        break;
        case "gyroscope":
            supported = deviceCapabilities.gyroscope;
        break;
        case "gyroscopeWakeup":
            supported = deviceCapabilities.gyroscopeWakeup;
        break;
        case "magnetometer":
            supported = deviceCapabilities.magnetometer;
        break;
        case "magnetometerWakeup":
            supported = deviceCapabilities.magnetometerWakeup;
        break;
        case "proximity":
            supported = deviceCapabilities.proximity;
        break;
        case "proximityWakeup":
            supported = deviceCapabilities.proximityWakeup;
        break;
        case "photometer":
            supported = deviceCapabilities.photometer;
        break;
        case "photometerWakeup":
            supported = deviceCapabilities.photometerWakeup;
        break;
        case "tiltmeter":
            supported = deviceCapabilities.tiltmeter;
        break;
        case "tiltmeterWakeup":
            supported = deviceCapabilities.tiltmeterWakeup;
        break;
        case "dataEncryption":
            supported = deviceCapabilities.dataEncryption;
        break;
        case "graphicsAcceleration":
            supported = deviceCapabilities.graphicsAcceleration;
        break;
        case "push":
            supported = deviceCapabilities.push;
        break;
        case "telephony":
            supported = deviceCapabilities.telephony;
        break;
        case "telephonyMms":
            supported = deviceCapabilities.telephonyMms;
        break;
        case "telephonySms":
            supported = deviceCapabilities.telephonySms;
        break;
        case "screenSizeNormal":
            supported = deviceCapabilities.screenSizeNormal;
        break;
        case "screenSize480_800":
            supported = deviceCapabilities.screenSize480_800;
        break;
        case "screenSize720_1280":
            supported = deviceCapabilities.screenSize720_1280;
        break;
        case "autoRotation":
            supported = deviceCapabilities.autoRotation;
        break;
        case "shellAppWidget":
            supported = deviceCapabilities.shellAppWidget;
        break;
        case "visionImageRecognition":
            supported = deviceCapabilities.visionImageRecognition;
        break;
        case "visionQrcodeGeneration":
            supported = deviceCapabilities.visionQrcodeGeneration;
        break;
        case "visionQrcodeRecognition":
            supported = deviceCapabilities.visionQrcodeRecognition;
        break;
        case "visionFaceRecognition":
            supported = deviceCapabilities.visionFaceRecognition;
        break;
        case "secureElement":
            supported = deviceCapabilities.secureElement;
        break;
        case "nativeOspCompatible":
            supported = deviceCapabilities.nativeOspCompatible;
        break;
        default:
            supported = false;
    }
    return supported;
}

/**
 * Method to check if a device capability is supported.
 * Example usage:
 * check_capability("bluetooth");
 *
 * @param cap  device capability attribute
 */
function check_capability(cap) {
    // X = Tizen Device SystemInfo API, SystemInfoDeviceCapability object
    // If X TURE, then PASS.
    // If X FALSE and it's the mandatory item, then FAIL.
    // If X FALSE and it's the optional item, then PASS.
    var X = is_caps_supported_by_system_info(cap);
    var Y = false;
    for (var i=0 ; i < mandatoryItems.length ; ++i ){
        if(cap == mandatoryItems[i]){
            Y =true;
        }
    }
    if(!X && !Y){
        X = true;
    }
    assert_true(X, cap + " capability is supported");
}

/**
 * Method to check if an optional API is unsupported.
 * Example usage:
 * check_unsupported("bluetooth", tizen.bluetooth);
 *
 * @param cap  device capability attribute
 * @param optionalAPI  optional API to be validated
 */
function check_unsupported(cap, optionalAPI) {
    // X = Tizen Device SystemInfo API, SystemInfoDeviceCapability object
    // Y = Tizen Device API: tizen object
    // If X TRUE then PASS.
    // If X FALSE and Y "undefined", then PASS.
    // If X FALSE and Y others, then FAIL.

    var X = is_caps_supported_by_system_info(cap);

    if (!X) {
        assert_equals(optionalAPI, undefined, "undefined must be returned");
    }
}
