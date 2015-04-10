Feature: css3-fonts
 Scenario: font 010
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-010-manual.htm"
     And I save the page to "font-010"
     And I save the screenshot md5 as "font-010"
    Then file "font-010" of baseline and result should be the same
