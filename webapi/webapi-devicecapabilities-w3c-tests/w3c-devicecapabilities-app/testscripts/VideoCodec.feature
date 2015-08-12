Feature: devicecapabilities
 Scenario: VideoCodec
  When launch "w3c-devicecapabilities-app"
   And I go to "devicecapabilities/VideoCodec-manual.html"
   And I wait 4 seconds
  Then I should not see "Failed"
  Then I should not see "error"
  Then I verify value in "format" is "string" type
  Then I verify value in "hwAccel" is "string" type
  Then I verify value in "encode" is "boolean" type
