Feature: wrt-ux-app
 Scenario: Crosswalk WebApp BackKey Back
  When launch "touch_gesture_click"
    And I wait 20 seconds
    And I click view "description=mobile"
   Then I should see title "World Wide Web Consortium (W3C)" in 60 seconds
    And I wait 5 seconds
    And I click view "description=Participate"
   Then I should see title "Participate - W3C" in 60 seconds
    And I press "back" hardware key
   Then I should see title "World Wide Web Consortium (W3C)" in 30 seconds
