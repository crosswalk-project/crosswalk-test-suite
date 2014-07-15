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
        Liu, yun <yun.liu@archermind.com>

*/

// Get default address book.
var addressbook = tizen.contact.getDefaultAddressBook();

// Define the error callback
function errorCB(err) {
  $("#datawindow").html('The following error occurred: ' +  err.name);
}

function contactsFoundCB(contacts, id, mark) {
  // The contact has been successfully found
  if (id && mark == "modify") {
    contacts[id].name.lastName = $("#lastName").val();
    contacts[id].name.nicknames = $("#nicknames").val();
    contacts[id].emails = $("#emails").val();
    contacts[id].phoneNumbers = $("#phoneNumbers").val();
    try {
      addressbook.update(contacts[id]);
    } catch (err) {
      $("#datawindow").html('The following error occurred while updating: ' +  err.name);
    }
    getPerson();
  }
  else if (id && mark == "delete") {
    tizen.contact.remove(persons[id].id);
    getPerson();
  }
  else if (id && mark == "info") {
    $("#datawindow").html("<p>name: " + contacts[id].name.lastName + "</p><p>nicknames: " + contacts[id].name.nicknames + "</p><p>emails: " + contacts[id].emails + "</p><p>phoneNumbers: " + contacts[id].phoneNumbers + "</p><p><a href='javascript: getPerson();'>person list</a></p>");
  }
  else
  {
    for(var i = 0; i < contacts.length; i++) {
      $("#datawindow").html("<p>" + contacts[i].name.lastName + "<a href='javascript: updatePerson(" + i +");'>modify</a><a href='javascript: removePerson(" + i +");'>delete</a><a href='javascript: getPersonInfo(" + i +");'>info</a></p>" + $("#datawindow").html());
    }
  }
}

function addPerson() {
  var contact = new tizen.Contact(
    {name: new tizen.ContactName({firstName:'Jeffrey',
    lastName:$("#lastName").val(),
    nicknames:[$("#nicknames").val()]}),
    emails:[new tizen.ContactEmailAddress($("#emails").val())],
    phoneNumbers:[new tizen.ContactPhoneNumber($("#phoneNumbers").val())]});
  try {
    addressbook.add(contact);
  } catch (err) {
    $("#datawindow").html('The following error occurred while adding: ' +  err.name);
  }
  getPerson();
}

function updatePerson(id) {
  getPerson(id, "modify");
}

function removePerson(id) {
  getPerson(id, "delete");
}

function getPersonInfo(id) {
  getPerson(id, "info");
}

function getPerson(id, mark) {
  var filter = new tizen.AttributeFiilter('name.firstName', 'CONTAINS', 'Jeffrey');
  try {
    addressbook.find(contactsFoundCB(id, mark), errorCB, filter);
  } catch (err) {
    $("#datawindow").html('The following error occurred while finding: ' +  err.name);
  }
}

$(document).ready(function() {
  $("#addbutton").click(addPerson);
  getPerson();
});
