Feature: prompt
 Scenario: window prompt checking
    When launch "webapi-uiautomation-tests"
     And I go to "opt/webapi-uiautomation-tests/html5-extra/browsers/window_prompt_base-manual.html"
    When I press "btn"
    Then I should see an alert with text "1 + 1 = ?"
