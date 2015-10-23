Feature: system-state-and-capabilities
 Scenario: get navigator language
  When launch "html5-extra-app"
   And switch to language "English (United Kingdom)"
   And switch to "html5-extra-app"
   And I go to "w3c/system-state-and-capabilities/the-navigator-object/bdd/get-navigatorlanguage-manual.html"
  Then I should see "Pass" in 5 seconds
   And switch to language "English (United States)"
