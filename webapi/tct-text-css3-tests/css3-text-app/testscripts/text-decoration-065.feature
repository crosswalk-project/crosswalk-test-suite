Feature: css3-text
 Scenario: CSS3TextEffects text decoration none
   When launch "css3-text-app"
     And I go to "text/csswg/text-decoration-065.html"
     And I save the page to "text-decoration-065"
     And I save the screenshot md5 as "text-decoration-065"
    Then file "text-decoration-065" of baseline and result should be the same
