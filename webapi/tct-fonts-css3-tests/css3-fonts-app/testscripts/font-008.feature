Feature: css3-fonts
 Scenario: font 008
   When launch "css3-fonts-app"
     And I go to "csswg/font-008-manual.htm"
     And I save the page to "font-008"
    Then pic "font-008" of baseline and result should be "100" similar if have results
