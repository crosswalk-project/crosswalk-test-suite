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
        Fan,Weiwei <weiwix.fan@intel.com>
        Xu,Yuhan <yuhanx.xu@intel.com>

*/

    function PassTest(desc) {
        t.step(function() { assert_true(true, desc); } );
        t.done();
    }

    function FailTest(desc) {
        t.step(function() { assert_true(false, desc); } );
        t.done();
    }

    function ExistTest(obj, propertyName, desc) {
        t.step(function() {
            assert_exists(obj, propertyName, desc);
        });
        t.done();
    }
    function testLog(pass, desc) {
        var span = document.createElement("span");
        span.style.cssText = "display:inline-block; width:80px; text-align:center;"
        if (pass) {
            span.style["color"] = "green";
            span.innerHTML = "Pass";
        }
        else {
            span.style["color"] = "red";
            span.innerHTML = "Fail";
        }
        var spandesc = document.createElement("span");
        spandesc.style.cssText = "padding-left:20px;"
        spandesc.innerHTML = desc;
        document.getElementById("log").appendChild(span);
        document.getElementById("log").appendChild(spandesc);
        document.getElementById("log").style.cssText = "height:45px; line-height:45px; border:#000 solid; border-width:3px 0 1px 0; font-weight:bold;";
    }
