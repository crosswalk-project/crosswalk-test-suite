Feature: css3-fonts
 Scenario: font style 003
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-style-003-manual.htm"
     And I save the page to "font-style-003"
     And I save the screenshot md5 as "font-style-003"
    Then file "font-style-003" of baseline and result should be the same
