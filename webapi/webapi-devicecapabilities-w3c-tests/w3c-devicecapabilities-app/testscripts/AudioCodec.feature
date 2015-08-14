Feature: devicecapabilities
 Scenario: AudioCodec
  When launch "w3c-devicecapabilities-app"
   And I go to "devicecapabilities/AudioCodec-manual.html"
   And I wait 2 seconds
  Then I should not see "Failed"
  Then I verify value in "format" is "string" type
