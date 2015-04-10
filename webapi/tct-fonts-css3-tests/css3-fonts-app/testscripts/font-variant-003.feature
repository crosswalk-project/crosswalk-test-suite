Feature: css3-fonts
 Scenario: font variant 003
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-variant-003-manual.htm"
     And I save the page to "font-variant-003"
     And I save the screenshot md5 as "font-variant-003"
    Then file "font-variant-003" of baseline and result should be the same
