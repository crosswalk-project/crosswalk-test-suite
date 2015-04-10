Feature: css3-fonts
 Scenario: font family 002
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-family-002-manual.htm"
     And I save the page to "font-family-002"
     And I save the screenshot md5 as "font-family-002"
    Then file "font-family-002" of baseline and result should be the same
