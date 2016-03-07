Feature: wrt-ux-app
 Scenario: Crosswalk WebApp Integration Switch
  When launch "touch_gesture_click"
    And I wait 20 seconds
    And I click view "description=mobile"
   Then I should see title "World Wide Web Consortium (W3C)" in 60 seconds
    And launch "wrt-ux-app"
   Then I should see title "test"
    And I press "recent" hardware key
    And I click view "description=touch_gesture_click"
   Then I should see view "description=W3C" in 30 seconds
    And I wait 5 seconds
    And I click view "description=Participate"
   Then I should see view "description=PARTICIPATE" in 30 seconds
