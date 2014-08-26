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
var reminder;
var flag = true;

function hideDiv() {
  setTimeout(function(){reminder.style.visibility = "hidden";},"2000");
}

function start() {
  tizen.content.getDirectories(getDirectoriesCB, errorCB);
}

function errorCB(err) {
  reminder.innerHTML =  'The following error occurred: ' +  err.name;
  reminder.style.visibility = "visible";
  hideDiv();
}

function printDirectory(directory, index, directories) {
  if(flag) {
    text = text + "<tr class='tr2'><td>" + directory.directoryURI + "</td><td>" + directory.title +"</td><td><a href='javascript: find(" + index +");'>GETFILES</a></td></tr>";     
  } else {
    text = text + "<tr class='tr1'><td>" + directory.directoryURI + "</td><td>" + directory.title +"</td><td><a href='javascript: find(" + index +");'>GETFILES</a></td></tr>";
  }
  flag = !flag;
  list.innerHTML = text;
}

function find(num) {
  tizen.content.find(findSuccess, findError, dirs[num].id, null, null, 20);
}

function findSuccess(contents) {
  cons = contents;
  text = "<tr class='tr0'><td width='25%'>Title</td><td width='25%'>URL</td><td width='25%'>MIME</td><td width='25%'>Operation</td></tr>";
  index = 0;
  contents.forEach(printContent);
}

function printContent(content, index, contents) {
  if(flag) {
    text = text + "<tr class='tr2'><td>" + content.title + "</td><td>" + content.contentURI +"</td><td>" + content.mimeType + "</td><td><a href='javascript: scan(" + index +");'>SCANFILE</a></td></tr>";     
  } else {
    text = text + "<tr class='tr1'><td>" + content.title + "</td><td>" + content.contentURI +"</td><td>" + content.mimeType + "</td><td><a href='javascript: scan(" + index +");'>SCANFILE</a></td></tr>"; 
  }
  flag = !flag;
  list.innerHTML = text;
}

function findError(err) {
  reminder.innerHTML =  'Find Files error: ' +  err.name;
  reminder.style.visibility = "visible";
  hideDiv();
}

function scan(num) {
  tizen.content.scanFile(cons[num].contentURI, scanSuccess, scanError);
}

function scanSuccess(path) {
  reminder.innerHTML = "scanning is completed. " + JSON.stringify(path);
  reminder.style.visibility = "visible";
  hideDiv();
}

function scanError(err) {
  reminder.innerHTML = "scanning error. " + err.name;
  reminder.style.visibility = "visible";
  hideDiv();
}

function getDirectoriesCB(directories) {
  dirs = directories;
  text = "<tr class='tr0'><td width='40%'>directoryURI</td><td width='40%'>Title</td><td width='20%'>Operation</td></tr>";
  directories.forEach(printDirectory);
}

$(document).ready(function(){
  list = document.getElementById("result");
  reminder = document.getElementById("reminder");
  var listener= {
    oncontentadded: function(content) {
      reminder.innerHTML = content.contentURI + ' content is added';
      reminder.style.visibility = "visible";
      hideDiv();
    },
    oncontentupdated: function(content) {
      reminder.innerHTML = content.contentURI + ' content is updated';
      reminder.style.visibility = "visible";
      hideDiv();
    },
    oncontentremoved: function(id) {
      reminder.innerHTML = id + ' is removed';
      reminder.style.visibility = "visible";
      hideDiv();
    }
 };
 tizen.content.setChangeListener(listener);
 start();
});
