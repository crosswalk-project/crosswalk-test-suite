Feature: css3-backgrounds
 Scenario: background size 032
   When launch "css3-backgrounds-app"
     And I go to "csswg/background-size-032-manual.html"
     And I save the page to "background-size-032"
    Then pic "background-size-032" of baseline and result should be "100" similar if have results
