# W3C WebDriver Tests

This suite integrates a set of conformance tests from [W3C WebDriver Test Suite]
(https://github.com/w3c/web-platform-tests/tree/master/webdriver) for the
[W3C WebDrirver Spec]
(https://dvcs.w3.org/hg/webdriver/raw-file/default/webdriver-spec.html).
The purpose is for the XwalkDriver implementation to be tested to determine
whether it meets the recognized standard.

## Pre-condition

1. It is highly recommended that you use a virtual Python environment.
   This allows you to safely make changes to your Python environment
   for XwalkDriver tests without affecting other software projects on
   your system.
   Install it using either `<sudo> easy_install virtualenv`, `<sudo> pip
   install virtualenv`, or `<sudo> apt-get install python-virtualenv`
2. Create and enter the directory for your Python virtual environment. This
   directory can be anywhere. It is recommended that you keep it separate
   from the webdriver tests folder, to avoid confusion with source control
  * Go to the directory where you store Python virtual environments.
     For example `cd ~; mkdir python-virtualenv; cd python-virtualenv`
  * Create a virtual env configuration and directory: `virtualenv webdriver-w3c-tests`
  * Enter the directory: `cd webdriver-w3c-tests`
3. `source bin/activate` to activate the local Python installation
4. Install Selenium: `pip install selenium` or `easy_install selenium`


## How to run the tests

Get xwalkdriver on Ubuntu (32bit/64bit):

  ```
  $ git clone https://github.com/iKevinHan/xwalkdriver_binary
  $ cd xwalkdriver/xwalkdriver_binary
  ```

For Android:
1. Start xwalkdriver server
  ```
  $ cd /path/to/xwalkdriver_binary
  $./xwalkdriver
  ```
2. Enable ADB and SSH on Android
  * Make sure your ZTE V975 had rooted
  * Connect your ZTE V975 to your Linux PC (e.g.Ubuntu 13.04)
  * Enable debug mode on ZTE V975 UI: Click “Setting”-> Click “All” on the bottom -> Choose “Developer Options”-> Enable “USB Debugging”
  * Setup Connect type to Share mobile network(Connect to Server by USB -> pull down Notification bar -> Click "PC connection" -> Choose "Share mobile network")
  * Setup IP of Linux PC with 192.168.42.100.
  ```
  # ifconfig usb0 192.168.42.100. it's better to setup the IP on UI
  ```
  * On Linux PC (eth0 is the network interface for webservice visiting)
  ```
  # sudo sysctl net.ipv4.ip_forward=1
  # sudo iptables -t nat -A POSTROUTING -s 192.168.42.0/24 -o eth0 -j MASQUERADE
  ```
  * On adb console(#adb shell)
   (note: if "adb shell" fails, and show error: insufficient permissions for device, you can try: "adb kill-server" then "sudo adb start-server")
  ```
  # su
  # ifconfig rndis0 192.168.42.129 netmask 255.255.255.0
  # busybox route add default gw 192.168.42.100 dev rndis0
  # setprop net.dns1 192.168.42.129
  # setprop net.dns2 10.239.27.228
  # netcfg
  ```
  * Modify /etc/resolv.conf as below content
  ```
  nameserver 10.248.2.5
  ```
  Then your Tizen Device can connect the external network by your Linux PC net forward.
3. Install it onto Android: `adb install XwalkDriverTest_1.0_x86.apk`
4. Run the tests:
  `testkit-lite -f /path/to/opt/webdriver-w3c-tests/tests.xml -k pyunit --comm localhost -o /path/to/opt/webdriver-w3c-tests/result.xml --testenvs WD_BROWSER=android`


For Tizen:
1. Start xwalkdriver server
  ```
  $ cd /path/to/xwalkdriver_binary
  $./xwalkdriver --sdb-port=26099
  ```
2. Install and launch the xwalk as server mode on Tizen IVI:
  '''
  su - app
  export XDG_RUNTIME_DIR="/run/user/5000"
  export DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/5000/dbus/user_bus_socket
  systemctl --user status xwalk.service
  pkgcmd -i -t wgt -q -p /path/to/opt/webdriver-w3c-tests/XwalkDriverTest.wgt
  '''
3. Set remote debug port by insert "--remote-debugging-port='PORT'" into "/usr/lib/systemd/user/xwalk.service" on Tizen IVI.
4. Connect Tizen IVI and PC with sdb
  * Run the follow command on Tizen IVI: #systemd start sdbd_tcp
  * Run the follow command on PC: $sdb connect <tizen ivi ip>
  * Run the follow command on PC: $sdb root on
5. Run the tests:
  `testkit-lite -f /path/to/opt/webdriver-w3c-tests/tests.xml -k pyunit --comm localhost -o /path/to/opt/webdriver-w3c-tests/result.xml --testenvs WD_BROWSER=tizen`


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
