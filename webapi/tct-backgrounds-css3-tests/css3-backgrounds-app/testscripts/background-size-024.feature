Feature: css3-backgrounds
 Scenario: background size 024
   When launch "css3-backgrounds-app"
     And I go to "backgrounds/csswg/background-size-024-manual.html"
     And I save the page to "background-size-024"
    Then pic "background-size-024" of baseline and result should be "100" similar if have results
