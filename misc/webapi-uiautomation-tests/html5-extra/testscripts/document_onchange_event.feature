Feature: dom
 Scenario: document onchange event
   When launch "webapi-uiautomation-tests"
    And I go to "opt/webapi-uiautomation-tests/html5-extra/dom/document_onchange_event-manual.html"
   When I fill in "test_input" with "a"
    And I click "test_text"
   Then I should see "PASS" in "test" area
