Feature: css3-fonts
 Scenario: font variant 002
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-variant-002-manual.htm"
     And I save the page to "font-variant-002"
     And I save the screenshot md5 as "font-variant-002"
    Then file "font-variant-002" of baseline and result should be the same
