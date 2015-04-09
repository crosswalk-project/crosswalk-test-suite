Feature: css3-text
 Scenario: css3 TextEffects tests entry3
   When launch "css3-text-app"
     And I go to "text/webkit/justification-padding-mid-word.html"
     And I save the page to "justification-padding-mid-word"
    Then pic "justification-padding-mid-word" of baseline and result should be "100" similar if have results
