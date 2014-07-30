Feature: dom
 Scenario: document oninput event
  When launch "webapi-uiautomation-tests"
   And I go to "opt/webapi-uiautomation-tests/html5-extra/dom/document_oninput_event-manual.html"
  When I input a character in "textarea"
  Then I can see "pass"
