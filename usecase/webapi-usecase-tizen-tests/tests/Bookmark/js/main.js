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
var bookmarkTitle_1;
var bookmarkTitle_2;
var bookmarkURL_1;
var bookmarkURL_2;
var bookmarkObj;
var bookmarkObj_1;
var bookmarkObj_2;

function Change() {
  bookmarkTitle = "Page A";
  bookmarkObj = bookmarkObj_1;
  window.parent.window['iframe2'].location='right1.html';
  show();
  $("#firstpage").addClass("ui-disabled");
  $("#secondpage").removeClass("ui-disabled");
}

function Change2() {
  bookmarkTitle = "Page B";
  bookmarkObj = bookmarkObj_2;
  window.parent.window['iframe2'].location='right2.html';
  show();
  $("#firstpage").removeClass("ui-disabled");
  $("#secondpage").addClass("ui-disabled");
}

function add() {
  tizen.bookmark.add(bookmarkObj);
  show();
}

function show() {
  var ret = tizen.bookmark.get();
  var a = 0;
  $("#bookmarklist").html("");
  if (ret.length === 0) {
    $("#add").removeClass("ui-disabled");
    $("#remove").addClass("ui-disabled");
  } else {
    for(var i = 0; i < ret.length; i++) {
      if(bookmarkTitle == ret[i].title) {
        $("#add").addClass("ui-disabled");
        $("#remove").removeClass("ui-disabled");
        a = 1;
      } else {
        if (a == 0) {
          $("#remove").addClass("ui-disabled");
          $("#add").removeClass("ui-disabled");
        }
      }
      $("#bookmarklist").html($("#bookmarklist").html() + "<p><a>" + ret[i].title + "</a></p>");
    }
  }
}

function remove() {
  tizen.bookmark.remove(bookmarkObj);
  show();
}

$(document).ready(function() {
  bookmarkTitle_1 = "Page A";
  bookmarkURL_1 = "http://127.0.1.1:8081/opt/webapi-usecase-tizen-tests/tests/Bookmark/right1.html";
  bookmarkTitle_2 = "Page B";
  bookmarkURL_2 = "http://127.0.1.1:8081/opt/webapi-usecase-tizen-tests/tests/Bookmark/right2.html";
  bookmarkTitle = bookmarkTitle_1;
  tizen.bookmark.remove();
  bookmarkObj_1 = new tizen.BookmarkItem(bookmarkTitle_1, bookmarkURL_1);
  bookmarkObj_2 = new tizen.BookmarkItem(bookmarkTitle_2, bookmarkURL_2);
  bookmarkObj = bookmarkObj_1;
  show();
  $("#firstpage").addClass("ui-disabled");
  $("#secondpage").removeClass("ui-disabled");
  $("#add").removeClass("ui-disabled");
  $("#remove").addClass("ui-disabled");
});
