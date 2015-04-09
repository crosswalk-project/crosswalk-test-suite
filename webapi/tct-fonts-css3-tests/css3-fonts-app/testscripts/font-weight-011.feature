Feature: css3-fonts
 Scenario: font weight 011
   When launch "css3-fonts-app"
     And I go to "csswg/font-weight-011-manual.htm"
     And I save the page to "font-weight-011"
    Then pic "font-weight-011" of baseline and result should be "100" similar if have results
