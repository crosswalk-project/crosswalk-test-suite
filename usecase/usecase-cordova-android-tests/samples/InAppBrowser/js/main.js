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

/**
* Function called when page has finished loading.
*/
function init() {
  document.addEventListener("deviceready", function() {
    document.cookie = "main page cookie";
    deviceReady = true;
    console.log("Device="+device.platform+" "+device.version);
  }, false);
  window.setTimeout(function() {
  	if (!deviceReady) {
  		alert("Error: Apache Cordova did not initialize. Demo will not run correctly.");
  	}
  },1000);
}

function doOpen(url, target, params, numExpectedRedirects) {
  numExpectedRedirects = numExpectedRedirects || 0;
  var iab = window.open(url, target, params);
  if (!iab) {
    alert('window.open returned ' + iab);
    return;
  }
  var counts;
  var lastLoadStartURL;
  var wasReset = false;
  function reset()  {
    counts = {
        'loaderror': 0,
        'loadstart': 0,
        'loadstop': 0,
        'exit': 0
    };
    lastLoadStartURL = '';
  }
  reset();

  function logEvent(e) {
    console.log('IAB event=' + JSON.stringify(e));
    counts[e.type]++;
    // Verify that event.url gets updated on redirects.
    if (e.type == 'loadstart') {
      if (e.url == lastLoadStartURL) {
        alert('Unexpected: loadstart fired multiple times for the same URL.');
      }
      lastLoadStartURL = e.url;
    }
    // Verify the right number of loadstart events were fired.
    if (e.type == 'loadstop' || e.type == 'loaderror') {
      if (e.url != lastLoadStartURL) {
        alert('Unexpected: ' + e.type + ' event.url != loadstart\'s event.url');
      }
      if (numExpectedRedirects === 0 && counts['loadstart'] !== 1) {
        // Do allow a loaderror without a loadstart (e.g. in the case of an invalid URL).
        if (!(e.type == 'loaderror' && counts['loadstart'] === 0)) {
          alert('Unexpected: got multiple loadstart events. (' + counts['loadstart'] + ')');
        }
      } else if (numExpectedRedirects > 0 && counts['loadstart'] < (numExpectedRedirects+1)) {
        alert('Unexpected: should have got at least ' + (numExpectedRedirects+1) + ' loadstart events, but got ' + counts['loadstart']);
      }
      wasReset = true;
      numExpectedRedirects = 0;
      reset();
    }
    // Verify that loadend / loaderror was called.
    if (e.type == 'exit') {
      var numStopEvents = counts['loadstop'] + counts['loaderror'];
      if (numStopEvents === 0 && !wasReset) {
        alert('Unexpected: browser closed without a loadstop or loaderror.')
      } else if (numStopEvents > 1) {
        alert('Unexpected: got multiple loadstop/loaderror events.');
      }
    }
  }
  iab.addEventListener('loaderror', logEvent);
  iab.addEventListener('loadstart', logEvent);
  iab.addEventListener('loadstop', logEvent);
  iab.addEventListener('exit', logEvent);

  return iab;
}
