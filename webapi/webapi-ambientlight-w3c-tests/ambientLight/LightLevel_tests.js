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
        Cui,Jieqiong <jieqiongx.cui@intel.com>

*/

(function() {
 //Type attribute tests
  test(function() {
    assert_throws(new TypeError(), function() {
      new LightLevelEvent();
    }, 'First argument is required, so was expecting a TypeError.');
  }, 'Missing type argument');

  test(function() {
    var event = new LightLevelEvent(undefined);
    assert_equals(event.type, 'undefined');
  }, 'Event type set to undefined');

  test(function() {
    var event = new LightLevelEvent(null);
    assert_equals(event.type, 'null');
  }, 'type argument is null');

  test(function() {
    var event = new LightLevelEvent(123);
    assert_equals(event.type, '123');
  }, 'type argument is number');

  test(function() {
    var event = new LightLevelEvent(true);
    assert_equals(event.type, 'true');
  }, 'type argument is boolean (true)');

  test(function() {
    var event = new LightLevelEvent(false);
    assert_equals(event.type, 'false');
  }, 'type argument is boolean (false)');

  test(function() {
    var event = new LightLevelEvent('test');
    assert_equals(event.type, 'test');
  }, 'type argument is string');

  test(function() {
    var desc = 'window.onlightlevel did not treat noncallable (string) as null';
    window.onlightlevel = function() {};
    window.onlightlevel = 'string';
    assert_equals(window.onlightlevel, null, desc);
  }, 'treat string as null');

  test(function() {
    var desc = 'window.onlightlevel did not treat noncallable (number) as null';
    window.onlightlevel = function() {};
    window.onlightlevel = 123;
    assert_equals(window.onlightlevel, null, desc);
  }, 'treat number as null');

  test(function() {
    var desc = 'window.onlightlevel did not treat noncallable (undefined) as null';
    window.onlightlevel = function() {};
    window.onlightlevel = undefined;
    assert_equals(window.onlightlevel, null, desc);
  }, 'treat undefined as null');

  test(function() {
    var desc = 'window.onlightlevel did not treat noncallable (array) as null';
    window.onlightlevel = function() {};
    window.onlightlevel = [];
    assert_equals(window.onlightlevel, null, desc);
  }, 'treat array as null');
})();
