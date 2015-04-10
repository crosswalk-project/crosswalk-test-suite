Feature: css3-fonts
 Scenario: font 024
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-024-manual.htm"
     And I save the page to "font-024"
     And I save the screenshot md5 as "font-024"
    Then file "font-024" of baseline and result should be the same
