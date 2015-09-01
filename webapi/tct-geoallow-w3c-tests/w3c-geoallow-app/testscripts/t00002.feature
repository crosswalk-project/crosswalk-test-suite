Feature: geoallow
 Scenario: t00002
  When launch "w3c-geoallow-app"
   And I close GPS
   And I open wifi
   And I go to "geoallow/w3c/bdd/t-manual.html?00002"
   And I open GPS
  Then I should see "PASS" in 2 seconds
