Feature: css3-text
 Scenario: css3 TextEffects tests entry7
   When launch "css3-text-app"
     And I go to "text/webkit/shadow-no-blur.html"
     And I save the page to "shadow-no-blur"
     And I save the screenshot md5 as "shadow-no-blur"
    Then file "shadow-no-blur" of baseline and result should be the same
