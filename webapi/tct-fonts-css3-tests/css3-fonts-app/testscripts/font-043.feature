Feature: css3-fonts
 Scenario: font 043
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-043-manual.htm"
     And I save the page to "font-043"
     And I save the screenshot md5 as "font-043"
    Then file "font-043" of baseline and result should be the same
