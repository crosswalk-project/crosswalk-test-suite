Feature: css3-fonts
 Scenario: font 022
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-022-manual.htm"
     And I save the page to "font-022"
    Then pic "font-022" of baseline and result should be "100" similar if have results
