Feature: webrtc
 Scenario: webrtc orientation
  When launch "webrtc"
   Then I should see view "description=REMOTE:"
    And I press "home" hardware key
    And I press "recent" hardware key
    And I save relative view "className=android.widget.ImageView" on the "right" side of view "text=WebRTC" to object "webrtc_app"
    And I click saved object "webrtc_app"
   Then I should see view "description=REMOTE:"
