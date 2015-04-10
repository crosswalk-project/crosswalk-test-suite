Feature: css3-fonts
 Scenario: font matching rule 006
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-matching-rule-006-manual.htm"
     And I save the page to "font-matching-rule-006"
     And I save the screenshot md5 as "font-matching-rule-006"
    Then file "font-matching-rule-006" of baseline and result should be the same
