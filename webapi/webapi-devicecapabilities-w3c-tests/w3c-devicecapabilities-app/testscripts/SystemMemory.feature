Feature: devicecapabilities
 Scenario: SystemMemory
  When launch "w3c-devicecapabilities-app"
   And I go to "devicecapabilities/SystemMemory-manual.html"
   And I wait 4 seconds
  Then I should not see "Failed"
  Then I verify value in "capacity" is "int" type
  Then I verify value in "availCapacity" is "int" type
