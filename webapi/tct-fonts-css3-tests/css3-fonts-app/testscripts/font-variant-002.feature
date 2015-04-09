Feature: css3-fonts
 Scenario: font variant 002
   When launch "css3-fonts-app"
     And I go to "csswg/font-variant-002-manual.htm"
     And I save the page to "font-variant-002"
    Then pic "font-variant-002" of baseline and result should be "100" similar if have results
