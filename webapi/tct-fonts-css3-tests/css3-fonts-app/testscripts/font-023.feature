Feature: css3-fonts
 Scenario: font 023
   When launch "css3-fonts-app"
     And I go to "fonts/csswg/font-023-manual.htm"
     And I save the page to "font-023"
     And I save the screenshot md5 as "font-023"
    Then file "font-023" of baseline and result should be the same
