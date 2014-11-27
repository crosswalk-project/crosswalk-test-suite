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

var MY_PUBID = "ca-app-pub-8571598764628778/2674780845";
var advertising = window.ad || xwalk.experimental.ad
$(document).ready(function () {
  $("#unoverlappedAd").click(function(){
    advertising.create({
      "service" : "admob",
      "publisherId" : MY_PUBID,
      "type" : "banner",
      "size" : "BANNER",
      "bannerAtTop" : false,
      "overlap" : false
    }).then(
      function(ad) {
        $("#testDiv").empty();
        ad.show(true);
        $("#testDiv").text("Show un-overlop advertising");
        ad.onopened = function() {
          $("#testDiv").text($("#testDiv").text() + "\n" + "Fired onopen event");
        }
        ad.onclosed = function() {
          $("#testDiv").text($("#testDiv").text() + "\n" + "Fired onclose event");
        }
        ad.onfailed = function(msg) {
          $("#testDiv").text($("#testDiv").text() + "\n" + "Failed message: " + JSON.stringify(msg));
          ad.destroy()
        }
        ad.onloaded = function() {
          $("#testDiv").text($("#testDiv").text() + "\n" + "Un-overlop advertising loaded");
        }
        $("#destoryUnover").click(function (){
          $("#testDiv").text($("#testDiv").text() + "\n" + "Destory un-overlop advertising successfully")
          ad.destroy()
        })
      },
      function(err) {
        $("#testDiv").text($("#testDiv").text() + "\n" + "Error message: " + JSON.stringify(msg));
      }
    );
  })

  $("#overlappedAd").click(function (){
    advertising.create({
      "service" : "admob",
      "publisherId" : MY_PUBID,
      "type" : "banner",
      "size" : "SMART_BANNER",
      "bannerAtTop" : true,
      "overlap" : true
    }).then(
      function(ad) {
        $("#testDiv").empty();
        ad.show(true)
        $("#testDiv").text("Show overlop advertising");
        ad.onopened = function() {
          $("#testDiv").text($("#testDiv").text() + "\n" + "Fired onopen event");
        }
        ad.onclosed = function() {
          $("#testDiv").text($("#testDiv").text() + "\n" + "Fired onclose event");
        }
        ad.onfailed = function(msg) {
          $("#testDiv").text($("#testDiv").text() + "\n" + JSON.stringify(msg) + "failed");
        }
        ad.onloaded = function() {
          $("#testDiv").text($("#testDiv").text() + "\n" + "Overlop advertising loaded");
        }
        $("#destoryOver").click(function (){
          $("#testDiv").text($("#testDiv").text() + "\n" + "Destory overlop advertising successfully")
          ad.destroy()
        })
      },
      function(err) {
        $("#testDiv").text($("#testDiv").text() + "\n" + JSON.stringify(err));
      }
    );
  })

  $("#interstitialAd").click(function (){
    advertising.create({
      "service" : "admob",
      "publisherId" : "ca-app-pub-8571598764628778/7104980442",
      "type" : "interstitial",
    }).then(
      function(ad) {
        $("#testDiv").empty();
        $("#testDiv").text($("#testDiv").text() + "\n" + "Show interstitial advertising")
        ad.onloaded = function() {
          $("#testDiv").text($("#testDiv").text() + "\n" + "Interstitial advertising loaded");
          ad.show(true)
        }
      },
      function(err) {
        $("#testDiv").text($("#testDiv").text() + "\n" + "Error" + JSON.stringify(err));
      }
    );
  })
})
