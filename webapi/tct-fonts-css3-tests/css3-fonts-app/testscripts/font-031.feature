Feature: css3-fonts
 Scenario: font 031
   When launch "css3-fonts-app"
     And I go to "csswg/font-031-manual.htm"
     And I save the page to "font-031"
    Then pic "font-031" of baseline and result should be "100" similar if have results
