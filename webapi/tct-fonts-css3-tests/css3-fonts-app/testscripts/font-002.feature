Feature: css3-fonts
 Scenario: font 002
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-002-manual.htm"
     And I save the page to "font-002"
    Then pic "font-002" of baseline and result should be "100" similar if have results
