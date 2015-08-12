Feature: devicecapabilities
 Scenario: DisplayUnit
  When launch "w3c-devicecapabilities-app"
   And I go to "devicecapabilities/DisplayUnit-manual.html"
   And I wait 4 seconds
  Then I should not see "Failed"
  Then I verify value in "id" is "int" type
  Then I verify value in "name" is "string" type
  Then I verify value in "primary" is "boolean" type
  Then I verify value in "external" is "boolean" type
  Then I verify value in "deviceXDPI" is "int" type
  Then I verify value in "deviceYDPI" is "int" type
  Then I verify value in "width" is "int" type
  Then I verify value in "height" is "int" type
  Then I verify value in "colorDepth" is "int" type
  Then I verify value in "pixelDepth" is "int" type
  Then I verify value in "availWidth" is "int" type
  Then I verify value in "availHeight" is "int" type
