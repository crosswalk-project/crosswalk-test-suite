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

var path;

$(document).delegate("#main", "pageinit", function() {
    $("#ringtone").delegate("li", "vclick", function() {
        path = $(this).data("url");
        setSystemProperty("INCOMING_CALL", path, onIncomingCallSetSuccess);
        return false;
    });
    $("#tone").bind("vclick", function() {
        getSystemProperty("INCOMING_CALL", onIncomingCallGetSuccess);
        return false;
    });
    fileAudio();
});

function onError(e) {
    alert("Error: " + e.message);
}

function onIncomingCallSetSuccess() {
    alert("Change of INCOMING_CALL ringtone");
}

function onIncomingCallGetSuccess(value) {
    alert("Sound(Get) path : " + value);
    var audio = document.getElementById("MyAudio");
    audio.src = value;
    audio.type = "audio/*";
    audio.play();
}

function setSystemProperty(property, path, onSuccess) {
    try {
        tizen.systemsetting.setProperty(property, path, onSuccess, onError);
        console.log(path);
    } catch (e) {
        console.log("Exception: " + e.message);
    }
}

function getSystemProperty(property, onSuccess) {
    try {
        tizen.systemsetting.getProperty(property, onSuccess, onError);
    } catch (e) {
        console.log("Exception: " + e.message);
    }
}

function fileAudio() {
    var documentsDir, length = 0, str = "";
    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            if(files[i].isFile == true)
            {
                var Url = files[i].toURI();
                Url = Url.replace("file:///", "/");
                str += '<li data-url="' + Url + '">' + files[i].name + '</li>';
                length++;
                if(length >= 9)
                    break;
            }
        }
        if(length == 0)
            alert("Not found Sound files\nPlease add sound files.\nAdd Path: " + documentsDir.toURI() + "/");
        $("#ringtone").html(str).trigger("create").listview("refresh");
    }

    function onerror(error) {
        console.log("The error " + error.message + " occurred when listing the files in the selected folder");
    }

    tizen.filesystem.resolve(
            'ringtones',
            function(dir){
                documentsDir = dir;
                dir.listFiles(onsuccess, onerror);
            }, function(e) {
                alert("Error " + e.message);
            }, "r"
    );
}
