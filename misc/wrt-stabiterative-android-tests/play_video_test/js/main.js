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
    DisablePassButton();
    document.getElementById("MediaPlayback").volume = 0.6;
    $("#slider-1").hide();

});

function musicplay1500() {
    musicplay()
    var cc = 1;
    var a = document.getElementById("MediaPlayback");
    a.addEventListener("ended", function() {
        cc++;
        if (cc <=1500) {
　　       a.play();
        }
    });

}

function musicplaypause1500() {
    musicplay()
    var cc = 1;
    var a = document.getElementById("MediaPlayback");
    a.addEventListener("ended", function() {
        cc++;
        if (cc <=200) {
　　       a.play();
        }
    });
    a.addEventListener("playing", function() {
        if (cc <=200) {
　　       pausewait();
        }
        
    });
    a.addEventListener("pause", function() {
        if (cc <=200) {
           playwait();
        }
    });

}

function pausewait() {
    testTarget= document.getElementById("MediaPlayback");
    setTimeout("testTarget.pause();",5000)
}

function playwait() {
    testTarget= document.getElementById("MediaPlayback");
    setTimeout("testTarget.play();",5000)
}
function musicplay() {
    testTarget=document.getElementById("MediaPlayback");
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
