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
         Fan,Weiwei <weiwix.fan@intel.com>

*/

var track;
var media;

//obtain track object
function getTrack() {
    if (track == null) {
        var trackElements = document.querySelectorAll("track");
        track = trackElements[0];
        return;
    }
}

function getmedia() {
    if (media == null) {
        media = document.getElementById("m");
        return;
    }
}

//audioTracks
function audiotracks_attribute_type() {
    test(function() {
        getmedia();
        assert_true("audioTracks" in media, "the audioTracks attribute exists");
        assert_true(typeof media.audioTracks == "object", "media.audioTracks is of type object");
    }, document.title);
}

function audiotracks_attribute_readonly() {
    test(function() {
        getmedia();
        assert_true("audioTracks" in media, "the audioTracks attribute exists");
        iniValue = media.audioTracks;
        media.audioTracks = null;
        assert_true(media.audioTracks == iniValue && media.audioTracks != null, "media.audioTracks is readonly");
    }, document.title);
}

//videoTracks
function videotracks_attribute_type() {
    test(function() {
        getmedia();
        assert_true("videoTracks" in media, "the videoTracks attribute exists");
        assert_true(typeof media.videoTracks == "object", "media.videoTracks is of type object");
    }, document.title);
}

function videotracks_attribute_readonly() {
    test(function() {
        getmedia();
        assert_true("videoTracks" in media, "the videoTracks attribute exists");
        iniValue = media.videoTracks;
        media.videoTracks = null;
        assert_true(media.videoTracks == iniValue && media.videoTracks != null, "media.videoTracks is readonly");
    }, document.title);
}

//textTracks
function texttracks_attribute_type() {
    test(function() {
        getmedia();
        assert_true("textTracks" in media, "the textTracks attribute exists");
        assert_true(typeof media.textTracks == "object", "media.textTracks is of type object");
    }, document.title);
}

function texttracks_attribute_readonly() {
    test(function() {
        getmedia();
        assert_true("textTracks" in media, "the textTracks attribute exists");
        iniValue = media.textTracks;
        media.textTracks = null;
        assert_true(media.textTracks == iniValue && media.textTracks != null, "media.textTracks is readonly");
    }, document.title);
}

function texttracks_attribute_value() {
    test(function() {
        getmedia();
        assert_true("textTracks" in media, "the textTracks attribute exists");
        var tracks = media.textTracks;
        //return an array host object for objects of type TextTrack
        assert_true(tracks && tracks[0] && tracks[0] instanceof TextTrack, "media.textTracks returns " + tracks);
    }, document.title);
}

//addTextTrack
function addtexttrack_function_type() {
    // MutableTextTrack addTextTrack(in DOMString kind, in optional DOMString label, in optional DOMString language);
    test(function() {
        getmedia();
        assert_true("addTextTrack" in media, "the addTextTrack method exists");
        assert_true(typeof media.addTextTrack == "function", "media.addTextTrack() is of type function");
    });
}

function addtexttrack_throw_exception(code) {
    test(function() {
        getmedia();
        assert_true("addTextTrack" in media, "the addTextTrack method does not exist");
        try {
            media.addTextTrack("subtitles", "English", "en");
            assert_true(false, "no exception be thrown");
        } catch (ex) {
            assert_true(ex && (ex.code == ex[code]), "throw an exception and code is "+ex.code);
        }
    });
}

function getFileNameFromPath(path){
    var filename;
    if (path.indexOf("/") > 0) {
        filename = path.substring(path.lastIndexOf("/") + 1, path.length);
    } else {
        filename = path;
    }
    return filename;
}
