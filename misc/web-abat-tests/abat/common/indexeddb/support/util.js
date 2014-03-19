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
 NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
 EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

 Authors:
         Fan,Weiwei < weiwix.fan@intel.com>

*/
    var dbname = "indexdb";
    var db = null;
    var dbVersion = 1; // version of the db
    var objectStoreName = "objectstore";
    var record = {key : 1, property : "data"};
    var indexName = "index";
    var timeout = 3000;

    function initial() {
        if (!window.indexedDB) {
            if (window.msIndexedDB) {
                window.indexedDB = window.msIndexedDB;
            } else if (window.mozIndexedDB) {
                window.indexedDB = window.mozIndexedDB;
            } else if (window.webkitIndexedDB) {
                window.indexedDB = window.webkitIndexedDB;
                IDBTransaction = window.webkitIDBTransaction;
                IDBFactory = window.webkitIDBFactory;
                IDBCursor = window.webkitIDBCursor;
                IDBDatabaseException = window.webkitIDBDatabaseException;
                IDBIndex = window.webkitIDBIndex;
                IDBObjectStore = window.webkitIDBObjectStore;
                IDBRequest = window.webkitIDBRequest;
                IDBKeyRange = window.webkitIDBKeyRange;
            }
        }

        if (!self.indexedDBSync) {
            if (self.msIndexedDBSync) {
                self.indexedDBSync = self.msIndexedDBSync;
            }else if (self.mozIndexedDBSync) {
                self.indexedDBSync = self.mozIndexedDBSync;
            }else if (self.webkitIndexedDBSync) {
                self.indexedDBSync = self.webkitIndexedDBSync;
                IDBTransactionSync = self.webkitIDBTransactionSync;
            }
        }
    }
    function closeDB(db) {
        if (db) {
            db.close();
            db = null;
        }
        window.indexedDB.deleteDatabase(dbname);
    }
    function fail(msg) {
        t.step(function () {
            assert_true(false, msg);
        });
        t.done();
    }
    function pass(msg) {
        t.step(function () {
            assert_true(true, msg);
        });
        t.done();
    }
	function open_request_error(event) {
		assert_unreached("Open request error: " + event.target.error.name);
	}
    initial();
