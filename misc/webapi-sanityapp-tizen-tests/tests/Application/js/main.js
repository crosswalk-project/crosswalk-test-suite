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

$(document).delegate("#main", "pageinit", function() {
    $("#image").delegate("li", "vclick", function() {
        name = $(this).data("file");
        path = $(this).data("url");
        mime = $(this).data("mime");
        setAppControlImage(path, mime, name);
        return false;
    });
    $("#audio").delegate("li", "vclick", function() {
        name = $(this).data("file");
        path = $(this).data("url");
        mime = $(this).data("mime");
        setAppControlAudio(path, mime, name);
        return false;
    });
    $("#video").delegate("li", "vclick", function() {
        name = $(this).data("file");
        path = $(this).data("url");
        mime = $(this).data("mime");
        setAppControlVideo(path, mime, name);
        return false;
    });
    $("#allFile").bind("vclick", function() {
        setAppControlFile("*/*");
        return false;
    });
    $("#imageFile").bind("vclick", function() {
        setAppControlFile("image/*");
        return false;
    });
    $("#videoFile").bind("vclick", function() {
        setAppControlFile("video/*");
        return false;
    });
    $("#audioFile").bind("vclick", function() {
        setAppControlFile("audio/*");
        return false;
    });
    $("#tizen").bind("vclick", function() {
        setAppControlBrowser("https://www.tizen.org");
        return false;
    });
    $("#browser").bind("vclick", function() {
        var url = $("#url").val();
        setAppControlBrowser(url);
        return false;
    });
    applicationPre();
    file();
});

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
        alert("The error " + error.message + " occurred when listing the files in the selected folder");
    }

    tizen.filesystem.resolve(
            'wgt-package/tests/Application/res/',
            function(dir){
                documentsDir = dir;
                dir.listFiles(onsuccess, onerror);
            }, function(e) {
                alert("Error " + e.message);
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
                    strImage += '<li data-url="' + Url + '" data-mime="' + mime + '" data-file="' + file + '"><img src="' + Url + '" alt="" />' + file + '</li>';
                if(text == "audio")
                    strAudio += '<li data-url="' + Url + '" data-mime="' + mime + '" data-file="' + file + '"><img src="' + thumAudio + '" alt="" />' + file + '</li>';
                if(text == "video")
                    strVideo += '<li data-url="' + Url + '" data-mime="' + mime + '" data-file="' + file + '"><img src="' + thumVideo + '" alt="" />' + file + '</li>';
            }
        }
        $("#image").html(strImage).trigger("create").listview("refresh");
        $("#audio").html(strAudio).trigger("create").listview("refresh");
        $("#video").html(strVideo).trigger("create").listview("refresh");
    }

    function onerror(error) {
        alert("The error " + error.message + " occurred when listing the files in the selected folder");
    }

    tizen.filesystem.resolve(
            'wgt-package/tests/Application/res/',
            function(dir){
                documentsDir = dir;
                dir.listFiles(onsuccess, onerror);
            }, function(e) {
                alert("Error " + e.message);
            }, "r"
    );
}

function setAppControlImage(url, mime, name) {
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
            console.log("launch appControl succeeded");
        },
        function(e){
            alert("launch appControl failed. Reason: " + e.message);
        },
        appControlReplyCB);
    } catch(e)
    {
        alert("launch appControl error: " + e.message);
    }
}

function setAppControlAudio(url, mime, name) {
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
            console.log("launch appControl succeeded");
        },
        function(e){
            alert("launch appControl failed. Reason: " + e.message);
        },
        appControlReplyCB);
    } catch(e)
    {
        alert("launch appControl error: " + e.message);
    }
}

function setAppControlVideo(url, mime, name) {
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
            console.log("launch appControl succeeded");
        },
        function(e){
            alert("launch appControl failed. Reason: " + e.message);
        },
        appControlReplyCB);
    } catch(e)
    {
        alert("launch appControl error: " + e.message);
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
                alert("Select File : " + app.attach[0]);
            },
            onfailure: function() {
            }
    };
    try {
        tizen.application.launchAppControl(appControl, null,
        function(){
            console.log("launch appControl succeeded");
        },
        function(e){
            alert("launch appControl failed. Reason: " + e.message);
        },
        appControlReplyCB);
    } catch(e)
    {
        alert("launch appControl error: " + e.message);
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
            console.log("launch appControl succeeded");
        },
        function(e){
            alert("launch appControl failed. Reason: " + e.message);
        },
        appControlReplyCB);
    } catch(e)
    {
        alert("launch appControl error: " + e.message);
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
                    console.log("PKGID/shared/data/ File Copy");
                },
                function(e){
                    console.log("Error : " + e.name);
                });
        }
    }

    function onerror(error) {
        console.log("The error " + error.message + " occurred when listing the files in the selected folder");
    }

    tizen.filesystem.resolve(
        'wgt-package/tests/Application/res',
        function(dir){
            documentsDir = dir;
            dir.listFiles(onsuccess, onerror);
        }, function(e) {
            alert("Error " + e.message);
        }, "r"
    );
}
