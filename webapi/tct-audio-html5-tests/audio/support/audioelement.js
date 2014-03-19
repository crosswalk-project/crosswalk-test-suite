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
         Zhang, Zhiqiang <zhiqiang.zhang@intel.com>

*/

/* http://www.w3.org/TR/html5/the-iframe-element.html#the-audio-element */

// <audio></audio>
function audio_element(desc)
{
    var media = document.getElementById("m");
    var audio = document.getElementById("m");

    if (audio == null) {
        test(function() {
            assert_false(true, "HTML audio element of value null");
        }, desc);
    } else if (typeof audio != 'object') {
        test(function() {
            assert_true(false, "HTML audio element of type object");
        }, desc);
    } else if (audio.toString() != '[object HTMLAudioElement]') {
        test(function() {
            assert_true(false, "HTML audio element of [object HTMLAudioElement]");
        }, desc);
    } else if (audio != media) {
        test(function() {
            assert_true(false, "HTML audio element of value media");
        }, desc);
    } else {
        test(function() {
            assert_true(true, "HTML audio element of type object");
        }, desc);
    }
}

// new Audio()
function audio_constructor(desc)
{
    var audio = new Audio();

    test(function() {
        assert_equals(audio.toString(), '[object HTMLAudioElement]',
            "HTML audio element of [object HTMLAudioElement]");
    }, desc);
}

// new Audio(src)
function audio_constructor_src(desc, src)
{
    var audio = new Audio(src);

    test(function() {
        assert_equals(audio.toString(), '[object HTMLAudioElement]',
            "HTML audio element of [object HTMLAudioElement]");
    }, desc);
}
