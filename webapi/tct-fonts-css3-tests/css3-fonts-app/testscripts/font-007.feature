Feature: css3-fonts
 Scenario: font 007
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-007-manual.htm"
     And I save the page to "font-007"
     And I save the screenshot md5 as "font-007"
    Then file "font-007" of baseline and result should be the same
