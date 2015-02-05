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
    Piotr Szydelko <p.szydelko@samsung.com>

*/

var TEST_DIR = "file://TESTER-HOME-DIR/content/tct-appcontrol-tizen-tests/";
var TEST_URL_HTTP = "http://www.tizen.org";
var TEST_URL_HTTPS = "https://www.tizen.org";

var TEST_FILE_IMAGE_BMP = TEST_DIR + "webapi-tizen-appcontrol-test_image.bmp";
var TEST_FILE_IMAGE_JPEG = TEST_DIR + "webapi-tizen-appcontrol-test_image.jpeg";
var TEST_FILE_IMAGE_GIF = TEST_DIR + "webapi-tizen-appcontrol-test_image.gif";
var TEST_FILE_IMAGE_PNG = TEST_DIR + "webapi-tizen-appcontrol-test_image.png";
var TEST_FILE_SOUND_AAC = TEST_DIR + "webapi-tizen-appcontrol-test_sound.aac";
var TEST_FILE_SOUND_AMR = TEST_DIR + "webapi-tizen-appcontrol-test_sound.amr";
var TEST_FILE_SOUND_MP3 = TEST_DIR + "webapi-tizen-appcontrol-test_sound.mp3";
var TEST_FILE_SOUND_WAV = TEST_DIR + "webapi-tizen-appcontrol-test_sound.wav";
var TEST_FILE_VIDEO_MP4 = TEST_DIR + "webapi-tizen-appcontrol-test_video.mp4";
var TEST_FILE_VIDEO_3GPP = TEST_DIR + "webapi-tizen-appcontrol-test_video.3gp";

function checkAppControls(this_test, appControls) {
    var onSuccess, onError, currentAppControl, appControlDesc;

    onSuccess = this_test.step_func(function(informationArray, appControl) {
        assert_true(Array.isArray(informationArray), "informationArray should be Array");
        assert_not_equals(informationArray.length, 0, "Number of application found for: " + appControlDesc);

        // check next from the list or report success if list is empty
        if(appControls.length === 0) {
            return this_test.done();
        } else {
            checkAppControls(this_test, appControls);
        }
    });

    onError = this_test.step_func(function(error) {
        assert_unreached("onError: " + error.message);
    });

    currentAppControl = appControls.shift();
    appControlDesc = '(' + currentAppControl.operation + " " + currentAppControl.uri + " " + currentAppControl.mime + ')';

    tizen.application.findAppControl(currentAppControl, onSuccess, onError);
}
