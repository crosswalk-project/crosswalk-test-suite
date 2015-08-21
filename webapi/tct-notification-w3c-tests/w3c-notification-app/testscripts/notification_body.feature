Feature: notification
 Scenario: notification_body
  When launch "w3c-notification-app"
   And I open notification
   And I count the elements with text "Room 101" and save result to object "number1"
   And switch to "w3c-notification-app"
   And I go to "notification/notification_body-manual.html"
   And I open notification
   And I count the elements with text "Room 101" and save result to object "number2"
  Then The saved info "number2" increase 1 compared with "number1"
