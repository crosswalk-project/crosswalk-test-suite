Feature: wrt-security-app
 Scenario: Crosswalk Permission Undefined Messaging
  When launch "permission_undefined_messaging_tests"
   And I wait 3 seconds
   Then I should see "Pass" with "green" color in "test" area
