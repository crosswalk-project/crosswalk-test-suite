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
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE
EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

Authors:

*/

var AlarmMethod = { "SOUND":0, "DISPLAY":1 };
var RecurrenceRuleFrequency = { "DAILY":0, "WEEKLY":1, "MONTHLY":2, "YEARLY":3 };
var DAYS = ["MO", "TU", "WE", "TH", "FR", "SA", "SU"];

function events_to_ids(events) {
    var ids = [];
    for (var i=0; i<events.length; i++) {
        ids.push(events[i].id);
    }
    return ids;
}

function cleanup(calendar) {
	var ids = [];
	calendar.find(function (found_events) {
		var ids = events_to_ids(found_events);
		if (ids.length > 0) {
			calendar.removeBatch(ids);
			console.log("cleanup: remove all events in calendar");
		} else {
			console.log("cleanup: no events in calendar");
		}
	});
}

function assert_equalsArrays(array1, array2, compare, msg) {
    assert_equals(array1.length, array2.length, msg);
    for (var i=0; i<array1.length; i++) {
        compare(array1[i], array2[i], msg);
    }
}
function assert_isArrayOfDays(value, msg) {
    assert_true(Array.isArray(value), msg)
    for (var i = 0; i < value.length; i++) {
        assert_in_array(value[i], DAYS, msg + " (item " + i + ")");
    }
}

function assert_equalsSimpleCoordinates(c_actual, c_expected, msg) {
    if (c_actual == null && c_expected == null) {
        return;
    }
    if (c_actual == null || c_expected == null) {
        assert_equals(c_actual, c_expected, msg);
    }
    assert_equals(c_actual.latitude, c_expected.latitude, msg +": same latitude");
    assert_equals(c_actual.longitude, c_expected.longitude, msg +": same longitude");
}

function assert_equalsDurations(d_actual, d_expected, msg) {
    if (d_actual == null && d_expected == null) {
        return;
    }
    if (d_actual == null || d_expected == null) {
        assert_equals(d_actual, d_expected, msg);
    }
    assert_equals(d_actual.length, d_expected.length, msg);
    assert_equals(d_actual.unit, d_expected.unit, msg);
}

function assert_equalsDates(actual_date, expected_date, msg) {
    if (actual_date == null && expected_date == null) {
        return;
    }
    if (actual_date == null || expected_date == null) {
        assert_true(actual_date, expected_date, msg);
    }
    assert_equals(actual_date.toString(), expected_date.toString(), msg);
}

function assert_equalsAlarms(actual_alarm, expected_alarm, msg) {
    if (actual_alarm == null && expected_alarm == null) {
        return;
    }
    if (actual_alarm == null || expected_alarm == null) {
        assert_equals(actual_alarm, expected_alarm, msg);
    }
    assert_equalsDates(actual_alarm.absoluteDate, expected_alarm.absoluteDate, msg);
    assert_equalsDurations(actual_alarm.before, expected_alarm.before, msg);
    assert_equals(actual_alarm.method, expected_alarm.method, msg);
    assert_equals(actual_alarm.description, expected_alarm.description, msg);
}

function assert_equalsRRules(actual_rrule, expected_rrule, msg) {
    if (actual_rrule == null && expected_rrule == null) {
        return;
    }
    if (actual_rrule == null || expected_rrule == null) {
        assert_equals(actual_rrule, expected_rrule, msg + ": one is null but not the other");
    }
    assert_equals(actual_rrule.frequency, expected_rrule.frequency, msg);
    assert_equalsDates(actual_rrule.untilDate, expected_rrule.untilDate, msg);
    assert_equals(actual_rrule.occurrenceCount, expected_rrule.occurrenceCount, msg);
    assert_array_equals(actual_rrule.daysOfTheWeek, expected_rrule.daysOfTheWeek, msg);
    assert_array_equals(actual_rrule.setPositions, expected_rrule.setPositions, msg);
    assert_equalsArrays(actual_rrule.exceptions, expected_rrule.exceptions, assert_equalsDates, msg);
}

function assert_equalsAttendees(actual_att, expected_att, msg) {
    if (actual_att == null && expected_att == null) {
        return;
    }
    if (actual_att == null || expected_att == null) {
        assert_equals(actual_att, expected_att, msg);
    }
   // assert_equals(actual_att.uri, expected_att.uri, msg);
    assert_equals(actual_att.name, expected_att.name, msg + " name");
    assert_equals(actual_att.role, expected_att.role, msg + " role");
    assert_equals(actual_att.status, expected_att.status, msg + " status");
    assert_equals(actual_att.RSVP, expected_att.RSVP, msg + " RSVP");
    assert_equals(actual_att.group, expected_att.group, msg+ " group");
    assert_equals(actual_att.delegatorURI, expected_att.delegatorURI, msg+ " delegatorURI");
    assert_equals(actual_att.delegateURI, expected_att.delegateURI, msg+ " delegateURI");
}

function assert_equalsEvents(ev_actual, ev_expected) {
    assert_equalsDates(ev_actual.startDate, ev_expected.startDate, "same startDate");
    assert_equalsDates(ev_actual.endDate, ev_expected.endDate, "same endDate");
    assert_equals(ev_actual.summary, ev_expected.summary, "same summary");
    assert_equals(ev_actual.description, ev_expected.description, "same description");
    assert_array_equals(ev_actual.categories, ev_expected.categories, "same categories");
    assert_equals(ev_actual.isAllDay, ev_expected.isAllDay, "same isAllDay");
    assert_equalsDurations(ev_actual.duration, ev_expected.duration, "same duration");
    assert_equals(ev_actual.location, ev_expected.location, "same location");
    assert_equalsSimpleCoordinates(ev_actual.geolocation, ev_expected.geolocation, "same geolocation");
    assert_equals(ev_actual.organizer, ev_expected.organizer, "same organizer");
    assert_equals(ev_actual.visibility, ev_expected.visibility, "same visibility");
    assert_equals(ev_actual.status, ev_expected.status, "same status");
    assert_equals(ev_actual.priority, ev_expected.priority, "same priority");
    assert_equalsArrays(ev_actual.alarms, ev_expected.alarms, assert_equalsAlarms, "same alarms");
    assert_equalsRRules(ev_actual.recurrenceRule, ev_expected.recurrenceRule, "same rrule");
    assert_equalsArrays(ev_actual.attendees, ev_expected.attendees, assert_equalsAttendees, "same attendees");
}

function createTestEvent() {
    return new tizen.CalendarEvent({description:'Tizen test event description',
             summary:'Tizen test event summary',
             startDate: new tizen.TZDate(2012, 1, 15, 10, 0),
             duration: new tizen.TimeDuration(1, "HOURS"),
             location:'Suwon'});
}

function createTestTask() {
    return new tizen.CalendarTask({description:'Tizen test task description',
                  summary:'Tizen test task summary',
                  dueDate: new tizen.TZDate(2012, 2, 15, 10, 0),
                  progress: 10,
                  location:'Seoul'});
}

function createTestEvents() {
    var ev1 = new tizen.CalendarEvent({description:'Open description 1',
                    summary:'Open 1',
                    startDate: new tizen.TZDate(2012, 1, 15, 10, 0),
                    duration: new tizen.TimeDuration(3600, "SECS"),
                    location:'Seoul'});
    var ev2 = new tizen.CalendarEvent({description:'Open description 2',
                    summary:'Open 2',
                    startDate: new tizen.TZDate(2012, 1, 15, 10, 0),
                    duration: new tizen.TimeDuration(3600, "SECS"),
                    location:'Seoul'});
    return [ev1, ev2];
}

function createTestTasks() {
    var task1 = new tizen.CalendarTask({description:'Open task description 1',
                    summary:'Open task 1',
                    dueDate: new tizen.TZDate(2012, 1, 15, 10, 0),
                    location:'Seoul'});
    var task2 = new tizen.CalendarTask({description:'Open task description 2',
                    summary:'Open task 2',
                    dueDate: new tizen.TZDate(2012, 1, 15, 10, 0),
                    location:'Seoul'});
    return [task1, task2];
}

function ensureContactRefIsValid(contactRef) {
    var addressBook, testContact, getAddressBook;

    try {
        getAddressBook = tizen.contact.getAddressBook(contactRef.addressBookId);
        getAddressBook.get(contactRef.contactId);
    } catch (error) {
        addressBook = tizen.contact.getDefaultAddressBook();
        testContact = new tizen.Contact({
            name: new tizen.ContactName({firstName: "Test", lastName: "Contact"})
        });
        addressBook.add(testContact);
        contactRef = new tizen.ContactRef(testContact.addressBookId, testContact.id);
    }

    return contactRef;
}
