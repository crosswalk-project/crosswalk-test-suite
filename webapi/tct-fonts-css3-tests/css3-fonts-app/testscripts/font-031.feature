Feature: css3-fonts
 Scenario: font 031
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-031-manual.htm"
     And I save the page to "font-031"
     And I save the screenshot md5 as "font-031"
    Then file "font-031" of baseline and result should be the same
