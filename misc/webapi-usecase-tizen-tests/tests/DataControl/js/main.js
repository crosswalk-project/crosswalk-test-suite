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
        Liu, yun <yun.liu@archermind.com>

*/

var globalSQLConsumer = tizen.datacontrol.getDataControlConsumer(
  "http://tizen.org/datacontrol/provider/DictionaryDataControlProvider", "Dictionary", "SQL");
var globalReqId = new Date().getTime() % 1e8;
var rowData;
var testFlag = {
    green: false,
    red: false,
    blue: false
};

function status () {
  if (testFlag.green && testFlag.red && testFlag.blue) {
    EnablePassButton();
  }
}

function successAdd (id) {
  var array = ["WORD", "WORD_DESC" ];
  globalReqId++;
  globalSQLConsumer.select(globalReqId, array, "WORD='" + $("#new_value").val() + "'", getValueSuccessCB, errorcb);
  $("#new_value").attr("value", "");
  $("#new_value_desc").attr("value", "");
}

function successUpdate (id) {
  var array = ["WORD", "WORD_DESC" ];
  globalReqId++;
  globalSQLConsumer.select(globalReqId, array, "WORD='" + $("#old_value").val() + "'", getValueSuccessCB, errorcb);
  $("#old_value").attr("value", "");
  $("#new_value_desc_1").attr("value", "");
}

function successRemove (id) {
  $("#old_value_1").attr("value", "");
  $("#datawindow").html("Remove success : reqid "+ id);
}

function errorcb (id, error) {
  $("#datawindow").html("error id : " + id + ", error msg : " + error.message);
  $("#new_value").attr("value", "");
  $("#new_value_desc").attr("value", "");
  $("#old_value").attr("value", "");
  $("#new_value_desc_1").attr("value", "");
  $("#old_value_1").attr("value", "");
}

function getValueSuccessCB (result, id) {
  var length = result.length;
  for (var i = 0; i < length; i++) {
    var j = 0;
    for (j = 0; j < result[i].columns.length; j++) {
      $("#datawindow").html("column: " + result[i].columns[j] + ", value_desc: " + result[i].values[j]);
    }
  }
}

function add() {
  testFlag.green = true;
  rowData = { 
    columns : ["WORD", "WORD_DESC"] ,
    values  : ["'" + $("#new_value").val() + "'", "'" + $("#new_value_desc").val() + "'"]
  };
  globalReqId++;
  globalSQLConsumer.insert(globalReqId, rowData, successAdd, errorcb);
  status();
}

function update() {
  testFlag.red = true;
  rowData = { 
    columns : ["WORD", "WORD_DESC"] ,
    values  : ["'" + $("#old_value").val() + "'", "'" + $("#new_value_desc_1").val() + "'"]
  };
  globalReqId++;
  globalSQLConsumer.update(globalReqId, rowData, "WORD='" + $("#old_value").val() + "'", successUpdate, errorcb);
  status();
}

function remove() {
  testFlag.blue = true;
  globalReqId++;
  globalSQLConsumer.remove(globalReqId, "WORD='" + $("#old_value_1").val() + "'", successRemove, errorcb);
  status();
}

$(document).ready(function() {
  DisablePassButton();
  $("#addbutton").click(add);
  $("#updatebutton").click(update);
  $("#removebutton").click(remove);
});
