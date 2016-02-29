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

 Authors:
         Yun, Liu<yunx.liu@intel.com>
         Donna, Wu<donna.wu@intel.com>
*/

function XWalkExtensionHooks(app, configId, extraArgs, sharedState) {
    
    this._app = app;

    // The sharedState object is empty, but in can be used to
    // pass information from the prePackage() to postPackage()
    // because those hooks will run on a separate instance of
    // XWalkExtensionHooks.
    this._sharedState = sharedState;
}

XWalkExtensionHooks.prototype.prePackage =
function(platform, callback) {

    this._app.output.info("prePackage " + platform);

    // Store random message in sharedState
    this._sharedState.message = "prePackage finished";
    
    callback(0);
};

XWalkExtensionHooks.prototype.postPackage =
function(platform, callback) {
    
    this._app.output.info("postPackage " + platform);

    // Print message from sharedState
    this._app.output.info("postPackage " + this._sharedState.message);

    callback(0);
};

module.exports = XWalkExtensionHooks;
