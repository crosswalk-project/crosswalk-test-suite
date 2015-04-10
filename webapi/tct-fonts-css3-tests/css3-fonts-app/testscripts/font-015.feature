Feature: css3-fonts
 Scenario: font 015
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-015-manual.htm"
     And I save the page to "font-015"
     And I save the screenshot md5 as "font-015"
    Then file "font-015" of baseline and result should be the same
