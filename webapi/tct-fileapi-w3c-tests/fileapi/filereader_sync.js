/*
Copyright (c) 2014 Intel Corporation.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

* Redistributions of works must retain the original copyright notice, this lis
  of conditions and the following disclaimer.
* Redistributions in binary form must reproduce the original copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.
* Neither the name of Intel Corporation nor the names of its contributors
  may be used to endorse or promote products derived from this work withou
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
        Kaiyu <kaiyux.li@intel.com>
        Jin,Weihu <weihux.jin@intel.com>
*/
    try {
        var readerSync = new FileReaderSync();
        onmessage = function(event) {
        if(event.data == "fileReaderSync"){
            postMessage(readerSync.toString());
        } else if(event.data == "fileReaderSync_readAsText"){
            blob = new Blob(["fileReaderSync readAsText is OK"]);
            var text = readerSync.readAsText(blob);
            postMessage(text);
        } else if(event.data == "fileReaderSync_readAsBinaryString"){
            blob = new Blob(["fileReaderSync readAsBinaryString is OK"]);
            var text = readerSync.readAsBinaryString(blob);
            postMessage(text);
        } else if(event.data == "fileReaderSync_readAsDataURL"){
            blob = new Blob(["fileReaderSync readAsDataURL is OK"], {type: "text/plain"});
            var text = readerSync.readAsDataURL(blob);
            postMessage(text);
        } else if(event.data == "fileReaderSync_readAsArrayBuffer"){
            blob = new Blob(["fileReaderSync readAsArrayBuffer is OK"]);
            var text = readerSync.readAsArrayBuffer(blob);
            postMessage(text.toString());
        } else
   	        postMessage("There is a wrong");
        }
    } catch (ex) {
        postMessage("Throw an exception " + ex);	
    }
