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

var photoCapture;
var imgContext;
var currentPhoto;
var width;
var height;

window.onload = function() {
  width = $("#imgPreview")[0].width;
  height = $("#imgPreview")[0].height;
  imgContext = $("#imgPreview")[0].getContext("2d");
  $("#takePhoto").click(takePhoto);
  $("#setContainerImage").click(setContainerImage);
  $("#setColorImage").click(setColorImage);
  $("#setDepthImage").click(setDepthImage);
  $("#setRawDepthImage").click(setRawDepthImage);
  getStream();	
}

function getStream() {
  var constraints = {video: {
    width: 320,
    height: 240}
  };	
  navigator.getUserMedia(constraints, function successCallback(stream) {
    $("#preview")[0].src = URL.createObjectURL(stream);
    photoCapture = new realsense.DepthEnabledPhotography.PhotoCapture(stream);
    $("#log").text("init success");
  }, function(ex) {
    $("#log").text("access video stream fail.");
  });	
}

function takePhoto() {
  photoCapture.takePhoto()
    .then(function(photo) {
      currentPhoto = photo;
      return currentPhoto.queryContainerImage();
    })
    .then(function(image) {
      fillCanvas(image, false);
    })
    .catch(errorCallback);	
}

function setContainerImage(){
  if(currentPhoto == null) {
    $("#log").text("please capture photo first!");
    return;
  }
  photoCapture.takePhoto()
    .then(function(photo) {
      return photo.queryContainerImage();
    })
    .then(function(image) {
      return currentPhoto.setContainerImage(image);
    })
    .then(function() {
      $("#log").text("set container image succeed!");
      return currentPhoto.queryContainerImage();
    })
    .then(function(image) {
      fillCanvas(image, false);
    })
    .catch(errorCallback);
}

function setColorImage() {
  if(currentPhoto == null) {
    $("#log").text("please capture photo first!");
    return;
  }
  photoCapture.takePhoto()
    .then(function(photo) {
      return photo.queryImage();
    })
    .then(function(image) {
      return currentPhoto.setColorImage(image);
    })
    .then(function() {
      $("#log").text("set color image succeed!");
      return currentPhoto.queryImage();
    })
    .then(function(image) {
      fillCanvas(image, false);
    })
    .catch(errorCallback);	
}

function setDepthImage() {
  if(currentPhoto == null) {
    $("#log").text("please capture photo first!");
    return;
  }
  photoCapture.takePhoto()
    .then(function(photo) {
      return photo.queryDepth();
    })
    .then(function(image) {
      return currentPhoto.setDepthImage(image);
    })
    .then(function() {
      $("#log").text("set depth image succeed!");
      return currentPhoto.queryDepth();
    })
    .then(function(image) {
      fillCanvas(image, true);
    })
    .catch(errorCallback);	
}

function setRawDepthImage() {
  if(currentPhoto == null) {
    $("#log").text("please capture photo first!");
    return;
  }
  photoCapture.takePhoto()
    .then(function(photo) {
      return photo.queryRawDepth();
    })
    .then(function(image) {
      return currentPhoto.setRawDepthImage(image);
    })
    .then(function() {
      $("#log").text("set raw depth image succeed!");
      return currentPhoto.queryRawDepth();
    })
    .then(function(image) {
      fillCanvas(image, true);
    })
    .catch(errorCallback);	
}

function errorCallback(ex) {
  $("#log").text(ex.message);	
}

function fillCanvas(image, isdepth) {
  imgContext.clearRect(0, 0, width, height);	
  var imgData = imgContext.createImageData(image.width, image.height);
  if(isdepth) {
    ConvertDepthToRGBUsingHistogram(
      image, [255, 255, 255], [0, 0, 0], imgData.data);
  } else {
    imgData.data.set(image.data);	  
  }
  imgContext.putImageData(imgData, 0, 0);
}

function ConvertDepthToRGBUsingHistogram(
    depthImage, nearColor, farColor, rgbImage) {
  var depthImageData = depthImage.data;
  var imageSize = depthImage.width * depthImage.height;
  for (var l = 0; l < imageSize; ++l) {
    rgbImage[l * 4] = 0;
    rgbImage[l * 4 + 1] = 0;
    rgbImage[l * 4 + 2] = 0;
    rgbImage[l * 4 + 3] = 255;
  }
  var histogram = new Int32Array(256 * 256);
  for (var i = 0; i < imageSize; ++i) {
    if (depthImageData[i]) {
      ++histogram[depthImageData[i]];
    }
  }
  for (var j = 1; j < 256 * 256; ++j) {
    histogram[j] += histogram[j - 1];
  }

  for (var k = 1; k < 256 * 256; k++) {
    histogram[k] = (histogram[k] << 8) / histogram[256 * 256 - 1];
  }

  for (var l = 0; l < imageSize; ++l) {
    if (depthImageData[l]) {
      var t = histogram[depthImageData[l]];
      rgbImage[l * 4] = ((256 - t) * nearColor[0] + t * farColor[0]) >> 8;
      rgbImage[l * 4 + 1] = ((256 - t) * nearColor[1] + t * farColor[1]) >> 8;
      rgbImage[l * 4 + 2] = ((256 - t) * nearColor[2] + t * farColor[2]) >> 8;
      rgbImage[l * 4 + 3] = 255;
    }
  }
}
