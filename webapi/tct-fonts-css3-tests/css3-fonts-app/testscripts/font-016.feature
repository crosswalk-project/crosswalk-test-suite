Feature: css3-fonts
 Scenario: font 016
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-016-manual.htm"
     And I save the page to "font-016"
     And I save the screenshot md5 as "font-016"
    Then file "font-016" of baseline and result should be the same
