/*
Copyright (c) 2012 Intel Corporation.

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

*/

var docElm = document.documentElement;
var video;
var iframe;

function getFullScreenChangeName() {
  if("fullScreen" in document){
     return "fullscreenchange";
  }else if("mozFullScreen" in document){
      return "mozfullscreenchange";
  }else if("webkitIsFullScreen" in document){
     return "webkitfullscreenchange";
  }else{
  }
}

function getCssFullScreen() {
  if("fullScreen" in document){
     return "fullscreen";
  }else if("mozFullScreen" in document){
      return "-moz-full-screen";
  }else if("webkitIsFullScreen" in document){
     return "-webkit-full-screen";
  }else{
  }
}

function getVideoElement() {
  video = document.getElementById("video");
}

function getIframeElement() {
  iframe = document.getElementById("iframe");
}

function getCurrentStyle(prop) {
  var div = document.querySelector("#media");
    propprop = headProp(prop);
    return getComputedStyle(div)[propprop];
}

function headProp(s) {
var div = document.querySelector("#media");
  if (s in div.style) {
    return s;
  }
  s = s[0].toUpperCase() + s.slice(1);
  var prefixes = ["ms", "Moz", "moz", "webkit", "O"];
  for (var i = 0; i < prefixes.length; i++) {
    if ((prefixes[i] + s) in div.style) {
      return prefixes[i] + s;
    }
  }
  return s;
}
