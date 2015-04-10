Feature: css3-fonts
 Scenario: font family 003
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-family-003-manual.htm"
     And I save the page to "font-family-003"
     And I save the screenshot md5 as "font-family-003"
    Then file "font-family-003" of baseline and result should be the same
