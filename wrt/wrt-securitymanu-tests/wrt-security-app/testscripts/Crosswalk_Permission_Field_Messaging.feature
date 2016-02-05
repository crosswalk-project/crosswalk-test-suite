Feature: wrt-security-app
 Scenario: Crosswalk Permission Field Messaging
  When launch "permission_field_messaging_tests"
   And I wait 3 seconds
   Then I should see "Pass" with "green" color in "test" area
