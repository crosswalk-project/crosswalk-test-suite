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
        Liu, yun <yunx.liu@intel.com>

*/

var telephony = tizen.telephony;
var output = document.getElementById("consolelog");

function onError(error, text) {
  var t, en, em;
  if (error) {
    en = ':' + error.name;
    em = ';' + error.message;
  } else {
    em = en = '';
  }
  if (text)
    t = '[' + text + ']';
  else
    t = null;
  print('Error' + t + en + em);
  return null;
}

function print(message) {
  $("#consolelog").html("<p>" + message + "</p>" + $("#consolelog").html());
}

function printVal(thing, depth) {
  var out, key;
  if (thing instanceof Function) {
    out += '{}';
  } else if (thing instanceof Array) {
    out = '[ ';
  for (key in thing)
    out += printVal(thing[key], depth + 1) + ', ';
    out += ']';
  } else if (thing instanceof Object) {
    var tabs = '';
    for (var i = 0; i < depth; i++)
      tabs += '\t';
    out = '\n' + tabs + '{';
    for (key in thing) {
      if (!(thing[key] instanceof Function))
        out += '\n' + tabs + '\t' + key + ': ' +
      printVal(thing[key], depth + 1);
    }
    out += '\n' + tabs + '}';
  } else {
    out = thing;
  }
  return out;
}

function displayEntryList(array) {
  $("#consolelog").html("<p>List count = " + array.length + "; " + printVal(array, 0) + "</p>" + $("#consolelog").html());
}

function readStringField(name) {
  var input = document.getElementById(name);
  if (input)
    return input.value || null;
  return onError(null, "Invalid " + name + ": " + id);
}

function getServiceIds() {
  print("Getting telephony service id's...");
  tizen.telephony.getServiceIds().then(
  function(list) {
    displayEntryList(list);
  },
  function(err) {
    onError(err, 'getServiceIds');
  });
}

function readService() {
  var id = readStringField('service_id_input');
  var s = tizen.telephony.getService(id);
  if (!s)
    return onError(null, "No service for id: " + id);
  return s;
}

function setDefaultService() {
  var id = readStringField('service_id_input');
  tizen.telephony.setDefaultServiceId(id).then(
  function() {
    print('Default telephony service id set to ' + id);
  },
  function(err) {
    onError(err, 'setDefaultService');
  });
}

function getDefaultService() {
  print("Default service id: " + tizen.telephony.defaultServiceId);
}

function getService() {
  var service = readService();
  if (service)
    print('service[' + id + ']: ' + printVal(service));
}

function enableService() {
  var service = readService();
  if (service) {
    service.setEnabled(true).then(
    function() {
      print('Enabled service id ' + service.serviceId);
    },
    function(err) {
      onError(err, 'enableService');
    });
  }
}

function disableService() {
  var service = readService();
  if (service) {
    service.setEnabled(false).then(
    function() {
      print('Disabled service id ' + service.serviceId);
    },
    function(err) {
      onError(err, 'disableService');
    });
  }
}

function onServiceAdded(evt) {
  print("onServiceAdded: " + printVal(evt.service));
}

function onServiceRemoved(evt) {
  print("onServiceRemoved: " + printVal(evt.service));
}

function onDefaultServiceChanged(evt) {
  print("onDefaultServiceChanged: " + printVal(evt.service));
}

function onCallAdded(evt) {
  print("onCallAdded: " + printVal(evt.call));
}

function onCallRemoved(evt) {
  print("onCallRemoved: " + printVal(evt.call));
}

function onActiveCallChanged(evt) {
  print("onActiveCallChanged to: " + evt.call ? evt.call.callId : "null");
}

function onCallStateChanged(evt) {
  print("onCallStateChanged: " + printVal(evt.call));
}

function addServiceListeners() {
  if (!telephony) {
    return onError(null, "telephony not supported");
  }
  tizen.telephony.addEventListener('serviceadded', onServiceAdded, false);
  tizen.telephony.addEventListener('serviceremoved', onServiceRemoved, false);
  tizen.telephony.addEventListener('defaultservicechanged', onDefaultServiceChanged, false);
  print("Event listeners added for 'serviceadded', 'serviceremoved', 'defaultservicechanged'.");
}

function removeServiceListeners() {
  if (!telephony) {
    return onError(null, "telephony not supported");
  }
  tizen.telephony.removeEventListener('serviceadded', onServiceAdded, false);
  tizen.telephony.removeEventListener('serviceremoved', onServiceRemoved, false);
  tizen.telephony.removeEventListener('defaultservicechanged', onDefaultServiceChanged, false);
  print("Event listeners removed for 'serviceadded', 'serviceremoved', 'defaultservicechanged'.");
}

function addCallListeners() {
  if (!telephony) {
    return onError(null, "telephony not supported");
  }
  tizen.telephony.addEventListener('calladded', onCallAdded, false);
  tizen.telephony.addEventListener('callremoved', onCallRemoved, false);
  tizen.telephony.addEventListener('activecallchanged', onActiveCallChanged, false);
  tizen.telephony.addEventListener('callstatechanged', onCallStateChanged, false);
  print("Event listeners added for 'calladded', 'callremoved', 'activecallchanged', 'callstatechanged'.");
}

function removeCallListeners() {
  if (!telephony) {
    return onError(null, "telephony not supported");
  }
  tizen.telephony.removeEventListener('calladded', onCallAdded, false);
  tizen.telephony.removeEventListener('callremoved', onCallRemoved, false);
  tizen.telephony.removeEventListener('activecallchanged', onActiveCallChanged, false);
  tizen.telephony.removeEventListener('callstatechanged', onCallStateChanged, false);
  print("Event listeners added for 'calladded', 'callremoved', 'activecallchanged', 'callstatechanged'.");
}

function getActiveCall() {
  var ac = tizen.telephony.activeCall;
  if (!ac)
    print("No active call");
  else
    print("Active call: " + printVal(ac));
}

function getCalls() {
  print('Getting telephony calls...');
  tizen.telephony.getCalls().then(
  function(list) {
    displayEntryList(list);
  },
  function(err) {
    onError(err, 'getCalls');
  });
}

function hangupAllCalls() {
  print("Disconnecting all calls...");
  tizen.telephony.getCalls().then(
  function(list) {
    var found = false;
    list.forEach(function(call) {
      if (call.state == 'held' || call.state == 'active') {
        found = true;
        call.disconnect().then(
        function(){
          print("Call " + call.callId + " disconnected.");
        },
        function(err) {
          onError(err, 'disconnect');
        });
      }
    });
    if (!found)
      print('No calls.');
  },
  function(err) {
    onError(err, 'getCalls');
  });
}

function createConference() {
  print("Creating conference call...");
  if (!tizen.telephony.activeCall) {
    print("No active call.");
    return;
  }
  tizen.telephony.createConference().then(
  function(confCall) {
    print('Conference call created: ' + printVal(confCall));
  },
  function(err) {
    onError(err, 'createConference');
  });
}

function getParticipants() {
  print("Getting participants of active conference call...");
  var ac = tizen.telephony.activeCall;
  if (!ac) {
    print("No active call.");
  } else if (!ac.conferenceId) {
    print("Active call not a conference. Remote party: " + ac.remoteParty);
    return;
  }
  tizen.telephony.getParticipants(id).then(
  function(list) {
    print('Conference participant calls: ');
    displayEntryList(list);
  },
  function(err) {
    onError(err, 'getParticipants');
  });
}

function split() {
  var id = readStringField('split_input');
  print("Splitting call id " + id + ' from its conference call');
  tizen.telephony.split(id).then(
  function() {
    print('Call id ' + id + ' split from conference and activated');
  },
  function(err) {
    onError(err, 'split');
  });
}

function dial() {
  var number = readStringField('dial_input');
  if (number) {
    print('Dialing ' + number);
    tizen.telephony.dial(number).then(
    function() {
      print('Dialing ' + number + ' successful.');
    },
    function(err) {
      onError(err, 'dial');
    });
  }
}

function accept() {
  print("Accepting incoming/waiting call...");
  tizen.telephony.getCalls().then(
  function(list) {
    var found = false;
    list.forEach(function(call) {
      if (call.state == 'incoming' || call.state == 'waiting') {
        var state = call.state;
        found = true;
        call.accept().then(
        function(){
          print("Accepted " + state + " call: ");
          print(call);
        },
        function(err) {
          onError(err, 'accept');
        });
      }
    });
    if (!found)
      print("No incoming or waiting calls")
  },
  function(err) {
    onError(err, 'getCalls');
  });
}

function disconnect() {
  print("Disconnecting active call...");
  if (!tizen.telephony.activeCall) {
    print("No active calls");
    return;
  }
  var id = tizen.telephony.activeCall.callId;
  tizen.telephony.activeCall.disconnect().then(
  function() {
    print('Disconnected call id ' + id);
  },
  function(err) {
    onError(err, 'disconnect');
  });
}

function hold() {
  print("Holding active call...");
  if (!tizen.telephony.activeCall) {
    print("No active calls");
    return;
  }
  var call = tizen.telephony.activeCall;
  call.hold().then(
  function() {
    print('Held call id ' + call.callId);
  },
  function(err) {
    onError(err, 'hold');
  });
}

function resume() {
  print("Resuming held call...");
  tizen.telephony.getCalls().then(
  function(list) {
    var found = false;
    list.forEach(function(call) {
      if (call.state == 'held') {
        found = true;
        call.resume().then(
        function(){
          print("Resumed call: " + call.callId);
        },
        function(err) {
          onError(err, 'resume');
        });
      }
    });
    if (!found)
      print("No held calls")
  },
  function(err) {
    onError(err, 'getCalls');
  });
}

function deflect() {
  print("Deflecting incoming/waiting call...");
  var number = readStringField('deflect_input');
  if (!number)
    return;
  tizen.telephony.getCalls().then(
  function(list) {
    var found = false;
    list.forEach(function(call) {
      if (call.state == 'incoming' || call.state == 'waiting') {
        var state = call.state;
        found = true;
        call.deflect(number).then(
        function(){
          print("Deflected " + state + " call: " + call.callId);
        },
        function(err) {
          onError(err, 'deflect');
        });
      }
    });
    if (!found)
      print("No incoming or waiting calls")
  },
  function(err) {
    onError(err, 'getCalls');
  });
}

function transfer() {
  print("Transfer: joining the active and held calls, then disconnect...");
  if (!tizen.telephony.activeCall) {
    print("No active call");
    return;
  }
  // not checking the held calls now, the system will signal error anyway
  tizen.telephony.transfer().then(
  function(){
    print("Transferred " + state + " call: " + call.callId);
  },
  function(err) {
    onError(err, 'transfer');
  });
}

function sendTones() {
  var tones = readStringField('tones_input');
  if (!tones)
    return;
  tizen.telephony.sendTones(tones).then(
  function() {
    print('Tones sent: ' + tones);
  },
  function(err) {
    onError(err, 'sendTones');
  });
}

function startTone() {
  var tones = readStringField('tones_input');
  if (!tones)
    return;
  tizen.telephony.startTone(tones).then(
  function() {
    print('Tone started: ' + tones);
  },
  function(err) {
    onError(err, 'startTone');
  });
}

function stopTone() {
  var tones = readStringField('tones_input');
  if (!tones)
    return;
  tizen.telephony.stopTone(tones).then(
  function() {
    print('Tone stopped: ' + tones);
  },
  function(err) {
    onError(err, 'stopTone');
  });
}

function getEmergencyNumbers() {
  tizen.telephony.getEmergencyNumbers().then(
  function(list) {
    print('Emergency number list: ');
    displayEntryList(list);
  },
  function(err) {
    onError(err, 'getEmergencyNumbers');
  });
}

function clearConsole() {
  $("#consolelog").html("");
}

$(document).ready(function() {
  $("#consolelog").html("");
  $("#add_service_listener_btn").click(addServiceListeners);
  $("#add_call_listeners_btn").click(addCallListeners);
  $("#services_btn").click(getServiceIds);
  $("#get_dservice_btn").click(getDefaultService);
  $("#active_call_btn").click(getActiveCall);
  $("#get_calls_btn").click(getCalls);
  $("#dial_btn").click(dial);
  $("#conf_btn").click(createConference);
  $("#conf_parties_btn").click(getParticipants);
  $("#split_btn").click(split);
  $("#disconnect_btn").click(disconnect);
  $("#disconnect_all_btn").click(hangupAllCalls);
  $("#hold_btn").click(hold);
  $("#resume_btn").click(resume);
  $("#accept_btn").click(accept);
  $("#deflect_btn").click(deflect);
  $("#transfer_btn").click(transfer);
  $("#emerg_nr_btn").click(getEmergencyNumbers);
  $("#remove_call_listeners_btn").click(removeCallListeners);
  $("#remove_service_listeners_btn").click(removeServiceListeners);
  $("#sendtones_btn").click(sendTones);
  $("#starttone_btn").click(startTone);
  $("#endtone_btn").click(stopTone);
  $("#get_service_btn").click(getService);
  $("#set_dservice_btn").click(setDefaultService);
  $("#enable_service_btn").click(enableService);
  $("#disable_service_btn").click(disableService);
  $("#clearconsole_btn").click(clearConsole);
});
