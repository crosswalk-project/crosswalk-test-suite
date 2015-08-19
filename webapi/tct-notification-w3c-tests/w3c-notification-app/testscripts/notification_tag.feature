Feature: notification
 Scenario: notification_tag
  When launch "w3c-notification-app"
   And I open notification
   And I count the elements with text "Room 102" and save result to object "number3"
   And switch to "w3c-notification-app"
   And I go to "notification/notification_tag-manual.html"
   And I open notification
   And I count the elements with text "Room 102" and save result to object "number4"
  Then The saved info "number4" increase 1 compared with "number3"
