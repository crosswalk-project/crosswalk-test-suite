## Usecase Design

This sample demonstrates cordova app can get the android device language correctly by using window.navigator.language in js script

This usecase covers following methods:

* $ cordova create Language com.example.language Language

* $ cordova platform add android

* $ cordova plugin add ../cordova-plugin-crosswalk-webview

* $ cordova build android

* alert(window.navigator.language);
