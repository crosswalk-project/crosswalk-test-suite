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
        Xu, Kang <kangx.xu@intel.com>

*/

dict = {};

function status(){
  $("#tableList").empty();
  var table = document.querySelector("table");
  table.insertRow(0)
  table.rows[0].insertCell(0).innerHTML = "Storage Type";
  table.rows[0].insertCell(1).innerHTML = "Key";
  table.rows[0].insertCell(2).innerHTML = "Value";

  for(var i in dict){
    var j = dict[i]
    len = table.rows.length;
    table.insertRow(len);
    table.rows[len].insertCell(0).innerHTML = i;
    table.rows[len].insertCell(1).innerHTML = j.key;
    table.rows[len].insertCell(2).innerHTML = j.value;
  }

}

function onAdd(){
  var session = $("#session").val();
  var local = $("#local").val();

  if (session !== "") {
    sessionStorage.setItem(session, session);
  }

  if (local !== "") {
    localStorage.setItem(local, local);
  }

  $("#tableList").empty();
  $("#status").text('Data Stored');
}

function onGet(){
  dict = {};
  var session = $("#session").val();
  var local = $("#local").val();
  
  if(session !== ""){
    var value = sessionStorage.getItem(session);
    if(value == null){
      value = "<font style='color:red'>The value is not found</font>";
    }
    dict["sessionStorage"] = {key: session, value: value};
  }

  if(local !== ""){
    var value = localStorage.getItem(local);
    if(value == null){
      value = "<font style='color:red'>The value is not found</font>";
    }
    dict["localStorage"] = {key: local, value: value};
  }

  status();
  $("#status").text('Data Found');
}

function onClear(){
  sessionStorage.clear();
  localStorage.clear();
  $("#tableList").empty();
  $("#status").text('storage cleared');
}

$(document).ready(function () {
    $("#add").click(onAdd);
    $("#get").click(onGet);
    $("#clear").click(onClear);
});
