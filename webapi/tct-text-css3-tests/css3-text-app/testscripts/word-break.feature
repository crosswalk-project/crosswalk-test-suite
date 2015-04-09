Feature: css3-text
 Scenario: css3 TextEffects tests entry15
   When launch "css3-text-app"
     And I go to "webkit/word-break.html"
     And I save the page to "word-break"
    Then pic "word-break" of baseline and result should be "100" similar if have results
