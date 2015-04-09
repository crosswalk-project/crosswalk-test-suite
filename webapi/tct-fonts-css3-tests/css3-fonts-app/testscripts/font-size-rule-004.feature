Feature: css3-fonts
 Scenario: font size rule 004
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-size-rule-004-manual.xht"
     And I save the page to "font-size-rule-004"
    Then pic "font-size-rule-004" of baseline and result should be "100" similar if have results
