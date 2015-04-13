Feature: css3-backgrounds
 Scenario: background size 033
   When launch "css3-backgrounds-app"
     And I go to "backgrounds/csswg/background-size-033-manual.html"
     And I save the page to "background-size-033"
    Then pic "background-size-033" of baseline and result should be "100" similar if have results
