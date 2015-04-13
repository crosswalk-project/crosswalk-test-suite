Feature: css3-fonts
 Scenario: font size 116
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-size-116-manual.xht"
     And I save the page to "font-size-116"
     And I save the screenshot md5 as "font-size-116"
    Then file "font-size-116" of baseline and result should be the same
