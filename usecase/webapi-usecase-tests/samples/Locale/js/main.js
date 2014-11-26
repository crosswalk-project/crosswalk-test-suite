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
var output = document.getElementById("output");
$("#setlocale_btn").live("click",function() {
	output.value = tizen.Locale.setLocale("ang");
});
$("#getlocale_btn").live("click",function() {
	output.value = tizen.Locale.getLocale();
});

/*function handle(button, callback) {
  var b = document.getElementById(button);
  alert(b);
  if(b){
  b.live("click", callback);
  }
}
function onErrorCallback(error) {
  output.value += '\n An error occurred: ' + error.message + '\n';
  output.scrollTop = output.scrollHeight;
}
handle("locale_btn", function() {
  var count = 0;
  var id = tizen.systeminfo.addPropertyValueChangeListener("LOCALE", function(locale) {
    output.value += '\n Property Locale changed.';
    output.value += '\n\t language: ' + locale.language;
    output.value += '\n\t country: ' + locale.country;
    count += 1;
    if (count == 3) {
      output.value += '\n Maximum listen times(3) reached. Remove listener with id = ' + id;
      output.scrollTop = output.scrollHeight;
      count = 0;
      tizen.systeminfo.removePropertyValueChangeListener(id);
    }
  });
  tizen.systeminfo.getPropertyValue("LOCALE", function(locale) {
    output.value += '\n Get property LOCALE returned.';
    output.value += '\n\t language: ' + locale.language;
    output.value += '\n\t country: ' + locale.country;
    output.scrollTop = output.scrollHeight;
  }, onErrorCallback);
});
handle("getlocale_btn", function() {
	output.value = tizen.Locale.getLocale();
}, onErrorCallback);
*/

