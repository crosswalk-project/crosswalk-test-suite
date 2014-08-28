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
    $("#imageHS").delegate("li", "vclick", function() {
        path = $(this).data("url");
        setSystemProperty("HOME_SCREEN", path, onScreenSetSuccess);
    });
    $("#imageLS").delegate("li", "vclick", function() {
        path = $(this).data("url");
        setSystemProperty("LOCK_SCREEN", path, onScreenSetSuccess);
    });
    $("#imageHG").bind("vclick", function() {
        getSystemProperty("HOME_SCREEN", onScreenGetSuccess);
        return false;
    });
    $("#imageLG").bind("vclick", function() {
        getSystemProperty("LOCK_SCREEN", onScreenGetSuccess);
        return false;
    });
    fileImage();
});

function onError(e) {
    alert("Error: " + e.message);
}

function onScreenSetSuccess() {
    alert("Change of SCREEN image");
}

function onScreenGetSuccess(value) {
    alert("Image(Get) path : " + value);
    var canvas = document.getElementById("canvas");
    var cx = canvas.getContext("2d");
    var image = new Image();
    image.src = value;
    cx.drawImage(image, 0, 0, 350, 200);
}

function setSystemProperty(property, path, onSuccess) {
    try {
        tizen.systemsetting.setProperty(property, path, onSuccess, onError);
        console.log(path);
    } catch (e) {
        alert("Exception: " + e.message);
    }
}

function getSystemProperty(property, onSuccess) {
    try {
        tizen.systemsetting.getProperty(property, onSuccess, onError);
    } catch (e) {
        alert("Exception: " + e.message);
    }
}

function fileImage() {
    var documentsDir, length = 0, str = "";
    var len, last, ext;
    function onsuccess(files) {
        for (var i = 0; i < files.length; i++)
        {
            if(files[i].isFile == true)
            {
                len = files[i].name.length;
                last = files[i].name.lastIndexOf(".");
                ext = files[i].name.substring(last, len);
                if(ext == ".jpg" || ext == ".jpeg" || ext == ".bmp" || ext == ".png" || ext == ".gif")
                {
                    var Url = files[i].toURI();
                    Url = Url.replace("file:///", "/");
                    str += '<li data-url="' + Url + '"><img src="' + files[i].toURI() + '" alt="" />' + "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;" + files[i].name + '</li>';
                    length++;
                    if(length >= 6)
                        break;
                }
            }
        }
        if(length == 0)
            alert("Not found Image files.\nPlease add image files.\nAdd Path: " + documentsDir.toURI() + "/");
        $("#imageHS").html(str).trigger("create").listview("refresh");
        $("#imageLS").html(str).trigger("create").listview("refresh");
    }

    function onerror(error) {
        console.log("The error " + error.message + " occurred when listing the files in the selected folder");
    }

    tizen.filesystem.resolve(
            'images',
            function(dir){
                documentsDir = dir;
                dir.listFiles(onsuccess, onerror);
            }, function(e) {
                alert("Error " + e.message);
            }, "r"
    );
}
