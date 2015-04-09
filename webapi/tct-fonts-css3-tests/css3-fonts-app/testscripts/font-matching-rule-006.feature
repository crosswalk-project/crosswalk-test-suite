Feature: css3-fonts
 Scenario: font matching rule 006
   When launch "css3-fonts-app"
     And I go to "csswg/font-matching-rule-006-manual.htm"
     And I save the page to "font-matching-rule-006"
    Then pic "font-matching-rule-006" of baseline and result should be "100" similar if have results
