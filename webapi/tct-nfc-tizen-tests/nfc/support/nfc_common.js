/*
Copyright (c) 2012 Intel Corporation. All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

*Redistributions of works must retain the original copyright notice, this list
of conditions and the following disclaimer.
*Redistributions in binary form must reproduce the original copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.
*Neither the name of Intel Corporation nor the names of its contributors
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
         Han, GuangX <guangx.han@intel.com>

Revision history:
Date                        Author                              Description
04-24-2012         Han, GuangX <guangx.han@intel.com>           code modification
05-18-2012         Han, GuangX <guangx.han@intel.com>           Spec updated
08-07-2012         Wang, ChaoX <chaox.wang@intel.com>           last modified
13-05-2013         Szydelko, Piotr <p.szydelko@samsung.com>     merged with nfc_common.js, renamed
*/

document.write("<script language=\"javascript\" src=\"..\/resources\/testharness.js\"><\/script>");
document.write("<script language=\"javascript\" src=\"..\/resources\/testharnessreport.js\"><\/script>");

var NDEFRecordTextEncoding = {
    "UTF-8": 1,
    "UTF-16": 2
};

var NFCTagType = {
    "GENERIC_TARGET": 1,
    "ISO14443_A": 2,
    "ISO14443_4A": 3,
    "ISO14443_3A": 4,
    "MIFARE_MINI": 5,
    "MIFARE_1K": 6,
    "MIFARE_4K": 7,
    "MIFARE_ULTRA": 8,
    "MIFARE_DESFIRE": 9,
    "ISO14443_B": 10,
    "ISO14443_4B": 11,
    "ISO14443_BPRIME": 12,
    "FELICA": 13,
    "JEWEL": 14,
    "ISO15693": 15,
    "UNKNOWN_TARGET": 16
};

var TYPE_MISMATCH_ERR = 'TypeMismatchError';
var INVALID_VALUES_ERR = 'InvalidValuesError';
var NOT_FOUND_ERR = 'NotFoundError';
var NOT_SUPPORTED_ERR = 'NotSupportedError';
var IO_ERR = 'IOError';
var UNKNOWN_ERR = 'UnknownError';
var EXCEPTION_TYPE = "name";

function createNDEFTextMessage(text) {
    var record = new tizen.NDEFRecordText(text, 'en-US');
    var message = new tizen.NDEFMessage([record]);
    return message;
}
