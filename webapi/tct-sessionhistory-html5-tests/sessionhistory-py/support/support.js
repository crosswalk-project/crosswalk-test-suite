/*

Copyright (c) 2012 Intel Corporation.

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
         Fan,Yugang <yugang.fan@intel.com>
         Ge, Qing <qingx.ge@intel.com>

*/

var loadTimeout = 500;
var t;
var newPage = "";

function getPagename(url)
{
        var tmp= new Array();
        tmp=url.split("/");
        var pp = tmp[tmp.length-1];
        tmp=pp.split("?");
        return tmp[0];
}

//replaceState Test
function locationreplaceStateCheck02(){
        assert_equals(getPagename(document.getElementById("testIframe").contentWindow.location.href), getPagename(newPage), "Current page name");
        t.done();
}

function locationreplaceStateCheck01(){
        document.getElementById("testIframe").contentWindow.history.replaceState({page: "test01"}, "title", getPagename(newPage));
	document.getElementById("testIframe").contentWindow.location.reload();
	setTimeout(t.step_func(locationreplaceStateCheck02), 1000);
}

//pushState Test
function locationpushStateCheck02(){
        assert_equals(getPagename(document.getElementById("testIframe").contentWindow.location.href), getPagename(newPage), "Current page name");
        t.done();
}

function locationpushStateCheck01(){
        document.getElementById("testIframe").contentWindow.history.pushState({page: "test01"}, "title", getPagename(newPage));
        document.getElementById("testIframe").contentWindow.location.reload();
        setTimeout(t.step_func(locationpushStateCheck02), loadTimeout);
}

//Assign APIs test
function locationAssignCheck02(){
        assert_equals(getPagename(document.getElementById("testIframe").contentWindow.location.href), getPagename(newPage), "Current page name");
        t.done();
}

function locationAssignCheck01(){
        document.getElementById("testIframe").contentWindow.location.assign(newPage);
        setTimeout(t.step_func(locationAssignCheck02), loadTimeout);
}
