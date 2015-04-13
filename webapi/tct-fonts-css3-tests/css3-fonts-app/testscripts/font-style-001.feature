Feature: css3-fonts
 Scenario: font style 001
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-style-001-manual.htm"
     And I save the page to "font-style-001"
     And I save the screenshot md5 as "font-style-001"
    Then file "font-style-001" of baseline and result should be the same
