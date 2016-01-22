Feature: geodeny
 Scenario: errorcallback_PERMISSION_DENIED
  When launch "w3c-geodeny-app"
   And I close GPS
   And I close wifi
   And I go to "geodeny/w3c/bdd/t-manual.html?00001"
   And I wait for 5 seconds
   And I open GPS
   And I open wifi
  Then I should see "PASS" in 2 seconds
