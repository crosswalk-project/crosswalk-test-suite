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
        Zhu, Yongyong <yongyongx.zhu@intel.com>

*/

function init() {
  testSyncEcho();
  testAsyncEcho();
}

function testSyncEcho() {
  try {
    var labelSync = document.getElementById('syncLabel');
    var d = new Date().toString();
    var expected = "From java sync:" + d;
    var msg = echo.echoSync(d);
    if (msg === expected) {
      labelSync.innerHTML = "<font color=green>passed</font>";
    } else {
      labelSync.innerHTML = "<font color=red>failed, expected value:" + msg + "</font>";
    }
  } catch(e) {
    labelSync.innerHTML = "<font color=red>failed, error:" + e + "</font>";
  }
}

function testAsyncEcho() {
  try {
    var labelAsync = document.getElementById('aSyncLabel');
    var d = new Date().toString();
    echo.echo(d, function(msg) {
      var expected = "From java:" + d;
      if (msg === expected) {
        labelAsync.innerHTML = "<font color=green>passed</font>";
      } else {
        labelAsync.innerHTML = "<font color=red>failed, expected value:" + msg + "</font>";
      }
    });
  } catch(e) {
    labelSync.innerHTML = "<font color=red>failed, error:" + e + "</font>";
  }
}

