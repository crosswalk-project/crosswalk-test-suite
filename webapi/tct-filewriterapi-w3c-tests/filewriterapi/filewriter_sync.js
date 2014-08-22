/*
Copyright (c) 2012 Intel Corporation.

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
        Kaiyu <kaiyux.li@intel.com>

Revision history:
Date                        Author                        Description
02-21-2012         Kaiyu <kaiyux.li@intel.com>   create

*/

var fileSystem = webkitRequestFileSystemSync(this.TEMPORARY, 100);

onmessage = function(event) {
   if(event.data == "fileWriterSynclength"){
       var fileEntrySync = fileSystem.root.getFile('test_length.txt',{create:true});
       var fileWriterSync = fileEntrySync.createWriter();
       var bb = new Blob(['test fileWriterSync length attribute'], {type: 'text/plain'});
       fileWriterSync.write(bb);
       postMessage(fileWriterSync.length);
   } else if(event.data == "fileWriterSyncposition"){
       var fileEntrySync = fileSystem.root.getFile('test_position.txt',{create:true});
       var fileWriterSync = fileEntrySync.createWriter();
       var bb = new Blob(['test fileWriterSync position attribute'], {type: 'text/plain'});
       fileWriterSync.write(bb);
       fileWriterSync.seek(5);
       postMessage(fileWriterSync.position);
   } else if(event.data == "fileWriterSyncseek"){
       var fileEntrySync = fileSystem.root.getFile('test_seek.txt',{create:true});
       var fileWriterSync = fileEntrySync.createWriter();
       var bb = new Blob(['test fileWriterSync seek attribute'], {type: 'text/plain'});
       fileWriterSync.write(bb);
       fileWriterSync.seek(10);
       postMessage(fileWriterSync.position);
   } else if(event.data == "fileWriterSyncwrite"){
       var fileEntrySync = fileSystem.root.getFile('test_write.txt',{create:true});
       var fileWriterSync = fileEntrySync.createWriter();
       var blob = new Blob(["test fileWriterSync write method"], {type: 'text/plain'});
       fileWriterSync.write(blob);
       postMessage(fileWriterSync.length);
   } else if(event.data == "fileWriterSynctruncate"){
       var fileEntrySync = fileSystem.root.getFile('test_truncate.txt',{create:true});
       var fileWriterSync = fileEntrySync.createWriter();
       var bb = new Blob(['test fileWriterSync truncate attribute'], {type: 'text/plain'});
       fileWriterSync.write(bb);
       fileWriterSync.truncate(15);
       postMessage(fileWriterSync.length);
   } else
       postMessage("There is a wrong");
}
