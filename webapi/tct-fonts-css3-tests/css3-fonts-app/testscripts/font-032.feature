Feature: css3-fonts
 Scenario: font 032
   When launch "css3-fonts-app"
     And I go to "csswg/font-032-manual.htm"
     And I save the page to "font-032"
    Then pic "font-032" of baseline and result should be "100" similar if have results
