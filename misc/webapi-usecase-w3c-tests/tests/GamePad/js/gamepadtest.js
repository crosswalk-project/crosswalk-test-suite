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
        Xu, Jianfeng <jianfengx.xu@intel.com>

*/

var GAMEPAD = null;
var rAF = window.requestAnimationFrame;

function gamepadconnect(e) {
 GAMEPAD = e.gamepad;
  adddevice(e.gamepad);
}
function adddevice(gamepad) {
  var gameTxt =  "gamepad: " + gamepad.id;
  document.getElementById("Axes").style.display =  "block";
  document.getElementById("GamePad").style.display =  "block";
  document.getElementById("start").innerHTML = gameTxt;
  for (var i = 0; i < gamepad.buttons.length; i++) {
    document.getElementById("button" + i).className = "button used";
  }
  for (var i = 0; i < gamepad.axes.length; i++) {
    var e = document.getElementById("axes" + i);
    e.style.display = "block";
    e.setAttribute("max", "2");
    e.setAttribute("value", "1");
  }
  refreshStatus();
}

function disconnecthandler(e) {
  removegamepad(e.gamepad);
}

function removegamepad(gamepad) {
  var d = document.getElementById("controller" + gamepad.index);
  for (var i = 0; i <= 16 ; i++)
  {
     document.getElementById("button" + i).className = "button";
     if (i < 8)
     {
        document.getElementById("axes" + i).style.display = "none";
     }
  }
  document.getElementById("GamePad").style.display =  "none";
  document.getElementById("Axes").style.display =  "none";
  document.getElementById("start").innerHTML = "Connect and press a button on your gamepad to start";
}

function refreshStatus() {
  for (var i = 0; i < GAMEPAD.buttons.length; i++) {
    var b = document.getElementById("button" + i);
    var val = GAMEPAD.buttons[i];
    var pressed = val == 1.0;
    if (typeof(val) == "object") {
      pressed = val.pressed;
      val = val.value;
    }
    if (pressed) {
      b.className = "button pressed used";
    } else {
      b.className = "button used";
    }
  }
  for (var i = 0; i < GAMEPAD.axes.length; i++) {
    var a = document.getElementById("axes" + i);
    a.innerHTML = i + ": " + GAMEPAD.axes[i].toFixed(4);
    a.setAttribute("value", GAMEPAD.axes[i] + 1);
  }
  rAF(refreshStatus);
}

window.addEventListener("gamepadconnected", gamepadconnect);
window.addEventListener("gamepaddisconnected", disconnecthandler);
