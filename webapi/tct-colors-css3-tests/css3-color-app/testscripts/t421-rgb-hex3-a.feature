Feature: css3-color
 Scenario: t421 rgb hex3 a
   When launch "css3-color-app"
     And I go to "csswg/t421-rgb-hex3-a.htm"
     And I save the page to "t421-rgb-hex3-a"
    Then pic "t421-rgb-hex3-a" of baseline and result should be "100" similar if have results
