## Usecase Design

This sample demonstrates XWALK-2394 feature basic functionalities, include:

* Temporary directories are created in "/tmp" directory when building, and removed if the building exits (whether successfully or via exception)
* A working project directory can be created during the build for use later to create valid APKs
* APK creation can be skipped if developer only wants to create a project directory for use later

This usecase covers following methods:

* $ python make_apk.py --[manifest|app-url|app-root|app-url]
* $ python make_apk.py --manifest --project-dir
  $ ant release -f build.xml
* $ python make_apk.py --project-dir --project-only
