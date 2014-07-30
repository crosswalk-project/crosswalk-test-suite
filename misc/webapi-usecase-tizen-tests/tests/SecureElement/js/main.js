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
        Liu, Xin <xinx.liu@intel.com>

*/

function getReadersName() {
  try {
    //A success callback that is invoked when a list of available Secure Element readers is retrieved.
    tizen.seService.getReaders(getReadersSuccess, getReadersError);

    //Registers a callback function that is invoked when an available Secure Element reader is detected
    tizen.seService.registerSEListener(onSEReady, onSENotReady);

    tizen.seService.shutdown();
  } catch (err) {
      console.log (err.name + ": " + err.message);
  }
}

function getReadersSuccess(readers) {
  var readernames = "Reader Name : ";
  for (var i = 0; i < readers.length; i++) {
    if (readers[i].isPresent) {
      readernames  +=  readers[i].getName() + " open Session Success:";
      readers[i].openSession(function(session) {
        readernames += !session.isClosed + ", ";
      }, openSessionError);
    }
  }
  jQuery("#readersName").html(readernames);
}

function getReaderserror(error) {
  jQuery("#readersName").html("Error Name: " + error.name);
}

function openSessionError(error) {
  jQuery("#readersName").html("Error Name: " + error.name);
}

function onSEReady(reader) {
  jQuery("#readyStatus").html(reader.getName() + "is ready.");
}

function onSENotReady(reader) {
  jQuery("#readyStatus").html(reader.getName() + "is not ready.");
}
