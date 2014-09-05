 ## Introduction

This is a test suite for Crosswalk, which includes:

* `behavior/`: behavior test tool
* `cordova/`: Crosswalk based Cordova tests
* `webapi/`: Web API tests
* `wrt/`: Web Runtime Tests
* `misc/`: miscellaneous tests
  * `web-abat-tests` and `web-mbat-tests`: basic acceptance tests
  * `webapi-usecase-tizen-tests`: usecase tests for Tizen Device APIs
  * `webapi-usecase-standard-tests`: usecase tests for standard APIs, e.g.
W3C/HTML5 APIs, Supplementary APIs, Crosswalk experimental APIs
  * `wrt-usecase-*-tests`: usecase tests for Web Runtime
  * `wrt-stab*-tests`: stability tests
  * `wrt-*-UA-tests`: user acceptance tests
  * `wrt-documentation-verification-tests`: tests for documents verification
* `doc/`: see [documentaion](#Documentation) below
* `tools/`: tools for this test suite

## Documentation

Check out our documents at `doc/`.

For test suite and test case development, please go through the following
documents firstly:

* `doc/Behavior_Test_Tool_Developer_Guide`
* `doc/Coding_Style_Guide_CheatSheet`
* `doc/Web_Test_Suite_Developer_Guide`
* `doc/Web_Test_Suite_Packaging_Guide`

For testing execution and reports, please follow these user guides:

* `doc/Behavior_Test_Tool_User_Guide`
* `doc/Cordova_Test_Suite_User_Guide`
* `doc/WebAPI_Test_Suite_User_Guide`
* `doc/Web_BAT_Test_Suite_User_Guide`
* `doc/Web_Runtime_Test_Suite_User_Guide`

## Contributing

Move the Web, Write Some Tests!

Absolutely everyone is welcome (and even encouraged) to contribute to test
development and bug report. No test is too small or too simple, especially
if it corresponds to something for which you've noted an bug in Crosswalk
project.

The way to contribute is just as usual:

* fork this repository (and make sure you're still relatively in sync with it
  if you forked a while ago);
* create a branch for your changes, `git checkout -b username/topic`;
* make your changes;
* push that to your repo;
* and send in a pull request based on the above.

Please make your pull requests to `master`.

Or you can report an issue of the tests and/or tools in this JIRA system:

* https://crosswalk-project.org/jira/browse/XWALK/component/10303

## License

Except as noted in `COPYING` and/or `NOTICE` files, or as headed with license
info, test suite source code uses a BSD-style license that can be found in the
`LICENSE` file.
