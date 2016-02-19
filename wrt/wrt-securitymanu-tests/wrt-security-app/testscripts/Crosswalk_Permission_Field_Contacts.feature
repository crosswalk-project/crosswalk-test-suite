Feature: wrt-security-app
 Scenario: Crosswalk Permission Field Contacts
  When launch "permission_field_contacts_tests"
   And I wait 3 seconds
   Then I should see "Pass" with "green" color in "test" area