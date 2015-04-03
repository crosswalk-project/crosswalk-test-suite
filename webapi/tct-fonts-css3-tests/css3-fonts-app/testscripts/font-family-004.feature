Feature: css3-fonts
 Scenario: font family 004
   When launch "css3-fonts-app"
     And I go to "csswg/font-family-004-manual.htm"
     And I save the page to "font-family-004"
    Then pic "font-family-004" of baseline and result should be "100" similar if have results
