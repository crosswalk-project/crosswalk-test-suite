Feature: css3-text
 Scenario: css3 TextEffects tests entry4
   When launch "css3-text-app"
     And I go to "text/webkit/justify-nbsp.html"
     And I save the page to "justify-nbsp"
     And I save the screenshot md5 as "justify-nbsp"
    Then file "justify-nbsp" of baseline and result should be the same
