Feature: css3-fonts
 Scenario: font family 006
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-family-006-manual.htm"
     And I save the page to "font-family-006"
     And I save the screenshot md5 as "font-family-006"
    Then file "font-family-006" of baseline and result should be the same
