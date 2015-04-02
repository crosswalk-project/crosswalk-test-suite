Feature: css3-fonts
 Scenario: font 044
   When launch "css3-fonts-app"
     And I go to "csswg/font-044-manual.htm"
     And I save the page to "font-044"
    Then pic "font-044" of baseline and result should be "100" similar if have results
