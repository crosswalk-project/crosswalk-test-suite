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

var debug = 0;
var loadTimeout = 500;
var t;
var srcPage = "./support/001.html"
var srcLen = 0;
var newPage = "";
var replacestate = false;
var path = "127.0.0.1:8080";
var port = "8080";
var ip = "127.0.0.1";

function getPagename(url)
{
        var tmp= new Array();
        tmp=url.split("/");
        var pp = tmp[tmp.length-1];
        tmp=pp.split("?");
        return tmp[0];
}

function showInfo(info, clear){
        var testIframe= document.getElementById("testIframe");
	if (debug == 1){
		testIframe.style.display = "";
		if (info == null){
			return;
		}
	} else {
		testIframe.style.display = "none";
	}
}

function showWindowHistory(){
        showInfo("State: "+window.history.state, 0);
        showInfo("Length: "+window.history.length, 0);
        showInfo("Location: "+window.location.href, 0);
}

function showHistory(){
       	showInfo("Len="+srcLen+", Newlen="+document.getElementById("testIframe").contentWindow.history.length, 0);
       	showInfo("Location: "+document.getElementById("testIframe").contentWindow.location.href, 0);
       	showInfo("Pagename: "+getPagename(document.getElementById("testIframe").contentWindow.location.href), 0);
}

//Go APIs test
function historyGoCheck03(){
        showHistory();
        assert_equals(getPagename(document.getElementById("testIframe").contentWindow.location.href), getPagename(srcPage), "Current page name");
	t.done();
}

function historyGoCheck02(){
	showHistory();
        document.getElementById("testIframe").contentWindow.history.go(-1);
	setTimeout(t.step_func(historyGoCheck03), loadTimeout);
}

function historyGoCheck01(){
        document.getElementById("testIframe").src = newPage;
        setTimeout(t.step_func(historyGoCheck02), loadTimeout);//1000
}

//Len test
function historyLenCheck02(){
	showHistory();
	assert_equals(getPagename(document.getElementById("testIframe").contentWindow.location.href), getPagename(newPage), "Current page name");
        assert_equals(document.getElementById("testIframe").contentWindow.history.length, srcLen+1, "Current history length");
	t.done();
}

function historyLenCheck01(){
        document.getElementById("testIframe").src = newPage;
	setTimeout(t.step_func(historyLenCheck02), loadTimeout);
}

//Back APIs test
function historyBackCheck03(){
        showHistory();
        assert_equals(getPagename(document.getElementById("testIframe").contentWindow.location.href), getPagename(srcPage), "Current page name");
        t.done();
}

function historyBackCheck02(){
        showHistory();
        document.getElementById("testIframe").contentWindow.history.back();
        setTimeout(t.step_func(historyBackCheck03), loadTimeout);
}

function historyBackCheck01(){
        document.getElementById("testIframe").src = newPage;
        setTimeout(t.step_func(historyBackCheck02), loadTimeout);//1000
}

//Forward APIs test
function historyForwardCheck04(){
        showHistory();
        assert_equals(getPagename(document.getElementById("testIframe").contentWindow.location.href), getPagename(newPage), "Current page name");
        t.done();
}

function historyForwardCheck03(){
        showHistory();
	document.getElementById("testIframe").contentWindow.history.forward();
        setTimeout(t.step_func(historyForwardCheck04), loadTimeout);
}

function historyForwardCheck02(){
        showHistory();
        document.getElementById("testIframe").contentWindow.history.back();
        setTimeout(t.step_func(historyForwardCheck03), loadTimeout);
}

function historyForwardCheck01(){
        document.getElementById("testIframe").src = newPage;
        setTimeout(t.step_func(historyForwardCheck02), loadTimeout);//1000
}

//State Test
function locationStateCheck02(){
        document.getElementById("testIframe").contentWindow.history.back();
}

function locationStateCheck01(){
	document.getElementById("testIframe").contentWindow.onpopstate = t.step_func(function(e) {
		assert_equals(e.state.page, "test01");
        	t.done();
    	});
   	document.getElementById("testIframe").contentWindow.history.pushState({page: "test01"}, "title 1", getPagename(newPage));
   	document.getElementById("testIframe").contentWindow.history.pushState({page: "test02"}, "title 2", getPagename(srcPage));
	setTimeout(t.step_func(locationStateCheck02), loadTimeout);
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

//Href APIs test
function locationHrefCheck02(){
	assert_equals(getPagename(document.getElementById("testIframe").contentWindow.location.href), getPagename(newPage), "Current page name");
        t.done();
}

function locationHrefCheck01(){
	document.getElementById("testIframe").contentWindow.location.href = newPage;
        setTimeout(t.step_func(locationHrefCheck02), loadTimeout);
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

//Reload APIs test
function locationReloadCheck03(){
        assert_equals(getPagename(document.getElementById("testIframe").contentWindow.location.href), getPagename(newPage), "Current page name");
	t.done();
}

function locationReloadCheck02(){
        document.getElementById("testIframe").contentWindow.location.reload();
        setTimeout(t.step_func(locationReloadCheck03), loadTimeout);
}

function locationReloadCheck01(){
        document.getElementById("testIframe").contentWindow.location.assign(newPage);
        setTimeout(t.step_func(locationReloadCheck02), loadTimeout);
}

//Replace APIs test
function locationReplaceCheck04(){
        assert_equals(getPagename(document.getElementById("testIframe").contentWindow.location.href), getPagename(srcPage), "Current page name");
	t.done();
}

function locationReplaceCheck03(){
        document.getElementById("testIframe").contentWindow.history.back();
	setTimeout(t.step_func(locationReplaceCheck04), loadTimeout);
}

function locationReplaceCheck02(){
        document.getElementById("testIframe").contentWindow.location.replace("./support/003.html");
        setTimeout(t.step_func(locationReplaceCheck03), loadTimeout);
}

function locationReplaceCheck01(){
        document.getElementById("testIframe").contentWindow.location.assign(newPage);
        setTimeout(t.step_func(locationReplaceCheck02), loadTimeout);
}

//Resolve APIs test
function locationResolveCheck01(){
        assert_equals(document.getElementById("testIframe").contentWindow.location.href, window.location.resolveURL(srcPage), "Current page absolute URL");
        t.done();
}

function historybackPushstate(){
    document.getElementById("testIframe").contentWindow.history.pushState({page: "test01"}, "title",getPagename(newPage));
    setTimeout(t.step_func(historybackReload), 2000);
}
function historybackReload(){
    document.getElementById("testIframe").contentWindow.location.reload();
    setTimeout(t.step_func(historybackFinalCheck), loadTimeout);
}
function historybackFinalCheck(){
    if(!replacestate){
        document.getElementById("testIframe").contentWindow.history.back();
        setTimeout(t.step_func(historyassert),loadTimeout);
    }else{
        setTimeout(t.step_func(historyassert_new),loadTimeout);
        replacestate = false;
    }
    t.done();
}

function historybackReplacestate(){
    replacestate = true;
    document.getElementById("testIframe").contentWindow.history.replaceState({page: "test01"}, "title", getPagename(newPage));
    setTimeout(t.step_func(historybackReload), 2000);
}

function historyforwordPushstate(){
    document.getElementById("testIframe").contentWindow.history.pushState({page: "test01"}, "title", getPagename(newPage));
    setTimeout(t.step_func(historyforwordReload), 2000);
}
function historyforwordReload(){
    document.getElementById("testIframe").contentWindow.location.reload();
    setTimeout(t.step_func(historyback), loadTimeout);
}
function historyforwordFinalCheck(){
    if(!replacestate){
        document.getElementById("testIframe").contentWindow.history.forward();
        srcPage=newPage;
        setTimeout(t.step_func(historyassert),loadTimeout);
    }else{
        setTimeout(t.step_func(historyassert_new),loadTimeout);
        replacestate = false;
    }
    t.done();
}
function historyforwordReplacestate(){
    replacestate = true;
    document.getElementById("testIframe").contentWindow.history.pushState({page: "test01"}, "title", "001.html");
    document.getElementById("testIframe").contentWindow.history.replaceState({page: "test01"}, "title", getPagename(newPage));
    setTimeout(t.step_func(historyforwordReload), loadTimeout);
}
function historygoPushstate(){
    document.getElementById("testIframe").contentWindow.history.pushState({page: "test01"}, "title", getPagename(newPage));
    setTimeout(t.step_func(historygoReload), loadTimeout);
}
function historygoReload(){
    document.getElementById("testIframe").contentWindow.location.reload();
    setTimeout(t.step_func(historygoFinalCheck), loadTimeout);
}
function historygoFinalCheck(){
    if(!replacestate){
        document.getElementById("testIframe").contentWindow.history.go(-1);
        setTimeout(t.step_func(historyassert),loadTimeout);
    }else{
        setTimeout(t.step_func(historyassert_new),loadTimeout);
        replacestate = false;
    }
    t.done();
}
function historygoReplacestate(){
    replacestate = true;
    document.getElementById("testIframe").contentWindow.history.replaceState({page: "test01"}, "title", getPagename(newPage));
    setTimeout(t.step_func(historygoReload), 2000);
}
function historylengthPushstate(){
    document.getElementById("testIframe").contentWindow.history.pushState({page: "test01"}, "title", getPagename(newPage));
    var historyLength = document.getElementById("testIframe").contentWindow.history.length;
    //history's quota is max 100 in Tizen (chrome is max 50)
    //if history's quota comes to max, new "history" is not pushed and it will be replaced.
    assert_true((historyLength == srcLen) || (historyLength == srcLen +1), "Current history length increased");
    t.done();
}
function historylengthReplacestate(){
    document.getElementById("testIframe").contentWindow.history.replaceState({page: "test01"}, "title", getPagename(newPage));
    assert_equals(document.getElementById("testIframe").contentWindow.history.length, srcLen, "Current history length");
    t.done();
}
function historylengthFinalCheck(){
    assert_equals(getPagename(document.getElementById("testIframe").contentWindow.location.href), getPagename(newPage), "Current page name");
    t.done();
}
function historyPushstate(){
    document.getElementById("testIframe").contentWindow.history.pushState({page: "test01"}, "title", getPagename(newPage));
    document.getElementById("testIframe").contentWindow.location.reload();
    assert_equals(getPagename(document.getElementById("testIframe").contentWindow.location.href), getPagename(newPage), "Current page name");
    t.done();
}
function historyPushstate_back(){
    document.getElementById("testIframe").contentWindow.history.pushState({page: "test01"}, "title", getPagename(newPage));
    setTimeout(t.step_func(function() {
        document.getElementById("testIframe").contentWindow.history.back();
        setTimeout(t.step_func(historyassert),loadTimeout);
    }), loadTimeout);
    t.done();
}
function historyPushstate_null(){
    document.getElementById("testIframe").contentWindow.history.pushState(null, "title", newPage);
    setTimeout(t.step_func(function() {
        document.getElementById("testIframe").contentWindow.location.reload();
        assert_equals(getPagename(document.getElementById("testIframe").contentWindow.location.href), getPagename(newPage), "Current page name");
        t.done();
   }), loadTimeout);
}
function historyPushstate_noparam() {
    document.getElementById("testIframe").contentWindow.history.pushState();
    setTimeout(t.step_func(function() {
        document.getElementById("testIframe").contentWindow.location.reload();
        assert_equals(getPagename(document.getElementById("testIframe").contentWindow.location.href), getPagename(srcPage), "Current page name");
       t.done();
    }), loadTimeout);
}
function historyPushstate_urlnull() {
    document.getElementById("testIframe").contentWindow.history.pushState({page: "test01"}, "title", null);
    setTimeout(t.step_func(function() {
        document.getElementById("testIframe").contentWindow.location.reload();
        assert_equals(getPagename(document.getElementById("testIframe").contentWindow.location.href), getPagename(srcPage), "Current page name");
        t.done();
    }), loadTimeout);
}
function historyReplacestate(){
    document.getElementById("testIframe").contentWindow.history.replaceState({page: "test01"}, "title", getPagename(newPage));
    setTimeout(t.step_func(function() {
        document.getElementById("testIframe").contentWindow.location.reload();
        assert_equals(getPagename(document.getElementById("testIframe").contentWindow.location.href), getPagename(newPage), "Current page name");
        t.done();
    }), loadTimeout);
}
function historyReplacestate_back(){
    document.getElementById("testIframe").contentWindow.history.replaceState({page: "test01"}, "title", getPagename(newPage));
    document.getElementById("testIframe").contentWindow.location.reload();
    setTimeout(t.step_func(function() {
        document.getElementById("testIframe").contentWindow.history.back();
        setTimeout(t.step_func(historyassert_new),loadTimeout);
    }), loadTimeout);
    t.done();
}
function historyReplacestate_datanull(){
    document.getElementById("testIframe").contentWindow.history.replaceState(null, "title", newPage);
    setTimeout(t.step_func(function() {
        assert_equals(getPagename(document.getElementById("testIframe").contentWindow.location.href), getPagename(newPage), "Current page name");
        t.done();
    }), loadTimeout);
}
function historyReplacestate_noparam(){
    document.getElementById("testIframe").contentWindow.history.replaceState();
    setTimeout(t.step_func(function() {
        assert_equals(getPagename(document.getElementById("testIframe").contentWindow.location.href), getPagename(srcPage), "Current page name");
        t.done();
    }), loadTimeout);
}
function historyReplacestate_urlnull(){
    document.getElementById("testIframe").contentWindow.history.replaceState({page: "test01"}, "title", null);
    setTimeout(t.step_func(function() {
        assert_equals(getPagename(document.getElementById("testIframe").contentWindow.location.href), getPagename(srcPage), "Current page name");
        t.done();
    }), loadTimeout);
}
function historyassert(){
    assert_equals(getPagename(document.getElementById("testIframe").contentWindow.location.href), getPagename(srcPage), "Current page name");
}
function historyassert_new(){
    assert_equals(getPagename(document.getElementById("testIframe").contentWindow.location.href), getPagename(newPage), "Current page name");
}
function historyback(){
    document.getElementById("testIframe").contentWindow.history.back();
    setTimeout(historyforwordFinalCheck,100);
}
