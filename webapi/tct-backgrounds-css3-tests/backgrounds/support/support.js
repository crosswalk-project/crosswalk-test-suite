/*
Copyright (c) 2014 Intel Corporation.

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
        Xu, Yi <yix.xu@intel.com>
        Nian, Gan <nianx.gan@intel.com>
        Li, Hao <haox.li@intel.com>

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

function GetCurrentStyle(prop) {
    try{
        var div = document.querySelector("#test");
        prop = prop.replace(/([-][a-z])/g, function ($1) { return $1.toUpperCase().replace("-","") });
        var headprop = headProp(prop);
        var fixprop = getComputedStyle(div)[headprop];
        if (!fixprop) {
            return "";
        }
        return fixprop;
    }catch(e){
        return "";
    }
}

function headProp(s) {
    var div = document.querySelector("#test");
    if (s in div.style) {
        return s;
    }
    s = s.replace(/([-][a-z])/g, function ($1) { return $1.toUpperCase().replace("-", "") });
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

function getmatrixm(matrix3d,i) {
    var matrix3d = matrix3d.replace("matrix3d(","").replace(")","");
    var m = matrix3d.split(",");
    if (m.length > i) {
        return m[i].replace(" ","");
    }
    return "";
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

String.prototype.hexColor = function () {
    if (this.indexOf("#") >= 0) return this; //return hex value
    var pattern = new RegExp("2[0-4]\\d|25[0-5]|[01]?\\d\\d?", "ig"); // 0 ~ 255
    var va = this.match(pattern);
    if (va.length != 3) return "NaN";
    var result = "#";
    for (var i = 0; i < 3; i++) {
        var num = parseInt(va[i]);
        result += num < 16 ? "0" + num.toString(16) : num.toString(16);
    }
    return result;
}
