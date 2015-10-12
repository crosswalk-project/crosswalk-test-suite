Feature: web-system-app
 Scenario: Crosswalk LocalStorage kill
  When I launch "localstorage" with "org.xwalk.localstorage" and "LocalstorageActivity" on android
    And I wait for 3 seconds
    And I click view "description=Set LocalStorage"
    And I wait for 3 seconds
   Then I expect the content "Save localStorage value successfully: test" in the dumped xml
    And I click view "description=Get LocalStorage"
    And I wait for 3 seconds
   Then I expect the content "Get localStorage value: test" in the dumped xml
    And I execute command "adb shell am force-stop org.xwalk.localstorage"
   Then I should not see view "description=Set LocalStorage"
    And I execute command "adb shell am start -n org.xwalk.localstorage/.LocalstorageActivity"
    And I wait for 3 seconds
    And I click view "description=Get LocalStorage"
    And I wait for 3 seconds
   Then I expect the content "Get localStorage value: test" in the dumped xml
