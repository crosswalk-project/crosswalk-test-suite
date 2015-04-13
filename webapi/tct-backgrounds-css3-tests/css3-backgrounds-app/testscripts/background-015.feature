Feature: css3-backgrounds
 Scenario: background 015
   When launch "css3-backgrounds-app"
     And I go to "backgrounds/csswg/background-015-manual.htm"
     And I save the page to "background-015"
    Then pic "background-015" of baseline and result should be "100" similar if have results
