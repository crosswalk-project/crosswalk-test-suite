Feature: css3-fonts
 Scenario: font 018
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-018-manual.htm"
     And I save the page to "font-018"
    Then pic "font-018" of baseline and result should be "100" similar if have results
