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

test(function() {
  assert_true(twoinone !== "undefined" && twoinone !== null); 
  assert_equals(typeof twoinone, "object");
}, "Check that twoinone is present on window");

test(function() {
  assert_own_property(twoinone, "emulator");
  assert_equals(typeof twoinone.emulator, "object");
}, "Check that emulator is present on twoinone");

test(function() {
  assert_own_property(twoinone.emulator,"setIsTablet");
  assert_equals(typeof twoinone.emulator.setIsTablet, "function");
}, "Check that twoinone.emulator has setIsTablet function");

test(function() {
  assert_own_property(twoinone, "haveKeyboard");
  assert_equals(typeof twoinone.haveKeyboard, "function");
}, "Check that twoinone has haveKeyboard function");

test(function() {
  assert_own_property(twoinone, "isTablet");
  assert_equals(typeof twoinone.isTablet, "function");
}, "Check that twoinone has isTablet function");

test(function() {
  assert_own_property(twoinone, "log");
  assert_equals(typeof twoinone.log, "function");
}, "Check that twoinone has log function");

test(function() {
  assert_own_property(twoinone, "monitorKeyboard");
  assert_equals(typeof twoinone.monitorKeyboard, "function");
}, "Check that twoinone has monitorKeyboard function");

test(function() {
  assert_own_property(twoinone, "monitorTablet");
  assert_equals(typeof twoinone.monitorTablet, "function");
}, "Check that twoinone has monitorTablet function");


async_test(function(t) {
  twoinone.monitorTablet(function (isTablet){
    assert_equals(typeof isTablet, "boolean");
  });
  t.done();
},"Check monitorTablet can got boolean callback value")

async_test(function(t) {
  twoinone.monitorKeyboard(function (hasKeyboard){
    assert_equals(typeof hasKeyboard, "boolean");
  });
  t.done();
},"Check monitorKeyboard can got boolean callback value")
