Feature: w3c-touchevent
 Scenario: TouchEvent altKey exist
  When launch "w3c-touchevent-app"
   And I go to "touchevent/bdd/TouchEvent_shiftKey_exist-manual.html"
   And I click view "description=Touch"
  Then I should see "Pass" in 2 seconds
