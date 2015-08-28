Feature: w3c-pagevisibility
 Scenario: pagevisibility DocumentVisibility hidden lockScreen
   When launch "w3c-pagevisibility-app"
     And I go to "pagevisibility/bdd/pagevisibility_DocumentVisibility_hidden_lockScreen-manual.html"
     And I turn off screen
     And I wait 6 seconds
     And I turn on screen
    Then I should see "Pass"
