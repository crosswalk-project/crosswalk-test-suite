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
        Wang, Hongjuan <hongjuanx.wang@intel.com>

*/

var deviceReady = false;
var platformId = cordova.require('cordova/platform').id;
var pictureUrl = null;
var fileObj = null;
var fileEntry = null;
var pageStartTime = +new Date();

//default camera options
var camQualityDefault = ['quality value', 50];
var camDestinationTypeDefault = ['FILE_URI', 1];
var camPictureSourceTypeDefault = ['CAMERA', 1];
var camAllowEditDefault = ['allowEdit', false];
var camEncodingTypeDefault = ['JPEG', 0];
var camMediaTypeDefault = ['mediaType', 0];

//-------------------------------------------------------------------------
// Camera
//-------------------------------------------------------------------------

function log(value) {
  console.log(value);
 // document.getElementById('camera_status').textContent += (new Date() - pageStartTime) / 1000 + ': ' + value + '\n';
}

function clearStatus() {
  //document.getElementById('pic').innerHTML = '';
  document.getElementById('camera_image').src = 'about:blank';
  //var canvas = document.getElementById('canvas');
  // canvas.width = canvas.height = 1;
  pictureUrl = null;
  fileObj = null;
  fileEntry = null;
}

function setPicture(url, callback) {
try {
	window.atob(url);
	// if we got here it is a base64 string (DATA_URL)
	url = "data:image/jpeg;base64," + url;
} catch (e) {
	// not DATA_URL
    log('URL: ' + url.slice(0, 100));
}

  pictureUrl = url;
  var img = document.getElementById('camera_image');
  var startTime = new Date();
  img.src = url;
  img.onloadend = function() {
    log('Image tag load time: ' + (new Date() - startTime));
    callback && callback();
  };
}

function onGetPictureError(e) {
    log('Error getting picture: ' + e.code);
}

function getPictureWin(data) {
  setPicture(data);
  // TODO: Fix resolveLocalFileSystemURI to work with native-uri.
  if (pictureUrl.indexOf('file:') == 0 || pictureUrl.indexOf('content:') == 0) {
    resolveLocalFileSystemURI(data, function(e) {
      fileEntry = e;
      logCallback('resolveLocalFileSystemURI()', true)(e.toURL());
    }, logCallback('resolveLocalFileSystemURI()', false));
  } else if (pictureUrl.indexOf('data:image/jpeg;base64' == 0)) {
  	// do nothing
  } else {
    var path = pictureUrl.replace(/^file:\/\/(localhost)?/, '').replace(/%20/g, ' ');
    fileEntry = new FileEntry('image_name.png', path);
  }
}

function getPicture() {
  clearStatus();
  var options = extractOptions();
  log('Getting picture with options: ' + JSON.stringify(options));
  var popoverHandle = navigator.camera.getPicture(getPictureWin, onGetPictureError, options);

  // Reposition the popover if the orientation changes.
  window.onorientationchange = function() {
    var newPopoverOptions = new CameraPopoverOptions(0, 0, 100, 100, 0);
    popoverHandle.setPosition(newPopoverOptions);
  }
}

function uploadImage() {
  var ft = new FileTransfer(),
    uploadcomplete=0,
    progress = 0,
    options = new FileUploadOptions();
  options.fileKey="photo";
  options.fileName='test.jpg';
  options.mimeType="image/jpeg";
  ft.onprogress = function(progressEvent) {
    log('progress: ' + progressEvent.loaded + ' of ' + progressEvent.total);
  };
  var server = "http://cordova-filetransfer.jitsu.com";

  ft.upload(pictureUrl, server + '/upload', win, fail, options);
  function win(information_back){
    log('upload complete');
  }
  function fail(message) {
    log('upload failed: ' + JSON.stringify(message));
  }
}

function logCallback(apiName, success) {
  return function() {
    log('Call to ' + apiName + (success ? ' success: ' : ' failed: ') + JSON.stringify([].slice.call(arguments)));
  };
}

function extractOptions() {
  var els = document.querySelectorAll('#image-options select');
  var ret = {};
  for (var i = 0, el; el = els[i]; ++i) {
    var value = el.value;
    if (value === '') continue;
    if (el.isBool) {
      ret[el.keyName] = !!+value;
    } else {
      ret[el.keyName] = +value;
    }
  }
  return ret;
}

function createOptionsEl(name, values, selectionDefault) {
  var table = document.createElement('table');
  var tr = document.createElement('tr');
  var container = document.createElement('td');
  table.appendChild(tr);
  tr.appendChild(container);
  table.style.cssText = "border: 1px;"
  container.appendChild(document.createTextNode(name + ': '));
  var select = document.createElement('select');
  select.keyName = name;
  container.appendChild(select);

  // if we didn't get a default value, insert the blank <default> entry
  if (selectionDefault == undefined) {
    var opt = document.createElement('option');
    opt.value = '';
    opt.text = '<default>';
    select.appendChild(opt);
  }

  select.isBool = typeof values == 'boolean';
  if (select.isBool) {
    values = {'true': 1, 'false': 0};
  }

  for (var k in values) {
    var opt = document.createElement('option');
    opt.value = values[k];
    opt.textContent = k;
    if (selectionDefault) {
      if (selectionDefault[0] == k) {
        opt.selected = true;
      }
    }
    select.appendChild(opt);
  }
  var optionsDiv = document.getElementById('image-options');
  optionsDiv.appendChild(table);
}

/**
 * Function called when page has finished loading.
 */
function init() {
    document.addEventListener("deviceready", function() {
      deviceReady = true;
      createOptionsEl('Encoding Type', Camera.EncodingType, camEncodingTypeDefault);
      createOptionsEl('Media Type', Camera.MediaType, camMediaTypeDefault);
      createOptionsEl('Destination Type', Camera.DestinationType, camDestinationTypeDefault);
      createOptionsEl('Source Type', Camera.PictureSourceType, camPictureSourceTypeDefault); 
    }, false);
    window.setTimeout(function() {
      if (!deviceReady) {
        alert("Error: Apache Cordova did not initialize.  Demo will not run correctly.");
      }
    },1000);
};
