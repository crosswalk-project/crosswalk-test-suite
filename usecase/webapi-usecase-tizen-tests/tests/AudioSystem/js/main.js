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
        Xu, Jianfeng <jianfengx.xu@intel.com>

*/

var audiosystem = tizen.audiosystem;
var context = null;

function dumpVolumeControl(vc) {
  var table = document.getElementById('volume_controls_table');
  var row, cell;

  row = table.insertRow(table.rows.length);
  row.id = vc.id;

  cell = row.insertCell(0);
  cell.innerHTML = vc.id;

  cell = row.insertCell(1);
  cell.innerHTML = vc.label;
  
  var select = document.createElement('select');
  select.id = vc.id;
  select.onchange = function () {
    try  {
    console.log("Setting Volume : " + typeof select.value);
    vc.set_volume(parseFloat(select.value), function() {
      console.log("set_volume: SUCCES");
    }, function() {
      console.log("set_volume: FAILED");
    });
    } catch(exp) {
      console.log("EXception : " + exp.name);
    }
  };
  for (var i = 0.0; i < 1.0; i+= 0.1) {
    var opt = document.createElement('option');
    opt.value = i.toFixed(1);
    opt.innerHTML = i.toFixed(1);
    if (i.toFixed(1) === vc.volume.toFixed(1)) {
      opt.selected = true;
    }
    select.add(opt);
  }

  vc.onvolumechanged = function(ev) {
    select.value = vc.volume.toFixed(1);
  };
 
  cell = row.insertCell(2);
  cell.appendChild(select);

  var p_table = document.createElement('table');
  var b_table = document.createElement('table');
  for (var i = 0; i < vc.balance.length; i++) {
    var b = vc.balance[i];
    var tr = p_table.insertRow();
    tr.innerHTML = '<td>' + b.label;

    tr = b_table.insertRow();
    tr.innerHTML = '<td>' + b.balance;
  }

  cell = row.insertCell(3);
  cell.appendChild(p_table);
  cell = row.insertCell(4);
  cell.appendChild(b_table);

  cell = row.insertCell(5);
  cell.innerHTML = (context.main_output_volume_control && 
                    vc.id == context.main_output_volume_control.id) ? 'Yes' : '';

  cell = row.insertCell(6);
  cell.innerHTML = (context.main_input_volume_control &&
                    vc.id == context.main_input_volume_control.id) ? 'Yes' : '';
}

function dumpAudioGroup(ag) {
  var table = document.getElementById('audio_groups_table');

  var row = table.insertRow(table.rows.length);
  row.id = ag.id;
  var cell;

  cell = row.insertCell(0);
  cell.innerHTML = ag.id;

  cell = row.insertCell(1);
  cell.innerHTML = ag.label;

  cell = row.insertCell(2);
  cell.innerHTML = ag.volume_control ? ag.volume_control.label : '[NONE]';
}

function dumpAudioStream(as) {
  var table = document.getElementById('audio_streams_table');

  var row = table.insertRow(table.rows.length);
  row.id = as.id;
  var cell;

  cell = row.insertCell(0);
  cell.innerHTML = as.id;

  cell = row.insertCell(1);
  cell.innerHTML = as.label;

  cell = row.insertCell(2);
  cell.innerHTML = as.volume_control ? as.volume_control.label : '[NONE]';
}

function dumpAudioDevice(ad) {
  var table = document.getElementById('audio_devices_table');

  var row = table.insertRow(table.rows.length);
  row.id = ad.id;
  var cell;

  cell = row.insertCell(0);
  cell.innerHTML = ad.id;

  cell = row.insertCell(1);
  cell.innerHTML = ad.label;

  cell = row.insertCell(2);
  cell.innerHTML = ad.direction;

  cell = row.insertCell(3);
  cell.innerHTML = ad.device_types;

  cell = row.insertCell(4);
  cell.innerHTML = ad.volume_control ? ad.volume_control.label : '[NONE]';
}

function removeRowById(table_id, id) {
  var table = document.getElementById(table_id);

  for (i = 0; i < table.rows.length; i++) {
    if (table.rows[i].id == id)
      table.deleteRow(i);
  }
}

function showDivision(id) {
  var div = document.getElementById(id);
  div.style.display = 'block';
}

function hideDivision(id) {
  var div = document.getElementById(id);
  div.style.display = 'none';
}

function connect() {
  audiosystem.connect(function(ctx) {
    document.getElementById('connect').disabled= true;
    document.getElementById('disconnect').disabled = false;

    context = ctx;

    if (ctx.volume_controls.length > 0) {
      showDivision('volume_controls_container');
      ctx.volume_controls.forEach(function(vc) {
        dumpVolumeControl(vc);
      });
    }

    if (ctx.audio_groups.length > 0) {
      showDivision('audio_groups_container');
      ctx.audio_groups.forEach(function(ag) {
        dumpAudioGroup(ag);
      });
    }

    if (ctx.streams.length > 0) {
      showDivision('audio_streams_container');
      ctx.streams.forEach(function(as) {
        dumpAudioStream(as);
      });
    }

    if (ctx.devices.length > 0) {
      showDivision('audio_devices_container');
      ctx.devices.forEach(function(ad) {
        dumpAudioDevice(ad);
      });
    }

    ctx.onvolumecontroladded = function(ev) {
      if (ctx.volume_controls.length == 1)
        showDivision('volume_controls_container');
      dumpVolumeControl(ev.control);
    };
    ctx.onvolumecontrolremoved = function(ev) {
      removeRowById('volume_controls_table', ev.control.id);
      if (ctx.volume_controls.length == 0)
        hideDivision('volume_controls_container');
    };

    ctx.onstreamadded = function(ev) {
      if (ctx.streams.length == 1)
        showDivision('audio_streams_container');
      dumpAudioStream(ev.stream);
    };
    ctx.onstreamremoved = function(ev) {
      removeRowById('audio_streams_table', ev.stream.id);
      if (ctx.streams.length == 0)
        hideDivision('audio_streams_container');
    };

    ctx.ondeviceadded = function(ev) {
      if (ctx.devices.length == 1)
        showDivision('audio_devices_container');
      dumpAudioDevice(ev.device);
    };
    ctx.ondeviceremoved = function(ev) {
      removeRowById('audio_devices_table', ev.device.id);
      if (ctx.devices.length == 0)
        hideDivision('audio_devices_container');
    };

    ctx.onaudiogroupadded = function(ev) {
      if (ctx.audio_groups.length == 1)
        showDivision('audio_groups_container');
      dumpAudioGroup(ev.group);
    };
    ctx.onaudiogroupremoved = function(ev) {
      removeRowById('audio_groups_table', ev.group.id);
      if (ctx.audio_groups.length == 0)
        hideDivision('audio_groups_container');
    };

  }, function(err) {
    var context_container = document.getElementById('audioSystemContextContainer');
    context_container.innerHTML = "<p><b>Failed to Connect : " + err + "</b></br>";

    document.getElementById('connect').disabled = false;
    document.getElementById('disconnect').disabled = true;
  });
}

function disconnect() {
  audiosystem.disconnect();
}

audiosystem.addEventListener('disconnected', function () {
  console.log("disconnected");
  context = null;
  document.getElementById('connect').disabled = false;
  document.getElementById('disconnect').disabled = true;

  var table;

  table = document.getElementById('volume_controls_table');
  while (table.rows.length > 2) {
    table.deleteRow(table.rows.length-1);
  }
  document.getElementById('volume_controls_container').style.display = 'none';

  table = document.getElementById('audio_devices_table');
  while (table.rows.length > 1) {
    table.deleteRow(table.rows.length-1);
  }
  document.getElementById('audio_devices_container').style.display = 'none';

  table = document.getElementById('audio_groups_table');
  while (table.rows.length > 1) {
    table.deleteRow(table.rows.length-1);
  }
  document.getElementById('audio_groups_container').style.display = 'none';

  table = document.getElementById('audio_streams_table');
  while (table.rows.length > 1) {
    table.deleteRow(table.rows.length-1);
  }
  document.getElementById('audio_streams_container').style.display = 'none';
});
