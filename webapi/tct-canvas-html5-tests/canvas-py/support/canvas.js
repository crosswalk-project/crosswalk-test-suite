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
         Cao, Jun <junx.cao@intel.com>

*/

var canvas;
var purpose;

function getcanvas()
{
    if (canvas == null) {
        canvas = document.getElementById("canvas").getContext('2d');
    }
}

//attribute/method/constant type
function canvas_property_type(property_name, property_type,isInstance)
{
    getcanvas();
    if (isInstance) {
       test( function() {
            assert_true(canvas[property_name] instanceof property_type, "canvas." + property_name +" is of type   "+ canvas[property_name].toString());
        }, purpose);
    } else {
        test( function() {
            assert_true(typeof canvas[property_name] == property_type, "canvas." + property_name +" is of type   "+property_type);
        }, purpose);
    }
}

//attribute/method/constant exist
function canvas_property_exists(property_name)
{
    test( function() {
        getcanvas();
        assert_true(property_name in canvas, "canvas." + property_name +" exists");
    }, purpose);
}
