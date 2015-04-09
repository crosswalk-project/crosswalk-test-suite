Feature: css3-fonts
 Scenario: font systemfont rule 004
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-systemfont-rule-004-manual.htm"
     And I save the page to "font-systemfont-rule-004"
    Then pic "font-systemfont-rule-004" of baseline and result should be "100" similar if have results
