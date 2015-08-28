Feature: wrt-packagemgt-app
 Scenario: Crosswalk WebApp Icon Launcher
  When launch "wrt_packagemgtmanu_android_tests"
    And I click app icon "text=wrt_packagemgt_app" in all apps
   Then I should see view "description=hello"
