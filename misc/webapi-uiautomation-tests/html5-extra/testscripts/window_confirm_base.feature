Feature: confirm
 Scenario: confirm base checking
  When launch "webapi-uiautomation-tests"
   And I go to "opt/webapi-uiautomation-tests/html5-extra/browsers/window_confirm_base-manual.html"
   And I press "btn"
   Then I should see an alert with text "Are you ok?"
