Feature: devicecapabilities
 Scenario: StorageUnit
  When launch "w3c-devicecapabilities-app"
   And I go to "devicecapabilities/StorageUnit-manual.html"
   And I wait 4 seconds
  Then I should not see "Failed"
  Then I verify value in "id" is "int" type
  Then I verify value in "name" is "string" type
  Then I verify value in "type" is "string" type
  Then I verify value in "capacity" is "int" type
