Feature: notification
 Scenario: event-onclick-manual
  When launch "w3c-notification-app"
   And I clear notifications with text "Click me to test clicking on notifications."
   And I go to "notification/w3c/bdd/event-onclick-manual.html"
   And I click notifications with text "Click me to test clicking on notifications."
   And I wait for 5 seconds
  Then I should see "Pass"
