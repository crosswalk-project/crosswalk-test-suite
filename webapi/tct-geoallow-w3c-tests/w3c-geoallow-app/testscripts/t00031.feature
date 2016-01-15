Feature: geoallow
 Scenario: t00031
  When launch "w3c-geoallow-app"
   And I open GPS
   And I open wifi
   And I go to "geoallow/w3c/bdd/t-manual.html?00031"
  Then I should see "PASS" in 10 seconds
