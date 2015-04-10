Feature: css3-fonts
 Scenario: font 032
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-032-manual.htm"
     And I save the page to "font-032"
     And I save the screenshot md5 as "font-032"
    Then file "font-032" of baseline and result should be the same
