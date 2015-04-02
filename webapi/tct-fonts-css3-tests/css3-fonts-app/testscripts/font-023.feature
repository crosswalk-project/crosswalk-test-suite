Feature: css3-fonts
 Scenario: font 023
   When launch "css3-fonts-app"
     And I go to "csswg/font-023-manual.htm"
     And I save the page to "font-023"
    Then pic "font-023" of baseline and result should be "100" similar if have results
