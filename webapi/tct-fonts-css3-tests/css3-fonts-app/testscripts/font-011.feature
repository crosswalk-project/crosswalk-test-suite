Feature: css3-fonts
 Scenario: font 011
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-011-manual.htm"
     And I save the page to "font-011"
     And I save the screenshot md5 as "font-011"
    Then file "font-011" of baseline and result should be the same
