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
        tizen.systeminfo.addPropertyValueChangeListener("STORAGE", onStorageSuccess);
    } catch (e) {
        alert("Exception: " + e.message);
    }
    getPropertyValue();
};

function getPropertyValue() {
    try {
        tizen.systeminfo.getPropertyValue("STORAGE", onStorageSuccess);
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

function onStorageSuccess(storages) {
    gInfo = makeDividerListItem("STORAGE Status")
          + make1lineListItem("Storage : " + storages.units.length);
    alert("storage length=",storages.units.length);
    for (var i = 0; i < storages.units.length; i++) {
        gInfo += makeDividerListItem("Type : " + storages.units[i].type)
               + make1lineListItem("Capacity : " + Math.floor(storages.units[i].capacity / 1000000) + " MB")
               + make1lineListItem("Available capacity : " + Math.floor(storages.units[i].availableCapacity / 1000000) + " MB")
               + make1lineListItem("Removable : " + (storages.units[i].isRemovable == true ? "Yes" : "No"));
    }
    $("#info-list").html(gInfo).trigger("create").listview("refresh");
}

$(document).bind("pageinit", init);
