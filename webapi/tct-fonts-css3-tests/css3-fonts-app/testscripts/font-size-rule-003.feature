Feature: css3-fonts
 Scenario: font size rule 003
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-size-rule-003-manual.htm"
     And I save the page to "font-size-rule-003"
     And I save the screenshot md5 as "font-size-rule-003"
    Then file "font-size-rule-003" of baseline and result should be the same
