Feature: Usecase WebAPI
 Scenario: Device & Hardware/Notifications Test
    When launch "usecase-webapi-xwalk-tests"
     And I wait 3 seconds
     And I go to "/samples/Notifications/index.html"
     And I click "showNotification"
     And I wait 3 seconds
     And I open notification
    Then I should see view "text=New Email Received"
     And I press "back" hardware key
     And I click "closeNotification"
     And I open notification
    Then I should not see view "text=New Email Received"

