/*
Copyright (c) 2013 Intel Corporation.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of works must retain the original copyright notice, this list
  of conditions and the following disclaimer.sandbox
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
        Hao, Yunfei <yunfeix.hao@intel.com>

*/

var systime = new Date();
var timer = systime.getTime();
var timer2 = systime.toString().substr(15, 16);
// Time interval
var t = 1000;
//Counter of js
var Num = 0;

var visibilitychange = "visibilitychange";
var array = new Array("webkit", "o", "moz", "ms");
for(var i = 0; i < array.length; i++) {
    if(array[i] + "Hidden" in document) {
        visibilitychange = array[i] + "visibilitychange";
    }
}

$(document).ready(function () {
    Refresh();
    setInterval("Refresh();", t);
    //The time when entry this page timer2
    $("#en_time").html(timer2);
    DisablePassButton();
    document.addEventListener(visibilitychange, notification);
});

function Refresh() {
    Num = Num + 1;
    //The current time
    var curtime = new Date();
    var timer3 = curtime.toString().substr(15, 16);
    $("#current_time").html(timer3);
    //The true timer: NowTime - entryTime
    $("#diff_time").html(Math.floor((new Date().getTime()-timer)/t) % 60);
    //The timer of js
    $("#js_time_tensecond").html((Num-1) / 10);
    $("#js_time_second").html((Num-1) % 10);
    if(Num == 60){
        Num = 0;
    }
}

function notification() {
    EnablePassButton();
}
