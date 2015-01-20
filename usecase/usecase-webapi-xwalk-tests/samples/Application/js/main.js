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

var path = "", mime = "", name = "", Url = "";
var thumAudio = "", thumVideo = "";
var sharedDir;

$(document).ready(function () {
    applicationPre();
    file();
});

function browser() {
    var url = $("#url").val();
    setAppControlBrowser(url);
}

function file() {
    var documentsDir;
    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            var text = files[i].name.substring(0, 5);
            if(text == "iconA")
            {
                thumAudio = files[i].toURI();
                thumAudio = thumAudio.replace("file:///", "/");
            }
            if(text == "iconV")
            {
                thumVideo = files[i].toURI();
                thumVideo = thumVideo.replace("file:///", "/");
            }
        }
        file2();
    }

    function onerror(error) {
        $("#popup_info").modal(showMessage("error", "The error " + error.message + " occurred when listing the files in the selected folder"));
    }

    tizen.filesystem.resolve(
            'wgt-package/tests/Application/res/',
            function(dir){
                documentsDir = dir;
                dir.listFiles(onsuccess, onerror);
            }, function(e) {
                $("#popup_info").modal(showMessage("error", "Error " + e.message));
            }, "r"
    );
}

function file2() {
    var documentsDir, strImage = "", strVideo = "", strAudio = "";
    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            if(files[i].isFile == true)
            {
                var mime = files[i].name.replace(".", "/");
                var text = files[i].name.substring(0, 5);
                var file = files[i].name;
                Url = files[i].toURI();
                Url = Url.replace("file:///", "/");
                if(text == "image")
                    strImage += '<div class="panel-body"><img src="' + Url + '" alt="" />' + file + '<div type="button" class="btn btn-default btn-block" onclick="setAppControl(' + Url + ', ' + mime + ', ' + file + ');">Launch</div></div>';
                if(text == "audio")
                    strAudio += '<div class="panel-body"><img src="' + thumAudio + '" alt="" />' + file + '<div type="button" class="btn btn-default btn-block" onclick="setAppControl(' + Url + ', ' + mime + ', ' + file + ');">Launch</div></div>';
                if(text == "video")
                    strVideo += '<div class="panel-body"><img src="' + thumVideo + '" alt="" />' + file + '<div type="button" class="btn btn-default btn-block" onclick="setAppControl(' + Url + ', ' + mime + ', ' + file + ');">Launch</div></div>';
            }
        }
        $("#image").html(strImage);
        $("#audio").html(strAudio);
        $("#video").html(strVideo);
    }

    function onerror(error) {
        $("#popup_info").modal(showMessage("error", "The error " + error.message + " occurred when listing the files in the selected folder"));
    }

    tizen.filesystem.resolve(
            'wgt-package/tests/Application/res/',
            function(dir){
                documentsDir = dir;
                dir.listFiles(onsuccess, onerror);
            }, function(e) {
                $("#popup_info").modal(showMessage("error", "Error " + e.message));
            }, "r"
    );
}

function setAppControl(url, mime, name) {
    var appControl = new tizen.ApplicationControl(
            "http://tizen.org/appcontrol/operation/view",
            sharedDir+"/data/"+name,
            mime);
    var appControlReplyCB = {
            onsuccess: function(data) {
            },
            onfailure: function() {
            }
    };
    try {
        tizen.application.launchAppControl(appControl, null,
        function(){
            $("#popup_info").modal(showMessage("success", "launch appControl succeeded"));
        },
        function(e){
            $("#popup_info").modal(showMessage("error", "launch appControl failed. Reason: " + e.message));
        },
        appControlReplyCB);
    } catch(e)
    {
        $("#popup_info").modal(showMessage("error", "launch appControl error: " + e.message));
    }
}

function setAppControlFile(mime) {
    var app = {attach:[]};
    app.attach = [];
    var appControl = new tizen.ApplicationControl(
            "http://tizen.org/appcontrol/operation/pick",
            null,
            mime);
    var appControlReplyCB = {
            onsuccess: function(data) {
                app.attach.push(data[0].value[0]);
                $("#popup_info").modal(showMessage("success", "Select File : " + app.attach[0]));
            },
            onfailure: function() {
            }
    };
    try {
        tizen.application.launchAppControl(appControl, null,
        function(){
            $("#popup_info").modal(showMessage("success", "launch appControl succeeded"));
        },
        function(e){
            $("#popup_info").modal(showMessage("error", "launch appControl failed. Reason: " + e.message));
        },
        appControlReplyCB);
    } catch(e)
    {
        $("#popup_info").modal(showMessage("error", "launch appControl error: " + e.message));
    }
}

function setAppControlBrowser(url) {
    var appControl = new tizen.ApplicationControl(
            "http://tizen.org/appcontrol/operation/view",
            url,
            null);
    var appControlReplyCB = {
            onsuccess: function(data) {
            },
            onfailure: function() {
            }
    };
    try {
        tizen.application.launchAppControl(appControl, null,
        function(){
            $("#popup_info").modal(showMessage("success", "launch appControl succeeded"));
        },
        function(e){
            $("#popup_info").modal(showMessage("error", "launch appControl failed. Reason: " + e.message));
        },
        appControlReplyCB);
    } catch(e)
    {
        $("#popup_info").modal(showMessage("error", "launch appControl error: " + e.message));
    }
}

function applicationPre() {
    var documentsDir;
    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            sharedDir = tizen.application.getAppSharedURI();
            sharedDir = sharedDir.replace("file:///", "/");
            documentsDir.copyTo(
                files[i].fullPath,
                sharedDir+"/data/"+files[i].name,
                true,
                function() {
                    $("#popup_info").modal(showMessage("success", "PKGID/shared/data/ File Copy"));
                },
                function(e){
                    $("#popup_info").modal(showMessage("error", "Error : " + e.name));
                });
        }
    }

    function onerror(error) {
        $("#popup_info").modal(showMessage("error", "The error " + error.message + " occurred when listing the files in the selected folder"));
    }

    tizen.filesystem.resolve(
        'wgt-package/tests/Application/res',
        function(dir){
            documentsDir = dir;
            dir.listFiles(onsuccess, onerror);
        }, function(e) {
            $("#popup_info").modal(showMessage("error", "Error " + e.message));
        }, "r"
    );
}
