Feature: css3-text
 Scenario: CSS3TextEffects text transform none
   When launch "css3-text-app"
     And I go to "csswg/text-transform-004.html"
     And I save the page to "text-transform-004"
    Then pic "text-transform-004" of baseline and result should be "100" similar if have results
