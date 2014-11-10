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
        Lei Yang <lei.a.yang@intel.com>
        Fan,Weiwei <weiwix.fan@intel.com>
*/

function checkExceptionCode (ecode,ename) {
    try {
        throw ecode;
    } catch (ex) {
        if (ex.code === ex.message) {
            return 1;
        } else {
            return 0;
        }
    }
}
var checkRefNum = 0;
checkRefNum += checkExceptionCode(0, "UNKNOWN_ERR");
checkRefNum += checkExceptionCode(1, "DATABASE_ERR");
checkRefNum += checkExceptionCode(2, "VERSION_ERR");
checkRefNum += checkExceptionCode(3, "TOO_LARGE_ERR");
checkRefNum += checkExceptionCode(4, "QUOTA_ERR");
checkRefNum += checkExceptionCode(5, "SYNTAX_ERR");
checkRefNum += checkExceptionCode(6, "CONSTRAINT_ERR");
checkRefNum += checkExceptionCode(7, "TIMEOUT_ERR");

if (checkRefNum == 8) {
  postMessage ("PASS");
} else {
  postMessage((8-checkRefNum) + " error codes are not supported");
}
