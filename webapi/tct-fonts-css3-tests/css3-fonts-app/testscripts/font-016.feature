Feature: css3-fonts
 Scenario: font 016
   When launch "css3-fonts-app"
     And I go to "csswg/font-016-manual.htm"
     And I save the page to "font-016"
    Then pic "font-016" of baseline and result should be "100" similar if have results
