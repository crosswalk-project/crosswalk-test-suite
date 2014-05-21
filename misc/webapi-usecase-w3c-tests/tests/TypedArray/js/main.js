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
        Li, Hao <haox.li@intel.com>

*/


$(document).ready(function () {
    //init array
    var elementSize = 16 * Int32Array.BYTES_PER_ELEMENT;
    var buffer = new ArrayBuffer(elementSize);
    var i32a = new Int32Array(buffer, 0);
    showArray("#array1", i32a);

    $("#fillValue").click(function (){
        fillValue(i32a, 1);
        showArray("#array1", i32a);
    });

});

function showArray(table, array) {
    var tab =$(table);
    tab.html("");
    for (var i = 0; i < 4; i++) {
        var sub_arr = array.subarray(i, i+4);
        var td = "";
        for (var j = 0; j < 4; j++) {
            td = td + "<td>" + sub_arr[j] + "</td>";
        }
        tab.html(tab.html() + "<tr>" + td + "</tr>");
    }
}

function fillValue(array, value) {
    for (var i = 0; i < array.byteLength/array.BYTES_PER_ELEMENT; i++) {
        array[i] = value;
   }
}
