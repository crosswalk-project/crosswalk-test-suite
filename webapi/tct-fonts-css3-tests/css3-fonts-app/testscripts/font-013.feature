Feature: css3-fonts
 Scenario: font 013
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-013-manual.htm"
     And I save the page to "font-013"
     And I save the screenshot md5 as "font-013"
    Then file "font-013" of baseline and result should be the same
