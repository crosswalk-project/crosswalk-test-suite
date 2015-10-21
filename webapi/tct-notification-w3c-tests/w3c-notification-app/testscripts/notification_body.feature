Feature: notification
 Scenario: notification_body
  When launch "w3c-notification-app"
   And I clear notifications with text "Room 101"
   And I go to "notification/notification_body-manual.html"
  Then I should see notifications with text "Room 101"
   And I clear notifications with text "Room 101"
