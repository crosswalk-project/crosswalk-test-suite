Feature: css3-fonts
 Scenario: font 043
   When launch "css3-fonts-app"
     And I go to "csswg/font-043-manual.htm"
     And I save the page to "font-043"
    Then pic "font-043" of baseline and result should be "100" similar if have results
