Feature: css3-text
 Scenario: CSS3TextEffects text decoration none
   When launch "css3-text-app"
     And I go to "csswg/text-decoration-065.html"
     And I save the page to "text-decoration-065"
    Then pic "text-decoration-065" of baseline and result should be "100" similar if have results
