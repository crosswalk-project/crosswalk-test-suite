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

function createVCard() {
    var vcard = "BEGIN:VCARD\n"+
        "VERSION:3.0\n"+
        "N:Gump;Forrest\n"+
        "FN:Forrest Gump\n"+
        "ORG:Bubba Gump Shrimp Co.\n"+
        "TITLE:Shrimp Man\n"+
        "PHOTO;VALUE=URL;TYPE=GIF:http://www.example.com/dir_photos/my_photo.gif\n"+
        "TEL;TYPE=WORK,VOICE:(111) 555-1212\n"+
        "TEL;TYPE=HOME,VOICE:(404) 555-1212\n"+
        "EMAIL;TYPE=PREF,INTERNET:forrestgump@example.com\n"+
        "X-PHONETIC-FIRST-NAME:ForestGamp\n"+
        "X-TIZEN-RINGTONE:run_forest_run.snd\n"+
        "X-TIZEN-ANNIVERSARY;TYPE=Anniversary:1980-12-31\n"+
        "END:VCARD";
    return vcard;
}

function generateFirstName() {
    var firstNames = ['Anna','Mia','Jenni','Sanna','Milla','Charlie','Alex','Michael','Jorma'];
    return firstNames[Math.floor(Math.random()*firstNames.length)];
}

function generateLastName() {
    var lastNames = ['Pfifer','Leibowitz','Jackson','Stevensson','Vanhanen','Pitkanen','Pukkinen','Tukkinen','Olofsson'];
    return lastNames[Math.floor(Math.random()*lastNames.length)];
}

function generateMiddleName() {
    var middleNames = ['Ani','Christian','Manteli','X-Man','Wolvorine','MIB','Santa','Claus','Tonttu'];
    return middleNames[Math.floor(Math.random()*middleNames.length)];
}

function generatePrefix() {
    var prefixes = ['Mr','Dr','Mrs','Ms','Miss'];
    return prefixes[Math.floor(Math.random()*prefixes.length)];
}

function generatePhoneNumber() {
    var phones = ['+18009382345','+358399372573','+78124785427','+848567123','+95873624532'];
    return phones[Math.floor(Math.random()*phones.length)];
}

function generateDisplayName() {
    return generateLastName() + ' ' + generateFirstName() + ' ' + generateMiddleName();
}

function generateNickNames() {
    var nickNames = ['norsu','mammi','echidna','Mr.Fox','fixus'],
    nicks = [], i,
    nickCount = Math.floor(Math.random()*3);
    for(i = 0; i <  nickCount; i++) {
        nicks.push(nickNames[Math.floor(Math.random()*nickNames.length)]);
    }
    return nicks;
}

function generatePhoneticName() {
    var phoneticNames = ['Pfifer','Leibowitz','Jackson','Stevensson','Vanhanen','Pitkanen','Pukkinen','Tukkinen','Olofsson'];
    return phoneticNames[Math.floor(Math.random()*phoneticNames.length)];
}

function generateEmail(seed) {
    var emails = ['anna@gmail.com','mia@yahoo.com','jenna.lehtinen@msn.com',
                  'valteri.nurminen@kolumbus.fi','jack.all.trades@intei.com',
                  'alex@alex.com', 'dmitry.morozow@ya.ru', 'elena.ivanova@mail.ru'];
    return emails[seed || Math.floor(Math.random()*emails.length)];
}

function generatePhoneNumberTypes(seed) {
    var types = ['work','home'],
    typesArray = [], i,
    typesCount;
    if(seed === undefined) {
        seed = [];
    }
    typesCount = Math.floor(seed.length || Math.random()*4);
    for (i = 0; i <  typesCount; i++) {
        typesArray.push(types[seed[i] || Math.floor(Math.random()*types.length)]);
    }
    return typesArray;
}

function generateCountry() {
    var countries = ['USA','Finland','Greece','UK','Sweden','Italy','Germany','France','Turkey'];
    return countries[Math.floor(Math.random()*countries.length)];
}

function generateRegion() {
    var regions = ['WA','UT','LA','NY','UUSIMAA','RU','MA'];
    return regions[Math.floor(Math.random()*regions.length)];
}

function generateCity() {
    var cities = ['Helsinki','Portland','St.Petersburg','Athens','Rome','Paris','New York', 'London'];
    return cities[Math.floor(Math.random()*cities.length)];
}

function generateStreetAddress() {
    var streetAddresses = ['Sinimaentie 8','Westendentie 28','Ilmallankuja 3','Times Square rd. 4','Street st. 4','Another street 9'];
    return streetAddresses[Math.floor(Math.random()*streetAddresses.length)];
}

function generateAdditionalInformation() {
    var additionalInfos = ['Main building, floor 3', 'Door code 3424', 'Ask for Hannu', 'Super informatino', 'James Bond home'];
    return additionalInfos[Math.floor(Math.random()*additionalInfos.length)];
}

function generatePostalCode() {
    var postCodes = ['03984', '30289', '90210', '038', '198207', '12345'];
    return postCodes[Math.floor(Math.random()*postCodes.length)];
}

function generateBirthday() {
    var dates = [new Date(1980,10,12), new Date(1956,6,1), new Date(1970,1,9), new Date(1930,4,19)];
    return dates[Math.floor(Math.random()*dates.length)];
}

function generateAnniversaryLabel() {
    var anniversaries = ['Marriage', 'Honeymoon', 'Reunion', 'Another anniversary'];
    return anniversaries[Math.floor(Math.random()*anniversaries.length)];
}

function generateOrganizationName() {
    var orgName = ['Intel', 'Foxconn', 'Nokia', 'BOS', 'Micron', 'PnG', 'Sony', 'BMG'];
    return orgName[Math.floor(Math.random()*orgName.length)];
}

function generateDepartment() {
    var departments = ['sales', 'marketing', 'management', 'it support', 'rnd', 'hr', 'logistics', 'legal'];
    return departments[Math.floor(Math.random()*departments.length)];
}

function generateOffice() {
    var offices = ['Main', 'Head', 'Branch', 'Kama', 'Tolo', 'Humwee'];
    return offices[Math.floor(Math.random()*offices.length)];
}

function generateTitle() {
    var titles = ['SW Engineer', 'Manager', 'Architect', 'VP', 'CEO', 'CFO'];
    return titles[Math.floor(Math.random()*titles.length)];
}

function generateRole() {
    var roles = ['RnD', 'Sales', 'Somestuff', 'IMHO', 'Support', 'Marketing'];
    return roles[Math.floor(Math.random()*roles.length)];
}

function generateLogoURI() {
    var logos = [TEST_IMAGE_1, TEST_IMAGE_2];
    return logos[Math.floor(Math.random()*logos.length)];
}

function generatePhotoURI() {
    var photos = [TEST_IMAGE_1, TEST_IMAGE_2];
    return photos[Math.floor(Math.random()*photos.length)];
}

function generateNotes() {
    var notes = ['note one','note two','note three','fifth note','fourth note'];
    notesArray = [], i,
    notesCount = Math.floor(Math.random()*3);
    for (i = 0; i <  notesCount; i++) {
        notesArray.push(notes[Math.floor(Math.random()*notes.length)]);
    }
    return notesArray;
}

function generateURL() {
    var urls = ['http://www.myblog.com', 'http://www.myhomepage.com', 'http://www.mygallery.com'];
    return urls[Math.floor(Math.random()*urls.length)];
}

function generateURLType() {
    var urltypes = ['blog', 'homepage','company'];
    return urltypes[Math.floor(Math.random()*urltypes.length)];
}

function generateRingtoneURI() {
    var ringtones = [TEST_RING_1, TEST_RING_2];
    return ringtones[Math.floor(Math.random()*ringtones.length)];
}

function createContacts(number) {
    var contacts = [], i;
    for(i = 0; i < number; i++) {
        contacts.push(createContact());
    }
    return contacts;
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
        var nCont = contacts.length, i, date;
        console.log(nCont + " contacts found");
        for(i = 0; i < nCont; i++) {
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
            console.log("Contact categories: " + contacts[i].categories[0]);
            console.log("Contact ringtone: " + contacts[i].ringtoneURI);
        }
}
