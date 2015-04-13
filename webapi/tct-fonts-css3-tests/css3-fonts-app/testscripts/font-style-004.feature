Feature: css3-fonts
 Scenario: font style 004
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-style-004-manual.htm"
     And I save the page to "font-style-004"
     And I save the screenshot md5 as "font-style-004"
    Then file "font-style-004" of baseline and result should be the same
