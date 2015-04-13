Feature: css3-text
 Scenario: css3 TextEffects tests entry15
   When launch "css3-text-app"
     And I go to "text/webkit/word-break.html"
     And I save the page to "word-break"
     And I save the screenshot md5 as "word-break"
    Then file "word-break" of baseline and result should be the same
