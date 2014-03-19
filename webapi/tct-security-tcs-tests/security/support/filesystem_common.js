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



*/

var TEST_ROOT_LOCATION = "downloads";

var UNKNOWN_ERR         = "UnknownError";
var TYPE_MISMATCH_ERR   = "TypeMismatchError";
var IO_ERR              = "IOError";
var INVALID_VALUES_ERR  = "InvalidValuesError";
var SECURITY_ERR        = "SecurityError";
var NOT_FOUND_ERR       = "NotFoundError";

var globalCounter = 1;

function isFileObject(obj) {
    return true;
}

function isFile(obj) {
    return (isFileObject(obj) && !obj.isDirectory);
}

function isDir(obj) {
    return (isFileObject(obj) && obj.isDirectory);
}

function isFilestream(obj) {
    return true;
}

function deleteDirectory(parent, dir) {
    function onError(err) {
        assert_false("deleteDirectory() [" + err.name + "]");
    }

    function onSuccess() {
    }
    parent.deleteDirectory(dir.fullPath, true, onSuccess, onError);
}

function deleteFile(parent, file) {
    function onError(err) {
        assert_false("deleteFile [" + err.name + "]");
    }

    function onSuccess() {
    }
    parent.deleteFile(file.fullPath, onSuccess, onError);
}

// For common behaviour use resolve_root_location
function resolve_root(on_success_callback, on_error_callback) {
    tizen.filesystem.resolve(TEST_ROOT_LOCATION, on_success_callback, on_error_callback);
}

function resolve_root_location(handler) {
    function on_resolve_error(err) {
        assert_false("resolve error: [" + err.name + "]");
    }

    function on_resolve_success(file) {
        assert_true(isFileObject(file), "resolve()");
        handler(file);
    }
    tizen.filesystem.resolve(TEST_ROOT_LOCATION, on_resolve_success, on_resolve_error);
}

function getCurrentTestName() {
    if (typeof(this_test) === 'undefined') {
        return t.name;
    } else {
        return this_test.name;
    }
}

function getFileName(fileName) {
    var nr = Math.floor(Math.random() * 1000), date = new Date();
    if (!fileName) {
        return "test_tizen_filesystem_file_" + nr + "_" + (globalCounter++) + "_"
             + date.getMinutes() + date.getSeconds() + date.getMilliseconds();
    } else {
        return "test_" + getCurrentTestName() + "_" + fileName;
    }
}

function getDirName(dirName) {
    var nr = Math.floor(Math.random() * 1000), date = new Date();
    if (!dirName) {
        return "test_tizen_filesystem_dir_" + nr + "_" + (globalCounter++) + "_"
             + date.getMinutes() + date.getSeconds() + date.getMilliseconds();
    } else {
        return "test_" + getCurrentTestName() + "_" + dirName;
    }
}

function createFileForParent(parent) {
    var result = parent.createFile(getFileName());
    assert_true(isFile(result), "createFile");
    return result;
}

function createDirForParent(parent) {
    var result = parent.createDirectory(getDirName());
    assert_true(isDir(result), "createDirectory()");
    return result;
}

function deleteFileAndDone(test, file) {
    if(file === undefined) {
        throw new Error("deleteFileAndDone: file is undefined");
    }
    if(file.parent === null){
        throw new Error("deleteFileAndDone: parent directory is null");
    }
    file.parent.deleteFile(file.fullPath,
        test.step_func(function() {
            test.done();
        }),
        test.step_func(function(err) {
            assert_unreached("deleteFileAndDone: delete onError " + err.message);
        }));
}

function prepareForTesting(test, filesNames, successCallback) {
    var i, j, removedCounter = 0, resolveSuccess, resolveError, fileToRemove,
        deleteSuccess, deleteError, parentName, childName, filesDictionary = [];

    deleteSuccess = test.step_func(function () {
        if (++removedCounter === filesNames.length) {
            test.step_func(successCallback)();
        }
    });

    deleteError = test.step_func(function (error) {
        if ((error.name === "NotFoundError") && (++removedCounter === filesNames.length)) {
            test.step_func(successCallback)();
        } else if (error.name !== "NotFoundError") {
            assert_unreached("delete() error callback invoked: name:" + error.name + "msg:" + error.message);
        }
    });

    resolveSuccess = test.step_func(function (dir) {
        for (j = 0; j < filesDictionary[dir.path].length; j++) {
            try {
                fileToRemove = dir.resolve(filesDictionary[dir.path][j]);
                if (fileToRemove.isDirectory) {
                    dir.deleteDirectory(fileToRemove.fullPath, true, deleteSuccess, deleteError);
                } else {
                    dir.deleteFile(fileToRemove.fullPath, deleteSuccess, deleteError);
                }
            } catch (e) {
                if ((e.name === "NotFoundError") && (++removedCounter === filesNames.length)) {
                    test.step_func(successCallback)();
                }
            }
        }
    });

    resolveError = test.step_func(function (error) {
        assert_unreached("resolve() error callback invoked: name:" + error.name + "msg:" + error.message);
    });

    for (i = 0; i < filesNames.length; i++) {
        parentName = filesNames[i].substring(0,filesNames[i].indexOf("/"));
        childName = filesNames[i].substring(filesNames[i].indexOf("/") + 1, filesNames[i].length);
        if (!filesDictionary[parentName]) {
            filesDictionary[parentName] = [];
        }
        filesDictionary[parentName].push(childName);
    }

    for (i in filesDictionary) {
        if (filesDictionary.hasOwnProperty(i)) {
            tizen.filesystem.resolve(i, resolveSuccess, resolveError, "rw");
        }
    }
}

setup({timeout: 90*1000});
