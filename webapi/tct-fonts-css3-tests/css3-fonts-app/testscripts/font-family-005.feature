Feature: css3-fonts
 Scenario: font family 005
   When launch "css3-fonts-app"
     And I go to "csswg/font-family-005-manual.htm"
     And I save the page to "font-family-005"
    Then pic "font-family-005" of baseline and result should be "100" similar if have results
