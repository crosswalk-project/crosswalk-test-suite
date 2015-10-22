Feature: notification
 Scenario: tag-same-manual
  When launch "w3c-notification-app"
   And I clear notifications with text "This is the body: Room 101"
   And I clear notifications with text "This is the body: Room 202"
   And I go to "notification/w3c/bdd/tag-same-manual.html"
  Then I should not see notifications with text "This is the body: Room 101"
  Then I should see notifications with text "This is the body: Room 202"
   And I clear notifications with text "This is the body content: Room 202"
