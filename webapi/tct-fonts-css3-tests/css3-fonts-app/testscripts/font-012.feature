Feature: css3-fonts
 Scenario: font 012
   When launch "css3-fonts-app"
     And I go to "csswg/font-012-manual.htm"
     And I save the page to "font-012"
    Then pic "font-012" of baseline and result should be "100" similar if have results
