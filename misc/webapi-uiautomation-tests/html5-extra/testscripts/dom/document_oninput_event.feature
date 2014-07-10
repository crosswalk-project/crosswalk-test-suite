Feature: Crosswalk test
 Scenario: test document oninput event
  Given I go to "file:///opt/web-demo-tests/html5-extra/dom/document_oninput_event-manual.html"
   When I input a character in "textarea"
    Then I can see pass
