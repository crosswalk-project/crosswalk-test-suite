Feature: css3-fonts
 Scenario: font size 116
   When launch "css3-fonts-app"
     And I go to "csswg/font-size-116-manual.xht"
     And I save the page to "font-size-116"
    Then pic "font-size-116" of baseline and result should be "100" similar if have results
