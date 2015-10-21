Feature: notification
 Scenario: tag-different-manual
  When launch "w3c-notification-app"
   And I clear notifications with text "This is the body: Room 101"
   And I clear notifications with text "This is the body: Room 202"
   And I go to "notification/w3c/bdd/tag-different-manual.html"
  Then I should see notifications with text "This is the body: Room 101"
  Then I should see notifications with text "This is the body: Room 202"
   And I clear notifications with text "This is the body: Room 101"
   And I clear notifications with text "This is the body: Room 202"
