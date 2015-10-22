Feature: notification
 Scenario: notification_tag
  When launch "w3c-notification-app"
   And I clear notifications with text "Room 102"
   And I go to "notification/notification_tag-manual.html"
  Then I should see notifications with text "Room 102"
   And I clear notifications with text "Room 102"
