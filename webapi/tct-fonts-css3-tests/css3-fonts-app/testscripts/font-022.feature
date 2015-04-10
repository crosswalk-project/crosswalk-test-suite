Feature: css3-fonts
 Scenario: font 022
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-022-manual.htm"
     And I save the page to "font-022"
     And I save the screenshot md5 as "font-022"
    Then file "font-022" of baseline and result should be the same
