Feature: prompt
 Scenario: window prompt checking
    When launch "html5-extra-app"
     And I go to "browsers/window_prompt_base-manual.html"
    When I press "btn"
    Then I should see an alert with text "1 + 1 = ?"
