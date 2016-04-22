Feature: Usecase WRT
 Scenario: Web Runtime/WebAppTaskManager
  When launch "webappxwalkhost"
   Then I should see title "xwalk_hosts_value_tests"
    And I press "home" hardware key
   Then I press "recent" hardware key
    And I close app "webappxwalkhost" from task manager
    And I wait 2 seconds
    And I should not see view "description=webappxwalkhost"
    And I press "home" hardware key
