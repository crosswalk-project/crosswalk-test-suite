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
         Zhang, Zhiqiang <zhiqiang.zhang@intel.com>

*/



/* http://www.w3.org/TR/html5/the-iframe-element.html#the-video-element */

var media;
var name;

function getmedia() {
    if (media == null) {
        media = document.getElementById("m");
        name = document.getElementsByName("assert")[0].content;
    }
}


//check the property of media is exist
function video_property_exist(property_name)
{
    test( function() {
        getmedia();
        assert_true(property_name in media, "media." + property_name +" exists");
    }, name);
}

//attribute type
function video_property_type(property_name, property_type)
{
    getmedia();

    test(function() {
         assert_true(typeof media[property_name] == property_type, "media." + property_name +" is of type   "+property_type);
    }, name);

}


//default value
function video_default_value(property_name, defaut_value)
{
    test(function() {
        getmedia();
        assert_equals(media[property_name],defaut_value,"the defaut value of video." + property_name + "is " + defaut_value);
    }, name);
}

//attribute readonly
function video_property_readonly(property_name, new_value)
{
    test(function() {
        getmedia();
        media[property_name] = new_value;
        assert_true(media[property_name] != new_value,"the video." + property_name + "is readonly");
    }, name);
}

function video_poster_empty_string()
{
    getmedia();
    media.poster = "";
}

function video_poster_null()
{
    getmedia();
    media.poster = null;
}

function video_poster_first_frame()
{
    setTimeout(function () {
        getmedia();
        media.pause();
    }, 2000)
}



var ULONG = {
    'DEFAULT'  : 0,
    'MIN'      : 0,
    'INTEGER'  : 480,
    'FLOAT'    : 480.5,
    'MAX'      : 2147483647,
    'UPPER'    : 2147483648,
    'NEGATIVE' : -480,
    'INVALID'  : 'INVALID'
};

/* attribute unsigned long width; */

function video_width_attribute_type()
{
    getmedia();
    test(function() {
      assert_equals(typeof media.width, 'number', "media.width of type");
    }, name);
}

function video_width_initial()
{
    getmedia();
    test(function() {
        assert_false(media.width < ULONG.MIN, "media.width initial negative");
    }, name);
}

function width_reflects(value, expected)
{
    getmedia();
    test(function() {
        media.width = value;
        assert_equals(media.width, expected, "media.width new value");
    }, name);
}

/* attribute unsigned long height; */

function video_height_attribute_type()
{
    getmedia();
    test(function() {
        assert_equals(typeof media.height, 'number', "media.height of type");
    }, name);
}

function video_height_initial()
{
    getmedia();
    test(function() {
        assert_false(media.height < ULONG.MIN, "media.height initial negative");
    }, name);
}

function height_reflects(value, expected)
{
    getmedia();
    test(function() {
        media.height = value;
        assert_equals(media.height, expected, "media.height new value");
    }, name);
}

// <video></video>
function video_element(desc)
{
    var video = document.getElementById("m")
    var media = document.getElementById("m");

    if (video == null) {
        test(function() {
            assert_false(true, "HTML video element of value null");
        }, desc);
    } else if (typeof video != 'object') {
        test(function() {
            assert_true(false, "HTML video element of type object");
        }, desc);
    } else if (video.toString() != '[object HTMLVideoElement]') {
        test(function() {
            assert_true(false, "HTML video element of [object HTMLVideoElement]");
        }, desc);
    } else if (video != media) {
        test(function() {
            assert_true(false, "HTML video element of value media");
        }, desc);
    } else {
        test(function() {
            assert_true(true, "HTML video element of type object");
        }, desc);
    }
}
