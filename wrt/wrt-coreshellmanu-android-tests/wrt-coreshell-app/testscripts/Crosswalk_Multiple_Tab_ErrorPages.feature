Feature: wrt-coreshell-app
 Scenario: Crosswalk Multiple Tab ErrorPages
  When I launch "XWalkViewShell" with "org.xwalk.core.xwview.shell" and "XWalkViewShellActivity" on android
    And I edit index 0 EditText to input "http://www.w3.org"
    And I press "enter" hardware key
   Then I should see view "text=World Wide Web Consortium (W3C)" in 60 seconds
    And I register watcher "errorpage" when "Attention" click "OK"
    And I click view "className=android.widget.TextView^^^text=New Tab"
    And I edit index 0 EditText to input "error.page"
    And I press "enter" hardware key
   Then I should see view "text=error.page^^^className=android.widget.TextView" in 60 seconds
