Feature: wrt-packagemgt-app
 Scenario: Crosswalk WebApp Icon Launcher
  When launch "wrt_packagemgtmanu_tests"
    And I click app icon "text=wrt_packagemgt_app" in all apps
    And I wait for 2 seconds
   Then I should see view "description=hello"
