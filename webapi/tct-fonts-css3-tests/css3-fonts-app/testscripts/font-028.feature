Feature: css3-fonts
 Scenario: font 028
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-028-manual.htm"
     And I save the page to "font-028"
     And I save the screenshot md5 as "font-028"
    Then file "font-028" of baseline and result should be the same
