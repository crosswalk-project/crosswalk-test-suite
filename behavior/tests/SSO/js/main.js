/*
Copyright (c) 2015 Intel Corporation.

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
        Xu, Jianfeng <jianfengx.xu@intel.com>

*/

var info = {
    'type': "WEB",
    'username': "test",
    'secret': "test", 
    'storeSecret': true, 
    'caption': "cap", 
    'realms': ["realm1"], 
    'owner': {"sysContext":"*","appContext":"*"}, 
    'accessControlList': [{"secContext":{"sysContext":"*","appContext":"*"},
    "method":"password","mechanisms":["password"]}]  
  };
var res;

function createIdentify() {
  res = tizen.sso.authService.createIdentity(info);
  if (res.syncOpErrorMsg != null) {
    _logData('Identity creation FAILED with error: ' + res.asyncOpErrorMsg);
  }
  res.identity.store().then(function() {
    _logData('Identity store success.');
  }, function(err) {
    _logData('Identity store fail.');
  });
}

function startSession() {
  var identobj = tizen.sso.authService.getIdentityByJSId(
    res.identity.jsid);
  if (identobj == null) {
    _logData('identity NOT selected/found. Please select/create an identity first');
    return;
  }
  _logData('identity found with JSId: ' + identobj.jsid);
  var method = "username";
  
  var ses = identobj.startSession(method);
  if (ses != null) {
    ses.then(onStartSessionComplete,
      function(err) {_logData('startSession failed: ' + err);});
  } else {
    _logData('Session cannot be started');
  }
}

function onStartSessionComplete(sessionobj) {
  _logData('startSession successful: ' + JSON.stringify(sessionobj));
  sessionobj.addEventListener('statechanged', onSessionStateChanged);

  _logData('Session with jsid as ' + sessionobj.jsid + ' is added for identity with jsid '
     + sessionobj.identityJSId);
}

function _logData(info) {
  $("#message").html(info);
}


