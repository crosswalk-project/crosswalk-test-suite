Feature: css3-color
 Scenario: t32 opacity basic a
   When launch "css3-color-app"
     And I go to "csswg/t32-opacity-basic-0.6-a.htm"
     And I save the page to "t32-opacity-basic-0.6-a"
    Then pic "t32-opacity-basic-0.6-a" of baseline and result should be "100" similar if have results
