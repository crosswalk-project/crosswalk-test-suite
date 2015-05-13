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

Authors:
         Zhang, Zhiqiang <zhiqiang.zhang@intel.com>

*/

/* http://www.w3.org/TR/html5/the-iframe-element.html#htmlmediaelement */

var media;
var name;

function getmedia()
{
    if (media == null) {
        media = document.getElementById("m");
        name = document.getElementsByName("assert")[0].content;
    }
}

//attribute constant value
function media_property_constant_value(constant_name,constant_value)
{
    test( function() {
        getmedia();
        assert_true(media[constant_name] == constant_value , "media." + constant_name +" of value " + constant_value);
    }, name);
}

//attribute/method/constant type
function media_property_type(property_name, property_type,isInstance)
{
    getmedia();
    if (isInstance) {
       test( function() {
            assert_true(media[property_name] instanceof property_type, "media." + property_name +" is of type   "+ media[property_name].toString());
        }, name);
    } else {
        test( function() {
            assert_true(typeof media[property_name] == property_type, "media." + property_name +" is of type   "+property_type);
        }, name);
    }
}

//attribute/method/constant exist
function media_property_exists(property_name)
{
    test( function() {
        getmedia();
        assert_true(property_name in media, "media." + property_name +" exists");
    }, name);
}

//default value of attribute
function media_default_value(property_name, defaut_value)
{
    test( function() {
        getmedia();
        assert_equals(media[property_name],defaut_value, "the defaut value of media." + property_name + " is " + defaut_value);
    }, name);
}

//attribute readonly
function media_property_readonly(property_name, new_value)
{
    test( function() {
        getmedia();
        media[property_name] = new_value;
        assert_true(media[property_name] != new_value, "the video." + property_name + " is readonly");
    }, name);
}

function error_MEDIA_ERR_SRC_NOT_SUPPORTED()
{
    test( function() {
        getmedia();
        media.src = 'a-video-that-is-unsupported';
        media.onerror = function(e) {
            assert_true(media.error.code === media.error.MEDIA_ERR_SRC_NOT_SUPPORTED,document.title);
        }
    });
}

function src_null()
{
    test( function() {
       getmedia();
       media.src = null;
       var filename = getFileNameFromPath(media.src);
       assert_true(filename === "", document.title);
    });
}

var media_resource = 'movie_5.ogv';
var media_resource_2 = 'movie_5.webm';

function src_basic()
{
    test( function() {
        getmedia();
        assert_equals(getFileNameFromPath(media.src), media_resource, document.title);
        }
    );
}

function src_modify()
{
    test( function() {
        getmedia();
        media.src = "media/" + media_resource_2;
        assert_equals(getFileNameFromPath(media.src), media_resource_2, document.title);
        }
    );
}

function currentSrc_src_empty_string()
{
     test( function() {
         getmedia();
         media.src = "";
         var filename = getFileNameFromPath(media.currentSrc);
         assert_equals(filename, "", document.title);
         }
    );
}

function currentSrc_src_null()
{
     test( function() {
         getmedia();
         media.src = null;
         var filename = getFileNameFromPath(media.currentSrc);
         assert_equals(filename, "", document.title);
         }
    );
}

function networkState_states(state)
{
    getmedia();
    if (state == 'NETWORK_LOADING')
    {
       media.load();
    }
    test( function() {

        assert_true(media.networkState === media[state], document.title);
        }
    );

}

function preload_auto()
{
    test( function() {
        getmedia();
        media.preload = "auto";
        assert_equals(media.preload, "auto", document.title);
        }
    );
}

function preload_empty_string()
{
    test( function() {
        getmedia();
        media.preload = "";
        assert_equals(media.preload, "auto", document.title);
        }
    );
}

function preload_null()
{
    test( function() {
        getmedia();
        media.preload = null;
        assert_equals(media.preload, "auto", document.title);
        }
    );
}

function buffered_end_type()
{
    test( function () {
        getmedia();
        assert_true(typeof media.buffered.end == 'function', document.title);
        }
    );
}

function buffered_length_default_value()
{
    test( function() {
        getmedia();
        assert_equals(media.buffered.length, 0, document.title);
        }, document.title);
}

function buffered_start_type()
{
    test( function() {
        getmedia();
        assert_true(typeof media.buffered.start == 'function', document.title);
    });
}

function load_method()
{
    test( function() {
        getmedia();
        media.src = "media/" + media_resource;
        media.load();
        var filename = getFileNameFromPath(media.src);
        assert_equals(filename, media_resource, document.title);
    });
}

function canPlayType_empty_string()
{
    test( function() {
        getmedia();
         assert_equals(media.canPlayType(""), '', "not return empty string if arguments is a empty string")
         }
    );
}

function canPlayType_null()
{
    test( function() {
         getmedia();
         assert_equals(media.canPlayType(null), '', "not return empty string if arguments is null")
         }
    );
}

//media event
function media_event(event_name , parameter)
{
    var t = async_test(document.title, {timeout: 30000});
    setup({timeout:15000});
    getmedia();

    media.addEventListener(event_name, t.step_func(function () {
         t.done();
     }), false);

     if (event_name == 'abort'){
         setTimeout( function () {
             media.src = "";
             media.load();
         }, 300);
     }
     else if(event_name == 'emptied')
     {
         media.load();
     }
     else if(event_name == 'pause')
     {
        setTimeout(function () {
            media.pause();
        },1000)
     }
     else if(event_name == 'ended')
     {
        media.load();
        setTimeout(function () {
           media.currentTime = media.duration - 2;
           media.play();
       },1000)
     }
     else if(event_name == 'seeking')
     {
        media.addEventListener('loadedmetadata', function() {
            media.currentTime=media.duration-2;
        }, false);
     }
     else if(event_name == 'waiting')
     {
        media.play();
        media.pause();
     }
     else if(event_name == 'ratechange' && parameter == 'defaultPlaybackRate')
     {
        setTimeout(function () {
           media.defaultPlaybackRate = 0.5;
        },500)
     }
     else if(event_name == 'ratechange' && parameter == 'playbackRate')
     {
         setTimeout(function () {
             media.playbackRate = 0.5;
         },500)
     }
     else if(event_name == 'volumechange' && parameter == 'muted')
     {
         setTimeout(function () {
             media.muted = "muted";
         },500)
     }
     else if(event_name == 'volumechange' && parameter == 'volume')
     {
         setTimeout(function () {
             media.volume = 0.5;
         },500)
     }
     setTimeout( function () {
         t.step(function() {
             assert_true(false,"not support this "+event_name+" event");
         });
     }, 10000);
}

function duration_attribute_value_resource() {
    getmedia();
    var t = async_test(document.title, { timeout: 30000 });
    media.addEventListener("loadedmetadata", function () {
        t.step(function () {
            var flag = media.duration > 0;
            assert_true(flag, window.title);
        });
        t.done();
    }, false);
}

function media_property_value_setting(property_name, new_value) {
    test(function () {
        getmedia();
        media[property_name] = new_value;
        assert_true(media[property_name] == new_value, "the media." + property_name + " value is " + new_value);
    });
}

function defaultPlaybackRate_value_null() {
    test(function () {
        getmedia();
        media.defaultPlaybackRate = null;
        assert_true(media.defaultPlaybackRate == 0, "the media.defaultPlaybackRate is 0");
    });
}

function playbackRate_value_null() {
    test(function () {
        getmedia();
        media.playbackRate = null;
        assert_true(media.playbackRate == 0, "the media.playbackRate is 0");
    });
}

function currentTime_exception_INVALID_STATE_ERR() {
    test(function () {
        getmedia();
        try {
            media.currentTime = 3;
        } catch (err) {
            assert_true(err.name == 'InvalidStateError', document.title);
        }
    });
}

function currentTime_basic() {
    getmedia();
    var t = async_test(document.title, { timeout: 3000 });
    media.addEventListener("loadedmetadata", function () {
        t.step(function () {
            media.currentTime = 4;
            assert_true(media.currentTime==4, window.title);
        });
        t.done();
    }, false);
}

function currentTime_value_duration() {
    getmedia();
    var t = async_test(document.title, { timeout: 3000 });
    media.addEventListener("loadedmetadata", function () {
        t.step(function () {
            media.currentTime = media.duration;
            assert_true(media.ended, window.title);
        });
        t.done();
    }, false);
}

function currentTime_value_later_end() {
    getmedia();
    var t = async_test(document.title, { timeout: 3000 });
    media.addEventListener("loadedmetadata", function () {
        t.step(function () {
            media.currentTime = 5;
            assert_equals(media.currentTime, Math.round(media.duration), "The media.currentTime ");
        });
        t.done();
    }, false);
}

function currentTime_value_null() {
    getmedia();
    var t = async_test(document.title, { timeout: 3000 });
    media.addEventListener("loadedmetadata", function () {
        t.step(function () {
            media.currentTime = null;
            assert_true(media.currentTime == 0, window.title);
        });
        t.done();
    }, false);
}

function seeking_value_true() {
    getmedia();
    var t = async_test(document.title, { timeout: 3000 });
    media.addEventListener("loadedmetadata", function () {
        t.step(function () {
            media.currentTime = 4;
            assert_true(media.seeking == true, window.title);
        });
        t.done();
    }, false);
}

function defaultMuted_empty_stirng(){
    test(function () {
        getmedia();
        media.defaultMuted = "";
        assert_false(media.defaultMuted, "media.defaultMuted is false");
    }, name);
}

function defaultMuted_null()
{
    test(function () {
        getmedia();
        media.defaultMuted = null;
        assert_false(media.defaultMuted, "media.defaultMuted is false");
    }, name);
}

function volume_exception(){
    test(function() {
        getmedia();
        try{
            media.volume = 1.2;
        }catch(err){
                assert_true(err.name === "INDEX_SIZE_ERR" ,"throw an INDEX_SIZE_ERR exception");
        }
    }, name);
}

function volume_empty_string()
{
    test(function() {
        getmedia();
        media.volume = "";
        assert_true(media.volume === 0.0, "audio.volume value is 0.0");
    }, name);
}

function volume_null(){
    test(function() {
        getmedia();
        media.volume = null;
        assert_true(media.volume === 0.0, "audio.volume value is 0.0");
    }, name);
}

function volume_exception_upper()
{
        var time = 30000;
        var t = async_test("volume - to verify if user agent is able to get an INDEX_SIZE_ERR exception when set volume with new value more than 1.0", {timeout:time});
        getmedia();
        var lastVolume = media.volume;
        var newVolume = 1.1;
        function startTest() {
            t.step(function() {
                try {
                    media.volume = newVolume;
                } catch(e) {
                    assert_equals(e.code, e.INDEX_SIZE_ERR, "An INDEX_SIZE_ERR exception must be raised if the new volume value is outside the range 0.0 to 1.0 inclusive");
                }
                media.pause();
            });
            t.done();
            return false;
        }
        media.addEventListener("loadedmetadata", startTest, false);
        media.src="media/" + media_resource;
}

function volume_exception_lower()
{
        var time = 30000;
        var t = async_test("volume - to verify if user agent is able to get an INDEX_SIZE_ERR exception when set volume with new value less than 1.0", {timeout:time});
        getmedia();
        var lastVolume = media.volume;
        var newVolume = 0.1;
        function startTest() {
            t.step(function() {
                try {
                    media.volume = newVolume;
                } catch(e) {
                    assert_equals(e.code, e.INDEX_SIZE_ERR, "An INDEX_SIZE_ERR exception must be raised if the new volume value is outside the range 0.0 to 1.0 inclusive");
                }
                media.pause();
            });
            t.done();
            return false;
        }
        media.addEventListener("loadedmetadata", startTest, false);
        media.src="media/" + media_resource;
}

function controls_null(){
    test(function () {
        getmedia();
        media.controls = null;
        assert_false(media.controls, "media.controls is false");
    }, name);
}

function controls_empty_string()
{
    test(function () {
        getmedia();
        media.controls = "";
        assert_false(media.controls, "media.controls is false");
    }, name);
}

function controls_false()
{
    test(function () {
        getmedia();
        media.controls = false;
        assert_false(media.controls, "media.controls is false");
    }, name);
}

function controls_true()
{
    test(function () {
        getmedia();
        media.controls = true;
        assert_true(media.controls, "media.controls is true");
    }, name);
}

function controls_MediaController()
{
    test(function () {
        getmedia();
        var myController = new MediaController();
        media.controller = myController;
        assert_true(media.controls !=null, "media.controls is not null");
    }, name);
}

function mediaGroup_empty_stirng()
{
    test(function () {
        var m1 = document.getElementById('m1');
        var m2 = document.getElementById('m2');
        m1.mediaGroup= "";
        m2.mediaGroup = "";
        var flag = (m1.mediaGroup == m2.mediaGroup) && (m1.mediaGroup == "") && (m2.mediaGroup == "");
        assert_true(flag, "media.mediaGroup is empty string");
    }, name);
}

function mediaGroup_null()
{
    test(function () {
        var m1 = document.getElementById('m1');
        var m2 = document.getElementById('m2');
        m1.mediaGroup= null;
        m2.mediaGroup = null;
        var flag = (m1.mediaGroup == m2.mediaGroup) && (m1.mediaGroup == "") && (m2.mediaGroup == "");
        assert_true(flag, "media.mediaGroup is empty string");
    }, "To check the value of attribute audio.mediaGroup is empty string when set it null");
}

function mediaGroup_valid_value(){
    test(function () {
        var m1 = document.getElementById('m1');
        var m2 = document.getElementById('m2');
        m1.mediaGroup= "group";
        m2.mediaGroup = "group";
        var flag = (m1.mediaGroup == m2.mediaGroup) && (m1.mediaGroup == "group") && (m2.mediaGroup == "group");
        assert_true(flag, "media.mediaGroup is 'group'");
    }, name);
}

function loop_empty_stirng()
{
    test(function () {
        getmedia();
        media.loop = "";
        assert_false(media.loop, "media.loop is false");
    }, name);
}

function loop_null()
{
    test(function () {
        getmedia();
        media.loop = null;
        assert_false(media.loop, "media.loop is false");
    }, name);
}

function autoplay_null()
{
    test(function () {
        getmedia();
        media.autoplay = null;
        assert_false(media.autoplay, "media.autoplay is false");
    }, name);
}

function autoplay_empty_string()
{
    test(function () {
        getmedia();
        media.autoplay = "";
        assert_false(media.autoplay, "media.autoplay is false");
    }, name);
}

function autoplay_true_autoplay_present()
{
    test(function () {
        getmedia();
        assert_true(media.autoplay, "media.autoplay is true");
    }, name);
}

function ended_playing()
{
    var t = async_test();
    getmedia();
    media.addEventListener("playing", function() {
        t.step(function() {
            assert_false(media.ended, "media.ended is false");
        });
        t.done();
        media.pause();
    }, false);
}

function ended_loadeddata()
{
    var t = async_test();
    getmedia();
    media.addEventListener("loadeddata", function() {
        t.step(function() {
            assert_false(media.ended, "media.ended is false");
        });
        t.done();
        media.pause();
    }, false);
}

function ended_currentTime_duration()
{
    var t = async_test();
    getmedia();
    media.addEventListener("loadeddata", function() {
        media.currentTime = media.duration;
        t.step(function() {
            assert_true(media.ended,window.title);
        });
        t.done();
    }, false);
}

function ended_canplaythrough()
{
    var t = async_test();
    getmedia();
    media.addEventListener("canplaythrough", function() {
        t.step(function() {
            assert_false(media.ended,window.title);
        });
        t.done();
    }, false);
}

function seekable_length_default_value()
{
    test(function () {
        getmedia();
        assert_equals(media.seekable.length, 0);
    }, name);
}

function played_length_default_value()
{
    test(function () {
        getmedia();
        assert_equals(media.played.length, 0);
    }, name);
}

function controls_false_controls_absent()
{
    getmedia();
    test(function() {
        assert_false(media.controls, "media.controls of value");
    }, name);
}

function controls_true_controls_present()
{
    getmedia();
    test(function() {
        assert_true(media.controls, "media.controls of value");
    }, name);
}

function controls_reflects_false()
{
    getmedia();
    test(function() {
        media.controls = false;
        assert_false(media.controls, "media.controls of value");
    }, name);
}

function controls_reflects_true()
{
    getmedia();
    test(function() {
        media.controls = true;
        assert_true(media.controls, "media.controls of value");
    }, name);
}

function defaultMuted_false_muted_absent()
{
    getmedia();
    test(function() {
        assert_false(media.defaultMuted, "media.defaultMuted of value");
    }, name);
}

function defaultMuted_no_dynamic_effect()
{
    getmedia();
    test(function() {
        media.muted = true;
        assert_false(media.defaultMuted, "media.defaultMuted of value");
    }, name);
}

function defaultMuted_no_dynamic_effect_muted()
{
    getmedia();
    test(function() {
        media.muted = false;
        assert_true(media.defaultMuted, "media.defaultMuted of value");
    }, name);
}

function defaultMuted_true_muted_present()
{
    getmedia();
    test(function() {
        assert_true(media.defaultMuted, "media.defaultMuted of value");
    }, name);
}

function loop_false_loop_absent()
{
    getmedia();
    test(function() {
        assert_false(media.loop, "media.loop of value");
    }, name);
}

function loop_true_loop_present()
{
    getmedia();
    test(function() {
        assert_true(media.loop, "media.loop of value");
    }, name);
}

function loop_reflects_false()
{
    getmedia();
    test(function() {
        media.loop = false;
        assert_false(media.loop, "media.loop of value");
    }, name);
}

function loop_reflects_true()
{
    getmedia();
    test(function() {
        media.loop = true;
        assert_true(media.loop, "media.loop of value");
    }, name);
}

/* attribute boolean muted; */
function muted_attribute_type()
{
    getmedia();
    test(function() {
       assert_equals(typeof media.muted, 'boolean', "media.muted of type");
    }, name);
}

function muted_false_muted_absent()
{
    getmedia();
    test(function() {
        assert_false(media.muted, "media.muted of value");
    }, name);
}

function muted_true_muted_present()
{
    getmedia();
    test(function() {
        assert_true(media.muted, "media.muted of value");
     }, name);
}

 function muted_false_unmuted()
{
    getmedia();
    test(function() {
        media.muted = false;
        assert_false(media.muted, "media.muted of value");
    }, name);
}

function muted_true_muted()
{
    getmedia();
    test(function() {
        media.muted = true;
        assert_true(media.muted, "media.muted of value");
    }, name);
}

function volume_initial()
{
    getmedia();
    test(function() {
        assert_false(media.volume < VOLUME.SILENT || media.volume > VOLUME.LOUDEST, "media.volume outside the range 0.0 to 1.0 inclusive");
    }, name);
}

var VOLUME = {
    'SILENT'  :  0.0,
    'NORMAL'  :  0.5,
    'LOUDEST' :  1.0,
    'LOWER'   : -1.1,
    'UPPER'   :  1.1,
};

function getFileNameFromPath(path){
    var filename;
    if(path.indexOf("/")>0)
    {
        filename=path.substring(path.lastIndexOf("/")+1,path.length);
    }
    else
    {
        filename=path;
    }
    return filename;
}
