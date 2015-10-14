Feature: webrtc
 Scenario: webrtc orientation
  When launch "webrtc"
   Then I should see view "description=REMOTE:"
    And I set orientation "l"
   Then I should see view "description=REMOTE:"
    And I set orientation "r"
   Then I should see view "description=REMOTE:"
