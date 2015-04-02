Feature: css3-fonts
 Scenario: font 007
   When launch "css3-fonts-app"
     And I go to "csswg/font-007-manual.htm"
     And I save the page to "font-007"
    Then pic "font-007" of baseline and result should be "100" similar if have results
