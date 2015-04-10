Feature: css3-fonts
 Scenario: font size 003
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-size-003-manual.htm"
     And I save the page to "font-size-003"
     And I save the screenshot md5 as "font-size-003"
    Then file "font-size-003" of baseline and result should be the same
