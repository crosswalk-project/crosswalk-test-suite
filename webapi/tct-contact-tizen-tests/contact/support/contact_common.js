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
        yananx.xu <yananx.xu@intel.com>
        Jakub Siewierski <j.siewierski@samsung.com>
        Tomasz Paciorek<t.paciorek@samsung.com>

*/
var RESOURCE_DIR = "TESTER-HOME-DIR/content";
var TEST_IMAGE_1 = "file://" + RESOURCE_DIR + "/webapi-tizen-contact-test_image1.png";
var TEST_IMAGE_2 = "file://" + RESOURCE_DIR + "/webapi-tizen-contact-test_image2.png";
var TEST_RING_1 = "file://" + RESOURCE_DIR + "/webapi-tizen-contact-test_ring1.mp3";
var TEST_RING_2 = "file://" + RESOURCE_DIR + "/webapi-tizen-contact-test_ring2.mp3";

var TYPE_MISMATCH_ERR = "TypeMismatchError";
var INVALID_VALUES_ERR = "InvalidValuesError";
var NOT_FOUND_ERR = "NotFoundError";
var UNKNOWN_ERR = "UnknownError";
var NOT_SUPPORTED_ERR = "NotSupportedError";
var PERMISSION_DENIED_ERR = "SecurityError";
var watcherId = null;

function createTestContactInit() {
    return {
        name:new tizen.ContactName({
            firstName:"John",
            lastName:"Doe",
            displayName:"John Doe"
        }),
        addresses:[new tizen.ContactAddress({
            country:"United States",
            region:"Florida",
            city:"Miami",
            streetAddress:"124 SW 17th Ave."
        })],
        phoneNumbers:[new tizen.ContactPhoneNumber("817-444-2345")],
        emails:[new tizen.ContactEmailAddress("email@example.org")],
        birthday:new Date(1980, 3, 4),
        anniversaries:[new tizen.ContactAnniversary(new Date(2000, 4, 12))],
        note:"Lorem Ipsum",
        isFavorite:true
    };
}

function createTestContact() {
    return new tizen.Contact({
        name:new tizen.ContactName({
            firstName:"John",
            lastName:"Doe",
            displayName:"John Doe"
        }),
        addresses:[new tizen.ContactAddress({
            country:"United States",
            region:"Florida",
            city:"Miami",
            streetAddress:"124 SW 17th Ave."
        })],
        phoneNumbers:[new tizen.ContactPhoneNumber("817-444-2345")],
        emails:[new tizen.ContactEmailAddress("email@example.org")],
        birthday:new Date(1980, 3, 4),
        anniversaries:[new tizen.ContactAnniversary(new Date(2000, 4, 12))],
        note:"Lorem Ipsum",
        isFavorite:true
    });
}

function createTestContacts(id) {
    var contact1 = new tizen.Contact({
        name:new tizen.ContactName({
            firstName:"Jennifer"+id,
            lastName:"Lewis",
            displayName:"Jenny"
        }),
        addresses:[new tizen.ContactAddress({
            country:"Canada",
            region:"BC",
            city:"Vancouver",
            streetAddress:"934 Laurel St."
        })],
        phoneNumbers:[new tizen.ContactPhoneNumber("416-412-5555")],
        emails:[new tizen.ContactEmailAddress("jenni@somemail.com")],
        note:"Some Note"
    }),
    contact2 = new tizen.Contact({
        name:new tizen.ContactName({
            firstName:"Edward"+id,
            lastName:"Butch",
            displayName:"Edward Butch"
        }),
        addresses:[new tizen.ContactAddress({
            country:"United Kingdom",
            city:"London"
        })],
        phoneNumbers:[new tizen.ContactPhoneNumber("554-555-4895")]
    });
    return [contact1, contact2];
}

function addContactsToAddressBook(contacts) {
    for (i = 0; i < contacts.length; i++) {
        tizen.contact.getDefaultAddressBook().add(contacts[i]);
    }
}

function removeContactsFromAddressBook(contacts) {
    for (i = 0; i < contacts.length; i++) {
        tizen.contact.getDefaultAddressBook().remove(contacts[i].id);
    }
}

// Define the error callback
function errorCB(err) {
    console.log( 'The following error occurred: ' +  err.name);
}

// Define the add contact success callback
function contactsAddedCB(contacts) {
    console.log( contacts.length + ' contact(s) were successfully added to an Address Book' );
}

function FailTest()
{
    var description = "Fail Test",
    t = async_test("Test Description: " + description);
    t.step(function() { assert_true(false); } );
    t.done();
}
function PassTest()
{
    t.step(function() { assert_true(true); } );
    t.done();
}

function find(addressBook, callback, filter, sortMode) {

    function errorCB(error) {
      console.log("tizen.contact.find");
      console.log('The following error occurred: ' +  error.code + ' ' + error.message);
    }

    try {
        if(filter !== undefined && sortMode !== undefined) {
            addressBook.find(callback, errorCB, filter, sortMode);
        } else if(filter !== undefined && sortMode === undefined) {
            addressBook.find(callback, errorCB, filter);
        } else if(filter === undefined && sortMode !== undefined) {
            addressBook.find(callback, errorCB, null, sortMode);
        } else {
            addressBook.find(callback, errorCB);
        }
    } catch(error) {
        console.log("tizen.contact.find" + error.name + ' ' + error.message);
    }
}

function printContactsProperty(contacts, propName, subPropName, str) {
    var nCont = contacts.length, i;
    for (i = 0; i < nCont; i++) {
        if (subPropName !== undefined && subPropName !== null && subPropName.length !== '') {
            console.log(str + contacts[i][propName][subPropName]);
        } else {
            console.log(str + contacts[i][propName]);
        }
    }
}

function printContacts(contacts) {
    var nCont = contacts.length, date;
    console.log(nCont + " contacts found");
    for (i = 0; i < nCont; i++) {
        console.log("Contact id: " + contacts[i].id);
        console.log("Contact lastUpdated: " + contacts[i].lastUpdated);
        console.log("Contact displayName: " + contacts[i].name.displayName);
        console.log("Contact first + last name: " + contacts[i].name.firstName
            + " " + contacts[i].name.lastName);
        console.log("Contact nickname: " + contacts[i].name.nicknames[0]);
        console.log("Contact email: " + contacts[i].emails[0].email);
        console.log("Contact phone: " + contacts[i].phoneNumbers[0].number);
        date = contacts[i].birthday;
        if (date !== undefined) {
            console.log("Contact birthday: " + date.getFullYear() + "-" + date.getMonth() + "-" + date.getDate());
        }
        console.log("Contact ringtone: " + contacts[i].ringtoneURI);
    }
}
