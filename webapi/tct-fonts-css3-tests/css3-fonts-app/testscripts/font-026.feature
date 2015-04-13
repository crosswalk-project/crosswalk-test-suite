Feature: css3-fonts
 Scenario: font 026
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-026-manual.htm"
     And I save the page to "font-026"
     And I save the screenshot md5 as "font-026"
    Then file "font-026" of baseline and result should be the same
