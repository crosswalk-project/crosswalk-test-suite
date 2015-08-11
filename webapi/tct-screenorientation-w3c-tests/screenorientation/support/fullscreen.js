/*
Copyright (c) 2015 Intel Corporation.

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
        Li, Hao <haox.li@intel.com>

*/

if (document.getElementsByName("flags").length == 0) {
  document.write('<meta name="flags" content="interact">\n');
}
if (document.getElementsByName("timeout").length == 0) {
  document.write('<meta name="timeout" content="long">\n');
}

document.write('<div id="log"></div>\n');
document.write('<button id="start">Start to Test</button>\n');
document.write('<button id="cancel" hidden>Cancel FullScreen</button>\n');

window.onload = function() {
  document.getElementById("start").onclick = function() {
    document.onwebkitfullscreenchange = function() {
      document.getElementById("start").hidden = true;
      document.getElementById("cancel").hidden = false;
      if (runTestRequireFullScreen) {
        runTestRequireFullScreen();
      }
    };
    document.documentElement.webkitRequestFullScreen();
  };

  document.getElementById("cancel").onclick = function() {
    document.onwebkitfullscreenchange = function() {
      document.getElementById("start").hidden = false;
      document.getElementById("cancel").hidden = true;
    };
    document.webkitCancelFullScreen();
  };
};

