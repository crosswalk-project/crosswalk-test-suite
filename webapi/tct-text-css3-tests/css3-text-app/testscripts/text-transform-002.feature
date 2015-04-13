Feature: css3-text
 Scenario: CSS3TextEffects text transform lowercase
   When launch "css3-text-app"
     And I go to "text/csswg/text-transform-002.html"
     And I save the page to "text-transform-002"
     And I save the screenshot md5 as "text-transform-002"
    Then file "text-transform-002" of baseline and result should be the same
