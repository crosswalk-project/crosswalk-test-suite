Feature: Crosswalk test
 Scenario: test document onchange event
  Given I go to "file:///opt/web-demo-tests/html5-extra/dom/document_onchange_event-manual.html"
   When I input a character in "input"
   When I click on blank
    Then I can see pass
