Feature: w3c-pagevisibility
 Scenario: pagevisibility DocumentVisibility hidden minimize
   When launch "w3c-pagevisibility-app"
     And I go to "pagevisibility/bdd/pagevisibility_DocumentVisibility_hidden_minimize-manual.html"
     And I open quick settings
     And I wait 6 seconds
     And I press "back" hardware key
    Then I should see "Pass"
