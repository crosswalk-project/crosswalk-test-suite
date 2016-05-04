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

var handModule;

test(function() {
  assert_own_property(realsense, "Hand", "realsense should expose Hand");
  assert_equals(typeof realsense.Hand, "object");
}, "Check that Hand is present on realsense");

test(function() {
  assert_own_property(realsense.Hand, "HandModule", "realsense.Hand should expose HandModule");
}, "Check that realsense.Hand support HandModule");

test(function() {
  handModule = new realsense.Hand.HandModule();
  assert_equals(typeof handModule, "object");
}, "Check that construct a HandModule object");

test(function() {
  assert_own_property(handModule, "init", "init method exists");
  assert_equals(typeof handModule.init, "function", "typeof handModule.init");
}, "Check that handModule has implement init method");

test(function() {
  assert_own_property(handModule, "start", "start method exists");
  assert_equals(typeof handModule.start, "function", "typeof handModule.start");
}, "Check that handModule has implement start method");

test(function() {
  assert_own_property(handModule, "stop", "stop method exists");
  assert_equals(typeof handModule.stop, "function", "typeof handModule.stop");
}, "Check that handModule has implement stop method");

test(function() {
  assert_own_property(handModule, "track", "track method exists");
  assert_equals(typeof handModule.track, "function", "typeof handModule.track");
}, "Check that handModule has implement track method");

test(function() {
  assert_own_property(handModule, "getDepthImage", "getDepthImage method exists");
  assert_equals(typeof handModule.getDepthImage, "function", "typeof handModule.getDepthImage");
}, "Check that handModule has implement getDepthImage method");

promise_test(function(t) {
  return handModule.init()
    .then(function() {
      assert_true(true);
    })
    .catch(function(ex) {
      assert_unreached("get unexpected exception. " + ex.message);
    });
}, "Check that init a hand tracking");

promise_test(function(t) {
  return handModule.start()
    .then(function() {
      assert_true(true);
    })
    .catch(function(ex) {
      assert_unreached("get unexpected exception. " + ex.message);
    });
}, "Check that start hand tracking successfully");

promise_test(function(t) {
  return handModule.stop()
    .then(function() {
      assert_true(true);
    })
    .catch(function(ex) {
      assert_unreached("get unexpected exception. " + ex.message);
    });
}, "Check that stop hand tracking successfully");

