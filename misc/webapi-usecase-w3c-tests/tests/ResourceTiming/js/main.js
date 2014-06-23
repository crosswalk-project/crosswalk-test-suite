/*
Copyright (c) 2013 Intel Corporation.

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
        Xin, liu <xinx.liu@intel.com>

*/

window.onload = function() {
  loadingImg();
}

function make1lineListItem(value) {
  return '<li>' + value + '</li>';
}

function makeDividerListItem(value) {
  return '<li data-role="list-divider">' + value + '</li>';
}

function resourceTiming() {
  var resourceList = window.performance.getEntriesByType("resource");
  var fetchStart_redirectStart = resourceList[0].fetchStart - resourceList[0].redirectStart;
  var domainLookupStart_redirectStart = resourceList[0].domainLookupStart - resourceList[0].redirectStart;
  var connectStart_domainLookupEnd = resourceList[0].connectStart - resourceList[0].domainLookupEnd;
  var responseEnd_requestStart = resourceList[0].responseEnd - resourceList[0].requestStart;
  var responseEnd_redirectStart = resourceList[0].responseEnd - resourceList[0].redirectStart;
  gInfo = makeDividerListItem("PerformanceResourceTiming")
          + make1lineListItem("fetch start timing : " + fetchStart_redirectStart)
          + make1lineListItem("domain lookup timing : " + domainLookupStart_redirectStart)
          + make1lineListItem("connect start timing compare with domain end timing: " + connectStart_domainLookupEnd)
          + make1lineListItem("response end timing compare with request start timing : " + responseEnd_requestStart)
          + make1lineListItem("End to end resource fetch : " + responseEnd_redirectStart);
  $("#info-list2").html(gInfo).trigger("create").listview("refresh");
}

function loadingImg() {
  gInfo = makeDividerListItem("Loading image resource")
          +  '<a href="javascript:resourceFetchSuccess()" id="requestShow" data-role="button" class="opt">Load image</a>';
  $("#info-list1").html(gInfo).trigger("create").listview("refresh");
}

function resourceFetchSuccess(){
  var image1 = new Image();
  image1.src = 'http://test.csswg.org/source/support/cat.png';
  image1.onload = resourceTiming;
}
