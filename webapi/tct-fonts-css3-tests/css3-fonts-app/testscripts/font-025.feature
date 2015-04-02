Feature: css3-fonts
 Scenario: font 025
   When launch "css3-fonts-app"
     And I go to "csswg/font-025-manual.htm"
     And I save the page to "font-025"
    Then pic "font-025" of baseline and result should be "100" similar if have results
