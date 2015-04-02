Feature: css3-backgrounds
 Scenario: background 012
   When launch "css3-backgrounds-app"
     And I go to "csswg/background-012-manual.htm"
     And I save the page to "background-012"
    Then pic "background-012" of baseline and result should be "100" similar if have results
