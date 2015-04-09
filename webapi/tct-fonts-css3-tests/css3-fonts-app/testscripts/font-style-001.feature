Feature: css3-fonts
 Scenario: font style 001
   When launch "css3-fonts-app"
     And I go to "csswg/font-style-001-manual.htm"
     And I save the page to "font-style-001"
    Then pic "font-style-001" of baseline and result should be "100" similar if have results
