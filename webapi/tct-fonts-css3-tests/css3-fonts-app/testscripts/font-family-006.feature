Feature: css3-fonts
 Scenario: font family 006
   When launch "css3-fonts-app"
     And I go to "csswg/font-family-006-manual.htm"
     And I save the page to "font-family-006"
    Then pic "font-family-006" of baseline and result should be "100" similar if have results
