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
var bookmarkTitle;
var bookmarkURL;
var bookmarkObj;

function Change() {
  bookmarkTitle = "right1.html";
  bookmarkURL = "http://127.0.1.1:8081/opt/webapi-usecase-tizen-tests/tests/Bookmark/right1.html";
  window.parent.window['iframe2'].location='right1.html';
  $("#firstpage").addClass("ui-disabled");
  $("#secondpage").removeClass("ui-disabled");
}

function Change2() {
  bookmarkTitle = "right2.html";
  bookmarkURL = "http://127.0.1.1:8081/opt/webapi-usecase-tizen-tests/tests/Bookmark/right2.html";
  window.parent.window['iframe2'].location='right2.html';
  $("#firstpage").removeClass("ui-disabled");
  $("#secondpage").addClass("ui-disabled");
}

function add() {
  bookmarkObj = new tizen.BookmarkItem(bookmarkTitle, bookmarkURL);
  tizen.bookmark.add(bookmarkObj);
  show();
}

function show() {
  var ret = tizen.bookmark.get();
  if (ret.length === 0) {
    $("#bookmarklist").html("");
    $("#add").removeClass("ui-disabled");
    $("#remove").addClass("ui-disabled");
  } else {
    for(var i = 0; i < ret.length; i++) {
      if(bookmarkTitle == ret[i].title) {
        $("#add").addClass("ui-disabled");
        $("#remove").removeClass("ui-disabled");
      } else {
        $("#remove").addClass("ui-disabled");
        $("#add").removeClass("ui-disabled");
      }
      $("#bookmarklist").html("<p><a>" + ret[i].title + "</a></p>" + $("#bookmarklist").html());
    }
  }
}

function remove() {
  tizen.bookmark.remove(bookmarkObj);
  show();
}

$(document).ready(function() {
  bookmarkTitle = "right1.html";
  bookmarkURL = "http://127.0.1.1:8081/opt/webapi-usecase-tizen-tests/tests/Bookmark/right1.html";
  tizen.bookmark.remove();
  $("#firstpage").addClass("ui-disabled");
  $("#secondpage").removeClass("ui-disabled");
  $("#add").removeClass("ui-disabled");
  $("#remove").addClass("ui-disabled");
});
