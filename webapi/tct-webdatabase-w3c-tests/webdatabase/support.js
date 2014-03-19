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
        Lei Yang <lei.a.yang@intel.com>
        Fan,Weiwei <weiwix.fan@intel.com>

*/
function PassTest(desc) {
    t.step(function() { assert_true(true, desc); });
    t.done();
}

function FailTest(desc) {
    t.step(function() { assert_true(false, desc); });
    t.done();
}

function ExistTest(obj, propertyName, desc) {
    t.step(function() { assert_exists(obj, propertyName, desc); });
    t.done();
}

function Initialize() {
}

function Deinitialize() {
}

function sleep(mSec) {
    var sTime = new Date().getTime();
    while (new Date().getTime() < sTime + mSec);
}

function GenerateDatabase() {
    try {
        if (!("openDatabase" in window))
            FailTest("openDatabase not in window");
        var now = new Date();
        var dbname = "db" + now.getTime();
        // create 1024b database on the phone
        db = openDatabase (dbname, '1.0', 'database for websql test', 1024);
        db.transaction(function (tx) {
            tx.executeSql("CREATE TABLE test_table(col_int, col_str, col_float);");
            tx.executeSql("INSERT INTO test_table VALUES (1, 'text 1', 0.1);");
            tx.executeSql("INSERT INTO test_table VALUES (2, null, 0.0);");
            tx.executeSql("INSERT INTO test_table VALUES (3, '', -0.1);");
        });
        if (!db)
            FailTest("Initiation: create db fail - testdatabase is null");
        return db;
    } catch (e) {
        FailTest("{Exception code: " + e + "}");
    }
}

function GenerateDatabaseSync() {
    try {
        var now = new Date();
        var dbname = "dbsync" + now.getTime();
        // create 2MB database on the phone
        db = openDatabaseSync (dbname, '1.0', 'database for websql test', 1024);
        db.transaction(function (tx) {
        tx.executeSql("CREATE TABLE test_table(col_int, col_str, col_float)");
        tx.executeSql("INSERT INTO test_table VALUES (1, 'text 1', 0.1)");
            tx.executeSql("INSERT INTO test_table VALUES (2, 'text 2', 1.1)");
            tx.executeSql("INSERT INTO test_table VALUES (3, 'this is column 2', 2.0)");
            tx.executeSql("INSERT INTO test_table VALUES (4, '4', 0.001)");
            tx.executeSql("INSERT INTO test_table VALUES (5, 'nameNo1', 1000.0001)");
            tx.executeSql("INSERT INTO test_table VALUES (6, 'nameNo2', 1000.0002)");
            tx.executeSql("INSERT INTO test_table VALUES (7, 'Test Here', 3.1415926)");
            tx.executeSql("INSERT INTO test_table VALUES (8, 'test here', 3.1415927)");
            tx.executeSql("INSERT INTO test_table VALUES (9, null, 0.0)");
            tx.executeSql("INSERT INTO test_table VALUES (10, '', -0.1)");
            });
        if (!db) {
            postMessage("Initiation: create db fail - testdatabase is null");
        } else {
            return db;
        }
    } catch (e) {
        postMessage("{Exception code: " + e + "}");
    }
}

/**
 * create db with PK constraint
 */
function openDB() {
    try {
        var now = new Date();
        var dbname = "db" + now.getTime();
        db = openDatabase(dbname, '1.0', 'database for websql test', 1024);
        db.transaction(function (tx) {
            tx.executeSql("CREATE TABLE test_table(col_int PRIMARY KEY, col_str, col_float);");
        });
        if (!db) {
            FailTest("Initiation: create db fail - testdatabase is null");
            return;
        } else {
            return db;
        }
    } catch (e) {
        FailTest("{Exception code: " + e.message + "}");
    }
}

/**
* create Sync db with PK constraint
*/
function openDBSync() {
    try {
        var now = new Date();
        var dbname = "db" + now.getTime();
        db = openDatabaseSync(dbname, '1.0', 'database for websql test', 1024);
        db.transaction(function (tx) {
            tx.executeSql("CREATE TABLE test_table(col_int PRIMARY KEY, col_str, col_float);");
        });
        if (!db) {
            postMessage("Create db fail - testdatabase is null");
        } else {
            return db;
        }
    } catch (e) {
        postMessage("{Exception code: " + e.message + "}");
    }
}
