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

var testAudio = document.getElementById("MediaPlayback");;
var cc = 0;

function start() {
    testAudio.addEventListener("ended", function() {
        cc++;
        if (cc <=14400) {
　　       musicplay();
        }
    });
    musicplay();
}

function musicplay1500() {
    window.location.reload();
}

function musicplaypause1500() {
    cc = 0;
    start();
    testAudio.addEventListener("playing", function() {
        if (cc <=14400) {
　　       pausewait();
        }
    });
    testAudio.addEventListener("pause", function() {
        if (cc <=14400) {
　　      playwait();
        }
    });
}
function pausewait() {
    setTimeout("testAudio.pause();",1000);
}

function playwait() {
    setTimeout("testAudio.play();",1000);
}

function musicplay() {
    testAudio.play();
}
