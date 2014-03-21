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
var gInfo;
var init = function () {
    try {
        tizen.systeminfo.addPropertyValueChangeListener("WIFI_NETWORK", onWifiNetworkSuccess);
        tizen.systeminfo.addPropertyValueChangeListener("DEVICE_ORIENTATION", onDeviceOrientationSuccess);
        tizen.systeminfo.addPropertyValueChangeListener("DISPLAY", onDisplaySuccess);
        tizen.systeminfo.addPropertyValueChangeListener("BATTERY", onBatterySuccess);
        tizen.systeminfo.addPropertyValueChangeListener("STORAGE", onStorageSuccess);
        tizen.systeminfo.addPropertyValueChangeListener("CPU", onCpuSuccess);
        tizen.systeminfo.addPropertyValueChangeListener("BUILD", onBuildSuccess);
        tizen.systeminfo.addPropertyValueChangeListener("LOCALE", onLocaleSuccess);
        tizen.systeminfo.addPropertyValueChangeListener("NETWORK", onNetworkSuccess);
        tizen.systeminfo.addPropertyValueChangeListener("CELLULAR_NETWORK", onCellularNetworkSuccess);
        tizen.systeminfo.addPropertyValueChangeListener("SIM", onSimSuccess);
        tizen.systeminfo.addPropertyValueChangeListener("PERIPHERAL", onPeripheralSuccess);
    } catch (e) {
        alert("Exception: " + e.message);
    }
    getPropertyValue();
};

function getPropertyValue() {
    try {
        tizen.systeminfo.getPropertyValue("WIFI_NETWORK", onWifiNetworkSuccess);
        tizen.systeminfo.getPropertyValue("DEVICE_ORIENTATION", onDeviceOrientationSuccess);
        tizen.systeminfo.getPropertyValue("DISPLAY", onDisplaySuccess);
        tizen.systeminfo.getPropertyValue("BATTERY", onBatterySuccess);
        tizen.systeminfo.getPropertyValue("STORAGE", onStorageSuccess);
        tizen.systeminfo.getPropertyValue("CPU", onCpuSuccess);
        tizen.systeminfo.getPropertyValue("BUILD", onBuildSuccess);
        tizen.systeminfo.getPropertyValue("LOCALE", onLocaleSuccess);
        tizen.systeminfo.getPropertyValue("NETWORK", onNetworkSuccess);
        tizen.systeminfo.getPropertyValue("CELLULAR_NETWORK", onCellularNetworkSuccess);
        tizen.systeminfo.getPropertyValue("SIM", onSimSuccess);
        tizen.systeminfo.getPropertyValue("PERIPHERAL", onPeripheralSuccess);
    } catch (e) {
        alert("Exception: " + e.message);
    }
}

function onError(e) {
    alert("Error: " + e.message);
}

function make1lineListItem(value) {
    return '<li>' + value + '</li>';
}

function makeDividerListItem(value) {
    return '<li data-role="list-divider">' + value + '</li>';
}

function onWifiNetworkSuccess(wifi) {
    gInfo = makeDividerListItem("WIFI_NETWORK Status")
            + make1lineListItem("Stauts : " + wifi.status)
            + make1lineListItem("SSID : " + wifi.ssid)
            + make1lineListItem("IPAddress : " + wifi.ipAddress)
            + make1lineListItem("IPv6Address : " + wifi.ipv6Address)
            + make1lineListItem("SignalStrength : " + wifi.signalStrength);
    $("#info-list1").html(gInfo).trigger("create").listview("refresh");
}

function onDeviceOrientationSuccess(orientation) {
    gInfo = makeDividerListItem("DEVICE_ORIENTATION Status")
            + make1lineListItem("Status : " + orientation.status)
            + make1lineListItem("AutoRotation : " + (orientation.isAutoRotation == true ? "Yes" : "No"));
    $("#info-list2").html(gInfo).trigger("create").listview("refresh");
}

function onDisplaySuccess(display) {
    gInfo = makeDividerListItem("DISPLAY Status")
            + make1lineListItem("Brightness : " + (display.brightness * 100) + "%")
            + makeDividerListItem("Resolution")
            + make1lineListItem("Width : " + display.resolutionWidth)
            + make1lineListItem("Height : " + display.resolutionHeight)
            + makeDividerListItem("Dots per inch")
            + make1lineListItem("Horizontal : " + display.dotsPerInchWidth)
            + make1lineListItem("Vertical : " + display.dotsPerInchHeight)
            + makeDividerListItem("Physical size")
            + make1lineListItem("Width : " + display.physicalWidth)
            + make1lineListItem("Height : " + display.physicalHeight);
    $("#info-list4").html(gInfo).trigger("create").listview("refresh");
}

function onBatterySuccess(battery) {
    gInfo = makeDividerListItem("BATTERY Status")
            + make1lineListItem("Level : " + (battery.level * 100) + "%")
            + make1lineListItem("Charging : " + (battery.isCharging == true ? "Yes" : "No"));
    $("#info-list3").html(gInfo).trigger("create").listview("refresh");
}

function onStorageSuccess(storages) {
    gInfo = makeDividerListItem("STORAGE Status")
          + make1lineListItem("Storage : " + storages.units.length);
    for (var i = 0; i < storages.units.length; i++) {
        gInfo += makeDividerListItem("Type : " + storages.units[i].type)
               + make1lineListItem("Capacity : " + Math.floor(storages.units[i].capacity / 1000000) + " MB")
               + make1lineListItem("Available capacity : " + Math.floor(storages.units[i].availableCapacity / 1000000) + " MB")
               + make1lineListItem("Removable : " + (storages.units[i].isRemovable == true ? "Yes" : "No"));
    }
    $("#info-list5").html(gInfo).trigger("create").listview("refresh");
}

function onCpuSuccess(cpu) {
    gInfo = makeDividerListItem("CPU Status")
            + make1lineListItem("Load : " + cpu.load);
    $("#info-list6").html(gInfo).trigger("create").listview("refresh");
}

function onBuildSuccess(build) {
    gInfo = makeDividerListItem("BUILD Status")
            + make1lineListItem("Model : " + build.model)
            + make1lineListItem("Manufacturer : " + build.manufacturer)
            + make1lineListItem("BuildVersion : " + build.buildVersion);
    $("#info-list7").html(gInfo).trigger("create").listview("refresh");
}

function onLocaleSuccess(locale) {
    gInfo = makeDividerListItem("LOCALE Status")
            + make1lineListItem("Language : " + locale.language)
            + make1lineListItem("Country : " + locale.country);
    $("#info-list8").html(gInfo).trigger("create").listview("refresh");
}

function onNetworkSuccess(network) {
    gInfo = makeDividerListItem("NETWORK Status")
            + make1lineListItem("NetworkType : " + network.networkType);
    $("#info-list9").html(gInfo).trigger("create").listview("refresh");
}

function onCellularNetworkSuccess(cellular) {
    gInfo = makeDividerListItem("CELLULAR_NETWORK Status")
            + make1lineListItem("Status : " + cellular.status)
            + make1lineListItem("Apn : " + cellular.apn)
            + make1lineListItem("IPAddress : " + cellular.ipAddress)
            + make1lineListItem("IPv6Address : " + cellular.ipv6Address)
            + make1lineListItem("Mcc : " + cellular.mcc)
            + make1lineListItem("Mnc : " + cellular.mnc)
            + make1lineListItem("CellId : " + cellular.cellId)
            + make1lineListItem("Lac : " + cellular.lac)
            + make1lineListItem("IsRoaming : " + cellular.isRoaming)
            + make1lineListItem("IsFlightMode : " + cellular.isFlightMode)
            + make1lineListItem("IMEI : " + cellular.imei);
    $("#info-list10").html(gInfo).trigger("create").listview("refresh");
}

function onSimSuccess(sim) {
    gInfo = makeDividerListItem("SIM Status")
            + make1lineListItem("State : " + sim.state)
            + make1lineListItem("OperatorName : " + sim.operatorName)
            + make1lineListItem("Msisdn : " + sim.msisdn)
            + make1lineListItem("Iccid : " + sim.iccid)
            + make1lineListItem("Mcc : " + sim.mcc)
            + make1lineListItem("Mnc : " + sim.mnc)
            + make1lineListItem("Msin : " + sim.msin)
            + make1lineListItem("Spn : " + sim.spn);
    $("#info-list11").html(gInfo).trigger("create").listview("refresh");
}

function onPeripheralSuccess(peripheral) {
    gInfo = makeDividerListItem("PERIPHERAL Status")
            + make1lineListItem("IsVideoOutputOn : " + peripheral.isVideoOutputOn);
    $("#info-list12").html(gInfo).trigger("create").listview("refresh");
}

$(document).bind("pageinit", init);
