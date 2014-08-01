Feature: Crosswalk test
 Scenario: test document onchange event
  Given I go to "file:///opt/webapi-uiautomation-tests/html5-extra/dom/document_onchange_event-manual.html"
   When I input a character in "input"
   When I check the "p"
    Then I can see pass
