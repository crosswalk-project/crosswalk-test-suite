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
        Shentu, Jiazhen <jiazhenx.shentu@intel.com>

*/

$("#start").live("tap", function () {
    $("#start").closest(".ui-btn").hide();
    $("#stop").closest(".ui-btn").show();
    $("#abort").button("enable");
    window.speechReco = new webkitSpeechRecognition();
    speechReco.continuous = true;
    speechReco.interimResults = true;
    speechReco.onresult = function (evt) {
        for (var i = evt.resultIndex; i < evt.results.length; ++i) {
            if (evt.results[i].isFinal) {
                final_transcript += evt.results[i][0].transcript;
            } else {
                interim_transcript += evt.results[i][0].transcript;
            }
        }
        $("#infobox").text("SpeechRecognition final - " + final_transcript + "\n" +
            "SpeechRecognition interim - " + interim_transcript + "\n" + $("#infobox").text());
    };
    speechReco.onerror = function(err) {
        $("#infobox").text("SpeechRecognition error - " + err.error + "\n" + $("#infobox").text());
        $("#start").closest(".ui-btn").show();
        $("#stop").closest(".ui-btn").hide();
        $("#abort").button("disable");
        speechReco.stop();
        $("#infobox").text("SpeechRecognition stop.\n" + $("#infobox").text());
    };
    speechReco.onend = function() {
        $("#infobox").text("SpeechRecognition end.\n" + $("#infobox").text());
    };
    speechReco.start();
    $("#infobox").text("SpeechRecognition start.\n" + $("#infobox").text());
});

$("#stop").live("tap", function () {
    $("#start").closest(".ui-btn").show();
    $("#stop").closest(".ui-btn").hide();
    $("#abort").button("disable");
    speechReco.stop();
    $("#infobox").text("SpeechRecognition stop.\n" + $("#infobox").text());
});

$("#abort").live("tap", function () {
    speechReco.abort();
    $("#infobox").text("SpeechRecognition abort.\n" + $("#infobox").text());
});

$(document).live('pageshow', function () {
    $("#stop").closest(".ui-btn").hide();
    $("#abort").button("disable");
    $("#infobox").text("");
});
