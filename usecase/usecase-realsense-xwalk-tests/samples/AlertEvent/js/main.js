/*
Copyright (c) 2016 Intel Corporation.

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
*/

var videoElement;
var msg;
var alertMsg;
var newFaceCheckbox;
var faceOutFovCheckbox;
var faceBackFovCheckbox;
var faceOccludedCheckbox;
var faceNoLongerOccludedCheckbox;
var faceLostCheckbox;
var ft;

function init() {
  videoElement = document.getElementById("preview");
  msg = document.getElementById("log");
  alertMsg = document.getElementById("alert");
  newFaceCheckbox = document.getElementById("enableNewFace");
  faceOutFovCheckbox = document.getElementById("enableFaceOutFov");
  faceBackFovCheckbox = document.getElementById("enableFaceBackFov");
  faceOccludedCheckbox = document.getElementById("enableFaceOccluded");
  faceNoLongerOccludedCheckbox = document.getElementById("enableFaceNoLongerOccluded");
  faceLostCheckbox = document.getElementById("enableFaceLost");
}

function setConfig() {
  var alertConf = {};
  alertConf.newFaceDetected = true;
  alertConf.faceOutOfFov = true;
  alertConf.faceBackToFov = true;
  alertConf.faceOccluded = true;
  alertConf.faceNoLongerOccluded = true;
  alertConf.faceLost = true;

  var detectionConf = {};
  detectionConf.enable = true;
  detectionConf.maxFaces = 12;

  var landmarksConf = {};
  landmarksConf.enable = true;
  landmarksConf.maxFaces = 12;

  var recognitionConf = {};
  recognitionConf.enable = true;

  var faceConf = {};
  faceConf.mode = "color_depth";
  faceConf.strategy = "closest_farthest";
  faceConf.alert = alertConf;
  faceConf.detection = detectionConf;
  faceConf.landmarks = landmarksConf;
  faceConf.recognition = recognitionConf;

  ft.configuration.set(faceConf)
  .then(function() {
    msg.textContent = "set configuration success";
  })
  .catch(errorCallback);
}

function getConfig() {
  ft.configuration.get()
  .then(function(configData) {
    newFaceCheckbox.checked = configData.alert.newFaceDetected;
    faceOutFovCheckbox.checked = configData.alert.faceOutOfFov;
    faceBackFovCheckbox.checked = configData.alert.faceBackToFov;
    faceOccludedCheckbox.checked = configData.alert.faceOccluded;
    faceNoLongerOccludedCheckbox.checked = configData.alert.faceNoLongerOccluded;
    faceLostCheckbox.checked = configData.alert.faceLost;
  })
  .catch(errorCallback);	
}

function initFaceModule(stream) {
  try {
    ft = new realsense.Face.FaceModule(stream);
  } catch(ex) {
    msg.textContent = "init face module error: " + ex.message;
    return; 
  }

  setConfig();

  ft.onready = function(evt) {
    ft.start()
    .then(function() {
      msg.textContent = "start success!";
    })
    .catch(errorCallback);
  }

  ft.onalert = function(evt) {
    alertMsg.textContent = "Alert event is fired. get faceId: " + evt.faceId +
                           ", AlertType: " + evt.typeLabel;
  }

  ft.onerror = function(evt) {
    msg.textContent = "onerror:" + evt.message;
  }

  ft.onprocessedsample = function(evt) {
    ft.getProcessedSample(false, false)
    .then(function(processedSample) {
      if(processedSample.faces != null) {
        for (var i = 0; i < processedSample.faces.length; i++) {
          var face = processedSample.faces[i];
          msg.textContent = "current faceId: " + face.faceId +
                            ", userId: " + face.recognition.userId;					
        }
      }
    })
    .catch(errorCallback);
  }
}

function errorCallback(ex) {
  msg.textContent = ex.message;	
}

window.onload = function() {
  init();
  navigator.getUserMedia({
    video: true
    }, function getStream(stream) {
      videoElement.src = URL.createObjectURL(stream);
      initFaceModule(stream);
    }, function(ex) {
      msg.textContent = "Get error when access media stream:" + ex.message;
    });
}
