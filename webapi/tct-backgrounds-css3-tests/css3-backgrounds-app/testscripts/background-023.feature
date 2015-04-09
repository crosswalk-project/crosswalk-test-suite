Feature: css3-backgrounds
 Scenario: background 023
   When launch "css3-backgrounds-app"
     And I go to "backgrounds/csswg/background-023-manual.htm"
     And I save the page to "background-023"
    Then pic "background-023" of baseline and result should be "100" similar if have results
