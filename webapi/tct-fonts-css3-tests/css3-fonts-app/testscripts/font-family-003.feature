Feature: css3-fonts
 Scenario: font family 003
   When launch "css3-fonts-app"
     And I go to "csswg/font-family-003-manual.htm"
     And I save the page to "font-family-003"
    Then pic "font-family-003" of baseline and result should be "100" similar if have results
