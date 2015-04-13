Feature: css3-fonts
 Scenario: font matching rule 001
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-matching-rule-001-manual.htm"
     And I save the page to "font-matching-rule-001"
     And I save the screenshot md5 as "font-matching-rule-001"
    Then file "font-matching-rule-001" of baseline and result should be the same
