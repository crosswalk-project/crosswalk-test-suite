Feature: css3-fonts
 Scenario: font 025
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-025-manual.htm"
     And I save the page to "font-025"
     And I save the screenshot md5 as "font-025"
    Then file "font-025" of baseline and result should be the same
