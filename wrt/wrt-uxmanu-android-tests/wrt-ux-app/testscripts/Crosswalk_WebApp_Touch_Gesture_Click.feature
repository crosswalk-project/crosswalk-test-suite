Feature: wrt-ux-app
 Scenario: Crosswalk WebApp Touch Gesture Click
  When launch "touch_gesture_click"
    And I should see title "World Wide Web Consortium (W3C)" in 60 seconds
    And I wait 5 seconds
    And I click view "description=STANDARDS"
   Then I should see title "Standards - W3C" in 60 seconds
