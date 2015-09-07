Feature: wrt-ux-app
 Scenario: Crosswalk WebApp Touch Gesture Click
  When I launch "XWalkViewShell" with "org.xwalk.core.xwview.shell" and "XWalkViewShellActivity" on android
    And I edit index 0 EditText to input "http://www.w3.org"
    And I press "enter" hardware key
   Then I should see view "text=World Wide Web Consortium (W3C)" in 60 seconds
    And I click view "className=android.widget.TextView^^^text=New Tab"
    And I edit index 0 EditText to input "http://www.intel.com/content/www/us/en/homepage.html"
    And I press "enter" hardware key
   Then I should see view "text=Intel: Tablet, 2in1, Laptop, Desktop, Smartphone, Server, Embedded" in 60 seconds
