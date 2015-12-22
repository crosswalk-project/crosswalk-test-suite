/*
 * Copyright (c) 2012, Intel Corporation.
 *
 * This program is licensed under the terms and conditions of the 
 * Apache License, version 2.0.  The full text of the Apache License is at
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 */

var messages;
function initGetMessage ()
{
    if (window.getMessages) {
        return;
    }

    if (window.chrome && window.chrome.i18n && window.chrome.i18n.getMessage) {
        window.getMessage = chrome.i18n.getMessage;
    }
    else {
        var request = new XMLHttpRequest();
        request.open("GET", "_locales/en/messages.json", false);  // TODO: synchronous for now
        request.send();
        var requestStr = request.responseText;
        try {
	    messages = JSON.parse(requestStr);
            window.getMessage = fallbackGetMessage;
        }
        catch(err) {
	    console.log("Unable to read fallback messages from _locales/en_US/messages.json");
            window.getMessage = errorGetMessage;
        }
    }
}

function errorGetMessage (key, args)
{
    var msgStr = "!" + key + "!";

    var substitutions;
    if (args === undefined) {
        substitutions = [];
    }
    else if (args instanceof Array === false) {
        substitutions = [args];
    }
    else {
        substitutions = args;
    }

    msgStr += (" " + substitutions.join(" "));
    return msgStr;
}

function fallbackGetMessage (key, args)
{
    var msgStr = "";
    if (key in messages) {
        var msgData = messages[key];
        if ("message" in msgData) {
            msgStr = msgData.message;
        }
    }

    var substitutions;
    if (args === undefined) {
        substitutions = [];
    }
    else if (args instanceof Array === false) {
        substitutions = [args];
    }
    else {
        substitutions = args;
    }

    // This simple routine just substitutes args in order
    // Does not reorder and does not use the "contents" value.
    for (var i = 0; i < substitutions.length; ++i) {
        msgStr = msgStr.replace(/\$[^$]+\$/, substitutions[i]);
    }
    msgStr = msgStr.replace(/\$\$/g, "$");

    return msgStr;
}

function initStaticStrings () 
{
    var elemList = document.querySelectorAll(".i18n");
    var numElems = elemList.length;
    var elem;
    for (var i = 0; i < numElems; ++i) {
        elem = elemList[i];
        var msgStr = getMessage(elem.id);
        
        var substituted = false;
        var child = elem.firstChild;
        while (child) {
            if (child.nodeType == 3) {
                child.nodeValue = msgStr;
                substituted = true;
                break;
            }
            else {
                child = child.nextSibling;
            }
        }
        if (!substituted) {
            elem.innerText = msgStr;
        }
    }
}
