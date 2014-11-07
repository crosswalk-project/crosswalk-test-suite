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
        Cui,Jieqiong <jieqiongx.cui@intel.com>

*/

var testTarget;

$(document).ready(function(){
    document.getElementById("MediaPlayback").volume = 0.6;
    $("#slider-1").hide();
    musicplaylongtime();
});

function musicplay1500() {
    musicplay()
    var cc = 1;
    var a = document.getElementById("MediaPlayback");
    a.addEventListener("ended", function() {
        cc++;
        if (cc <=2880) {
　　       a.play();
        }
    });

}

function musicplaylongtime() {
    musicplay()
    var cc = 1;
    var a = document.getElementById("MediaPlayback");
    a.addEventListener("ended", function() {
        cc++;
        if (cc <=2880) {
　　       a.play();
        }
    });
}

function videoplaylongtime() {
    videoplay()
    var cc = 1;
    var a = document.getElementById("MediaPlayback1");
    a.addEventListener("ended", function() {
        cc++;
        if (cc <=60) {
　　       a.play();
        }
    });
}

function pausewait() {
    testTarget= document.getElementById("MediaPlayback");
    setTimeout("testTarget.pause();",1000)
}

function pausewait1() {
    testTarget= document.getElementById("MediaPlayback1");
    setTimeout("testTarget.pause();",1000)
}

function playwait() {
    testTarget= document.getElementById("MediaPlayback");
    setTimeout("testTarget.play();",1000)
}

function playwait1() {
    testTarget= document.getElementById("MediaPlayback1");
    setTimeout("testTarget.play();",1000)
}

function musicplay() {
    testTarget=document.getElementById("MediaPlayback");
    testTarget.play();
}
function videoplay() {
    testTarget=document.getElementById("MediaPlayback1");
    testTarget.play();
}

function musicpause() {
    testTarget=document.getElementById("MediaPlayback");
    testTarget.pause();
}

function musicreplay() {
  document.getElementById("MediaPlayback").load();
  testTarget.play();
}
