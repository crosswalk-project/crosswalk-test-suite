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
        Xu,Jianfeng <jianfengx.xu@intel.com>

*/

var flag;

function addCookie() {
  var oDate = new Date();        
  document.cookie = 'CookieName=Crosswalk_Cookie'+';max-age=' + 60*10;
  showResult();
}

function delCookie() {
  var str = "CookieName=Crosswalk_Cookie";
  str += ";max-age="+0;
  document.cookie = str;
  showResult();
}

function showResult() {
  flag = false;
  var arr = document.cookie.split('; ');  
  for (var i = 0; i < arr.length; i++) {
    var arr2 = arr[i].split('=');               
    if (arr2[0] == "CookieName"){           
      $("#message").text(arr2[1]);
      flag = true;       
    }   
  }
  if (!flag) {
    $("#message").text("No Result");    
  }        
  
}

$(function(){
    $("#btnAdd").click(function(){
        addCookie();
    });
    $("#btnDelete").click(function(){
        delCookie();
    });
    showResult();
});

