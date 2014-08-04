Feature: alert
 Scenario: window alert checking
    When launch "webapi-uiautomation-tests"
     And I go to "opt/webapi-uiautomation-tests/html5-extra/browsers/window_alert_base-manual.html"
    When I press "btn"
    Then I should see an alert with text "PASS"
