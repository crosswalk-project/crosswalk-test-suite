Feature: css3-fonts
 Scenario: font weight 012
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-weight-012-manual.htm"
     And I save the page to "font-weight-012"
    Then pic "font-weight-012" of baseline and result should be "100" similar if have results
