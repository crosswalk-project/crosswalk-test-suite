/*
Copyright (c) 2013 Samsung Electronics Co., Ltd.

Licensed under the Apache License, Version 2.0 (the License);
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Authors:
        Choi, Jongheon <j-h.choi@samsung.com>

*/

var errorMessage = '',
    emailReg = /^([\w\-\.]+@([\w\-]+\.)+[\w\-]{2,4})?$/,
    emailArray = [],
    numberOfBadEmails = 0,
    app = {
        attach: []
    };

function replaceAll(txt, replace, with_this) {
    return txt.replace(new RegExp(replace, 'g'), with_this);
}

function verifyEmail() {
    var result = false, i, tempEmail, email = $('#email').val(), tab = null;

    if (email === '') {
        errorMessage = 'Enter email address';
    } else {
        numberOfBadEmails = 0;
        emailArray = [];
        tab = email.split(/[,; ]/);
        for (i = 0; i < tab.length; i += 1) {
            tempEmail = $.trim(tab[i]);
            if (tempEmail !== '') {
                if (emailReg.test(tempEmail)) {
                    emailArray.push(tempEmail);
                } else {
                    numberOfBadEmails += 1;
                }
            }
        }
        if (emailArray.length > 0 && numberOfBadEmails === 0) {
            result = true;
        } else {
            if (numberOfBadEmails === 1) {
                errorMessage = 'one email address is incorrect';
            } else {
                errorMessage = numberOfBadEmails + ' email addresses are incorrect';
            }
        }
    }

    return result;
}

function verifyTitle() {
    var result = false,
        title = $('#title').val();

    if (title === '') {
        errorMessage = 'enter email title';
    } else {
        result = true;
    }

    return result;
}

function verifyContent() {
    var result = false,
        content = $('#emailContent').val();

    if (content === '') {
        errorMessage = 'Enter email content';
    } else {
        result = true;
    }

    return result;
}

function createAttachList(element) {
    return ('<div class="panel-body">' + element + '</div>');
}

function attachListUpdate() {
    var fileName = 'filename', size = '0kB', i, len;
    $('#attachmentsList').replaceWith($('<div class="panel panel-primary" id="attachmentsList"></div>'));

    for (i = 0, len = app.attach.length; i < len; i += 1) {
        $('#attachmentsList').append(createAttachList(app.attach[i]));
    }

    $('#attachmentsList').trigger('create');
}

// Define the success callback.
function messageSent() {
    app.attach = [];
    attachListUpdate();
    //alert('Email was sent');
}

// Define the error callback.
function messageFailed(error) {
    $("#popup_info").modal(showMessage("error", 'Error occured while sending the message!'));
}

// workaround for launch accounts settings;
function runEmailService() {
    var apps = "";
    function onGetInfo(data) {
        for (var i = 0; i < data.length; i++)
        {
            if(data[i].id == "setting-myaccount-efl")
                apps = data[i].id;
        }
        if (apps) {
            tizen.application.launch(apps);
        } else {
            $("#popup_info").modal(showMessage("error", 'Account settings cannot be launched. Please configure email account by system options.'));
        }
    }
    tizen.application.getAppsInfo(onGetInfo);
}

function virtualAttachmentPath(absolutePath) {
    absolutePath = absolutePath.replace(/^\/opt\/usr\/media\//, "");
    var parts = absolutePath.split("/");
    switch (parts[0]) {
    case "Images":
        parts[0] = "images";
        break;
    case "Videos":
        parts[0] = "videos";
        break;
    case "Sounds":
        parts[0] = "music";
        break;
    case "Documents":
        parts[0] = "documents";
        break;
    case "Downloads":
        parts[0] = "downloads";
        break;
    default:
        return null;
    }
    return parts.join("/");
}

// Define the success callback.
function serviceListCB(services) {
    var i, len, msgService, email, tmpArray = [], name, vname;
    function split(str) {
        return str.split(/[,; ]/).filter(function (item) {
            return (item.trim() !== '');
        });
    }

    if (services.length > 0) {
        msgService = services[0];
        //alert('Sending an Email(takes about 1 minute)');

        email = new tizen.Message('messaging.email');
        email.subject = $('#title').val();
        email.to = split($('#email').val());
        email.cc = split($('#cc').val());
        email.bcc = split($('#bcc').val());
        email.body.plainBody = $('#emailContent').val();
        email.body.htmlBody = "<div>" + $("#emailContent").val();

        for (i = 0, len = app.attach.length; i < len; i += 1) {
            name = app.attach[i];
            vname = virtualAttachmentPath(name);
            try {
                tmpArray.push(new tizen.MessageAttachment(vname));
            } catch (err) {
                $("#popup_info").modal(showMessage("error", "Attachment could not be added:\n" + name));
            }
        }
        email.attachments = tmpArray;

        // Send request
        msgService.sendMessage(email, messageSent, messageFailed);
    } else {
        if (confirm('This application for proper running requires configure email account.\n Do you want configure account now?')) {
            runEmailService();
        }
    }
}

function serviceListError(e) {
    $("#popup_info").modal(showMessage("error", 'err: ' + e.message));
}

function sendMessage() {
    try {
        tizen.messaging.getMessageServices("messaging.email", serviceListCB, serviceListError);
    } catch (e) {
        $("#popup_info").modal(showMessage("error", 'err: ' + e.message));
    }
}

function startFileManager() {
    function getDataFromFileManager(data) {
        app.attach.push(data[0].value[0]);
        attachListUpdate();
    }

    var serviceRequest = new tizen.ApplicationControl('http://tizen.org/appcontrol/operation/pick', null, '*/*');

    var appControlReplyCB = {
            onsuccess: getDataFromFileManager,
            onfailure: function() {}
    };

    try {
    tizen.application.launchAppControl(serviceRequest, null,
    function() {
        console.log("launch appControl succeeded");
    },
    function(e) {
        $("#popup_info").modal(showMessage("error", "launch appControl failed. Reason: " + e.message));
    },
    appControlReplyCB);
    } catch(e) {
       $("#popup_info").modal(showMessage("error", "launch appControl error: " + e.message));
    }
}

function init() {
    $('#send').bind('click', function (event) {
        if (verifyEmail() && verifyTitle() && verifyContent()) {
            sendMessage();
        } else {
            $("#popup_info").modal(showMessage("error", errorMessage));
        }
    });
    $('#addAttach').bind('click', function (event) {
        startFileManager();
    });
}

$(document).ready(init);
