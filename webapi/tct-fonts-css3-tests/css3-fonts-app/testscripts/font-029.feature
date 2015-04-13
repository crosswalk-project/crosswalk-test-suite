Feature: css3-fonts
 Scenario: font 029
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-029-manual.htm"
     And I save the page to "font-029"
    Then pic "font-029" of baseline and result should be "100" similar if have results
