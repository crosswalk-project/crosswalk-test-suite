Feature: css3-color
 Scenario: t31 color text a
   When launch "css3-color-app"
     And I go to "csswg/t422-rgba-a0.6-a.htm"
     And I save the page to "t422-rgba-a0.6-a"
    Then pic "t422-rgba-a0.6-a" of baseline and result should be "100" similar if have results
