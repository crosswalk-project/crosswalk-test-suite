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

window.onload = function(){
    $("#download").click(downloaded);
    $("#resume").click(resume);
    $("#pause").click(pause);
    $("#cancel").click(cancel);
};

function downloaded() {
    if(downloadItem != undefined) {
        var state = downloadItem.state;
        if(state == "running") {
            $("#popup_info").modal(showMessage("success", "Already downloading"));
        } else {
            $("#popup_info").modal(showMessage("error", "Another download in progress"));
        }
    } else {
        download();
    }
}

function resume() {
    if (downloadItem != undefined) {
        var state = downloadItem.state;
        if (state == "paused") {
            downloadItem.resume().then(function(){
                  $("#popup_info").modal(showMessage("success", "Resumed"));
              },function(error){
                  $("#popup_info").modal(showMessage("error", "download.resume failed: " + error.message));
              });
        } else {
            $("#popup_info").modal(showMessage("error", "Another download in progress"));
        }
    } else {
        $("#popup_info").modal(showMessage("error", "No download in progress"));
    }
}

function pause() {
    if (downloadItem == undefined) {
        $("#popup_info").modal(showMessage("error", "No download in progress"));
    }
    var state = downloadItem.state;
    if (state == "paused") {
        $("#popup_info").modal(showMessage("error", "Already paused"));
    } else {
        downloadItem.pause().then(function(){
              $("#popup_info").modal(showMessage("success", "paused"));
          },function(error){
              $("#popup_info").modal(showMessage("error", "download.pause failed: " + error.message));
          });
    }
}

function cancel() {
    if (downloadItem == undefined) {
        $("#popup_info").modal(showMessage("error", "No download in progress"));
    }
    downloadItem.cancel().then(function(){
          $("#popup_info").modal(showMessage("success", "canceled"));
      },function(error){
          $("#popup_info").modal(showMessage("error", "download.cancel failed: " + error.message));
      });
}

function onError(err) {
    $("#popup_info").modal(showMessage("error", "Error: " + err.message));
}

function download() {
    url = $("#url").val();
    if (url == "") {
        $("#popup_info").modal(showMessage("error", "Input target URL"));
        return;
    }
    targetFile = $("#targetFile").val();
    if (targetFile == "") {
        $("#popup_info").modal(showMessage("error", "Input target File"));
        return;
    }
    DownloadManager.createDownload(url, targetFile).then( function (item) {
        downloadItem = item;
        //alert(downloadItem);
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
              $("#popup_info").modal(showMessage("error", "start download error"));
          });
    }, function (error){ 
        $("#popup_info").modal(showMessage("error", "create download error"));
    });
}

