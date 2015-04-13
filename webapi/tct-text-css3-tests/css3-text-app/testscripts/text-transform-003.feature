Feature: css3-text
 Scenario: CSS3TextEffects text transform uppercase
   When launch "css3-text-app"
     And I go to "text/csswg/text-transform-003.html"
     And I save the page to "text-transform-003"
     And I save the screenshot md5 as "text-transform-003"
    Then file "text-transform-003" of baseline and result should be the same
