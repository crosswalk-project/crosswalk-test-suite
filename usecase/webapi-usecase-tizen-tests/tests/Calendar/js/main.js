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


var calendar;
var cal_text;

// Defines the error callback for all the asynchronous calls.
function errorCallback(response) {
  cal_text.text('The following error occurred: ' +  response.name);
}

function addEventsSuccess(events) {
  cal_text.text('Successfully added ' + events.length + ' events!');
}

// Defines the success callback.
function updateEventsSuccess() {
  cal_text.text('Successfully updated!' + events.length + ' results found.');
}

// Defines the removeBatch callback.
function removeBatchCallback() {
  cal_text.text('Requested events were successfully removed.');
}

// Defines the event success callback.
function eventSearchSuccessCallback1(events) {
  events[0].description = 'New Description';
  // Updates the first existing event.
  calendar.update(events[0]);
  cal_text.text('The first item description was updated!');
}

function eventSearchSuccessCallback2(events) {
  events[0].description = 'New Description1';
  events[1].description = 'New Description 2';
  // Update the first two existing events.
  calendar.updateBatch(events.slice(0,2), updateEventsSuccess, errorCallback);
}

function eventSearchSuccessCallback3(events) {
  events[0].description = 'New Description';
  // Deletes the first existing event.
  calendar.remove(events[0].id);
  cal_text.text('The first event was removed');
}

function eventSearchSuccessCallback4(events) {
  // Deletes the first two existing events.
  calendar.removeBatch([events[0].id, events[1].id],  removeBatchCallback,  errorCallback);
}

function eventSearchSuccessCallback5(events) {
  cal_text.text(events.length + ' results found.');
}


$(document).ready(function() {
  cal_text = $('#calendar_text');
  if(JSON.stringify(tizen.calendar) == undefined){
    document.write('The tizen.calendar is ' + JSON.stringify(tizen.calendar));
  }else{
    // Gets a list of available calendars.
    calendar = tizen.calendar.getDefaultCalendar("EVENT");

    var ev = new tizen.CalendarEvent({description:'HTML5 Introduction',
                                      summary:'HTML5 Webinar', 
                                      startDate: new tizen.TZDate(2011, 3, 30, 10, 0), 
                                      duration: new tizen.TimeDuration(1, "HOURS"),
                                      ocation:'Huesca'});

    var html5seminar = new tizen.CalendarEvent({startDate: new tizen.TZDate(2012, 3, 4),
                                                duration: new tizen.TimeDuration(3, "DAYS"),
                                                summary: "HTML5 Seminar"});

    // Finds all events the calendar that contain in the summary the string Tizen.
    var filter = new tizen.AttributeFilter('summary', 'CONTAINS', 'Tizen');

    // The events returned by the find() query will be sorted by ascending summary.
    var sortingMode = new tizen.SortMode('summary', 'ASC');

    $('#btn_add').click(function() {
      calendar.add(ev);
      cal_text.text('Event added with uid ' + ev.id.uid);
    });
    $('#btn_addBatch').click(function() {
      calendar.addBatch([ev], addEventsSuccess, errorCallback);
    });
    $('#btn_update').click(function() {
      calendar.find(eventSearchSuccessCallback1, errorCallback);
    });
    $('#btn_updateBatch').click(function() {
      calendar.find(eventSearchSuccessCallback2, errorCallback);
    });
    $('#btn_remove').click(function() {
      calendar.find(eventSearchSuccessCallback3, errorCallback);
    });
    $('#btn_removeBatch').click(function() {
      calendar.find(eventSearchSuccessCallback4, errorCallback);
    });
    $('#btn_find').click(function() {
      calendar.find(eventSearchSuccessCallback5, errorCallback, filter, sortingMode);
    });
    $('#btn_clone').click(function() {
      calendar.add(html5seminar);
      var tizenseminar = html5seminar.clone();
      tizenseminar.summary = "Tizen Seminar";
      calendar.add(tizenseminar);
      cal_text.text('Event added with uid ' + tizenseminar.id.uid);
    });
  }
})
