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

var webgl;
var purpose;

function getwebgl(wegglctxattr) {
    if (webgl == null) {
        var canvas = document.getElementById("canvas");
        if (wegglctxattr == null) {
            webgl = canvas.getContext('webgl') || canvas.getContext('experimental-webgl');
        } else {
            webgl = canvas.getContext('webgl', wegglctxattr) || canvas.getContext('experimental-webgl', wegglctxattr);
        }
        purpose = document.getElementsByName("assert")[0].content;
    }
}
//get WebGLRenderingContext object
function webglrenderctx_get_object() {
    test( function() {
        getwebgl();
        assert_true(webgl != null, purpose);
    }, purpose);
}

function webglrenderctx_case_sensitive() {
    test( function() {
        var canvas = document.getElementById("canvas");
        webgl = canvas.getContext('WEBGL') || canvas.getContext('WebGL');
        assert_true(webgl == null, purpose);
    }, purpose);
}

function webglrenderctx_onlyone() {
    test( function() {
        var canvas = document.getElementById("canvas");
        var webgl1 = canvas.getContext('webgl') ||  canvas.getContext('experimental-webgl');
        var webgl2 = canvas.getContext('webgl') ||  canvas.getContext('experimental-webgl');
        assert_true(webgl1 === webgl2, purpose);
    }, purpose);

}

function webglctxattr_passed() {
    test( function() {
        getwebgl({alpha : false, antialias: false});
        var webglctxattr = webgl.getContextAttributes();
        assert_true(webglctxattr.alpha == false &&  webglctxattr.antialias == false, purpose);
    }, purpose);
}

var programObject = null;
var v3PositionIndex = 0;

function drawTriangle() {
    var triangleData = [
     0.0, 1.0, 0.0,
    -1.0, -1.0, 0.0,
     1.0, 0.0, 0.0];

    triangleBuffer = webgl.createBuffer();
    webgl.bindBuffer(webgl.ARRAY_BUFFER, triangleBuffer);
    webgl.bufferData(webgl.ARRAY_BUFFER, new Float32Array(triangleData), webgl.STATIC_DRAW);

    webgl.bindBuffer(webgl.ARRAY_BUFFER, triangleBuffer);

    webgl.enableVertexAttribArray(v3PositionIndex);

    webgl.vertexAttribPointer(v3PositionIndex, 3, webgl.FLOAT, false, 0, 0);

    webgl.drawArrays(webgl.TRIANGLES, 0, 3);
}

function addShader() {
    var vertexShaderObject = null;
    var fragmentShaderObject = null;

    getwebgl();

    vertexShaderObject = webgl.createShader(webgl.VERTEX_SHADER);
    fragmentShaderObject = webgl.createShader(webgl.FRAGMENT_SHADER);

    webgl.shaderSource(vertexShaderObject, ShaderSourceFromScript("shader-vs"));
    webgl.shaderSource(fragmentShaderObject, ShaderSourceFromScript("shader-fs"));

    webgl.compileShader(vertexShaderObject);
    webgl.compileShader(fragmentShaderObject);

    programObject = webgl.createProgram();

    webgl.attachShader(programObject, vertexShaderObject);
    webgl.attachShader(programObject, fragmentShaderObject);

    webgl.bindAttribLocation(programObject, v3PositionIndex, "v3Position");

    webgl.linkProgram(programObject);

    webgl.useProgram(programObject);
}

function get_webglactiveinfo() {
    addShader();
    return webgl.getActiveAttrib(programObject, 0);
}

function ShaderSourceFromScript(scriptID) {
   var shaderScript = document.getElementById(scriptID);
   if (shaderScript == null)
       return "";
   var sourceCode = "";
   var child = shaderScript.firstChild;
   while (child) {
       if (child.nodeType == child.TEXT_NODE ) sourceCode += child.textContent;
            child = child.nextSibling;
       }

   return sourceCode;
}

function webgl_ok(fun) {
   fun();
   test(function () {
          assert_true(webgl.getError() == webgl.NO_ERROR, purpose);
   }, purpose);
}

//attribute/method/constant type
function webgl_property_type(object, property_name, property_type,isInstance) {
    if (isInstance) {
       test( function() {
            assert_true(object[property_name] instanceof property_type, object+"." + property_name +" is of type   "+ object[property_name].toString());
        }, purpose);
    } else {
        test( function() {
            assert_true(typeof object[property_name] == property_type, object+"." + property_name +" is of type   "+property_type);
        }, purpose);
    }
}

//attribute/method/constant exist
function webgl_property_exists(object, property_name) {
    test( function() {
        assert_true(property_name in object, object +"." + property_name +" exists");
    }, purpose);
}

//attribute/method/constant exist
function webgl_default_value(object, property_name, default_value) {
    test( function() {
        assert_true(object[property_name] == default_value, object +"." + property_name +" default value is " + default_value);
    }, purpose);
}

//readonly
function webgl_property_readonly(object, property_name, new_value) {
    test( function() {
        object[property_name] == new_value;
        assert_true(object[property_name] != new_value, object +"." + property_name +" is readonly");
    }, purpose);
}

//constant value
function webgl_constant_value(object, property_name, const_value) {
    test( function() {
        assert_true(object[property_name] == const_value, object +"." + property_name +" constant value is " + const_value);
    }, purpose);
}
