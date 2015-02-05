/*
Copyright (c) 2013 Intel Corporation.

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
        Xu, YuhanX <yuhanx.xu@intel.com>

*/

var SHARED_MEDIA_DIR = "file://TESTER-HOME-DIR/content",
    MEDIA_ID = "#media";
var count = 0, mediaDir;
var gFiles = [], createdId = [];

$(document).ready(function(){
    DisablePassButton();
    $('#createFileBtn').addClass("ui-disabled");

    function onError(err) {
        alert("Error: " + err.message);
    }

    function makeFileList(files, selector) {
        var str = "";

        for (var i = 0; i < files.length; i++) {
            if (files[i].isDirectory == false) {
                str += '<li id="'
                    + files[i].name
                    + '"><a href="#"><h4>'
                    + files[i].name
                    + '</h4></a><a href="'
                    + 'javascript:deleteFile('
                    + count
                    + ')" data-icon="delete" data-theme="c">'
                    + '</a></li>';
                gFiles[count++] = files[i];
            }
        }
        if (str) {
            $(selector).append(str).trigger("create").listview("refresh");
        }

        $('#createFileBtn').removeClass("ui-disabled");
        $('#openMediaBtn').addClass("ui-disabled");
    }

    function openDirectory(str, selector) {
        try {
            tizen.filesystem.resolve(str, function(dir) {
                dir.listFiles(function(files) {
                    $(MEDIA_ID).show();
                    makeFileList(files, selector);
                    mediaDir = dir;
                    alert("Open Success");
                }, function(err) {
                    alert("Open Fail: " + err.message);
                });
            }, onError, "rw");
        } catch (exc) {
            alert("tizen.filesystem.resolve(" + str + ") exc: " + exc.message);
        }
    }

    function createFile(dir, selector) {
        if (!dir) {
            alert("Create File Error: The directory can not be opened");
            return;
        }

        try {
            var newFile, str = "";
            var time = new Date().getTime();
            newFile = dir.createFile("newFile" + time);
            str += '<li id="'
                + newFile.name
                + '"><a href="#"><h4>'
                + newFile.name
                + '</h4></a><a href="'
                + 'javascript:deleteFile('
                + count
                + ')" data-icon="delete" data-theme="c">'
                + '</a></li>';
            createdId.push(count);
            gFiles[count++] = newFile;
            if (str) {
                $(selector).append(str).trigger("create").listview("refresh");
            }
        } catch (exc) {
            alert("Create File Error: " + exc.message);
        }
    }

    $("#openMediaBtn").on("click",function() {
        if (!mediaDir) {
            openDirectory(SHARED_MEDIA_DIR, MEDIA_ID);
        }
    });
    $("#createFileBtn").on("click",function() {
        createFile(mediaDir, MEDIA_ID);
        EnablePassButton();
    });
});

function deleteFile(id) {
    var dir, selector, index;

    if (id == null) {
        return;
    }
    //Only delete the file by user created.
    index = createdId.indexOf(id);
    if (index == -1) {
        return;
    }

    try {
        dir = mediaDir;
        selector = MEDIA_ID;
        dir.deleteFile(gFiles[Number(id)].fullPath, function() {
            //Delete the id in createdId array.
            createdId.splice(index, 1);
            $("#" + gFiles[Number(id)].name).remove();
            $(selector).trigger("create").listview("refresh");
        }, function (err) {
            alert("Error: " + err.message);
        });
    } catch (exc) {
        alert("Delete File Error: " + exc.message);
    }
}

//function backAppsHome() {
//    createdId.forEach(function(id) {
//        deleteFile(id);
//    });
//}
