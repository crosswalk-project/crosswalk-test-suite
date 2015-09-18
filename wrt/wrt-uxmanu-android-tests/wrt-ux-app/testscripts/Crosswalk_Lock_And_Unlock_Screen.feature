Feature: wrt-ux-app
 Scenario: Crosswalk Lock And Unlock Screen
  When launch "touch_gesture_click"
    And I wait 15 seconds
    And I click view "description=mobile"
   Then I should see title "World Wide Web Consortium (W3C)" in 60 seconds
    And I wait 5 seconds
    And I click view "description=Standards"
   Then I should see title "Standards - W3C" in 60 seconds
    And I turn off screen
   Then I should not see view "text=Standards"
    And I turn on screen
   Then I should see title "Standards - W3C"
    And I click view "description=Participate"
   Then I should see title "Participate - W3C" in 60 seconds
