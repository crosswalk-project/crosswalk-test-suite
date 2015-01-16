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
        Liu, Yun <yunx.liu@intel.com>
*/

function showMessage(type, msg) {
  $("#popup_info").html("<div id='modal-dialog' class='modal-dialog' style='position: fixed'><div class='modal-content'><div class='modal-header' style='padding: 5px;'><button type='button' class='close' data-dismiss='modal' aria-hidden='true'>&times;</button><h4 class='modal-title'><span id='myModalLabel' class='glyphicon'></span></h4></div><div id='modal-body' class='modal-body' style='max-height: 100px; overflow: auto;'></div><div id='modal-footer' class='modal-footer' style='padding-top: 5px; padding-bottom: 5px'></div></div></div>");
  $("#modal-body").html(msg);
  switch(type) {
    case "help":
      $("#modal-footer").html("<div style='text-align: center; font-size:70%; color:gray'>Icons from <a href='http://glyphicon.com/'>Glyphicons</a></div>");
      $("#modal-dialog").css("bottom", "10px");
      $("#modal-dialog").css("width", "70%");
      $("#modal-dialog").css("left", "15%");
      $("#myModalLabel").addClass("glyphicon-info-sign");
      break;
    case "success":
      $("#modal-dialog").css("bottom", "30%");
      $("#modal-dialog").css("width", "50%");
      $("#modal-dialog").css("left", "25%");
      $("#myModalLabel").addClass("glyphicon-ok-sign");
      break;
    case "error":
      $("#modal-dialog").css("bottom", "30%");
      $("#modal-dialog").css("width", "50%");
      $("#modal-dialog").css("left", "25%");
      $("#myModalLabel").addClass("glyphicon-warning-sign");
      break;
    case "lstorage":
      $("#modal-footer").html("<button type='button' class='btn btn-default' data-dismiss='modal'>Yes</button><button type='button' id='ifCancel' class='btn btn-default' data-dismiss='modal'>No</button>");
      $("#modal-dialog").css("bottom", "30%");
      $("#modal-dialog").css("width", "50%");
      $("#modal-dialog").css("left", "25%");
      $("#myModalLabel").addClass("glyphicon-question-sign");
      break;
    case "exit":
      $("#modal-footer").html("<button type='button' class='btn btn-default' data-dismiss='modal'>Cancel</button><button type='button' id='ifConfirm' class='btn btn-default'>Exit</button>");
      $("#modal-dialog").css("bottom", "30%");
      $("#modal-dialog").css("width", "50%");
      $("#modal-dialog").css("left", "25%");
      $("#myModalLabel").addClass("glyphicon-log-out");
      break;
    default:
      break;
  }
}

function getApps(url, type) {
  var tests = "";
  $.ajax({
    async : false,
    type : "GET",
    url : url,
    dataType : type,
    success : function(type){tests = type;},
    error: function(e){showMessage("error", "Error:" + e.message + " occurs when parsing " + url + " file!")}
  });
  return tests;
}
