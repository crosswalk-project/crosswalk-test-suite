Feature: css3-text
 Scenario: css3 TextEffects tests entry1
   When launch "css3-text-app"
     And I go to "webkit/find-hidden-text.html"
     And I save the page to "find-hidden-text"
    Then pic "find-hidden-text" of baseline and result should be "100" similar if have results
