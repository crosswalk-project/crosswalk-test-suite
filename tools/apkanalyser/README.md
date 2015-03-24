# Apk Analyser
Android APK Analyser especially for Crosswalk apps.

# Platform
* Host OS: Linux Ubuntu
* For Mac OSX users, you may need to run this command to resolve the python dependency:
`sudo easy_install lxml`

# Environment
* Java JDK 1.5 or greater http://www.oracle.com/technetwork/java/javase/downloads/index.html
* Python 2.7 https://www.python.org/download/
* Android SDK installed http://developer.android.com
* Install and set environment for apktool: http://ibotpeaches.github.io/Apktool/
* Update the jQuery path in result/apk-analyser-result.xsl in case you didn't clone the whole crosswalk-test-suite: `<script src='https://code.jquery.com/jquery-2.1.3.min.js'></script>`

# How to Run
A.
  1. `cd <pathto>/apk-analyser`
  2. `Put Android apks into "apks" folder`
  3. `python main.py`

B.
  1. `cd <pathto>/apk-analyser`
  2. `python main.py -p <pathto>/xxx.apk` or `python main.py -p <pathto>/<apk folder>`
	
C.
  1. `python <pathto>/apk-analyser/main.py -p <pathto>/xxx.apk` or `python <pathto>/apk-analyser/main.py -p <pathto>/<apk folder>`
	
# Review Results
* Get results in `<pathto>/apk-analyser/result` folder.
* If run the third method, please copy "`apk-analyser/result/apk-analyser-result.xsl`" to `<current dir>/result` folder.
* Launch local `apk-analyser-result_<date>_<time>.xml` by Firefox or IE. For Google Chrome`[1]`, need to access `.xml` and `.xsl` via url on web server.

`[1]` Google Chrome is unable to perform an xsl transform on a local xml file due to a security concern that blocking XML files from accessing local XSLT files in the same directory.
