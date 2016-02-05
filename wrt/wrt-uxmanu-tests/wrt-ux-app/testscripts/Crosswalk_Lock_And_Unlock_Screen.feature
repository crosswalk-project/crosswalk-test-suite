Feature: wrt-ux-app
 Scenario: Crosswalk Lock And Unlock Screen
  When launch "touch_gesture_click"
    And I wait 20 seconds
    And I click view "description=mobile"
   Then I should see title "World Wide Web Consortium (W3C)" in 60 seconds
    And I wait 5 seconds
    And I click view "description=Participate"
   Then I should see title "Participate - W3C" in 60 seconds
    And I turn off screen
   Then I should not see view "text=Participate"
    And I turn on screen
   Then I should see title "Participate - W3C"
    And I click view "description=Membership"
   Then I should see title "Membership - W3C" in 60 seconds
