Feature: css3-fonts
 Scenario: font 044
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-044-manual.htm"
     And I save the page to "font-044"
     And I save the screenshot md5 as "font-044"
    Then file "font-044" of baseline and result should be the same
