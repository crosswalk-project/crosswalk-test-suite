Feature: confirm
 Scenario: confirm base checking
  When launch "html5-extra-app"
   And I go to "browsers/window_confirm_base-manual.html"
   And I press "btn"
   Then I should see an alert with text "Are you ok?"
