Feature: dom
 Scenario: document onchange event
   When launch "webapi-uiautomation-tests"
    And I go to "opt/web-demo-tests/html5-extra/dom/document_onchange_event-manual.html"
    And I input a character in "input"
    And I click on blank
   Then I can see "pass"
