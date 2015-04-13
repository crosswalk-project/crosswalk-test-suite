Feature: css3-fonts
 Scenario: font 029
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-029-manual.htm"
     And I save the page to "font-029"
     And I save the screenshot md5 as "font-029"
    Then file "font-029" of baseline and result should be the same
