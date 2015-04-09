Feature: css3-fonts
 Scenario: font 015
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-015-manual.htm"
     And I save the page to "font-015"
    Then pic "font-015" of baseline and result should be "100" similar if have results
