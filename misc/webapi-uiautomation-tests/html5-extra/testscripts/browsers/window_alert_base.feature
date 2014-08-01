Feature: Crosswalk test
 Scenario: test window alert
  Given I go to "file:///opt/webapi-uiautomation-tests/html5-extra/browsers/window_alert_base-manual.html"
   When I press "btn"
   Then I should see an alert with text "PASS"
