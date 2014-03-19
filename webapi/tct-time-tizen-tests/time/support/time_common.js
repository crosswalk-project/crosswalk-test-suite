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
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Authors:

*/

var NOT_SUPPORTED_ERR     = "NotSupportedError";
var UNKNOWN_ERR           = "UnknownError";
var TYPE_MISMATCH_ERR     = "TypeMismatchError";
var INVALID_VALUES_ERR    = "InvalidValuesError";
var NOT_FOUND_ERR         = "NotFoundError";
var PERMISSION_DENIED_ERR = "SecurityError";
var IO_ERR                = "IOError";
var ERROR_STR             = "Error";
var ERROR_NUM             = 3;

var expected_year         = 2011;
var expected_month        = 10;
var expected_date         = 11;
var expected_hours        = 4;
var expected_minutes      = 55;
var expected_seconds      = 54;
var expected_milliseconds = 12;
var expected_time_zone    = "Asia/Seoul";//GMT+9
var expected_time_zone_offset = 9;

var date = new tizen.TZDate(
    expected_year,          //year
    expected_month,         //month
    expected_date,          //day
    expected_hours,         //hours
    expected_minutes,       //minutes
    expected_seconds,       //seconds
    expected_milliseconds,  //milliseconds
    expected_time_zone      //timeZone
);

var testAdditionalParamArray = [ERROR_NUM, null, undefined];
