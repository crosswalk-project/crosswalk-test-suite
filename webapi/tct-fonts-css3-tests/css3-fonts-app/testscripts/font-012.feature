Feature: css3-fonts
 Scenario: font 012
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-012-manual.htm"
     And I save the page to "font-012"
     And I save the screenshot md5 as "font-012"
    Then file "font-012" of baseline and result should be the same
