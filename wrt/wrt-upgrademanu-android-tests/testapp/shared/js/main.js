/*
Copyright (c) 2015 Intel Corporation.

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
        Wang, Hongjuan <hongjuanx.wang@intel.com>

*/

$(document).ready(function () {

  //LocalStorage
  $("#setLocalstorage").click(function(){
    var msg = $("#msg").val();
    if(msg){
      localStorage.setItem("data", msg);
      $('#testDiv').text($('#testDiv').text() + '\nSave LocalStorage value successfully: ' + msg);
    }
  })

  $("#getLocalstorage").click(function(){
    var msg = localStorage.getItem("data");
    if(msg)
    {
      $('#testDiv').text($('#testDiv').text() + '\nGet LocalStorage value: ' + msg);
    }
  })

  //IndexDB
  var myDB={
      name:'test',
      version:1,
      db:null
    };

  function openDB (name,version) {
    var version=version || 1;
    var request=window.indexedDB.open(name,version);
    request.onerror=function(e){
      $('#testDiv').text($('#testDiv').text() + '\nError message: ' + e.currentTarget.error.message);
    };
    request.onsuccess=function(e){
      myDB.db=e.target.result;
    };
    request.onupgradeneeded=function(e){
      var db=e.target.result;
      if(!db.objectStoreNames.contains('students')){
        db.createObjectStore('students',{keyPath:'id'});
      }
      //$('#testDiv').text($('#testDiv').text() + '\nDB version changed to '+version);
    };
  }

  function addData(name, db, storeName){
    var transaction=db.transaction(storeName,'readwrite');
    var store=transaction.objectStore(storeName);
    store.delete(1)
    var student = {id:1, value: $('#msg').val()};
    store.add(student);
    $('#testDiv').text($("#testDiv").text() + '\nSave Indexdb value successfully:  ' + student.value);
  }

  openDB(myDB.name, myDB.version);

  function getDataByKey(db,storeName,value){
    var transaction=db.transaction(storeName,'readwrite');
    var store=transaction.objectStore(storeName);
    var request=store.get(value);
    request.onsuccess=function(e){
      var student=e.target.result;
      $('#testDiv').text($('#testDiv').text() + '\nGet Indexdb vaule: '+ student.value);
    };
  }

  $('#setIndexdb').click(function(){
    addData(myDB.name, myDB.db, 'students');
  })

  $('#getIndexdb').click(function(){
    getDataByKey(myDB.db, 'students',1);
  })

  //Web SQL Database
  var db = openDatabase('testDB', '1.0', 'Test DB', 1024);
  var msg;

  $('#setWebsql').click(function(){
    msg = $('#msg').val();
    db.transaction(function (context) {
       context.executeSql('CREATE TABLE IF NOT EXISTS testTable (id unique, name)');
       context.executeSql('DELETE FROM testTable WHERE id=0');
       context.executeSql('INSERT INTO testTable (id, name) VALUES (0, "' + msg + '")');
       $('#testDiv').text($('#testDiv').text() + '\nSave Web SQL Database value successfully: ' + msg);
     })
   })

  $('#getWebsql').click(function(){
    db.transaction(function (context) {
        context.executeSql('SELECT * FROM testTable', [], function (context, results) {
          $('#testDiv').text($('#testDiv').text() + '\nGet Web SQL Database vaule: '+ results.rows.item(0).name);
        })
     })
  })

})
