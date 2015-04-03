Feature: css3-fonts
 Scenario: font weight 013
   When launch "css3-fonts-app"
     And I go to "csswg/font-weight-013-manual.htm"
     And I save the page to "font-weight-013"
    Then pic "font-weight-013" of baseline and result should be "100" similar if have results
