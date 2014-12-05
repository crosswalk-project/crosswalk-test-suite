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
        Xie,Yunxiao <yunxiaox.xie@intel.com>
        Xu, Kang <kangx.xu@intel.com>

*/

var testFlag = {
    green: false,
    red: false,
    blue: false
};
var showId;

function status() {
    if (testFlag.green && testFlag.red && testFlag.blue) {
        EnablePassButton();
    }
}

function show() {
    $("#infobox").text("Could not control a text-to-speech output. \n" + $("#infobox").text());
    $("#start").closest(".ui-btn").show();
    $("#cancel").closest(".ui-btn").hide();
    $("#resume").closest(".ui-btn").hide();
    $("#pause").button("disable");
    clearTimeout(showId);
}

$("#start").live("tap", function () {
    var content = $("#textcontent").val();
    if (!content) {
      $("#infobox").text("Please input content, such as Hello World!");
      return ;
    }

    testFlag.green = true;
    $("#start").closest(".ui-btn").hide();
    $("#resume").closest(".ui-btn").hide();
    $("#cancel").closest(".ui-btn").show();
    $("#pause").button("enable");
    clearTimeout(showId);
    showId = setTimeout("show()", 10000);
    $("#infobox").text("Starting......");
    window.speechUtter = new tizen.SpeechSynthesisUtterance(content);
    //speechUtter.text = content;
    speechUtter.lang = "en-US";
    speechUtter.rate = 1.2;
    speechUtter.onstart = function (evt) {
        clearTimeout(showId);
    };
    speechUtter.onend = function(evt) {
        clearTimeout(showId);
        $("#start").closest(".ui-btn").show();
        $("#cancel").closest(".ui-btn").hide();
        $("#resume").closest(".ui-btn").hide();
        $("#pause").button("disable");
        $("#infobox").text('Finished in ' + evt.elapsedTime + ' seconds. \n' + $("#infobox").text());
    }
    speechUtter.onerror = function(err) {
        clearTimeout(showId);
        $("#infobox").text("Error: " + err.message + "\n" + $("#infobox").text());
        $("#start").closest(".ui-btn").show();
        $("#cancel").closest(".ui-btn").hide();
        $("#resume").closest(".ui-btn").hide();
        $("#pause").button("disable");
    };
    window.speechSyn = tizen.speechSynthesis;
    speechSyn.speak(speechUtter);
    status();
});

$("#cancel").live("tap", function () {
    testFlag.red = true;
    $("#start").closest(".ui-btn").show();
    $("#cancel").closest(".ui-btn").hide();
    $("#resume").closest(".ui-btn").hide();
    $("#pause").button("disable");
    speechSyn.cancel();
    $("#infobox").text("SpeechSynthesis cancel.\n" + $("#infobox").text());
    status();
});

$("#pause").live("tap", function () {
    testFlag.blue = true;
    $("#resume").closest(".ui-btn").show();
    $("#pause").closest(".ui-btn").hide();
    speechSyn.pause();
    $("#infobox").text("SpeechSynthesis pause.\n" + $("#infobox").text());
    status();
});

$("#resume").live("tap", function () {
    testFlag.blue = true;
    $("#pause").closest(".ui-btn").show();
    $("#resume").closest(".ui-btn").hide();
    speechSyn.resume();
    $("#infobox").text("SpeechSynthesis resume.\n" + $("#infobox").text());
    status();
});

$(document).live('pageshow', function () {
    DisablePassButton();
    $("#cancel").closest(".ui-btn").hide();
    $("#resume").closest(".ui-btn").hide();
    $("#pause").button("disable");
});
