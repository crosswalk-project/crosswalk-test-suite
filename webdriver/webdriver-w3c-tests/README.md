# W3C WebDriver Tests

This suite integrates a set of conformance tests from [W3C WebDriver Test Suite]
(https://github.com/w3c/web-platform-tests/tree/master/webdriver) for the
[W3C WebDrirver Spec]
(https://dvcs.w3.org/hg/webdriver/raw-file/default/webdriver-spec.html).
The purpose is for the XwalkDriver implementation to be tested to determine
whether it meets the recognized standard.

## How to run the tests

1. It is highly recommended that you use a virtual Python environment.
   This allows you to safely make changes to your Python environment
   for XwalkDriver tests without affecting other software projects on
   your system.
   Install it using either `<sudo> easy_install virtualenv`, `<sudo> pip
   install virtualenv`, or `<sudo> apt-get install python-virtualenv`
2. Create and enter the directory for your Python virtual environment. This 
   directory can be anywhere. It is recommended that you keep it separate
   from the webdriver tests folder, to avoid confusion with source control
  1. Go to the directory where you store Python virtual environments. 
     For example `cd ~; mkdir python-virtualenv; cd python-virtualenv`
  2. Create a virtual env configuration and directory: `virtualenv webdriver-w3c-tests`
  3. Enter the directory: `cd webdriver-w3c-tests`
3. `source bin/activate` to activate the local Python installation
4. Install Selenium: `pip install selenium` or `easy_install selenium`
5. Go to the WebDriver tests: `cd _WEBDRIVER_TEST_ROOT_`
6. Build XwalkDriverTest APK and install it onto Android, `./pack.sh;
   adb install XwalkDriverTest_1.0_x86.apk`.
   Please refer to `../../doc/Web_Test_Suite_Packaging_Guide_v1.0.pdf`
   for environment setup to generate APK package.
7. Run the tests: `python runtests.py`

Note: that you will likely need to start the driver's server before running.

## Updating configuration

The _webdriver.cfg_ file holds any configuration that the tests might
require.  Change the value of browser to your needs.  This will then
be picked up by WebDriverBaseTest when tests are run.

Be sure not to commit your _webdriver.cfg_ changes when your create or modify tests.

## How to write tests

Please follow the [W3C WebDriver Howto]
(https://github.com/w3c/web-platform-tests/tree/master/webdriver#how-to-write-tests)
to create new tests; and submit the tests to the [W3C WebDriver Test Suite]
(https://github.com/w3c/web-platform-tests/tree/master/webdriver) directly.
We will conutinously integrate the approved tests from there.
