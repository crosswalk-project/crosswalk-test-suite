Feature: alert
 Scenario: window alert checking
    When launch "html5-extra-app"
     And I go to "browsers/window_alert_base-manual.html"
    When I press "btn"
    Then I should see an alert with text "PASS"
