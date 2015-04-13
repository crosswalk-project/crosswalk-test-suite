Feature: css3-fonts
 Scenario: font weight rule 002
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-weight-rule-002-manual.htm"
     And I save the page to "font-weight-rule-002"
     And I save the screenshot md5 as "font-weight-rule-002"
    Then file "font-weight-rule-002" of baseline and result should be the same
