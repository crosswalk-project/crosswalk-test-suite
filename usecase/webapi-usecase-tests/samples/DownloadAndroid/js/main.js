/*
Copyright (c) 2014 Intel Corporation.

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
        Zhu, YongyongX <yongyongx.zhu@intel.com>

*/

var gDocumentsDir, gFiles;

var url,targetFile;
var downloadItem;
function init() {
    url = "http://www.download.com/example.html";
    targetFile = "download/file/example.html";
}

$(document).delegate("#main", "pageinit", function() {

    $("#download").bind("vclick", function() {
        if(downloadItem != undefined) {
            var state = downloadItem.state;
            if(state == "running") {
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
        if (downloadItem != undefined) {
            var state = downloadItem.state;
            if (state == "paused") {
                downloadItem.resume().then(function(){
                      alert("Resumed");
                  },function(error){
                      alert("download.resume failed: " + error.message);
                  });
            } else {
                alert("Another download in progress");
            }
        } else {
            alert("No download in progress");
        }
        return false;
    });

    $("#pause").bind("vclick", function() {
        if (downloadItem == undefined) {
            alert("No download in progress");
            return false;
        }
        var state = downloadItem.state;
        if (state == "paused") {
            alert("Already paused");
        } else {
            downloadItem.pause().then(function(){
                  alert("paused");
              },function(error){
                  alert("download.pause failed: " + error.message);
              });
        }
        return false;
    });

    $("#cancel").bind("vclick", function() {
        if (downloadItem == undefined) {
            alert("No download in progress");
            return false;
        }
        downloadItem.cancel().then(function(){
              alert("canceled");
          },function(error){
              alert("download.cancel failed: " + error.message);
          });
        return false;
    });
    
    $("#delete").bind("vclick", function() {
        deleteAllFile();
        return false;
    });
    
});

function onError(err) {
    alert("Error: " + err.message);
}

function download() {
    url = $("#url").val();
    if (url == "") {
        alert("Input target URL");
        return;
    }
    targetFile = $("#targetFile").val();
    if (targetFile == "") {
        alert("Input target File");
        return;
    }
    DownloadManager.createDownload(url, targetFile).then( function (item) {
        downloadItem = item;
        alert(downloadItem);
        downloadItem.start().then(function(){
              if(downloadItem.state == "running"){
                  downloadItem.onProgress = function(receivedSize){
                      $("#progressbar").reportprogress(receivedSize/totalBytes*100);
                      if(receivedSize == totalBytes) {
                          downloadItem = undefined;
                      }
                  }
              }
              downloadItem.onCancel = function(){
                   downloadItem = undefined;
                   $("#progressbar").reportprogress(0);   
              }
          },function(error){
              alert("start download error");
          });
    }, function (error){ 
        alert("create download error");
    });
}

