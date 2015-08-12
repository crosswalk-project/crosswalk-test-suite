Feature: devicecapabilities
 Scenario: SystemCPU
  When launch "w3c-devicecapabilities-app"
   And I go to "devicecapabilities/SystemCPU-manual.html"
   And I wait 4 seconds
  Then I should not see "Failed"
  Then I verify value in "numOfProcessors" is "int" type
  Then I verify value in "archName" is "string" type
  Then I verify value in "load" is "float" type
