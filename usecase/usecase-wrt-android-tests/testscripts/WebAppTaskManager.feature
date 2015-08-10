Feature: Usecase WRT
 Scenario: Web Runtime/WebAppTaskManager
  When launch "webappxwalkhost"
   Then I should see title "xwalk_hosts_value_tests"
    And I press "home" hardware key
   Then I press "recent" hardware key
    And I save relative view "className=android.widget.ImageView" on the "right" side of view "text=webappxwalkhost" to object "usecase_app"
   Then I swipe saved object "usecase_app" to "left"
    And I wait 2 seconds
    And I should not see view "text=webappxwalkhost"
    And I press "home" hardware key
