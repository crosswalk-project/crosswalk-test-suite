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

var profileId = null;
var account, passwd, url, database;

function serverGuide() {
    //alert("<Sample OMA DS Server List>\n1. http://my.funambol.com/sync \n2. https://www.everdroid.com/web  \n3. OMA DS 1.2 protocol Server\n*Recommend the 1st server");
}

function addProfile() {
    try {
        account = $("#account").val();
        passwd = $("#passwd").val();
        url = $("#url").val();
        database = $("#database").val();

        // Create a sync info.
        var syncInfo = new tizen.SyncInfo(url, account, passwd, "MANUAL", "REFRESH_FROM_SERVER");

        // Sync both contacts and events.
        var contactInfo = new tizen.SyncServiceInfo(true, "CONTACT", database);
        var serviceInfo = [contactInfo];

        // Adds a profile to sync.
        var profile = new tizen.SyncProfileInfo("MyProfile", syncInfo, serviceInfo);
        tizen.datasync.add(profile);

        profileId = profile.profileId;
        alert("Add Profile ID : " + profileId);
    } catch(err) {
        alert(err.message);
    }
}

function startSync() {
    var total;
    var syncProgressCallback = {
            onprogress: function (profileId, serviceType, isFromServer, totalPerType, syncedPerType) {
                console.log('Total: ' + totalPerType + ', synced: ' + syncedPerType + ', for the sync type: ' + serviceType);
                total = totalPerType;
            },
            onstopped: function (profileId) {
                removeProfile();
            },
            onfailed: function (profileId, error) {
                alert('Please try again in a few minutes.');
                console.log('Failed with id: ' + profileId + ', error name: ' + error.name);
            },
            oncompleted: function (profileId) {
                console.log("Completed with id" + profileId);
                alert("Sync Completed - " + total + " Contacts");
                contactList();
            }
    };

    try {
        tizen.datasync.startSync(profileId, syncProgressCallback);
        alert("Contact sync start\n(OMA DS Server - Device)");
    } catch(err) {
        alert(err.message);
    }
}

function removeProfile() {
    try {
        tizen.datasync.remove(profileId);
        console.log("Removed ProfileId.");
    } catch(err) {
        alert(err.message);
    }
}

function stopSync() {
    try {
        tizen.datasync.stopSync(profileId);
        console.log("Stopped.");
    } catch(err) {
        alert(err.message);
    }
}

/*function getLastSyncStatistics() {
    try {
        // Gets the sync statistics information with the given id.
        var statistics = tizen.datasync.getLastSyncStatistics(profileId);
        alert("Num statistics: " + statistics.length);
        for(i in statistics) {
            alert("syncStatus: " + statistics[i].syncStatus + ", serviceType: " + statistics[i].serviceType + ", lastSyncTime: " + statistics[i].lastSyncTime);
            alert("serverToClientTotal: " + statistics[i].serverToClientTotal + ", serverToClientAdded: " + statistics[i].serverToClientAdded + ", serverToClientUpdated: " + statistics[i].serverToClientUpdated + ", serverToClientRemoved: " + statistics[i].serverToClientRemoved);
            alert("clientToServerTotal: " + statistics[i].clientToServerTotal + ", clientToServerAdded: " + statistics[i].clientToServerAdded + ", clientToServerUpdated: " + statistics[i].clientToServerUpdated + ", clientToServerRemoved: " + statistics[i].clientToServerRemoved);
        }
    } catch(err) {
        console.log(err.message);
    }
}*/

function contactList() {
    function successCallback(contacts) {
        var str = "";

        if(contacts.length > 0)
        {
            for (var i = 0; i < contacts.length; i++)
            {
                str += '<li>' + contacts[i].name.displayName + ' (' + contacts[i].phoneNumbers[0].number + ')</li>';
            }
            $("#contactsList").html(str).trigger("create").listview("refresh");
        }
        else
        {
            alert("Not found Contacts");
        }
        removeProfile();
    }

    function errorCallback(err) {
        alert("An error occurred: " + err.message);
    }

    var filter = new tizen.AttributeFilter("lastUpdated", "EXISTS", null);

    try {
        tizen.contact.getDefaultAddressBook().find(successCallback, errorCallback, filter);
    } catch(err) {
        alert('The following error occurred while finding: ' +  err.name);
    }
}
$(document).ready(function() {
  serverGuide();
});
