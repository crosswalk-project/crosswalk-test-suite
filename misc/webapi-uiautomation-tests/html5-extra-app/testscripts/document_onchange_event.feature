Feature: dom
 Scenario: document onchange event
   When launch "html5-extra-app"
    And I go to "dom/document_onchange_event-manual.html"
   When I fill in "test_input" with "a"
    And I click "test_text"
   Then I should see "PASS" in "test" area
