 /**
 Copyright (c) 2015 Intel Corporation.

 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions are met:

 * Redistributions of works must retain the original copyright notice, this
   list of conditions and the following disclaimer.
 * Redistributions in binary form must reproduce the original copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
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
         Hongjuan, Wang<hongjuanx.wang@intel.com>
**/

var test = "Cordova Mobile Spec Test";

//Alert location button
UIATarget.onAlert = function onAlert(alert) {
  var title = alert.name(); 
  UIALogger.logWarning("Alert with title '" + title + "' encountered!"); 
  msg = alert.scrollViews()[0].staticTexts().firstWithPredicate("name beginswith 'Allow'").name()
  if (title == msg) {
    UIALogger.logMessage("Allow access location");
    alert.buttons()[1].tap();
    return true;
  }
  return false;
}

// open the index.html
var target = UIATarget.localTarget();
var app = target.frontMostApp();
var window = app.mainWindow();
UIALogger.logStart(test);

var lnk = window.scrollViews()[1].webViews()[0].links()["Plugin Tests (Automatic and Manual)"];
target.captureScreenWithName(test);
UIALogger.logMessage(lnk.name());
lnk.tap();
 
// Open second page --> tap link "Plugin Tests (Automatic and Manual)"
//Start Auto Tests
var target = UIATarget.localTarget();
var app = target.frontMostApp();
var window = app.mainWindow();

var btn = window.scrollViews()[1].webViews()[0].staticTexts()["Auto Tests"];
UIALogger.logMessage(btn.name());
btn.tap();
target.delay(100);
//app.logElementTree();

var wv = window.scrollViews()[1].webViews()[0];
var sts = window.scrollViews()[1].webViews()[0].staticTexts();
wv.logElementTree();

