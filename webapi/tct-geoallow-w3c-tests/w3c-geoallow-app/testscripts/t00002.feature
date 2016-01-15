Feature: geoallow
 Scenario: t00002
  When launch "w3c-geoallow-app"
   And I open GPS
   And I open wifi
   And I go to "geoallow/w3c/bdd/t-manual.html?00002"
  Then I should see "PASS" in 10 seconds
