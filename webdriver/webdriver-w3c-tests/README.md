# XwalkDriver Tests

This repository defines a set of conformance tests for XwalkDrirver.

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
2a. Go to the directory where you store Python virtual environments. 
   For example
   ```
   cd ~
   mkdir python-virtualenv
   cd python-virtualenv
   ```
2b. Create a virtual env configuration and directory: `virtualenv webdriver-w3c-tests`
2c. Enter the directory: `cd webdriver-w3c-tests`
3. `source bin/activate` to activate the local Python installation
4. Install Selenium: `pip install selenium` or `easy_install selenium`
5. Go to the WebDriver tests: `cd _WEBDRIVER_TEST_ROOT_`
6. Install test apk to Android
   ```
   ./pack.sh
   adb install XwalkDriverTest_1.0_x86.apk
   ```
7. Run the tests: `python runtests.py`


Note: that you will need likely need to start the driver's server before running.

## Updating configuration

The _webdriver.cfg_ file holds any configuration that the tests might
require.  Change the value of browser to your needs.  This will then
be picked up by WebDriverBaseTest when tests are run.

Be sure not to commit your _webdriver.cfg_ changes when your create or modify tests.

## How to write tests

1. Create a test file per section from the specification.
2. For each test there needs to be one or more corresponding HTML
   files that will be used for testing.  HTML files are not to be
   reused between tests. HTML files and other support files
   should be stored in a folder named 'res'.
3. Test name should explain the intention of the test e.g. `def
   test_navigate_and_return_title(self):`
