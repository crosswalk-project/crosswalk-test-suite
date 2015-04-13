Feature: css3-fonts
 Scenario: font style 002
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-style-002-manual.htm"
     And I save the page to "font-style-002"
     And I save the screenshot md5 as "font-style-002"
    Then file "font-style-002" of baseline and result should be the same
