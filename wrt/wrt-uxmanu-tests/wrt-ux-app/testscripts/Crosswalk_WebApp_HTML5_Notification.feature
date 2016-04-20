Feature: wrt-ux-app
 Scenario: Crosswalk WebApp HTML5 Notification
  When launch "web_feature_notification_tests"
    And I click view "description=Get Notification"
    And I wait 5 seconds
    And I open notification
   Then I should see view "text=New Email Received"
    And I press "home" hardware key
