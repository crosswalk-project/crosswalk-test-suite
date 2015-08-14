Feature: wrt-ux-app
 Scenario: Crosswalk WebApp Integration Switch
  When launch "touch_gesture_click"
    And I should see title "World Wide Web Consortium (W3C)" in 60 seconds
   Then launch "wrt-ux-app"
    And I should see title "test"
    And I press "recent" hardware key
   Then I save relative view "className=android.widget.ImageView" on the "right" side of view "text=touch_gesture_click" to object "touch_app"
    And I click saved object "touch_app"
   Then I should see view "description=CollapseW3C Opens New Australia Office" in 30 seconds
    And I wait 5 seconds
    And I click view "description=STANDARDS"
   Then I should see view "description=STANDARDS" in 30 seconds
