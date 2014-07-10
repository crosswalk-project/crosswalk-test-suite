Feature: Crosswalk test
 Scenario: test window confirm
  Given I go to "file:///opt/webapi-uiautomation-tests/html5-extra/browsers/window_confirm_base-manual.html"
   When I press "btn"
   Then I should see an alert with text "Are you ok?"
