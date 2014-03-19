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
        haox.li <haox.li@intel.com>

*/

var browser = (function getBrowser() {
    if (navigator.userAgent.indexOf("WebKit") > 0) {
        return "webkit";
    }
    if (navigator.userAgent.indexOf("Firefox") > 0) {
        return "moz";
    }
    if (navigator.userAgent.indexOf("MSIE") > 0) {
        return "msie";
    }
    if (navigator.userAgent.indexOf("Safari") > 0) {
        return "safari";
    }
    if (navigator.userAgent.indexOf("Camino") > 0) {
        return "camino";
    }
    if (navigator.userAgent.indexOf("Gecko/") > 0) {
        return "gecko";
    }
})();

//get style propoty
function GetCurrentStyle(prop) {
    var div = document.querySelector("#testDiv");   //object
    var headprop = headProp(prop);
    return getComputedStyle(div)[headprop];
}

//
function headProp(s) {
    var div = document.querySelector("#testDiv");
    if (s in div.style) {
        return s;
    }
    s = s[0].toUpperCase() + s.slice(1);
    var prefixes = ["ms", "Moz", "moz", "webkit", "O"];
    for (var i = 0; i < prefixes.length; i++) {
        if ((prefixes[i] + s) in div.style) {
            return prefixes[i] + s;
        }
    }
    return s;
}

//get style propoty
function GetCurrentStyleWithId(id,prop) {
    var div = document.querySelector("#" + id);   //object
    var headprop = headPropWithId(id,prop);
    return getComputedStyle(div)[headprop];
}

//
function headPropWithId(id,s) {
    var div = document.querySelector("#" + id);
    if (s in div.style) {
        return s;
    }
    s = s[0].toUpperCase() + s.slice(1);
    var prefixes = ["ms", "Moz", "moz", "webkit", "O"];
    for (var i = 0; i < prefixes.length; i++) {
        if ((prefixes[i] + s) in div.style) {
            return prefixes[i] + s;
        }
    }
    return s;
}

//style existence check
function hasStyle(name, styles) {
    var arr = name.split("-");
    var nameStr = arr[0];
    for(i = 1; i < arr.length; i++) {
        nameStr = nameStr + arr[i][0].toUpperCase() + arr[i].slice(1);
    }
    //name without prefix
    if(nameStr in styles) {
        return true;
    }
    //browser prefixes
    var prefixes = ["ms", "Moz", "moz", "webkit", "O"];
    //Uppercase first letter
    nameStr = nameStr[0].toUpperCase() + nameStr.slice(1);
    for (i in prefixes) {
        //name with prefix
        if ((prefixes[i] + nameStr) in styles) {
            return true;
        }
    }
    return false;
}
