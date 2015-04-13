Feature: css3-fonts
 Scenario: font size rule 004
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-size-rule-004-manual.xht"
     And I save the page to "font-size-rule-004"
     And I save the screenshot md5 as "font-size-rule-004"
    Then file "font-size-rule-004" of baseline and result should be the same
