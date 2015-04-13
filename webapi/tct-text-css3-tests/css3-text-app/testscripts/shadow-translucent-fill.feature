Feature: css3-text
 Scenario: css3 TextEffects tests entry11
   When launch "css3-text-app"
     And I go to "text/webkit/shadow-translucent-fill.html"
     And I save the page to "shadow-translucent-fill"
     And I save the screenshot md5 as "shadow-translucent-fill"
    Then file "shadow-translucent-fill" of baseline and result should be the same
