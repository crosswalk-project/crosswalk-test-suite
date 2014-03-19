/*
 * Copyright (c) 2012 Intel Corporation.
 *
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted provided that the following conditions are met:
 *
 * *Redistributions of works must retain the original copyright notice, this list
 * of conditions and the following disclaimer.
 * *Redistributions in binary form must reproduce the original copyright notice,
 * this list of conditions and the following disclaimer in the documentation
 * and/or other materials provided with the distribution.
 * *Neither the name of Intel Corporation nor the names of its contributors
 * may be used to endorse or promote products derived from this work without
 * specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
 * INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 * BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 * DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
 * OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 * NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 * EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
 *
 * Authors:
 *         Jenny Cao <jenny.q.cao@intel.com>
 *
 *         Revision history:
 *
 */

var UNKNOWN_ERR         = "UnknownError";
var TYPE_MISMATCH_ERR   = "TypeMismatchError";
var IO_ERR              = "IOError";
var INVALID_VALUES_ERR  = "InvalidValuesError";
var SECURITY_ERR        = "SecurityError";
var NOT_FOUND_ERR       = "NotFoundError";
var NOT_SUPPORT_ERR     = "NotSupportedError";

var APPLICATION_ID = "testalar00.alarmTestApp";

function createAbsAlarm() {
    var absAlarm1, date = new Date();
    date.setFullYear(date.getFullYear() + 1);
    absAlarm1 = new tizen.AlarmAbsolute(date);
    return absAlarm1;
}

function createRelAlarm() {
    var alarmRel1 = new tizen.AlarmRelative(3 * tizen.alarm.PERIOD_HOUR);
    return alarmRel1;
}

function cleanAlarms() {
    tizen.alarm.removeAll();
}
