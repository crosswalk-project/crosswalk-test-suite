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
*/

var p2ps = {};

var ul = null;
var connectioninfo = null;
var statusLabel = null;
var statusString = "available";

var Error = function(error) {
  document.title = "Fail - " + error.message;
  console.log(error.message);
}

function refreshPeers(wd) {
  wd.getPeers().then(function(peers) {
    refreshPeersDisplay(wd, peers);
  },Error);
};

function init(wd) {
  wd.init().then(function() {
    wd.discoverPeers().then(function() {
      refreshPeers(wd);
    },Error);
  }, Error);
};

function getDisconnectButton(parent) {
  var buddy = parent['buddy'];
  if (!buddy) {
    buddy = document.createElement("button");
    buddy.style.marginLeft = "20px";
    parent.appendChild(buddy);
    parent['buddy'] = buddy;
  }
  buddy.visible = true;
  return buddy;
}

function showDisconnectButton(wd, parent, status) {
  if (status === "invited") {
    var buddy = getDisconnectButton(parent);
    buddy.onclick = function() {
      wd.cancelConnect();
    };
    buddy.innerHTML = "Cancel invite";
  } else if(status === "connected") {
    var buddy = getDisconnectButton(parent);
    buddy.onclick = function() {
      wd.disconnect();
    };
    buddy.innerHTML = "Disconnect";
  } else if (buddy) {
    buddy.visible = false;
  }
}

function refreshPeersDisplay(wd, peers) {
  while (ul.children.length > peers.length) {
    ul.removeChild(ul.children[ul.children.length - 1]);
  }
  
  while (ul.children.length < peers.length) {
    var li = document.createElement("li");
    var div = document.createElement("div");
    var btn_pbc = document.createElement("button");
    div.appendChild(btn_pbc);
    div.appendChild(document.createElement("label"));
    li.appendChild(div);
    ul.appendChild(li);
  }
  
  p2ps = peers;
    
  for (var i = 0; i < p2ps.length; ++i) {
    var peer = p2ps[i];
    var button = ul.children[i].children[0].children[0];
    button.id = peer.MAC;
    button.innerHTML = peer.name + " : " + peer.status;
    
    showDisconnectButton(wd, button.parentNode, peer.status);
    button.onclick = (function (peer, button) {
      return function() {
        button.disabled = true;
        wd.connect(peer).then(function() {
          button.innerHTML = peer.name + " : " + "connecting";
          button.disabled = false;
        }, function(error) {
          button.disabled = false;
          button.innerHTML = peer.name + " : " + error.message;
        });
      };
    })(peer, button);
  }
}

window.onload = function() {
  try {
    ul = document.createElement("ul");
    ul.id = "peerslist";
    document.body.appendChild(ul);
    var info = document.createElement("h4");
    info.innerHTML = "State:";
    document.body.appendChild(info);
    connectioninfo = document.createElement("div");
    connectioninfo.id = "connectioninfo";
    statusLabel = document.createElement("div");
    statusLabel.appendChild(document.createElement("label"));
    connectioninfo.appendChild(document.createElement("label"));
    document.body.appendChild(connectioninfo);
    document.body.appendChild(statusLabel);

    var wd = navigator.wifidirect || xwalk.experimental.wifidirect;
    init(wd);
    
    wd.onpeerschanged = function(ev) {
      refreshPeers(wd);
    };
    
    wd.onwifistatechanged = function(ev) {
      if (!ev.enabled)
        init(wd);
    };
    
    wd.onconnectionchanged = function(ev) {
      wd.getConnectionInfo().then(function(data) {
        displayConnectionInfo(data);
      },Error);
    };

    wd.onthisdevicechanged = function(ev) {
      var formerStatusString = statusString;
      statusString = ev.status;
      statusLabel.innerHTML = statusString;
      if (statusString !== formerStatusString && statusString === "available") {
        // only in this example, in other example it would happen 
        // after e.g. TCP connection is lost on user action
        wd.discoverPeers().then(function() {
          refreshPeers(wd);
        },Error);
      }        
    };
    
    wd.ondiscoverystopped = function(ev) {
      // restart discovery when it stopped in this example
      wd.discoverPeers().then(function() {
        refreshPeers(wd);
      },Error);
    };
  } catch(e) {
    console.log(e);
  }
};

function displayConnectionInfo(data) {
  if (data) {
    connectioninfo.innerHTML = data.groupFormed
      ? ("connected as " + (data.isServer ? "group server." 
                                          : ("client - server IP is " + data.serverIP)))
      : "disconnected" ; 
  }
}
