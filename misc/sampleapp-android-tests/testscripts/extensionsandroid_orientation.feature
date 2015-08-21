Feature: extensionsandroid
 Scenario: extensionsandroid orientation
  When I launch "xwalk-echo-app" with "org.crosswalkproject.sample" and "SampleActivity" on android
   Then I should see view "description=xwalk-echo-app"
    And I set orientation "l"
   Then I should see view "description=xwalk-echo-app"
    And I set orientation "r"
   Then I should see view "description=xwalk-echo-app"
