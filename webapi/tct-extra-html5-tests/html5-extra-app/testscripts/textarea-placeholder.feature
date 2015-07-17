Feature: confirm
 Scenario: confirm base checking
  When launch "html5-extra-app"
   And I go to "w3c/semantics/forms/the-textarea-element/textarea-placeholder-manual.html"
   Then I should see "Placeholder Text" in "text" area
   And I fill in "text" with "test"
   Then I should not see "Placeholder Text" in "text" area
