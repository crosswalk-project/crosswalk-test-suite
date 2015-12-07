## Usecase Design

This sample demonstrates XWALK-1947 feature basic functionalities, include:

* extension_manager.py can run with parameters: add/search/disable/enable/remove

This usecase covers following main methods:

* $ ./extension_manager.py --add=https://github.com/crosswalk-project/crosswalk-android-extensions.git
* $ ./extension_manager.py --search=crosswalk*
* $ ./extension_manager.py --disable=crosswalk*
* $ ./extension_manager.py --enable=crosswalk*
* $ ./extension_manager.py --remove=crosswalk-android-extensions
