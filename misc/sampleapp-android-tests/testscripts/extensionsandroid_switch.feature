Feature: extensionsandroid
 Scenario: extensionsandroid orientation
  When I launch "xwalk-echo-app" with "org.crosswalkproject.sample" and "SampleActivity" on android
   Then I should see view "description=xwalk-echo-app"
    And I press "home" hardware key
    And I press "recent" hardware key
    And I save relative view "className=android.widget.ImageView" on the "right" side of view "text=xwalk_echo_app" to object "es_app"
    And I click saved object "es_app"
   Then I should see view "description=xwalk-echo-app"
