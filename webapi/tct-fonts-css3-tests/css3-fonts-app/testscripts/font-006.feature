Feature: css3-fonts
 Scenario: font 006
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-006-manual.htm"
     And I save the page to "font-006"
     And I save the screenshot md5 as "font-006"
    Then file "font-006" of baseline and result should be the same
