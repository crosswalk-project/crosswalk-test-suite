Feature: css3-fonts
 Scenario: font matching rule 012
   When launch "css3-fonts-app"
     And I go to "csswg/font-matching-rule-012.xht"
     And I save the page to "font-matching-rule-012"
    Then pic "font-matching-rule-012" of baseline and result should be "100" similar if have results
