Feature: wrt-security-app
 Scenario: Crosswalk Permission Undefined Geolocation
  When launch "permission_undefined_geolocation_tests"
   And I wait 3 seconds
   Then I should see "Pass" with "green" color in "test" area