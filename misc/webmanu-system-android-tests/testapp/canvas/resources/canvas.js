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
        Li, cici <cici.x.li@intel.com>
        Cui, Jieqiong <jieqiongx.cui@intel.com>
*/

function reset() {
  $("#myCanvas").remove();
  $("<canvas id='myCanvas' width='300' height='240' style='border:1px solid #c3c3c3; margin-top: 19px;'>Your browser does not support the canvas element!</canvas>").appendTo($("#title"));
  cxt = document.getElementById("myCanvas").getContext("2d");
  img=new Image();
  img.src="resources/images/ryb-100x100.png";
  cxt.drawImage(img,0,0);
}

function rotate_90() {
  reset();
  cxt.clearRect(0,0,500,500);
  cxt.translate(100,0); 
  cxt.rotate(Math.PI/2); 
  cxt.drawImage(img,0,0);
}

function scale_double() {
  reset();
  cxt.clearRect(0,0,500,500);
  cxt.scale(2,2);
  cxt.drawImage(img,0,0);
}
