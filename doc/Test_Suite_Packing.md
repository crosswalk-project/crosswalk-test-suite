=Overview=
Web tests suite involves new packing solution to replace the old Shell and "autoconf" based packing structure. With this update:
*No need add "Makefile.am" for each folder
*No need "autoconf"  solution as it is hard to build/pack resource for multiple platforms
*All suites share one pack tool, suite just need a special JSON file for package resource organization
*A overall "version" file used by all suites' release
*Scalable options for tools/install destination/package source/packing debug ...
*Better experience for log and multiple packing processes
*Strict error handling
Here is the typical web test suite's structure:

[[File:crosswalk-test-srouce-new.jpg]]

=Tests Resource=
==Tests Source Code==
The new pack tool don't impact the existing tests source structure or just need minor changes for the existing source which has improper structure.

=="tests.xml"==
Still follow testkit-lite tests.xml scheme definition.

=="suite.json"==
New tests package specification file, provides the tests package's architecture in different package types. The pack tool will parse it for package generation.

{| class="wikitable"
|-
! Key !! Mandatory !! Desc !! Example !! Note
|-
| "pkg-name" || No || Package name || "pkg-name": "web-demo-tests" || 
|-
| "pkg-blacklist" || No || the common black list used by final zip package and top level package app || "pkg-blacklist":["pack.py", "COPYING"] || pack.py will handle some app framework files by itself, e.g. "icon.png","config.xml", so you just need add those files to thois common black list. The value of the list member can support "regular expression", e.g. "test/*.py" will add all files which have ".py" suffix in "test" folder to the black list.
|-
| "pkg-list" || Yes ||The detailed package type which the pack.py supported || ||the package should be the one of "apk", "xpk", "wgt", "apk-aio", "cordova". The package type can share a package json section, e.g. "apk,cordova", or use single section, e.g. "wgt"
|-
| "blacklist" || No || The black list used by the parent package or app || "blacklist":["specname/testapps","specname/testscripts"]|| Effective on relative path， e.g. package's "blacklist" acts on suite folder(in final zip package, is "/"), and package top level app's "blacklist" acts on suite folder(in final zip package, is "/opt/suite-name/" folder). but for sub apps' "blacklist", it act on sub apps source folder(in sub app package, is "/").The value of the list member can support "regular expression", e.g. "test/*.py" will add all files which have ".py" suffix in "test" folder to the black list.
|-
| "copylist"  || No || The copy list used by the parent package or app || "copylist": {"inst.apk.py": "inst.py","specname/testscripts": "specname/testscripts","specname/testscripts/app01/webdriver.xw_android.cfg": "specname/testscripts/app01/webdriver.cfg"}|| Effective on relative path too, just like "blacklist",but not support "regular expression". Support MARCO "PACK-TOOL-ROOT" to replace the prefix of "relative path", the "PACK-TOOL-ROOT" is the tools path(point out by "--tools" or default "suite-name/../../tools", e.g. "PACK-TOOL-ROOT/crosswalk/":"crosswalk" will copy crosswalk folder under tools to "crosswalk" folder of the package/app source tree)
|-
| "pkg-app" || No || The package's top level app || || Only some WebAPI test packages need this top level app
|-
| "subapp-list" || No || The black list used by the parent package or app|| || The key of the number should be the app's relative path in suite source folder
|-
| "app-dir" || No || Specify which directory will be packed as a sub app||"app-dir": "path/to/folder" || The sub-app will use the key in "subapp-list" if no "app-dir" provided in json by default
|-
| "app-name" || No || sub app name|| "app01" || the app will use the parent folder name if no "app-name" provided in json
|-
| "sign-flag" || No|| the sign flag of the wgt app|| "sign-flag": "true" || only used by wgt package type
|-
| "install-path" || No|| the app's installation folder in the final zip package || "install-path":"haha/kkkk"|| will use the "/" of final zip package if no "install-path" provided
|-
| "hosted-app" || No || point out if the package app is hosted app|| "hosted-app":"true" || Only use by package app("pkg-app"), the pack.py will update package app's index.html to point to remote http server webrunner
|-
| "all-apps" || No || the pack.py will pack all sub folders one by one automatically if the value is "true"|| "all-apps": "true" || The apps' name will use parent folder name
|-
| "apk-type" || No || point out the apk type, the type should one of "HOSTEDAPP", "MANIFEST" and "COMMANDLINE". the default apk type is "COMMANDLINE"
*"MANIFEST": will pack apk with default manifest.json in sub app folder by "--manifest=" options
*"HOSTEDAPP": will pack apk by "--app-url"
*"COMMANDLINE": will pack apk by make_apk.py command line, e.g. "python make_apk.py --package=org.xwalk.calculator_test --name=calculator_test --app-root=/tmp/tog4ffi40m68ri7/calculator_test --app-local-path=index.html --icon=/tmp/tog4ffi40m68ri7/calculator_test/icon.png --mode=embedded --arch=x86" 
|| "apk-type":"HOSTEDAPP" || the "HOSTEDAPP" need "apk-url-opt" at the same time
|-
| "apk-url-opt" || No || point out value "--app-url" option of make_apk.py|| "apk-url-opt":"www.baidu.com" || Only use by apk type "HOSTEDAPP"
|-
| "apk-ext-opt" || No || point out value "--extensions" option of make_apk.py, should be the relative path of suite source|| "apk-ext-opt":"haha/kkkk" ||
|-
| "apk-cmd-opt" || No || point out value "--xwalk-command-line" option of make_apk.py|| "apk-cmd-opt":"--disable-webgl --disable-webrtc" ||
|-
| "apk-mode-opt" || No || point out value "--mode" option of make_apk.py|| "apk-mode-opt":"embedded" || should be one of "shared" or "embedded", default value will be the value of "-m" option 
|-
| "apk-arch-opt" || No || point out value "--arch" option of make_apk.py|| "apk-arch-opt":"x86" || should be one of "arm" or "x86", default value will be the value of "-a" option 
|-
| "apk-icon-opt" || No || point out value "--icon" option of make_apk.py|| "apk-icon-opt":""(if no need of icon.png) || default value will use the icon.png under current "app-dir" folder
|-
| "key-file" || No || point out key file of make_xpk.py|| "key-file":"haha.pem" || "key.file" is reserved for default xpk packing
|-
| "embeddingapi-library-name" || No || point out embeddingapi core library folder name in tools folder|| "embeddingapi-library-name": "crosswalk-webview" || 
|-
| "apk-common-opts" || No || point out apk extra options|| "apk-common-opts": "--keep-screen-on --enable-remote-debugging" || 
|-
|}

=="pack.py"==
New Python based pack tool, run under Python 2.7* and only support Linux platform now:
 Usage: ./pack.py -t apk -m shared -a x86
 
 Options:
   -h, --help            show this help message and exit
   -c PKGCFG, --cfg=PKGCFG
                         specify the path of config json file
   -t PKGTYPE, --type=PKGTYPE
                         specify the pkg type, e.g. apk, xpk, wgt ...
   -m PKGMODE, --mode=PKGMODE
                         specify the apk mode, e.g. shared, embedded
   -a PKGARCH, --arch=PKGARCH
                         specify the apk arch, e.g. x86, arm
   -d DESTDIR, --dest=DESTDIR
                         specify the installation folder for packed package
   -s SRCDIR, --src=SRCDIR
                         specify the path of pkg resource for packing
   --tools=PKGPACKTOOLS  specify the parent folder of pack tools
   --notclean            disable the build root clean after the packing
   -v, --version         show this tool's version
   --pkg-version=PKGVERSION
                         specify the pkg version, e.g. 0.0.0.1

=="VERSION"==
New pack tool will read package version info from this "VERSION" file. Normally, the pack tool will go through folders "../../suite-source-folder", "../suite-source-folder" and "suite-source-folder" one by one, and will use the VERSION file found firstly.
{| class="wikitable"
|-
! Key !! Mandatory !! Desc !! Example !! Note
|-
| "main-version" || Yes ||  Package main version  || "main-version": "0.0.0.1" || 
|-
| "release-version" || Yes ||  Package release(hotfix) version  || "release-version": "1" || 
|}

=Package Structure=
[[File:crosswalk-test-package-new-001.jpg]]

[[File:crosswalk-test-package-new-002.jpg]]

Take Ubuntu as a example:
*Before the packing, you need install Python 2.7.*. and some pack tools for various package, the default tools folder is "suite-name-tests/../../tools", normally, you just need copy pack tools to this folder(you can also use pack.py's option "--tools" to point out the tools path), e.g:
 $cd /tmp
 $unzip crosswalk-version.zip
 $mv crosswalk-version path-to-tools/crosswalk -a //crosswalk make_apk.py is for apk packing
 $cp make_xpk.py path-to-tools/ //crosswalk make_xpk.py is for xpk packing
 $cp signing path-to-tools/ -a //for wgt signature
 $cp cordova path-to-tools/ -a //fro cordova package packing
 ...................
* Then, you need run pack.py to pack your package, e.g.:
 $python pack.py -t apk -m embedded -a x86
* Option "--notclean" will point out the pack tool will not clean build temp folder(e.g. "/tmp/build-folder-name", the build-folder-name contains 15 random characters) 
* After packing, you can find a zip in the suite folder, e.g. web-demo-tests-version.apk.zip
