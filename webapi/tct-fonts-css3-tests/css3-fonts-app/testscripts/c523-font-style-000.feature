Feature: css3-fonts
 Scenario: c523 font style 000
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/c523-font-style-000-manual.htm"
     And I save the page to "c523-font-style-000"
     And I save the screenshot md5 as "c523-font-style-000"
    Then file "c523-font-style-000" of baseline and result should be the same
