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
        Xu, Jianfeng <jianfengx.xu@intel.com>

*/

var text = "";
var list;
var dirs;
var cons;
function start() {
  tizen.content.getDirectories(getDirectoriesCB, errorCB);
}

function errorCB(err) {
  list.innerHTML =  'The following error occurred: ' +  err.name;
}

function printDirectory(directory, index, directories) {
  text = text + 'directoryURI: ' + directory.directoryURI + '&nbsp;&nbsp;Title: ' + directory.title + "&nbsp;&nbsp;&nbsp;<a href='javascript: find(" + index +");'>GETFILES</a><br>";
  list.innerHTML = text;
}

function find(num) {
  list.innerHTML = dirs[num].id;
  tizen.content.find(findSuccess, findError, dirs[num].id, null, null, 20);
}

function findSuccess(contents) {
  cons = contents;
  text = "";
  index = 0;
  contents.forEach(printContent);
}

function printContent(content, index, contents) {
  text = text  + ' Title: ' + content.title  + '&nbsp;&nbsp;URL: ' + content.contentURI + '&nbsp;&nbsp;MIME: ' + content.mimeType + "&nbsp;&nbsp;&nbsp;<a href='javascript: scan(" + index +");'>SCANFILE</a><br>";
  list.innerHTML = text;
}

function findError(err) {
  list.innerHTML =  'Find error: ' +  err.name;
}

function scan(num) {
  tizen.content.scanFile(cons[num].contentURI, scanSuccess, scanError);
}

function scanSuccess(path) {
  list.innerHTML = "scanning is completed. " + JSON.stringify(path);
}

function scanError(err) {
  list.innerHTML = "scanning error. " + err.name;
}

function getDirectoriesCB(directories) {
  list.innerHTML = directories.length;
  dirs = directories;
  text = "";
  directories.forEach(printDirectory);
}

$(document).ready(function(){
  list = document.getElementById("list");
  var listener= {
    oncontentadded: function(content) {
        list.innerHTML = content.contentURI + ' content is added';
    },
    oncontentupdated: function(content) {
        list.innerHTML = content.contentURI + ' content is updated';
    },
    oncontentremoved: function(id) {
        list.innerHTML = id + ' is removed';
    }
 };
 tizen.content.setChangeListener(listener);
});
