Feature: wrt-ux-app
 Scenario: Crosswalk WebApp BackKey Exit
  When launch "touch_gesture_click"
    And I wait 20 seconds
   Then I should see view "description=World Wide Web Consortium (W3C)" in 60 seconds
    And I press "back" hardware key
   Then I should not see view "description=World Wide Web Consortium (W3C)"
