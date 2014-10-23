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

var MY_PUBID = "<Your pubid>";
var testDiv = document.getElementById("testDiv");
var advertising = window.ad || xwalk.experimental.ad
showUnoverlappedAd = function() {
  advertising.create({
    "service" : "admob",
    "publisherId" : MY_PUBID,
    "type" : "banner",
    "size" : "BANNER",
    "bannerAtTop" : false,
    "overlap" : false
  }).then(
    function(ad) {
      ad.show(true)
      ad.onopened = function() {testDiv.innerHTML = "open";}
      ad.onclosed = function() {testDiv.innerHTML = "close";}
      ad.onfailed = function(msg) {
      testDiv.innerHTML = JSON.stringify(msg);
      testDiv.innerHTML = "failed";;
      ad.destroy()
    }
    ad.onloaded = function() {testDiv.innerHTML = "loaded";}
    },
    function(err) {
      testDiv.innerHTML = JSON.stringify(err);
    }
  );
}

showOverlappedAd = function() {
  advertising.create({
    "service" : "admob",
    "publisherId" : MY_PUBID,
    "type" : "banner",
    "size" : "SMART_BANNER",
    "bannerAtTop" : true,
    "overlap" : true
    }).then(
      function(ad) {
        ad.show(true)
        ad.onopened = function() {testDiv.innerHTML = "open";}
        ad.onclosed = function() {testDiv.innerHTML = "close";}
        ad.onfailed = function(msg) {
          testDiv.innerHTML = JSON.stringify(msg);
          testDiv.innerHTML = "failed";
          ad.destroy()
        }
        ad.onloaded = function() {testDiv.innerHTML = "loaded";}
        },
        function(err) {
          testDiv.innerHTML = JSON.stringify(err);
        }
  );
}

showInterstitialAd = function() {
  advertising.create({
    "service" : "admob",
    "publisherId" : MY_PUBID,
    "type" : "interstitial",
    }).then(
      function(ad) {
        ad.onloaded = function() {
        ad.show();
        }
      },
      function(err) {
        testDiv.innerHTML = JSON.stringify(err);
      }
  );
}
