/*
Copyright (c) 2014 Intel Corporation.

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
        Huang, Min <minx.huang@intel.com>

*/



function _logData(data) {
  var old = document.form_out.form_text.value;
  document.form_out.form_text.value = data + '\n\n' + old;
}

function queryMethods() {
  tizen.sso.authService.queryMethods().then(function(result) {
    _logData('QueryMethods successful: ' + JSON.stringify(result));},
    function (err) { document.form_out.form_text.value += "\n" + "QueryMethods failed: " + err;});
}

function queryMechanisms() {
  var method = document.getElementById('serv_method').value;
  tizen.sso.authService.queryMechanisms(method).then(function (result) {
    _logData('QueryMechanisms successful: ' + JSON.stringify(result));},
    function(err) {_logData('QueryMechanisms failed: ' + err);});
}

function queryIdentities() {
  var str = document.getElementById('serv_filter').value;
  var filters = {};
  if (typeof str === 'string' && str.length > 0) {
    var ufilter = str.split(",");
    for (var i = 0; i < ufilter.length; i++) {
      var keyval = ufilter[i].split(":");
      filters[keyval[0]] = keyval[1];
    }
  }
  tizen.sso.authService.queryIdentities(filters).then(onQueryIdentitiesComplete, function(err) {
    _logData('QueryIdentities failed: ' + err);});
}

function onQueryIdentitiesComplete(result) {
  _logData('QueryIdentities successful: ' + JSON.stringify(result));
}

function getIdentity() {
  var id = parseFloat(document.getElementById('serv_identityid').value);
  if (id == NaN) {
    _logData('Invalid id');
    return;
  }
  var res = tizen.sso.authService.getIdentity(id);
  if (res != null)
    res.then(onGetIdentityComplete, function(err) {
        _logData('GetIdentity failed: ' + err);});
  else
    _logData('Identity not found with the specified id');
}

function onGetIdentityComplete(result) {
  _logData('GetIdentity successful: ' + JSON.stringify(result));
}

function clearDB() {
  tizen.sso.authService.clear().then(function(result) {
    _logData('Clear successful: ' + JSON.stringify(result));
    clearSelect(document.getElementById("ident_options"));
    clearSelect(document.getElementById("sess_options"));},
    function(err) {_logData('Clear failed: ' + err);});
}

function getInfo() {
  var owner = {};
  var str = document.getElementById('cident_owner').value;
  if (typeof str === 'string' && str.length > 0) {
    arr = str.split(",");
    if (arr.length == 2) {
      owner.sysContext = arr[0];
      owner.appContext = arr[1];
    }
  }
  var realms = [];
  str = document.getElementById('cident_realms').value;
  if (typeof str === 'string' && str.length > 0) {
    arr = str.split(",");
    if (arr.length > 0) realms = arr;
  }
  var acl = [{}];
  str = document.getElementById('cident_acl').value;
  if (typeof str === 'string' && str.length > 0) {
    acl = JSON.parse(str);
  }
  var info = {
    'type': document.getElementById('cident_type').value,
    'username': document.getElementById('cident_username').value,
    'secret': document.getElementById('cident_secret').value,
    'storeSecret': document.getElementById('cident_storesecret').checked,
    'caption': document.getElementById('cident_caption').value,
    'realms': realms,
    'owner': owner,
    'accessControlList': acl
  };
  return info;
}

function onCreateIdentity() {
  var info = getInfo();
  var res = tizen.sso.authService.createIdentity(info);
  if (res.syncOpErrorMsg != null) {
    _logData('Identity creation FAILED with error: ' + res.asyncOpErrorMsg);
    return;
  }
  
  identityAdded(res.identity);
  _logData('Identity is added with jsid: ' + res.identity.jsid);
}

function onUpdateIdentity() {
  var info = getInfo();
  store(info);
}

function identityAdded(ident) {
  var select = document.getElementById("ident_options");
  var option = document.createElement('option');
  option.text = option.value = ident.jsid;
  select.add(option, 0);

  ident.onsignedout = function (ident) {
    _logData('Identity with id ' + ident.info.id + ' is signedout and jsid is ' + ident.jsid);};
  ident.onremoved = onIdentityRemoved;
}

function onIdentityRemoved(ident) {
  _logData('Identity with id ' + ident.info.id + ' is removed and its jsid is ' + ident.jsid);
  if (document.getElementById('ident_options').value == ident.jsid) {
    for (var i = 0; i < ident.sessions.length; i++) {
      var sessionobj = ident.sessions[i];
      sessionobj.removeEventListener('statechanged', onSessionStateChanged);
      document.getElementById('sess_options').remove(i);
    }
    clearSelectOption(document.getElementById("ident_options"), ident.jsid);
  }
}

function clearSelectOption(element, value) {
  for (var i=0; i<element.length; i++) {
    if (element.options[i].value == value)
       element.remove(i);
  }
}

function clearSelect(element) {
  for (var i=0; i<element.length; i++) {
    element.remove(i);
  }
}

function onIdentityChanged(select) {
  var jsid = document.getElementById("ident_options").value;
  _logData('Identity selected with jsid: ' + jsid);
  var identobj = tizen.sso.authService.getIdentityByJSId(jsid);
  if (identobj == null) {
    _logData('identity NOT found');
    return;
  }
  clearSelect(document.getElementById("sess_options"));
  for (var i = 0; i < identobj.sessions.length; i++) {
    var option = document.createElement('option');
    option.text = option.value = identobj.sessions[i].jsid;
    document.getElementById('sess_options').add(option, 0);
  }
}

//identity interface
function startSession() {
  var identobj = tizen.sso.authService.getIdentityByJSId(
    document.getElementById('ident_options').value);
  if (identobj == null) {
    _logData('identity NOT selected/found. Please select/create an identity first');
    return;
  }
  _logData('identity found with JSId: ' + identobj.jsid);
  var method = document.getElementById('ident_method').value;
  
  identobj.startSession(method).then(onStartSessionComplete,
    function(err) {_logData('startSession failed: ' + err);});
}

function onStartSessionComplete(sessionobj) {
  _logData('startSession successful: ' + JSON.stringify(sessionobj));
  sessionobj.addEventListener('statechanged', onSessionStateChanged);

  _logData('Session with jsid as ' + sessionobj.jsid + ' is added for identity with jsid ' + sessionobj.identityJSId);
  var select = document.getElementById("ident_options");
  if (select.value == sessionobj.identityJSId) {
    var sess_select = document.getElementById("sess_options");
    var option = document.createElement('option');
    option.text = option.value = sessionobj.jsid;
    sess_select.add(option, 0);
  }
}

function onSessionStateChanged(event) {
  var sessionobj = event.session;
  _logData('Session with jsid ' + sessionobj.jsid + ' state has changed to ' + sessionobj.sessionState);
}

function requestCredentialsUpdate() {
  var identobj = tizen.sso.authService.getIdentityByJSId(
    document.getElementById('ident_options').value);
  if (identobj == null) {
    _logData('identity NOT selected/found. Please select/create an identity first');
    return;
  }
  _logData('identity found with JSId: ' + identobj.jsid);
  var message = document.getElementById('ident_message').value;
  
  identobj.requestCredentialsUpdate(message).then(function(msg) {
    document.form_out.form_text.value += "\n" + "requestCredentialsUpdate succeeded";},
    function(err) {_logData('requestCredentialsUpdate failed: ' + err);});
}

function store(info) {
  var identobj = tizen.sso.authService.getIdentityByJSId(
    document.getElementById('ident_options').value);
  if (identobj == null) {
    _logData('identity NOT selected/found. Please select/create an identity first');
    return;
  }
  _logData('identity found with JSId: ' + identobj.jsid);
  if (info != null) identobj.updateInfo(info);

  identobj.store().then(function(msg) {
    _logData('store succeeded with resp: ' + JSON.stringify(msg));},
    function(err) {_logData('store failed: ' + err);});
}

function addReference() {
  var identobj = tizen.sso.authService.getIdentityByJSId(
    document.getElementById('ident_options').value);
  if (identobj == null) {
    _logData('identity NOT selected/found. Please select/create an identity first');
    return;
  }
  _logData('identity found with JSId: ' + identobj.jsid);
  var reference = document.getElementById('ident_addref').value;
  
  identobj.addReference(reference).then(function(msg) {
    _logData('addReference succeeded');},
    function(err) {_logData('addReference failed: ' + err);});
}

function removeReference() {
  var identobj = tizen.sso.authService.getIdentityByJSId(
    document.getElementById('ident_options').value);
  if (identobj == null) {
    _logData('identity NOT selected/found. Please select/create an identity first');
    return;
  }
  _logData('identity found with JSId: ' + identobj.jsid);
  var reference = document.getElementById('ident_remref').value;
  
  identobj.removeReference(reference).then(function(msg) {
    _logData('removeReference succeeded');},
    function(err) {_logData('removeReference failed: ' + err);});
}

function removeIdentity() {
  var identobj = tizen.sso.authService.getIdentityByJSId(
    document.getElementById('ident_options').value);
  if (identobj == null) {
    _logData('identity NOT selected/found. Please select/create an identity first');
    return;
  }
  _logData('identity found with JSId: ' + identobj.jsid);
  identobj.remove().then(onIdentityRemoved,
    function(err) {_logData('remove failed: ' + err);});
}

function signout() {
  var identobj = tizen.sso.authService.getIdentityByJSId(
    document.getElementById('ident_options').value);
  if (identobj == null) {
    _logData('identity NOT selected/found. Please select/create an identity first');
    return;
  }
  _logData('identity found with JSId: ' + identobj.jsid);
  identobj.signout().then(function(msg) {
    _logData('signout succeeded');},
    function(err) {_logData('signout failed: ' + err);});
}

//authsession interface
function queryAvailableMechanisms() {
  var identobj = tizen.sso.authService.getIdentityByJSId(
    document.getElementById('ident_options').value);
  if (identobj == null) {
    _logData('identity NOT selected/found. Please select/create an identity first');
    return;
  }
  _logData('identity found with JSId: ' + identobj.jsid);
  var sessionobj = identobj.getSessionByJSId(
    document.getElementById('sess_options').value);
  if (sessionobj == null) {
    _logData('session NOT selected/found. Please select/create session first');
    return;
  }
  _logData('session found with JSId: ' + sessionobj.jsid);

  var str = document.getElementById('sess_mechs').value;
  var wantedMechs = [];
  if (typeof str === 'string' && str.length > 0) {
      arr = str.split(",");
      if (arr.length > 0) wantedMechs = arr;
  }
  sessionobj.queryAvailableMechanisms(wantedMechs).then(function(msg) {
    _logData('queryAvailableMechanisms succeeded with mechanisms:' + JSON.stringify(msg));},
    function(err) {_logData('queryAvailableMechanisms failed: ' + err);});
}

function challenge() {
  var identobj = tizen.sso.authService.getIdentityByJSId(
    document.getElementById('ident_options').value);
  if (identobj == null) {
    _logData('identity NOT selected/found. Please select/create an identity first');
    return;
  }
  _logData('identity found with JSId: ' + identobj.jsid);
  var sessionobj = identobj.getSessionByJSId(document.getElementById('sess_options').value);
  if (sessionobj == null) {
    _logData('session NOT selected/found. Please select/create session first');
    return;
  }
  _logData('session found with JSId: ' + sessionobj.jsid);

  var mech = document.getElementById('sess_mech').value;
  var sessionData = document.getElementById('sess_data').value;
  
  sessionobj.challenge(mech, sessionData).then(function(msg) {
    _logData('challenge succeeded with sessionData: ' + JSON.stringify(msg));},
    function(err) {_logData('challenge failed: ' + err);});
}

function cancel() {
  var identobj = tizen.sso.authService.getIdentityByJSId(
    document.getElementById('ident_options').value);
  if (identobj == null) {
    _logData('identity NOT selected/found. Please select/create an identity first');
    return;
  }
  _logData('identity found with JSId: ' + identobj.jsid);
  var sessionobj = identobj.getSessionByJSId(document.getElementById('sess_options').value);
  if (sessionobj == null) {
    _logData('session NOT selected/found. Please select/create session first');
    return;
  }
  _logData('session found with JSId: ' + sessionobj.jsid);

  sessionobj.removeEventListener('statechanged', onSessionStateChanged);
  sessionobj.cancel().then(function(msg) {
    _logData('cancel succeeded');},
    function(err) {_logData('cancel failed: ' + err);});
  clearSelectOption(document.getElementById('sess_options'), sessionobj.jsid);
}

window.onload = function() {
  t = $('#resultContainer').offset().top;
  mh = $('#content').height();
  fh = $('#resultContainer').height();
  $(window).scroll(function(e){
    s = $(document).scrollTop();	
	if(s > t - 10){
	  $('#resultContainer').css('position','fixed');
	  if(s + fh > mh){
        $('.fixed').css('top',mh-s-fh+'px');
      }
    }else{
      $('#resultContainer').css('position','');
	}
  })
  document.getElementById('cident_acl').value = JSON.stringify([{"secContext":{"sysContext":"*","appContext":"*"},"method":"password","mechanisms":["password"]}]);
  document.getElementById('cident_owner').value = "*,*";
};

