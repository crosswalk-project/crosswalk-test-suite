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

var gDownloadId, gDocumentsDir, gFiles;

$(document).delegate("#main", "pageinit", function() {
    $("#list").delegate("div", "vclick", function() {
        deleteFileFromFolder($(this).parent().data("id"));
        return false;
    });

    $("#download").bind("vclick", function() {
        if (gDownloadId != undefined) {
            var state = tizen.download.getState(gDownloadId);

            if (state == "DOWNLOADING") {
                alert("Already downloading");
            } else {
                alert("Another download in progress");
            }
        } else {
            download();
        }
        return false;
    });

    $("#resume").bind("vclick", function() {
        if (gDownloadId != undefined) {
            var state = tizen.download.getState(gDownloadId);

            if (state == "PAUSED") {
                try {
                    tizen.download.resume(gDownloadId);
                    alert("Resumed");
                } catch (exc) {
                    alert("download.resume failed: " + exc.message);
                }
            } else {
                alert("Another download in progress");
            }
        } else {
            alert("No download in progress");
        }
        return false;
    });

    $("#pause").bind("vclick", function() {
        if (gDownloadId == undefined) {
            alert("No download in progress");
            return false;
        }

        var state = tizen.download.getState(gDownloadId);

        if (state == "PAUSED") {
            alert("Already paused");
        } else {
            try {
                tizen.download.pause(gDownloadId);
                alert("Paused");
            } catch (exc) {
                alert("download.pause failed: " + exc.message);
            }
        }
        return false;
    });

    $("#cancel").bind("vclick", function() {
        if (gDownloadId == undefined) {
            alert("No download in progress");
            return false;
        }

        try {
            tizen.download.cancel(gDownloadId);
        } catch (exc) {
            alert("download.cancel failed: " + exc.message);
        }
        return false;
    });

    $("#delete").bind("vclick", function() {
        deleteAllFile();
        return false;
    });
    prepareDirsAndFiles();
});

function onError(err) {
    alert("Error: " + err.message);
}

function prepareDirsAndFiles() {
    try {
        tizen.filesystem.resolve("downloads", function(dir) {
            gDocumentsDir = dir;
            showFileList();
        }, onError, "rw");
    } catch (exc) {
        alert("tizen.filesystem.resolve(\"downloads\") exc: " + exc.message);
    }
}

function makeFileList(files) {
    var str = "";

    gFiles = files;
    $("#list>li[data-id]").remove();

    for (var i = 0; i < files.length; i++) {
        if (files[i].isDirectory == false) {
            str += '<li class="ui-li-text-ellipsis" data-id="'
                + i
                + '">'
                + files[i].name
                + '<div data-role="button" data-inline="true">Delete</div></li>';
        }
    }
    $("#list").append(str).trigger("create").listview("refresh");
}

function showFileList() {
    if(gDocumentsDir) {
        gDocumentsDir.listFiles(function(files) {
            makeFileList(files);
        }, onError);
    }
}

function deleteFileFromFolder(id) {
    if (id == null) {
        return;
    }

    try {
        gDocumentsDir.deleteFile(gFiles[Number(id)].fullPath, showFileList, onError);
        alert("Download delete");
    } catch (exc) {
        alert("deleteFile exc: " + exc.message);
    }
}

function deleteAllFile() {
    alert("Download delete all");
    if(gFiles.length > 0)
        for(var i = 0; i < gFiles.length; i++)
            if(gFiles[i].isFile == true)
                gDocumentsDir.deleteFile(gFiles[i].fullPath, showFileList, onError);
}

function download() {
    var url = $("#url").val();

    if (url == "") {
        alert("Input target URL");
        return;
    }

    var downloadRequest = new tizen.DownloadRequest(url, "downloads"),
    listener = {
        onprogress: function(id, receivedSize, totalSize) {
            //$("#progressbar").progressbar("option", "value", receivedSize/totalSize*100);
            if(receivedSize > 0)
                $("#progressbar").reportprogress(receivedSize/totalSize*100);
            console.log('Received with id: ' + id + ', ' + receivedSize + '/' + totalSize);
        },
        onpaused: function(id) {
            console.log('Paused with id: ' + id);
            //showFileList();
        },
        oncanceled: function(id) {
            alert("Canceled");
            //showFileList();
            console.log(id);
            gDownloadId = undefined;
            $("#progressbar").reportprogress(0);
        },
        oncompleted: function(id, fullPath) {
            alert("Completed! Full path: " + fullPath);
            showFileList();
            gDownloadId = undefined;
        },
        onfailed: function(id, error) {
            alert("Failed! Err: " + error.name);
            //showFileList();
            gDownloadId = undefined;
            $("#progressbar").reportprogress(0);
        }
    };

    //$("#progressbar").progressbar("option", "value", 0);
    $("#progressbar").reportprogress(0);

    try {
        gDownloadId = tizen.download.start(downloadRequest, listener);
        alert("Download");
    } catch (exc) {
        alert("download.start failed : " + exc.message);
    }
}

var pct=0;
var handle=0;
function update(){
    $("#progressbar").reportprogress(++pct);
    if(pct==100){
        clearInterval(handle);
        $("#run").val("start");
        pct=0;
    }
}
jQuery(function($){
    $("#run").click(function(){
        if(this.value=="start"){
            handle=setInterval("update()",100);
            this.value="stop";
        }else{
            clearInterval(handle);
            this.value="start";
        }
    });
    $("#reset").click(function(){
        pct=0;
        $("#progressbar").reportprogress(0);
    });
});
