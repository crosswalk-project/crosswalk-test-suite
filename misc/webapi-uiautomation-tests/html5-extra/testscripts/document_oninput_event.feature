Feature: dom
 Scenario: document oninput event
  When launch "webapi-uiautomation-tests"
   And I go to "opt/webapi-uiautomation-tests/html5-extra/dom/document_oninput_event-manual.html"
  When I fill in "test_textarea" with "a"
  Then I should see "PASS" in "test" area
