Feature: web-system-app
 Scenario: Crosswalk LocalStorage upgrade
  When launch "localstorage"
    And I wait for 3 seconds
    And I click view "description=Set LocalStorage"
    And I wait for 3 seconds
   Then I expect the content "Save localStorage value successfully: test" in the dumped xml
    And I click view "description=Get LocalStorage"
    And I wait for 3 seconds
   Then I expect the content "Get localStorage value: test" in the dumped xml
    And reinstall "../../localstorage_upgrade.apk"
    And I execute command "adb shell am start -n org.xwalk.localstorage/.LocalstorageActivity"
    And I wait for 3 seconds
    And I click view "description=Get LocalStorage"
    And I wait for 3 seconds
   Then I expect the content "Get localStorage value: test" in the dumped xml
