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
        Xu, Jianfeng <jianfengx.xu@intel.com>

*/

var current_dt, current_zone, tzids, dateFormat, timeFormat, is_leap;
var day, year, mon, min, sec, hour;

$(document).ready(function() {
  current_dt = tizen.time.getCurrentDateTime();  
  refresh();
});

function changeTime() {
  day = $("#date").val();
  year = $("#year").val();
  mon = $("#mon").val();
  min = $("#min").val();
  sec = $("#sec").val();
  hour = $("#hour").val();
  current_dt.setDate(day);
  current_dt.setFullYear(year);
  current_dt.setHours(hour);
  current_dt.setMinutes(min);
  current_dt.setMonth(mon-1);
  current_dt.setSeconds(sec);
  refresh();
}

function refresh() {
  var text = current_dt.toLocaleString();
  $("#time").html(text);
  current_zone = tizen.time.getLocalTimezone();
  $("#zone").html(current_zone);
  tzids = tizen.time.getAvailableTimezones();
  $("#num").html(tzids.length);
  dateFormat = tizen.time.getDateFormat();
  $("#dateFormat").html(dateFormat);
  timeFormat = tizen.time.getTimeFormat();
  $("#timeFormat").html(timeFormat);
  is_leap = tizen.time.isLeapYear(current_dt.getFullYear())
  if (is_leap) {
    $("#leap").html("Yes");
  } else {
    $("#leap").html("No");
  }
}
