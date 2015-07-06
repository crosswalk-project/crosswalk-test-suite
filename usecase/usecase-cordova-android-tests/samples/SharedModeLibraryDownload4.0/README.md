## Usecase Design

This sample demonstrates SharedModeLibraryDownload feature basic functionalities, include:

* The shared mode app using '<meta-data android:name="xwalk_apk_url" android:value="http://host/XWalkRuntimeLib.apk" />' in the AndroidManifest.xml can download crosswalk library apk after launch it

This usecase covers following method:

* $ cordova create SharedModeLibraryDownload com.example.sharedModeLibraryDownload SharedModeLibraryDownload

* $ cordova platform add android

* $ cordova plugin add ../cordova-plugin-crosswalk-webview

* $ cordova build android
