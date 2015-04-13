Feature: css3-text
 Scenario: css3 TextEffects tests entry1
   When launch "css3-text-app"
     And I go to "text/webkit/find-hidden-text.html"
     And I save the page to "find-hidden-text"
     And I save the screenshot md5 as "find-hidden-text"
    Then file "find-hidden-text" of baseline and result should be the same
