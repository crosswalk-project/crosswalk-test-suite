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
        Krzysztof Lachacz <k.lachacz@samsung.com>
        Junghyuk Park <junghyuk.park@samsung.com>
*/

var TIMEOUT_ASYNC_TEST = 30000;
setup({timeout: TIMEOUT_ASYNC_TEST});

var SHARED_STORAGE_PATH = "TESTER-HOME-DIR/content";
var TEST_CONTENT_DIR_PATH = "TESTER-HOME-DIR/content/tct-content-tizen-tests/";

var TEST_CONTENT_IMAGES = [
    "tct-content-tizen-tests_image_default.jpg",
    "tct-content-tizen-tests_image_geolocation.jpg",
    "tct-content-tizen-tests_image_orientation_1.jpg",
    "tct-content-tizen-tests_image_orientation_2.jpg",
    "tct-content-tizen-tests_image_orientation_3.jpg",
    "tct-content-tizen-tests_image_orientation_4.jpg",
    "tct-content-tizen-tests_image_orientation_5.jpg",
    "tct-content-tizen-tests_image_orientation_6.jpg",
    "tct-content-tizen-tests_image_orientation_7.jpg",
    "tct-content-tizen-tests_image_orientation_8.jpg"
]

var TEST_CONTENT_AUDIOS = [
    "tct-content-tizen-tests_audio_default.mp3",
    "tct-content-tizen-tests_audio_lyrics.mp3",
    "tct-content-tizen-tests_audio_no_tag.mp3"
]

var TEST_CONTENT_VIDEOS = [
    "tct-content-tizen-tests_video.mp4",
    "tct-content-tizen-tests_video_tagged.mp4"
]

function setup_contents(async_test, onscaned) {
    var contents = [];
    contents = contents.concat(TEST_CONTENT_IMAGES);
    contents = contents.concat(TEST_CONTENT_AUDIOS);
    contents = contents.concat(TEST_CONTENT_VIDEOS);

    function scanFiles(files, oncompleted) {
        var file = files.shift();

        tizen.content.scanFile(
            "file://"+TEST_CONTENT_DIR_PATH+file,
            async_test.step_func(function (content) {
                if (files.length) {
                    scanFiles(files, oncompleted);
                } else {
                    oncompleted();
                }
            }),
            async_test.step_func(function (error) {
                assert_unreached("setup_contents fails: " + error.name + " with message: " + error.message);
            })
        );
    }

    scanFiles(contents, onscaned);
}

function check_content_object(content) {
    assert_type(content.editableAttributes, "array", "editableAttributes should be an array");
    assert_type(content.id, "string", "id should be a string");
    assert_type(content.name, "string", "name shoud be a string");
    assert_type(content.type, "string", "type should be a string");
    assert_type(content.mimeType, "string", "mimeType should be a string");
    assert_type(content.title, "string", "title should be a string");
    assert_type(content.contentURI, "string", "contentURI should be a string");
    assert_type(content.size, "number", "size should be a number");
    assert_type(content.rating, "number", "rating should be a number");
    if(content.thumbnailURIs !== null) {
        assert_type(content.thumbnailURIs, "array", "thumbnailURIs should be an array");
    }
    if(content.releaseDate !== null) {
        assert_type(content.releaseDate, "date", "releaseDate should be a date");
    }
    if(content.modifiedDate !== null) {
        assert_type(content.modifiedDate, "date", "modifiedDate should be a date");
    }
    if(content.description !== null) {
        assert_type(content.description, "string", "description should be a string");
    }
}

function prepare_file_for_scan(addedImagePath, onCopySuccess) {
    var onCopyError = t.step_func(function (error) {
        assert_unreached("Failed to copy a file to " + addedImagePath + " with message: " + error.message);
    });

    var copyContentFile = t.step_func(function () {
        tizen.filesystem.resolve(
            "file://" + TEST_CONTENT_DIR_PATH,
            function (contentDirectory){
                contentDirectory.copyTo(TEST_CONTENT_DIR_PATH + TEST_CONTENT_IMAGES[0], addedImagePath, true, onCopySuccess, onCopyError);
            },
            function (error) {
                assert_unreached("Failed to resolve a directory: " + error.message);
            },
            "r"
        );
    });

    var onDeleteSuccess = t.step_func(function () {
        tizen.content.scanFile("file://" + addedImagePath, function (){
            copyContentFile();
        });
    });

    var onDeleteError = t.step_func(function () {
        copyContentFile();
    });

    tizen.filesystem.resolve(
        "file://" + SHARED_STORAGE_PATH,
        function (directory){
            var sharedDirectory = directory;
            sharedDirectory.deleteFile(addedImagePath, onDeleteSuccess, onDeleteError);
        },
        function (error) {
            assert_unreached("Failed to resolve a directory: " + error.message);
        },
        "rw"
    );
}
