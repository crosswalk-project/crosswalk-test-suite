## Usecase Design

This sample demonstrates ConfigUrl feature basic functionalities, include:

* The shared mode app can download crosswalk library apk after configure

This usecase covers following method:

* $ python make_apk.py --mode=shared --xwalk-apk-url=http://host/XWalkRuntimeLib.apk
* Add '"xwalk-apk-url": "http://host/XWalkRuntimeLib.apk"' to manifest.json
* Add '&lt;meta-data android:name="xwalk_apk_url" android:value="http://host/XWalkRuntimeLib.apk" &gt;' to AndroidManifest.xml
