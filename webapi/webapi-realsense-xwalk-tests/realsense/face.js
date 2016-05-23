/*
Copyright (c) 2016 Intel Corporation.

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
*/

var fm;

test(function() {
  assert_own_property(realsense, "Face", "realsense should expose Face");
  assert_equals(typeof realsense.Face, "object");
}, "Check that Face is present on realsense");

test(function() {
  assert_own_property(realsense.Face, "FaceModule", "realsense should expose Face");
}, "Check that realsense.Face support FaceModule");

async_test(function(t) {
  navigator.getUserMedia({video: true}, function gotUserMediaSuccess(stream) {
    test(function() {
      fm = new realsense.Face.FaceModule(stream);
      assert_equals(typeof fm, "object");
    }, "Check that construct a FaceModule object");

    test(function() {
      assert_own_property(fm, "configuration");
    }, "Check that configuration exist");

    test(function() {
      assert_readonly(fm, "configuration", "configuration is readonly");
    }, "Check that configuration is readonly");

    test(function() {
      assert_equals(typeof fm.configuration, "object");
      assert_class_string(fm.configuration, "FaceConfiguration");
    }, "Check that configuration is type of FaceConfiguration object");

    test(function() {
      assert_own_property(fm, "recognition");
    }, "Check that recognition exists");

    test(function() {
      assert_readonly(fm, "recognition", "recognition is readonly");
    }, "Check that recognition is readonly");

    test(function() {
      assert_equals(typeof fm.recognition, "object");
      assert_class_string(fm.recognition, "Recognition");
    }, "Check that recognition is type of Recognition object");

    test(function() {
      assert_equals(typeof fm.previewStream, "object");
      assert_class_string(fm.previewStream, "MediaStream");
    }, "Check that previewStream is type of MediaStream object");

    test(function() {
      assert_own_property(fm, "onready");
    }, "Check that fm.onready exists");

    test(function() {
      assert_own_property(fm, "onended");
    }, "Check that fm.onended exists");

    test(function() {
      assert_own_property(fm, "onerror");
    }, "Check that fm.onerror exists");

    test(function() {
      assert_own_property(fm, "onprocessedsample");
    }, "Check that onprocessedsample exists");

    test(function() {
      assert_own_property(fm, "start");
      assert_equals(typeof fm.start, "function");
    }, "Check that fm.start() exists");

    test(function() {
      assert_own_property(fm, "stop");
      assert_equals(typeof fm.stop, "function");
    }, "Check that fm.stop() exists");

    test(function() {
      assert_own_property(fm, "getProcessedSample");
      assert_equals(typeof fm.getProcessedSample, "function");
    }, "Check that getProcessedSample() exists");

    test(function() {
      assert_own_property(fm.recognition, "registerUserByFaceID",
      "registerUserByFaceID exists");
      assert_equals(typeof fm.recognition.registerUserByFaceID, "function",
      "fm.recognition.registerUserByFaceID is type of function");
    }, "Check that registerUserByFaceID method exists");

    test(function() {
      assert_own_property(fm.recognition, "unregisterUserByID",
      "unregisterUserByID exists");
      assert_equals(typeof fm.recognition.unregisterUserByID, "function",
      "fm.recognition.unregisterUserByID is type of function");
    }, "Check that unregisterUserByID method exists");

  promise_test(function() {
    return fm.getProcessedSample(false, false)
      .then(function() {
        assert_unreached("unreached here when parameters are null");
      })
      .catch(function(ex) {
        assert_true(ex instanceof DOMException, "throw a DOMException");
        assert_equals(ex.code, 11);
        assert_equals(ex.name, "InvalidStateError");
      });
    }, "Check that fm.getProcessedSample should reject with InvalidStateError exception " +
       "when face module doesn't start");

    promise_test(function() {
      return fm.recognition.registerUserByFaceID()
        .then(function() {
          assert_unreached("unreached here when miss faceId parameter");
        })
        .catch(function(ex) {
          assert_true(ex instanceof DOMException, "throw a DOMException");
          assert_equals(ex.code, 11);
          assert_equals(ex.name, "InvalidStateError");
        });
    }, "Check that fm.recognition.registerUserByFaceID() should reject with InvalidStateError exception");

    promise_test(function() {
      return fm.recognition.registerUserByFaceID(null)
        .then(function() {
          assert_unreached("unreached here when faceId is null");
        })
        .catch(function(ex) {
          assert_true(ex instanceof DOMException, "throw a DOMException");
          assert_equals(ex.code, 11);
          assert_equals(ex.name, "InvalidStateError");
        });
    }, "Check that fm.recognition.registerUserByFaceID(null) should reject with InvalidStateError exception");

    promise_test(function() {
      return fm.recognition.unregisterUserByID()
        .then(function() {
          assert_unreached("unreached here when miss faceId parameter");
        })
        .catch(function(ex) {
          assert_true(ex instanceof DOMException, "throw a DOMException");
          assert_equals(ex.code, 11);
          assert_equals(ex.name, "InvalidStateError");
        });
    }, "Check that fm.recognition.unregisterUserByID() should reject with InvalidStateError exception");

    promise_test(function() {
      return fm.recognition.unregisterUserByID(null)
        .then(function() {
          assert_unreached("unreached here when userId is null");
        })
        .catch(function(ex) {
          assert_true(ex instanceof DOMException, "throw a DOMException");
          assert_equals(ex.code, 11);
          assert_equals(ex.name, "InvalidStateError");
        });
    }, "Check that fm.recognition.unregisterUserByID(null) should reject with InvalidStateError exception");

    test(function() {
      assert_own_property(fm.configuration, "set",
      "fm.configuration.set method exists");
      assert_equals(typeof fm.configuration.set, "function",
      "fm.configuration.set is type of function");
    }, "Check that FaceConfiguration.set method exist");

    test(function() {
      assert_own_property(fm.configuration, "getDefaults",
      "fm.configuration.getDefaults method exists");
      assert_equals(typeof fm.configuration.getDefaults, "function",
      "fm.configuration.getDefaults is type of function");
    }, "Check that FaceConfiguration.getDefaults method exist");

    test(function() {
      assert_own_property(fm.configuration, "get",
      "fm.configuration.get method exists");
      assert_equals(typeof fm.configuration.get, "function",
      "fm.configuration.get is type of function");
    }, "Check that FaceConfiguration.get method exist");

    promise_test(function() {
      return fm.configuration.set()
        .then(function() {
          assert_unreached("unreached here when miss faceId parameter");
        })
        .catch(function(ex) {
          assert_true(ex instanceof DOMException, "throw a DOMException");
          assert_equals(ex.code, 15);
          assert_equals(ex.name, "InvalidAccessError");
        });
    }, "Check that fm.configuration.set() should reject with InvalidAccessError exception");

    promise_test(function() {
      return fm.configuration.set(null)
        .then(function() {
          assert_unreached("unreached here when userId is null");
        })
        .catch(function(ex) {
          assert_true(ex instanceof DOMException, "throw a DOMException");
          assert_equals(ex.code, 15);
          assert_equals(ex.name, "InvalidAccessError");
        });
    }, "Check that fm.configuration.set(null) should reject with InvalidAccessError exception");

  promise_test(function() {
    var config = {
      mode: "color-depth",
      recognition: {enable: true},
      strategy: "left-right"
    };
    return fm.configuration.set(config)
      .then(function() {
        return fm.configuration.get();
      })
      .then(function (configData) {
        assert_equals(configData.mode, "color-depth", "configData.mode is color-depth");
        assert_true(configData.recognition.enable, "configData.recognition.enable is true");
        assert_equals(configData.strategy, "left-right", "configData.strategy is left-right");
      })
      .catch(function(ex) {
        assert_unreached("unreached here, get an error: " + ex.message);
      });
    }, "Check that set and get configuration values");

    promise_test(function() {
      return fm.configuration.getDefaults()
        .then(function(config) {
          assert_own_property(config, "detection");
          assert_own_property(config, "landmarks");
          assert_own_property(config, "mode");
          assert_own_property(config, "recognition");
          assert_own_property(config, "strategy");
        })
        .catch(function(ex) {
          assert_unreached("unreached here, get an error: " + ex.message);
        });
    }, "Check that Get configuration default values");

    t.done();

  }, function(ex) {
    assert_unreached("Access to audio and video stream get error: " + ex.message);
  });
}, "Check that get FaceModule stream");

