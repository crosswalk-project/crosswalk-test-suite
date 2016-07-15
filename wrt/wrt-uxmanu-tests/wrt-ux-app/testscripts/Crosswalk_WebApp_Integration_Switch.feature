Feature: wrt-ux-app
 Scenario: Crosswalk WebApp Integration Switch
  When launch "touch_gesture_click"
    And I wait 20 seconds
   Then I should see title "World Wide Web Consortium (W3C)" in 60 seconds
    And launch "wrt-ux-app"
   Then I should see title "test"
    And I press "recent" hardware key
    And I click app "touch_gesture_click" from task manager
   Then I should see view "description=World Wide Web Consortium (W3C)" in 30 seconds
    And I click view "description=PARTICIPATE"
   Then I should see view "description=Participate - W3C" in 60 seconds
