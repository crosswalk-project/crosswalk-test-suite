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

var FILE_AND_DIR_NAME_PREFIX = "tizen_WebAPI_test_";
var UNKNOWN_ERR              = "UnknownError";
var TYPE_MISMATCH_ERR        = "TypeMismatchError";
var IO_ERR                   = "IOError";
var INVALID_VALUES_ERR       = "InvalidValuesError";
var SECURITY_ERR             = "SecurityError";
var NOT_FOUND_ERR            = "NotFoundError";

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
        assert_false("deleteDirectory() [" + err.name + "]", "directory wasn't deleted");
    }

    function onSuccess() {
    }
    parent.deleteDirectory(dir.fullPath, true, onSuccess, onError);
}

function deleteFile(parent, file) {
    function onError(err) {
        assert_false("deleteFile [" + err.name + "]", "file wasn't deleted");
    }

    function onSuccess() {
    }
    parent.deleteFile(file.fullPath, onSuccess, onError);
}

function resolve_root_location(handler) {
    function on_resolve_error(err) {
        assert_false("resolve error: [" + err.name + "]", "error during resolving the root location");
    }

    function on_resolve_success(file) {
        assert_true(isFileObject(file), "resolve()");
        handler(file);
    }
    tizen.filesystem.resolve(TEST_ROOT_LOCATION, on_resolve_success, on_resolve_error);
}

function getFileName(fileName) {
    return FILE_AND_DIR_NAME_PREFIX + "_" + fileName;
}

function getDirName(dirName) {
    return FILE_AND_DIR_NAME_PREFIX + "_" + dirName;
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

function prepareForTesting(test, successCallback) {
    var i, j, toRemoveCounter = 0, dirCounter = 0, deleteSuccess, deleteError,
        resolveSuccess, resolveError, listFilesSuccess, listFilesError,
        filterRegExp = new RegExp("^" + FILE_AND_DIR_NAME_PREFIX),
        rootDirectories = ["documents", "images", "music", "videos", "downloads"];

    deleteError = test.step_func(function (error) {
        assert_unreached("delete() error callback invoked: name:" + error.name + "msg:" + error.message);
    });

    deleteSuccess = test.step_func(function () {
        if (--toRemoveCounter === 0) {
            test.step_func(successCallback)();
        }
    });

    listFilesSuccess = test.step_func(function (files) {
        dirCounter++;
        for (j = 0; j < files.length; j++) {
            if (files[j].name.search(filterRegExp) > -1) {
                toRemoveCounter++;
                if (files[j].isDirectory) {
                    files[j].parent.deleteDirectory(files[j].fullPath, true, deleteSuccess, deleteError);
                } else {
                    files[j].parent.deleteFile(files[j].fullPath, deleteSuccess, deleteError);
                }
            }
        }
        if ((dirCounter === rootDirectories.length) && (toRemoveCounter === 0)) {
            test.step_func(successCallback)();
        }
    });

    listFilesError = test.step_func(function (error) {
        assert_unreached("listFiles() error callback invoked: name:" + error.name + "msg:" + error.message);
    });

    resolveSuccess = test.step_func(function (dir) {
        dir.listFiles(listFilesSuccess, listFilesError);
    });

    resolveError = test.step_func(function (error) {
        assert_unreached("resolve() error callback invoked: name:" + error.name + "msg:" + error.message);
    });

    for (i =0; i < rootDirectories.length; i++) {
        tizen.filesystem.resolve(rootDirectories[i], resolveSuccess, resolveError, "rw");
    }
}

function checkOwnProperties(fileHandle) {
    var i, len, fileProperties = ["parent", "readOnly", "isFile", "isDirectory", "created", "modified", "path",
                                  "name", "fullPath", "fileSize", "length"];
    for (i = 0, len = fileProperties.length; i < len; i++) {
        assert_own_property(fileHandle, fileProperties[i], "object does not have its own " + fileProperties[i] + " property");
    }
}
