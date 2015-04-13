Feature: css3-fonts
 Scenario: font systemfont rule 004
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-systemfont-rule-004-manual.htm"
     And I save the page to "font-systemfont-rule-004"
     And I save the screenshot md5 as "font-systemfont-rule-004"
    Then file "font-systemfont-rule-004" of baseline and result should be the same
