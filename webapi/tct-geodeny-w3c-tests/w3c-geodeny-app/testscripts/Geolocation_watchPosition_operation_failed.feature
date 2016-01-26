Feature: geodeny
 Scenario: Geolocation_watchPosition_operation_failed
  When launch "w3c-geodeny-app"
   And I close GPS
   And I close wifi
   And I go to "geodeny/bdd/Geolocation_watchPosition_operation_failed-manual.html"
   And I wait for 5 seconds
   And I open GPS
   And I open wifi
  Then I should see "Pass" in 2 seconds
