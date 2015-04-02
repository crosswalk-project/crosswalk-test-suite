Feature: css3-backgrounds
 Scenario: background 019
   When launch "css3-backgrounds-app"
     And I go to "csswg/background-019-manual.htm"
     And I save the page to "background-019"
    Then pic "background-019" of baseline and result should be "100" similar if have results
