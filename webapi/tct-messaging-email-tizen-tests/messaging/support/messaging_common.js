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
        JungHyuk, Park <junghyuk.park@samsung.com>

*/

var TEST_EMAIL_RECIPIENT_1 = ""; // this variable MUST be set before executing tests
var TEST_EMAIL_RECIPIENT_2 = ""; // this variable MUST be set before executing tests

var EMAIL_SYNC_INTERVAL = 30000;
var EMAIL_RESEND_LIMIT = 30;
var EMAIL_RESYNC_LIMIT = 30;

var TYPE_MISMATCH_ERR  = 'TypeMismatchError';

var MESSAGE_FOLDER_TYPE_INBOX = "INBOX";

var MESSAGE_ATTACHMENT_IMAGE_PATH = "images/webapi-tizen-messaging-test_image.jpg";
var MESSAGE_ATTACHMENT_IMAGE_MIME_TYPE = "image/jpg";

var MESSAGE_ATTACHMENT_SOUND_PATH = "music/webapi-tizen-messaging-test_noise.mp3";
var MESSAGE_ATTACHMENT_SOUND_MIME_TYPE = "audio/mp3";

var MESSAGE_BODY_PLAIN = "Sample Plain Body"
var MESSAGE_BODY_HTML = "<p>Sample HTML Body</p>"

var generateSubject = function () {
    var datetime = new Date().getTime();
    var count = 0;
    var subject = function(datetime, count) {
        return "sample subject: "+datetime+"-"+count;
    }

    generateSubject = function () {
        count++;
        return subject(datetime, count);
    }
    return subject(datetime, count);
};


function createSimpleMessageTo(recipient) {
    return new tizen.Message("messaging.email", {
        subject: generateSubject(),
        to: [recipient],
        plainBody: MESSAGE_BODY_PLAIN
    }); 
}

function sendMessage(t, service, msg, onSuccess, onError) {
    var sendError, requestSending, resend=0;

    sendError = t.step_func(function (error) {
        if (resend <= EMAIL_RESEND_LIMIT) {
            setTimeout(requestSending, 5000);
        } else {
            onError(error);
        }
    });

    requestSending = t.step_func(function () {
        resend++;
        service.sendMessage(msg, onSuccess, sendError);
    });

    requestSending();
}


function sync(t, service, onSuccess, onError, limit) {
    var syncError, requestSync, argc=arguments.length, resync=0;

    syncError = t.step_func(function (error) {
        if (resync <= EMAIL_RESYNC_LIMIT) {
            setTimeout(requestSync, 5000);
        } else {
            onError(error);
        }
    });

    requestSync = t.step_func(function () {
        resync++;

        if (argc >= 5) {
            service.sync(onSuccess, syncError, limit);
        } else  {
            service.sync(onSuccess, syncError);
        }
    });

    setTimeout(t.step_func(function () {
        requestSync();
    }), EMAIL_SYNC_INTERVAL);
}


function getEmailService(t, onSuccess, onError) {
    t.step(function () {
        tizen.messaging.getMessageServices(
            "messaging.email",
            t.step_func(function (services) {
                assert_type(services, "array", "Not an array");
                assert_greater_than(services.length, 0, "Received empty services array");
                onSuccess(services[0]);
            }),
            onError
        );
    });
}


function message_conversation_test(t, onReady) {
    var service, message, serviceSuccess, serviceError, addDraftSuccess, addDraftError,
    filterConversation, findConversationsSuccess, findConversationsError;

    findConversationsSuccess = t.step_func(function (conversations) {
        assert_equals(conversations.length, 1, "Incorrect number of conversations found");
        assert_equals(conversations[0].id, message.conversationId, "Found incorrect convesation");
        t.step_func(onReady)(service, message, conversations[0]);
    });

    findConversationsError = t.step_func(function (error) {
        assert_unreached("findConversations() error callback: name:" + error.name + ", msg:" + error.message);
    });

    addDraftSuccess = t.step_func(function () {
        filterConversation = new tizen.AttributeFilter("id", "EXACTLY", message.conversationId);
        service.messageStorage.findConversations(filterConversation, findConversationsSuccess, findConversationsError);
    });

    addDraftError = t.step_func(function (error) {
        assert_unreached("addDraftMessage() error callback: name:" + error.name + ", msg:" + error.message);
    });

    serviceSuccess = t.step_func(function (emailService) {
        service = emailService;

        message = new tizen.Message("messaging.email", {
            subject: generateSubject(),
            to: [TEST_EMAIL_RECIPIENT_2],
            cc: [TEST_EMAIL_RECIPIENT_1],
            bcc: [TEST_EMAIL_RECIPIENT_1],
            plainBody: MESSAGE_BODY_PLAIN,
            htmlBody: MESSAGE_BODY_HTML,
            isHighPriority: false
        }); 

        assert_true("conversationId" in message, "No 'conversationId' attribute in message");
        assert_equals(message.conversationId, null, "message.conversationId default value should be null");
        check_readonly(message, "conversationId", null, "object", "12345");

        service.messageStorage.addDraftMessage(message, addDraftSuccess, addDraftError);
    });

    serviceError = t.step_func(function (error) {
        assert_unreached("getEmailService() error callback: name:" + error.name + ", msg:" + error.message);
    });

    t.step(function () {
        getEmailService(t, serviceSuccess, serviceError);
    });
}


function findFolders(t, service, onSuccess, onError) {
    var filter = new tizen.AttributeFilter("serviceId", "EXACTLY", service.id);
    service.messageStorage.findFolders(filter, onSuccess, onError);
}


function getInboxFolder(t, folders) {
    var i, inboxFolder;
    t.step(function () {
        for(i = 0; i < folders.length; i++) {
            if (folders[i].type === MESSAGE_FOLDER_TYPE_INBOX) {
                inboxFolder = folders[i];
                break;
            }
        }
        assert_not_equals(inboxFolder, undefined, "Inbox folder not found");
    });
    return inboxFolder;
}

function findMessages(t, service, folder, subject, onSuccess, onError) {
    var subjectFilter, folderFilter, compositefilter;

    t.step(function() {
        folderFilter = new tizen.AttributeFilter("folderId", "EXACTLY", folder.id);
        subjectFilter = new tizen.AttributeFilter("subject", "EXACTLY", subject);
        compositefilter = new tizen.CompositeFilter("INTERSECTION", [folderFilter, subjectFilter]);
        service.messageStorage.findMessages(compositefilter, onSuccess, onError);
    });
}

function assert_message_equals(t, messages, message, folder) {
    t.step(function() {
        assert_type(messages, "array", "Not an array");
        assert_equals(messages.length, 1, "incorrect messages found");
        assert_true(messages[0] instanceof tizen.Message, "Not a Message");
        assert_equals(messages[0].subject, message.subject, "Incorrect subject.");

        if (arguments.length >= 4) {
            assert_equals(messages[0].folderId, folder.id, "Incorrect folderId.");
        }
    });
}

function assert_draft_message_equals(t, messages, message) {
    t.step(function() {
        assert_type(messages, "array", "Not an array");
        assert_equals(messages.length, 1, "incorrect messages found");
        assert_true(messages[0] instanceof tizen.Message, "Not a Message");
        assert_equals(messages[0].id, message.id, "Incorrect folderId.");
        assert_equals(messages[0].subject, message.subject, "Incorrect subject.");
    });
}

function assert_inbox_message_equals(t, messages, message, folder) {
    t.step(function() {
        assert_type(messages, "array", "Not an array");
        assert_equals(messages.length, 1, "incorrect messages found");
        assert_true(messages[0] instanceof tizen.Message, "Not a Message");
        assert_equals(messages[0].subject, message.subject, "Incorrect subject.");
        assert_equals(messages[0].folderId, folder.id, "Incorrect folderId.");
    });
}

// change TEST_EMAIL_RECIPIENT_1 and TEST_EMAIL_RECIPIENT_2
document.write('<script src="../webrunner/jquery-1.10.2.min.js"></script>');
document.write('<script src="support/getJsonConf.js"></script>');
