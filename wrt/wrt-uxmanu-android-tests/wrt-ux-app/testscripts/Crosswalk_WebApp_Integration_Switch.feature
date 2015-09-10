Feature: wrt-ux-app
 Scenario: Crosswalk WebApp Integration Switch
  When launch "touch_gesture_click"
    And I wait 15 seconds
    And I click view "description=mobile"
   Then I should see title "World Wide Web Consortium (W3C)" in 60 seconds
    And launch "wrt-ux-app"
   Then I should see title "test"
    And I press "recent" hardware key
    And I save relative view "className=android.widget.ImageView" on the "right" side of view "text=touch_gesture_click" to object "touch_app"
    And I click saved object "touch_app"
   Then I should see view "description=W3C" in 30 seconds
    And I wait 5 seconds
    And I click view "description=Standards"
   Then I should see view "description=STANDARDS" in 30 seconds
   