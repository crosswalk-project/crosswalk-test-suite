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

$(document).ready(function() {
  var widthInput = document.getElementById('width-input');
  var heightInput = document.getElementById('height-input');
  var typeSelect = document.getElementById('type-select');
});

function filterTizen() {
  var widthValue = widthInput.value;
  if (!widthValue) {
    widthValue = widthInput.placeholder;
  }
  var heightValue = heightInput.value;
  if(!heightValue) {
    heightValue = heightInput.placeholder;
  }
  var count = 100;
  var widthFilter = new tizen.AttributeFilter("width", typeSelect.value, widthValue);
  var heightFilter = new tizen.AttributeFilter("height", typeSelect.value, heightValue);
  var filter = new tizen.CompositeFilter("INTERSECTION", [widthFilter, heightFilter]);
  tizen.content.find(findCB, errorCB, null, filter, null, count);
}

function errorCB(err) {
  $("#popup_info").modal(showMessage("error", 'The following error occurred: ' +  err.name));
}

function printContent(content, index, contents) {
  jQuery("#list").text('Track: ' + content.trackNumber + ' Title: ' + content.title + ' Duration: ' + content.duration + ' URL: ' + content.contentURI + ' MIME: ' + content.mimeType);
}

function findCB(contents) {
  if(contents.length == 0) {
    jQuery("#list").text("contents length is 0");
  }
  contents.forEach(printContent);
}
