Feature: wrt-ux-app
 Scenario: Crosswalk WebApp Terminated TaskManager
  When launch "web_feature_notification_tests"
    And I should see title "Web Features Test: web_feature_notification_tests"
    And I press "home" hardware key
   Then I press "recent" hardware key
    And I save relative view "className=android.widget.ImageView" on the "right" side of view "text=web_feature_notification_tests" to object "feature_app"
   Then I swipe saved object "feature_app" to "left"
    And I wait 3 seconds
    And I should not see view "text=web_feature_notification_tests"
    And I press "home" hardware key
